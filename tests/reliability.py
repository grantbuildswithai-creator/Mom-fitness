"""Run against a local server: python3 tests/reliability.py.
Requires the development environment's Playwright and Chromium, not app dependencies.
"""
from datetime import datetime, timedelta
from playwright.sync_api import sync_playwright, expect

BASE = 'http://127.0.0.1:8000/'
START = datetime.fromisoformat('2026-11-10T12:00:00-05:00')
with sync_playwright() as p:
    browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True, args=['--no-sandbox'])
    context = browser.new_context(timezone_id='America/New_York')
    page = context.new_page()
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.clock.install(time=START)
    page.goto(BASE)
    # Full program sequence, including partial days and gaps.
    good = stars = best = run = 0
    quotes = set()
    for i in range(56):
        page.clock.set_fixed_time(START + timedelta(days=i))
        page.evaluate("window.dispatchEvent(new Event('pageshow'))")
        expect(page.locator('#dateline')).to_contain_text(f'Day {i+1} of 56')
        quotes.add(page.locator('#quotetext').inner_text())
        n = [2, 3, 1, 0, 2, 3, 2][i % 7]
        for block in ['pedal', 'exercises', 'walk'][:n]:
            page.evaluate('(block)=>toggleBlock(block)', block)
        good += n >= 2
        stars += n == 3
        run = run + 1 if n >= 2 else 0
        best = max(best, run)
        assert page.evaluate('[streakDayTotal(),starTotal(),bestStreak(),UNLOCKABLES.filter(unlockEarned).length]') == [good, stars, best, min(good, 10)]
        assert page.evaluate('badgeStates().done') == (i == 55)
    assert len(quotes) == 56
    page.reload()
    assert page.evaluate('streakDayTotal()') == good
    page.clock.set_fixed_time(START)
    page.evaluate("window.dispatchEvent(new Event('focus'))")
    assert page.evaluate('[streakDayTotal(),starTotal()]') == [1, 0]
    expect(page.locator('#dateline')).to_contain_text('Day 1 of 56')
    page.clock.set_fixed_time(START + timedelta(days=3))
    page.clock.run_for(1100)
    expect(page.locator('#dateline')).to_contain_text('Day 4 of 56')
    expect(page.locator('#blk-pedal')).to_have_attribute('aria-pressed', 'false')
    # Current-day player survives completing the third block and focus refresh.
    page.goto(BASE + '?test=1&reset=1')
    expect(page.locator('#dateline')).to_contain_text('Day 1 of 56')
    page.evaluate("toggleBlock('pedal');toggleBlock('exercises');window.player=document.querySelector('#unlock-slot video');toggleBlock('walk');window.dispatchEvent(new Event('focus'))")
    assert page.evaluate("player===document.querySelector('#unlock-slot video') && player.isConnected")
    # Gallery survives view switching; normal reset removes old unlocks immediately.
    page.goto(BASE)
    page.evaluate("showView('badges');window.galleryPlayer=document.querySelector('#fam-slot video');showView('today');showView('badges')")
    assert page.evaluate("galleryPlayer===document.querySelector('#fam-slot video')")
    page.on('dialog', lambda d: d.accept())
    page.locator('#btn-reset').click()
    expect(page.locator('#fam-slot video')).to_have_count(0)
    # Two already-open tabs retain each other's updates.
    other = context.new_page()
    other.clock.install(time=START + timedelta(days=3))
    other.goto(BASE)
    page.evaluate("toggleBlock('pedal')")
    other.evaluate("toggleBlock('walk')")
    other.reload()
    expect(other.locator('#blk-pedal')).to_have_attribute('aria-pressed', 'true')
    expect(other.locator('#blk-walk')).to_have_attribute('aria-pressed', 'true')
    assert not errors, errors
    browser.close()
print('PASS: 56-day sequence, quotes, persistence, future cap, midnight/resume refresh, retained players, reset gallery, two-tab progress')

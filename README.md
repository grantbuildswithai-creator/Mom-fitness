# Susan's Stars 🌺

**Consistency beats intensity.**

A little exercise tracker made for Susan, to carry her through her
physical-therapy program — **November 10, 2026 to January 4, 2027**
(56 days). Hawaiian sunshine, made with love by her family.

**Live site:** https://grantbuildswithai.com/Mom-fitness/
*(the capital **M** matters — the lowercase address doesn't work)*

## How Susan uses it

1. Open the link in Safari on her iPhone and choose
   **Share → Add to Home Screen**. It then opens like an app.
2. Every day there are three big blocks to tap when done — no timers,
   no forms:
   - **Pedal** (20 minutes)
   - **Exercises** (the PT sets, shown inside the block for reference)
   - **Walk**
3. Finishing **2 of 3** makes it a good day. Finishing **all 3** earns
   a ⭐ perfect-day star.
4. **Every good day unlocks a new video message from the family.**
   They all stay in **My Badges**, where she can rewatch them anytime.
5. Badges celebrate streaks and weekly consistency, and a fresh quote
   waits under her "Aloha, Susan!" every morning — a different one for
   each of the 56 days.

There are no failure states and nothing to catch up on. A quiet day is
just a quiet day; the next good day picks right back up.

## For the family

Want to cheer her on? Send a short video (under ~30 seconds is perfect)
to Grant on WhatsApp. He uploads it to the `unlockables/` folder here
and it joins the end of the unlock queue — one new video per good day,
in this order so far:

1. Grant · 2–4. Marc ×3 · 5. Hannah · 6. Reid · 7. Marc's wife ·
8. Grant · 9. Reid · 10. Grant (the finale)

## Privacy, by design

No accounts, no sign-ups, no server. All of Susan's progress lives only
on her own phone (in the browser's local storage). Nothing is tracked
or sent anywhere.

## For Grant — testing & maintenance

- **Test mode:** open the site with `?test=1` on the end of the address
  for a control panel that pretends it's another day (step forward/back,
  jump to Day 1, seed a good week, erase everything). Erasing in test
  mode also resets the pretend clock to Day 1. Susan's link never has
  `?test=1`.
- **Start over:** the *My Badges* screen has a "Start over" button;
  `?reset=1` on the address does the same. Susan's own phone starts
  empty on its own — progress is per-device.
- **Badges and unlocks count only days up to today** — nothing can be
  earned early or "from the future."

## What's in here

| File | What it is |
|---|---|
| `index.html` | The whole app — one self-contained page |
| `DESIGN.md` | The design spec (rules, badges, palette) |
| `header.jpg`, `star-wreath.jpg` | Painted Hawaiian artwork for the page |
| `icon-180.png` | Home-screen icon |
| `unlockables/` | The family's video messages (MP4) |

Text files are pushed with the GitHub connector; images and videos are
uploaded through the GitHub website (the connector route is text-only).
This is a standalone project site — it is not part of
grantbuildswithai.com's main website.

## Local development checks

Serve the repository with `python3 -m http.server 8000 --bind 127.0.0.1`.
Run `node tests/rules.cjs` for quote and badge thresholds, then
`python3 tests/reliability.py` for browser regression checks against that server.
The browser checks use Playwright and `/usr/bin/chromium` provided by the cloud
development environment; the deployed app still has no dependencies or build.
Tests use isolated browser storage and never change Susan's saved progress.

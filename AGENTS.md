# Working on Susan's Stars

## Scope and coordination

- Work only in `grantbuildswithai-creator/Mom-fitness`. NEVER touch the separate `grantbuildswithai-creator/grantbuildswithai-creator.github.io` repository (Grant's main website).
- Read `README.md`, `DESIGN.md`, and `index.html` in full before changing application code.
- Muse also edits this repository through the GitHub connector. Check the working tree and pull before editing; preserve others' changes. Use small commits with clear messages. Never force-push.
- GitHub Pages publishes from `main`; anything pushed there goes live in about a minute. The canonical URL is https://grantbuildswithai.com/Mom-fitness/ — the capital M is required; the lowercase path 404s. Treat a push to main as deployment.
- Text files can be pushed through the GitHub connector; media is uploaded through the GitHub web UI.
- Use the existing checkout in cloud tasks; do not create a Git worktree unless explicitly requested.

## Product and architecture

Susan's Stars is an encouraging exercise tracker for Susan's physical-therapy program, November 10, 2026 through January 4, 2027 inclusive (56 days). Its theme is “Consistency beats intensity.” Susan uses iPhone Safari and Add to Home Screen.

- `index.html` is the entire app: vanilla HTML, CSS, and JavaScript. Preserve the single-page, dependency-free design: no build step, framework, backend, accounts, analytics, or remote progress storage.
- Two views: Today and My Badges. Keep large type, large tap targets, strong contrast, accessible button states (`aria-pressed`), and mobile safe-area support.
- Assets are `header.jpg`, `star-wreath.jpg`, `icon-180.png`, and the MP4 files in `unlockables/`. Preserve relative paths for project-site hosting.
- Positive reinforcement only. No failure states, streak-loss language, catch-up demands, or nagging.
- Blue and yellow lead; Hawaiian hibiscus and plumeria, with ocean/sunshine supporting. Preserve the painterly art. Avoid red/coral/pink, and palm-tree motifs.
- `DESIGN.md` is the frozen design spec. Any necessary deviation must include an update to that file in the same commit, explaining why.

## Persistent data: hard compatibility boundary

NEVER change the localStorage key `susans-stars-v1` or the state shape `{days, celebrated, unlockDay}`. Susan's real progress depends on compatibility.

- `days` maps local-calendar `YYYY-MM-DD` dates to `{pedal, exercises, walk}` boolean records.
- `celebrated` maps dates to flags preventing repeated perfect-day celebrations.
- `unlockDay` maps stable video IDs to the dates their unlock was first recorded; it drives today's new-message card.
- Statistics, badge eligibility, and video eligibility are derived from daily records. Do not replace them with independently stored counters or make `unlockDay` the eligibility source.
- Preserve existing data and stable record/video IDs. Never reset real progress as part of development or deployment.
- Test mode uses the SAME localStorage data as normal mode on the same origin. Use an isolated browser context or local development origin for testing. Only the fake-clock offset (`ss-test-offset`) lives in sessionStorage and is ignored outside test mode.

## Rules and implementation landmarks

- Three daily toggles: Pedal (20 minutes), Exercises (PT reference always visible), Walk. No timers, forms, or individual exercise check-offs.
- Two or three completed blocks make a good day; all three make a perfect day and earn one star. Large confetti/overlay celebration is for a perfect day, once per date.
- Dates use the device's local calendar. Day 1 is November 10; day 56 is January 4. Keep exactly 56 entries in `QUOTES`, indexed by program day; rendering clamps to the first/last quote outside the program.
- Nothing may be earned from future-dated records. Preserve `effDays()` and its use in totals, best streak, weekly calculations, participation, badges, and unlocks. Program days are bounded to the 56-day program.
- `currentStreak()` uses today's run when today qualifies, otherwise yesterday's run if applicable. Streak badges use `bestStreak()`, so earlier achievements remain after gaps.
- Badges: first good day; best streak of 2, 3, or 7 days; Weekly Star for 3+ good days in a program week; 4-Week Champion for four consecutive weekly stars; Program Complete only when January 4 has been reached AND at least one good day exists.
- Weeks are seven-day blocks anchored to program Day 1, not calendar weeks. Perfect-day stars have their own collection, separate from the seven entries in `BADGES`.
- Every good day unlocks the next video, consecutive or not. `unlockEarned(u)` compares `streakDayTotal()` against `u.n`. Never restore milestone-based unlocks or leave reward gaps while videos remain.
- `UNLOCKABLES` currently has ten entries: Grant, Marc ×3, Hannah, Reid, Marc's wife, Grant, Reid, Grant. A file uploaded to `unlockables/` does nothing until registered with a stable ID, correct source path, sender, and next `n` in this array. New messages join the end.
- Preserve lazy gallery construction: `renderGallery()` runs when My Badges opens, not in general `render()`. Video elements use `controls`, `playsinline`, and `preload="metadata"`. Do not eagerly build/preload the whole gallery on Today.

## Development and verification

From the repository root, serve locally with:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

There is no package installation, build, or repository test runner. Browser interaction is the meaningful validation. Check mobile layout and JavaScript/network errors; use iPhone Safari for device-specific behavior when available.

- Normal mode must hide the test panel. Susan's link never includes `?test=1`.
- `?test=1` exposes previous/next day, real today, Back to Day 1, seed a good week, and erase controls. Seeding writes preceding program days, not today's record.
- Test sequences day by day: good days, partial days, perfect days, and gaps. Verify current/best streak, star totals, and one video per cumulative good day across gaps.
- Reload to verify progress persistence. Toggle completed blocks to check derived totals and that celebrations do not repeat for an already celebrated date.
- Advance to record future progress, then step back: future stars, badges, and videos must be excluded. Test program-week boundaries, consecutive weekly stars, and January 4 with and without participation.
- Open My Badges to check gallery content, metadata loading, and video order. Verify Today does not construct the full gallery.
- Test-mode erase must reset BOTH stored progress and the fake clock to Day 1. Preserve this behavior for panel erase, confirmed Start over, and `?test=1&reset=1`. `?reset=1` erases data, so use only in disposable test storage.
- Preserve confirmation for button-driven erasure. Validate media paths and all 56 quotes when changing their lists.

## Known documentation differences

Grant's current instructions and the implementation clarify older wording in `DESIGN.md`: the live URL is the capital-M custom-domain URL above; Pages is already enabled; artwork is at the repository root; ten videos are already wired; Program Complete requires participation as well as the date. Do not revert working behavior to stale descriptions. Document any future design deviation with its reason in the same commit.

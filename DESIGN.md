# Susan's Stars — Design Document

A cheerful exercise tracker for Susan, built around her 7½-week physical-therapy
program. She opens it from her iPhone home screen each day, taps off three
blocks, and earns streaks, stars, and badges — with a little piece of Hawaii on
every screen.

- **Status:** Design phase. Not yet built.
- **Site (once built):** https://grantbuildswithai-creator.github.io/mom-fitness/
- **Program dates:** Nov 10, 2026 → Jan 4, 2027 (56 days)
- **Theme line (appears on the site):** "Consistency beats intensity"

---

## 1. Who it's for

Susan — Grant's mother — working through a home PT program after the program
card her therapist gave her. She does best with a checklist and small
achievements. She does **not** respond to negative feedback or nagging, and
the design never uses any: no failure states, no streak-loss shaming, nothing
red or alarming. Every day she shows up is framed as a win.

She loves Hawaii, and her favorite colors are blue and yellow.

## 2. The daily routine (from her program card)

- **Pedal** — 20 minutes (the card has 20 min morning + 20 min afternoon;
  the site simplifies this to one block — see Decisions).
- **Exercises** — her PT sets:
  - *Standing:* step ups ×10 · squats ×10 · square balance 30 sec with head
    moves · side leg lifts · marches · kick backs
  - *Bed:* ankle pumps ×20 · knee bends/lifts ×10 · heel slides ×10 ·
    leg side ×10 · leg lift ×10 · bridges ×10
  - *Upper + core + calves:* counter push ups ×10 · calf heel raises ×20 ·
    calf stretch ×10 · seated core crunches ("bugs") ×10
- **Walk** — a daily walk.

(The card's other three "legs" — Food, Sleep, Peace/Calm — are context only.
The tracker is exercise-only.)

## 3. Screens

Two screens, nothing more.

### Today

- **Header:** the Hawaiian sunrise artwork (see §6), with "Susan's Stars ★"
  and "Consistency beats intensity" overlaid.
- **Greeting:** "Aloha, Susan!"
- **Daily quote:** one inspirational quote under the greeting, changing daily
  and never repeating — 56 quotes, one per program day
  (Day 1 = Nov 10, 2026 … Day 56 = Jan 4, 2027).
- **Stats row, big numbers:** current streak · stars earned · days to Jan 4
  (the countdown runs to Jan 4, the end of the program — *not* to Christmas).
- **The checklist — three blocks, one tap each:**
  1. **Pedal** — 20 minutes
  2. **Exercises** — the PT sets shown as a reference list inside the block
     (no per-exercise check-offs)
  3. **Walk**
- **Perfect-day strip:** the star-wreath artwork with "A perfect day earns
  your star — finish all 3 to see your celebration."

### My Badges

- Every badge, earned ones lit up, locked ones greyed with a plain-language
  note on what unlocks them.
- Her best streak is always shown here, even after a streak ends.
- Star total (perfect days) displayed as its own collection.

## 4. Rules of the game

- **One tap per block.** No timers (she uses her own clock for the pedal),
  no forms, no settings.
- **2 of 3 blocks = a streak day.** The day counts, the streak grows, and the
  copy celebrates it: "You showed up — that's what counts."
- **3 of 3 = a perfect day.** It earns a **star** — a different badge from a
  streak day, with its own running total.
- **0–1 blocks** still gets encouragement. There is no failure state.
- **Missed day:** the streak quietly starts again. Nothing scolds, nothing
  is taken away; the best streak stays on the badge screen.

### Badges

| Badge | How she earns it |
|---|---|
| First Day | Complete her first day (2+ blocks) |
| 2-Day Streak | 2 streak days in a row |
| 3-Day Streak | 3 streak days in a row |
| 7-Day Streak | 7 streak days in a row |
| Perfect Day ★ | A 3-of-3 day (each one adds to her star total) |
| Weekly Star | 3+ streak days in one week |
| 4-Week Champion | 4 weeks in a row earning the Weekly Star |
| Program Complete | Reach Jan 4, 2027 |

### Celebrations & unlockables (Marc's design)

- Small celebration as each block is tapped done; the **big** celebration —
  balloons / fireworks / confetti, with the star-wreath artwork — is reserved
  for a perfect 3-of-3 day.
- **Unlockable encouragement:** family photos (grandkids — "you can do it,
  Mom") and short family voice notes that open only *after* she completes a
  day or a milestone. The slots are built into the design; the family
  supplies the photos/recordings as they arrive.
- **Optional real-world treats** tied to milestones, set by the family
  (Marc's examples: a little treat, new sunglasses, a new Hawaii outfit).
  The page just celebrates; the family handles the treats.

## 5. Visual design

- **Hawaiian theme, and make it fun** — a little vacation, not a medical app.
- **Palette: blue and yellow lead** (her favorites). Ocean and sky blues —
  deep sea `#0A3E60`, deep teal `#0B5563`, teal `#0E7C86`, bright blue
  `#1B9AAA`, pale sky `#EFF8FA` — with sunshine yellow `#FFD93D`, gold
  `#F5A623`, and white. **Go easy on red: no coral, pink, or sunset-red
  tones anywhere.**
- **Motifs: flowers first.** Hibiscus and plumeria lead; ocean waves and
  sunshine support. Palm trees are out. The hibiscus is yellow — the yellow
  hibiscus is Hawaii's state flower.
- **Readability is non-negotiable** even inside the fun: big type, big tap
  targets, strong contrast, one clear action per screen.

### Artwork (commissioned for this site, 2026-11-12)

Painterly storybook illustrations, generated for this project and saved with
the project files (to be added under `assets/` in this repo at build time):

- **`header.jpg`** — wide banner: yellow hibiscus and white plumeria framing
  a sunrise over a blue ocean; the title and tagline overlay the calm center.
- **`star-wreath.jpg`** — a gold star in a hibiscus-and-plumeria wreath on
  deep blue; used on the perfect-day celebration and the badge screen.

The earlier flat-icon look was tried and retired as too simple.

## 6. How it works (technical)

- One static web page (HTML/CSS/JS), no accounts, no backend, nothing for
  Susan to log into.
- Hosted on **GitHub Pages from this repository**, giving it the stable
  address above.
- Installed on her iPhone via Safari → Share → **Add to Home Screen**, where
  it opens full-screen like an app.
- **All her data stays on her phone** (on-device storage): check-offs,
  streaks, stars, and badges must persist between visits — a page that
  forgets on close cannot run a streak. Nothing is uploaded anywhere.
- Day counting is anchored to the program: Day 1 = Nov 10, 2026, and the
  quote/streak math keys off calendar dates in her local time.

## 7. Decisions log (Grant, 2026-11-12 unless noted)

- Name: **"Susan's Stars"** (not "Susan's gold stars").
- Checklist = 3 blocks only: Pedal (one 20-minute block), Exercises, Walk.
- One tap per block; no pedal timer; no per-exercise check-offs.
- 2 of 3 = streak day; 3 of 3 = perfect day earning a star, tracked separately.
- Daily quote on the Today screen, never repeating (56 quotes prepared).
- Countdown target: **Jan 4**, not Christmas.
- Hawaii theme; flowers over palm trees; blue and yellow, minimal red.
- Flat mockups "too simple" → commissioned painterly artwork (§5).
- Gamification shape (streak badges, weekly badge, 4-week badge, instant
  celebration, unlockable family photos/voice notes, positive-only):
  Marc's design, 2026-11-12, from Susan's actual PT program card.
- Exercise-only tracker (2026-11-11 pivot from a health tracker).

## 8. Open items (none block the build)

- Which family photos and voice notes fill the unlockable slots, and who
  records them.
- The milestone treat list (family decides).
- Exact pedal settings on the card — one line is partly illegible
  (resistance/minutes); confirm with Marc if it ever matters.
- Enable GitHub Pages when the build lands.

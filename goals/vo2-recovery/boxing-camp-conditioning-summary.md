# Boxing Camp Conditioning — Running Summary

**Living document.** Updated as new COROS/Hevy sessions land. Reviews
[boxing-camp-conditioning-context.md](boxing-camp-conditioning-context.md)
against actual recorded training.

**Location (10 Sep 2026):** moved to `goals/vo2-recovery/`. This file is the
chronological log; the current state of play is in [README.md](README.md).
Shoulder sections below are historical — the shoulder goal is now owned by
[../shoulder-rehab/README.md](../shoulder-rehab/README.md).

**Last updated:** 2026-09-21 (Mon) · **Data through:** Mon 21 Sep 2026

---

## Camp clock

Target: fight in **November 2026**, 5 × 3 min rounds, 1 min rests.

| Fight date | Weeks remaining |
| --- | --- |
| 1 Nov | **7.4** |
| 15 Nov | **9.4** |
| 30 Nov | **11.6** |

The plan assumes "roughly 10–12 weeks available", so **the camp window is open
now**. Per the plan's own phasing this is the **Early phase**: aerobic base,
Zone 2 ×2/week, aerobic intervals ×1/week.

---

## Athlete facts — plan vs COROS

| | Plan document | COROS account | Note |
| --- | --- | --- | --- |
| Age | 47 | **46** (b. 1979-10-27) | Turns 47 on 27 Oct, before the fight |
| Weight | 96 kg | **91 kg** | 5 kg lighter than the plan assumes |
| Device | PACE 2 | **PACE 3** (also owns PACE 2) | Runs recorded on PACE 3 |

The device difference matters for one plan recommendation — see
[Chest strap](#chest-strap) below.

### Reference values (from the plan)

- LTHR: **157 bpm**
- Zone 2 band: **126–141 bpm**
- Working target: **135–140 bpm**, soft ceiling **141–142 bpm**

**Provenance established 3 Sep.** These are not independent of COROS — they are
COROS's own **Lactate Threshold** zone model evaluated at LTHR 157. That model
defines Zone 2 as **80–90% of threshold HR**, and 0.80 × 157 = 125.6,
0.90 × 157 = 141.3 → **126–141**. The plan's band is COROS LT Zone 2 exactly.
Corroborated from the other direction by max HR 179: 157 / 179 = 88%.

Consequence: **the app must be on the Lactate Threshold zone type** for its
displayed zones to match the plan. What each threshold HR would produce:

| COROS threshold HR | Resulting Zone 2 | Matches plan? |
| --- | --- | --- |
| 150 | 120–135 | no — 6 bpm low |
| **157** | **126–141** | **exact** |
| 160 | 128–144 | no — ceiling 3 over |
| 165 | 132–148 | no — ceiling 7 over |

**Drift risk.** Threshold HR is algorithm-updated and cannot be pinned
(see [Standing finding 7](#7-possible-max-hr--zone-mis-set)). If COROS revises
it upward mid-camp the Zone 2 ceiling rises silently with it, and sessions that
read "in Zone 2" would sit above the plan's 141–142 ceiling. COROS does allow
**custom zone boundaries**; locking 126–141 by hand removes the risk.

Note also that EvoLab computes its metrics from the Lactate Threshold zones
**regardless of which model is displayed**, so choosing LT makes the display
agree with the analysis already running underneath.

---

## Week of 24–27 Aug 2026

### Sessions recorded

| Day | Session | Duration | Avg HR | Source |
| --- | --- | --- | --- | --- |
| Mon 24 | Indoor cycling | 51:58 | 120 | COROS |
| Tue 25 | Outdoor run, 8.59 km | 54:35 | 137 | COROS |
| Wed 26 | Shoulder Rehab (strength) | 48:57 | — | Hevy only |
| Thu 27 | Outdoor run, 8.41 km | 53:09 | **146** | COROS |

### Time in zone — measured from FIT files

Per-second HR, not lap averages. The plan states that *"time spent steadily in
the target HR zone is more informative than average HR alone"*, so this is the
metric it asks to be judged on.

| | Tue 25 Aug | Thu 27 Aug |
| --- | --- | --- |
| Average HR | 137 | 146 |
| Below Z2 (<126) | 4.7% · 2.5 min | 4.0% · 2.1 min |
| **In Z2 (126–141)** | **64.1% · 34.9 min** | **25.4% · 13.5 min** |
| In target (135–140) | 29.8% · 16.2 min | 18.6% · 9.9 min |
| **Above ceiling (>142)** | **24.3% · 13.2 min** | **67.7% · 36.0 min** |
| Above LTHR (>157) | 0.0% | **11.6% · 6.2 min** |
| Max HR | 153 | 162 |

### Assessment against the plan

**Monday bike — matches the plan's own read.** 51 min at 120 bpm is below the
Zone 2 working band. Useful easy aerobic/recovery volume, not a Zone 2 stimulus.

**Tuesday run — a good Zone 2 session, though the plan was slightly generous.**
The plan calls it *"very good... right around the desired working intensity."*
Per-second data: 64% in Z2 but only **30% in the 135–140 target**, with 13 min
above the 142 ceiling. Directionally right, executed loosely.

**Thursday run — this is the finding of the week.** The plan explicitly
anticipated this session and advised against it:

> *"A further aerobic session was planned for Thursday morning. Incline walking
> around 135–140 bpm was suggested instead of automatically doing another 50+
> minute run."*

What happened was another 53-minute run. It was **not a Zone 2 session**:
**68% of it sat above the 142 ceiling**, only 25% in Z2, and **6.2 minutes above
lactate threshold**. Training load 158 vs Tuesday's 134 — a *higher* cost from a
session intended to be easier.

Same pace as Tuesday (6:19 vs 6:21) for **+9 bpm**. Running mechanics actually
held better than Tuesday (cadence steady at 163–164, second-half fade halved
from +32 to +15 s/km), so the legs coped — the cost was cardiac and came from
accumulated fatigue on the second run in three days.

**COROS graded it "Poor".** Ignore the label: it scores performance against
predicted HR-for-pace, so the same pace at a higher HR always scores badly. It
is a fatigue flag, not a bad session.

### Weekly balance vs the plan's template

| Plan category | Target/week | This week |
| --- | --- | --- |
| Zone 2 | 1–2 | **1** (Tue; Thu overshot, Mon undershot) |
| Hard aerobic intervals | ~1 | **0** |
| Explosive repeated efforts | ~1 | **0** |
| Hard sparring | ~1 | **0** |
| Pads / bag / technical boxing | additional | **0** |
| Strength / power | additional | 1 (shoulder rehab only) |

Three aerobic sessions and one rehab session. **No boxing of any kind was
recorded this week**, and no interval or explosive work. The week was entirely
base, with the one Zone 2 session that mattered partly overcooked.

---

## Week of 31 Aug – 3 Sep 2026 (in progress)

### Sessions recorded

| Day | Session | Duration | Avg HR | Source |
| --- | --- | --- | --- | --- |
| Mon 31 | Upper pull (strength) | 45:20 | — | Hevy only |
| Wed 2 | Indoor "run" — incline walk, 2.71 km | 30:00 | 118 | COROS |
| Wed 2 | Core (strength) | 18:43 | — | Hevy only |
| Thu 3 | Outdoor run, 8.75 km | 53:42 | **143** | COROS |

No boxing and no interval work recorded 28 Aug – 3 Sep.

### Wed 2 Sep — the incline walk, measured

Logged as **Indoor Run** (sport type `101`), but the numbers are walking.
This is the session the plan asked for in place of a second long run.

**Recording overran the session.** The watch was left running at the end; the
athlete confirmed 30 minutes. FIT data agrees precisely — movement stops at
31:00 (4 m covered, cadence 3), after which HR simply decays. **All figures
below are trimmed to 30:00.** COROS's own totals (37:47, 2.94 km, 12:50 /km,
avg HR 114) are inflated by ~7:47 of dead time and should not be used.

| | Trimmed (real) | As recorded |
| --- | --- | --- |
| Duration | **30:00** | 37:47 |
| Distance | **2.71 km** | 2.94 km |
| Average pace | **11:04 /km** | 12:50 /km |
| Average HR | **118** | 114 |
| Max HR | 140 | 140 |
| Training load | ~35 (dead time was low-HR; barely affected) | 35 |
| Aerobic TE / Anaerobic TE | 2.0 / 0.0 | 2.0 / 0.0 |
| Training focus | Base | Base |

COROS's *moving* average pace (11:00 /km) was already correct — it excluded the
stopped time. Only the headline figures were contaminated.

Per-second HR from the FIT file, trimmed (1,800 samples):

| Band | % | Minutes |
| --- | --- | --- |
| Below Z2 (<126) | 61.9% | 18.6 |
| In Z2 (126–141) | 38.1% | 11.4 |
| — of which target (135–140) | 8.9% | 2.7 |
| Above ceiling (>142) | **0.0%** | 0.0 |
| Above LTHR (>157) | **0.0%** | 0.0 |

**The trim moves the percentages, not the work.** Time in Z2 went from 11.6 to
11.4 minutes and time in target stayed at 2.7. The discarded 7:47 was entirely
below Zone 2, so the session looks better as a ratio and is identical as a
stimulus.

Five-minute blocks (all within the real 30 minutes):

| Block | Avg HR | Max |
| --- | --- | --- |
| 0–5 | 94.6 | 128 |
| 5–10 | 119.8 | 135 |
| 10–15 | 115.3 | 126 |
| 15–20 | 115.1 | 123 |
| 20–25 | **131.0** | 139 |
| 25–30 | **133.7** | 140 |

### Assessment

**The ceiling was respected for the first time on record.** Zero seconds above
142, zero above LTHR, load ~35 against 158 for the Thursday run. This is a
correctly-easy session and it directly answers the plan's Thursday
recommendation.

**The session ended while still working — there was no fade.** Minutes 26–29
held 131–138 bpm at a steady 74–80 m/min. The walk finished inside the target
band, not falling out of it. Whatever limited this session, it was not capacity.

**The whole problem is the front end.** The first 20 minutes averaged ~111 bpm;
only the last 10 reached 131–134. Just 2.7 minutes landed in the 135–140 target
the plan named. Structure, not effort, is the limiter.

**The incline hypothesis is confirmed.** The slowest portion of the session
(cadence collapsing to ~55 spm, ~17 min/km equivalent) carried the *highest*
heart rate. Slower pace + higher HR + shorter stride is the signature of walking
up a gradient. Flat portions sat around 115; the gradient portion reached
131–134. The gradient does all the work — see
[Standing finding 1](#1-zone-2-discipline-is-the-live-issue).

**Suggested fix — hold one setting, do not raise the gradient.** See
[Treadmill settings](#treadmill-settings-what-actually-works) below. 5 min
warm-up, then ~25 min held unbroken at gradient 6 / 6 km/h. Same 30 minutes,
roughly 25 min in target instead of 2.7.

### Treadmill settings — what actually works {#treadmill-settings-what-actually-works}

Athlete-reported, 2 Sep: **gradient cannot be used as the intensity lever.**
At the treadmill maximum of 15% the legs give out before the heart rate rises.
Gradient 6 with a fast walk (6 km/h) is what raised HR successfully.

Per-minute reconstruction from the FIT file confirms it:

| Minutes | Watch speed | Cadence | Avg HR | What it was |
| --- | --- | --- | --- | --- |
| 0–2 | 2.8–4.3 km/h | 42–53 | 70–91 | Warm-up |
| 3–4 | **8.1–9.7 km/h** | 74–81 | 105–122 | Running |
| 5–19 | 3.8–8.5 km/h, constantly changing | 48–76 | 104–124 | Unsettled |
| **20–29** | **4.8–5.1 km/h, steady** | 55–57 | **122 → 138** | Gradient 6, fast walk |

**Two findings.**

**1. The limiter is muscular, not cardiac.** Legs failing at 15% gradient with
cardio to spare is the same limiter as the outdoor "run out of leg" problem —
calf, soleus and quad endurance. Steep incline walking is a strength-endurance
exercise before it is an aerobic one, and this athlete does not yet have the
base to use it. This promotes
[Standing finding 3](#3-missing-calf-and-lower-leg-work) from a nice-to-have to
**the constraint gating the preferred Zone 2 tool**.

**2. HR was still climbing when the session ended.** Across minutes 20–29 the
speed was flat (4.8–5.1 km/h) but HR went 122 → 132 → 137 → 138 and held
131–138. That is normal cardiac lag and drift: HR needs 3–5 minutes to meet a
workload and keeps rising after. Minutes 5–19 changed speed every minute or two,
so HR never settled anywhere. **The setting was never the problem — the holding
was.** Another 10 minutes at the same gradient 6 / 6 km/h would very likely have
drifted into 138–142 unaided.

**Prescription.** Warm up 5 min. Set gradient 6, 6 km/h, and *do not touch the
controls* for 25 min. Expect 135–140 by minute 8–10. If HR plateaus below 135
once fitness improves, add **speed** (6.2, 6.4 km/h) — not gradient. Revisit
gradient only after calf/soleus strength work is established.

**Watch calibration.** The watch recorded ~4.9 km/h during a block the athlete
set at 6 km/h — indoor speed is estimated from stride, not read from the
treadmill, so it under-reads by roughly 15–20%. Indoor distance and pace figures
(including the 2.71 km and 11:04 /km above) are correspondingly understated.
**Heart rate is unaffected and remains the metric to train by indoors.**

**Leg-load note.** Low impact, aerobic stimulus, no pounding — the right tool
for the running-durability problem while the base is rebuilt. It does not
substitute for calf/soleus strength work
(see [Standing finding 3](#3-missing-calf-and-lower-leg-work)).

**Data-hygiene note.** Stopping the watch at the end matters: 7:47 of dead time
shifted average HR by 4 bpm, pace by 1:46 /km and distance by 230 m. Future
sessions should be trimmed or verified before being read against the plan.

### Thu 3 Sep — the run, measured

Same Sydney course as 25 and 27 Aug. **The fastest and the most expensive run
on record.** Run the day after the incline walk, and the third run in nine days.

| | Tue 25 Aug | Thu 27 Aug | **Thu 3 Sep** |
| --- | --- | --- | --- |
| Distance | 8.59 km | 8.41 km | **8.75 km** |
| Duration | 54:35 | 53:09 | 53:42 |
| Average pace | 6:21 /km | 6:19 /km | **6:08 /km** |
| Adjusted pace (grade-corrected) | 6:15 /km | 6:05 /km | **5:55 /km** |
| Best kilometre | 5:34 | 5:42 | **5:18** |
| Elevation gain | 56 m | 88 m | 88 m |
| Average HR | 137 | **146** | 143 |
| Max HR | 153 | 162 | 161 |
| Cadence | 161 | 163 | 162 |
| Stride length | 0.98 m | 0.97 m | **1.01 m** |
| Average power | 250 W | 254 W | **261 W** |
| Training load | 134 | 158 | **197** |
| Aerobic / Anaerobic TE | 3.0 / 3.0 | 3.1 / 3.5 | 3.4 / **3.9** |
| Training focus | Tempo | Anaerobic | Anaerobic |
| COROS "Performance" | Best | Poor | Good |

Time in zone, per-second from FIT (all three recomputed with one method):

| Band | Tue 25 Aug | Thu 27 Aug | **Thu 3 Sep** |
| --- | --- | --- | --- |
| Below Z2 (<126) | 4.7% · 2.5 min | 4.0% · 2.1 min | 10.3% · 5.5 min |
| **In Z2 (126–141)** | **64.1% · 34.9 min** | 25.4% · 13.5 min | **18.4% · 9.9 min** |
| — of which target (135–140) | 29.8% · 16.2 min | 18.6% · 9.9 min | **7.8% · 4.2 min** |
| **Above ceiling (>142)** | 24.3% · 13.2 min | 67.7% · 36.0 min | **68.1% · 36.6 min** |
| Above LTHR (>157) | 0.0% | 11.6% · 6.2 min | 4.5% · 2.4 min |

### Assessment — 3 Sep

**Aerobic efficiency genuinely improved.** Against 27 Aug on the identical
course and identical 88 m of climb: **11 s/km faster at 3 bpm lower**, adjusted
pace 6:05 → 5:55, and time above lactate threshold cut from 6.2 to 2.4 minutes.
Stride length rose to 1.01 m — the longest recorded — at unchanged cadence, so
the extra speed came from stride, not turnover. This is a real week-on-week
gain and COROS flipping its grade from "Poor" to "Good" reflects it.

**It was still not the Zone 2 session the plan asked for — it was the worst of
the three on that measure.** 68% above the 142 ceiling and only **4.2 minutes**
in the 135–140 target, against 9.9 on 27 Aug and 16.2 on 25 Aug. Three runs, and
the amount of correctly-pitched aerobic work has fallen every time.

**Training load 197 is the highest figure in the file** — 47% above 27 Aug,
which the plan had already flagged as too costly for its purpose. It came one
day after the treadmill session and made three runs in nine days.

**The first 15 minutes were a textbook Zone 2 run.** Minutes 5–15 averaged
137.7 and 135.0 bpm at roughly 6:05 /km. The session then left the band at
minute 15 and never returned: every five-minute block from 15:00 onward sat
between 143 and 154.

| Block | 25 Aug | 27 Aug | **3 Sep** |
| --- | --- | --- | --- |
| 0–5 | 138.4 | 139.6 | 111.6 |
| 5–10 | 127.3 | 139.4 | 137.7 |
| 10–15 | 136.1 | **159.7** | 135.0 |
| 15–20 | 142.7 | 147.3 | **148.1** |
| 20–25 | 136.1 | 149.9 | 149.5 |
| 25–30 | 141.1 | 150.8 | 148.9 |
| 30–35 | 140.0 | 149.5 | 148.3 |
| 35–40 | 140.4 | 141.5 | **154.0** |
| 40–45 | 131.8 | 141.8 | 143.2 |
| 45–50 | 136.6 | 141.5 | 148.8 |
| 50+ | 141.1 | 151.2 | 148.3 |

**Cause: the middle kilometres were raced, not run.** Per-km laps show km 3–6 at
5:34, 5:47, 5:58 and 5:53 /km — up to 13% faster than session average, with a
best kilometre of 5:18. HR went 136 → 145 → 149 → 150 across them. It then
**failed to come back down**: km 7 slowed to 6:25 /km but HR stayed at 152.
So this is over-pacing first and inability to recover second, not passive drift.

**Decoupling — the three runs have three different failure shapes.** Halves
computed identically for all three:

| | 1st half | 2nd half | Pace change | HR change |
| --- | --- | --- | --- | --- |
| Tue 25 Aug | 6:08 @ 136.4 | 6:33 @ 138.4 | **+25 s/km** | +2.0 bpm |
| Thu 27 Aug | 6:19 @ 146.9 | 6:18 @ 145.9 | −1 s/km | −1.0 bpm |
| **Thu 3 Sep** | **6:01 @ 136.8** | 6:15 @ 149.0 | +14 s/km | **+12.2 bpm** |

- **25 Aug** — cardiac stability, pacing failure. HR flat, legs faded 25 s/km.
- **27 Aug** — flat both halves, but pitched too high from the first minute.
- **3 Sep** — **started correctly and then decoupled.** Losing 14 s/km *and*
  gaining 12 bpm is aerobic durability being exceeded, not a mechanical failure.

*These half-splits supersede the +32 / +15 s/km figures quoted in the 27 Aug
review, which used a different (lap-based) split. All three are now computed
the same way.*

**The limiter today was cardiac, not muscular.** Cadence held 161 → 162 across
the halves and stride length was the longest on record, so the legs did not go —
which is the opposite of the treadmill session's finding. The calf/soleus
constraint gates *incline walking*; **aerobic durability past ~15 minutes** gates
*running*. They are two different problems and both are live.

**The Anaerobic TE 3.9 is not HR-driven** — see
[Standing finding 7](#7-possible-max-hr--zone-mis-set), now corrected. 3 Sep
spent *less* time above every HR threshold than 27 Aug yet scored higher.

**Prescription.** The first 15 minutes were the session — the rest was a
different workout bolted on. Hold **6:05–6:15 /km** for the whole hour and
refuse to go faster on the downhills and flats; if HR crosses 142 at minute 15,
slow to 6:30 rather than holding pace. That converts a load-197 anaerobic run
into the Zone 2 session the plan has now asked for three times.

### Shoulder-relevant note

Neither strength session included overhead pressing, matching the rehab plan's
avoid-list. Pulling volume was heavy (Pull Ups 16/10/7/7; Lat Pulldown and
Seated Row both 120 kg × 3 sets). **Two shoulder rehab sessions on record —
26 Aug (48:57) and 4 Sep (13:03).** The rehab plan depends on frequency; the
gap was nine days and the second was a quarter the length of the first.

Core session: Cable Pallof Press 35 kg × 10/10/10 (no decay — has room to
increase), Cable Crunch 80 kg × 16/16/11, Cossack Squats 14 kg × 12/12/12.
Pallof press is anti-rotation trunk work that loads neither the cuff nor
overhead position — compatible with the rehab plan.

---

## Week of 4–10 Sep 2026

### Sessions recorded

| Day | Session | Duration | Avg HR | Source |
| --- | --- | --- | --- | --- |
| Fri 4 | Calf & Soleus Endurance | 13:12 | — | Hevy (2 exercises, 6 sets) |
| Fri 4 | W1 | 14:47 | — | Hevy |
| Fri 4 | Shoulder Rehab | 13:03 | — | Hevy |
| Mon 7 | W2 | **2:20:35** | — | Hevy (8 ex, 28 sets) |
| Thu 10 | Outdoor run, 8.35 km | 51:00 | **150** | COROS |

**Two COROS activities in seven days**, both runs, both hard. No Zone 2 session,
no interval session, no boxing. Daily steps on 6, 8 and 9 Sep were 1,497 / 1,422
/ 2,326 — near-sedentary between hard efforts.

**Credit where due:** the calf/soleus routine was performed for the first time
(4 Sep) and a shoulder rehab session was done the same morning, the first since
26 Aug. Both were standing open items.

### Thu 10 Sep — the run, measured

Same Sydney course, 89 m of climb (88 m on 3 Sep). **Same pace, seven beats
higher.**

| | Tue 25 Aug | Thu 27 Aug | Thu 3 Sep | **Thu 10 Sep** |
| --- | --- | --- | --- | --- |
| Distance | 8.59 km | 8.41 km | 8.75 km | 8.35 km |
| Duration | 54:35 | 53:09 | 53:42 | 51:00 |
| Average pace | 6:21 | 6:19 | 6:08 | **6:07** |
| Adjusted pace | 6:15 | 6:05 | 5:55 | **5:53** |
| Average HR | 137 | 146 | 143 | **150** |
| Max HR | 153 | 162 | 161 | 163 |
| Cadence | 161 | 163 | 162 | **165** |
| Training load | 134 | 158 | 197 | 179 |
| Training focus | Tempo | Anaerobic | Anaerobic | **Threshold** |
| COROS "Performance" | Best | Poor | Good | **Below Average** |

Time in the athlete's own COROS zones (minutes):

| Zone | 25 Aug | 27 Aug | 3 Sep | **10 Sep** |
| --- | --- | --- | --- | --- |
| Recovery <126 | 2.5 | 2.1 | 5.5 | 2.6 |
| **Aerobic Endurance 126–141** | **34.9** | 13.5 | 9.9 | **7.3** |
| Aerobic Power 142–149 | 16.4 | 14.2 | 19.2 | 6.6 |
| **Threshold 150–160** | 0.6 | 21.8 | 19.0 | **28.7** |
| Anaerobic Endurance 161–166 | 0.0 | 1.5 | 0.1 | **5.8** |

**Time above LTHR 157: 19.3 minutes** — against 2.4 on 3 Sep and 6.2 on 27 Aug.

### Assessment — 10 Sep

**Intent: the athlete states this run was deliberately intended to be faster.**
It should therefore be judged as a hard effort, not as a failed Zone 2 session.
On its own terms it did not succeed — see below — but it was not an execution
error against a Zone 2 intention, and the initial assessment framed it wrongly.

**It did not achieve its goal.** Average pace 6:07 vs 6:08, adjusted 5:53 vs
5:55 — inside noise. The shorter total time (51:00 vs 53:42) is 400 m less
distance, not more speed. **Best kilometre was 5 s slower** (5:23 vs 5:18).
Same pace, +7.5 bpm.

**The limiting mechanism, in one comparison.** Kilometre 3 both weeks:

| | Pace | Lap avg HR |
| --- | --- | --- |
| 3 Sep km 3 | 5:34 | 145 |
| **10 Sep km 3** | 5:32 | **159** |

Two seconds faster for **fourteen beats more**, and 159 is above LTHR 157 — over
the line at km 3 of 8. The surge was then repaid: km 4 fell to 6:17 with HR
still 150. On 3 Sep the same surge cost 13 s in the following km; on 10 Sep it
cost 45 s. **Fast kilometres are being cashed in for slow ones, netting no
faster overall.** This, not willingness, is what caps the pace.

**Last week's efficiency gain has reversed.** On 3 Sep the athlete ran 11 s/km
faster than 27 Aug at 3 bpm lower. Today, at an adjusted pace two seconds
*faster* than 3 Sep on the same course, average HR was **+7.5 bpm**. Higher
almost block for block, and worst at the end: the final five minutes averaged
158.0 against 148.8 a week ago.

**This was a threshold workout, not a base run.** 28.7 minutes in the Threshold
zone and 19.3 minutes above lactate threshold. COROS labelled the focus
"Threshold" and graded it Below Average.

**Every trend is monotonic and going the wrong way** across four runs:

| | 25 Aug | 27 Aug | 3 Sep | 10 Sep |
| --- | --- | --- | --- | --- |
| Aerobic Endurance (min) | 34.9 | 13.5 | 9.9 | **7.3** |
| Threshold (min) | 0.6 | 21.8 | 19.0 | **28.7** |
| Above LTHR (min) | 0.0 | 6.2 | 2.4 | **19.3** |
| **Load per Z2 minute** | **3.8** | 11.7 | 19.9 | **24.5** |

**Three independent fatigue markers agree.**

- **Resting HR 56 → 59** (+3 bpm week on week)
- **Recovery 69%, "Light training recommended"**, 32 h to full — the run was
  done in that state
- **HR at a fixed pace up 7.5 bpm** on an identical course

**It is not a volume problem.** Two runs and roughly 3 h of gym in seven days,
with three days under 2,500 steps. The issue is that *everything* performed is
hard and nothing is easy — no Zone 2, no easy volume, then a threshold effort
from a sedentary base.

**Pacing contributed but does not explain it.** The first five minutes averaged
127.7 against 111.6 last week, and km 1 (26 m of climb) spiked to 161 — above
LTHR inside the first kilometre, with no warm-up. That accounts for perhaps
1.5 bpm of the 7.5. The rest is spread through the run and concentrated at the
end, which is the signature of under-recovery rather than a bad first mile.

**Worth ruling out:** a minor illness or unusual heat would produce the same
signature. If the athlete felt unwell or the day was hot, discount the fatigue
reading accordingly.

**Revised prescription — two runs a week, one hard and structured, one easy.**
The athlete wants to train hard; the fix is to redirect that, not suppress it.

*Hard session — replace the fast continuous run with intervals.*
**5 × 3 min hard, 1 min easy jog between** (~25 min with warm-up/cool-down).
Rationale: a continuous 8 km trains holding one speed for 50 minutes, whereas
the fight is five 3-minute rounds with 1-minute rests. Intervals train lactate
clearance during the recovery minute — the determinant of rounds 4 and 5 — cost
less total fatigue than 10 Sep did, and are measurable week to week. This also
fills the plan's ~1 interval session per week, of which **zero** have been done.

*Easy session — capped by heart rate, not pace.* Slow to 6:30 or walk when HR
crosses 142. Expect it to feel far too easy and to run 30–45 s/km slower than
desired; that is the session working.

**Why the easy run is the one that raises the fast pace.** Threshold pace rises
when the aerobic base beneath it rises. Four consecutive hard runs with nothing
easy is squeezing a tank that is not being refilled — the +7.5 bpm at fixed pace
and the +3 resting HR are that tank reading empty.

---

## Week of 11–16 Sep 2026

### Sessions recorded

| Day | Session | Duration | Avg HR | Source |
| --- | --- | --- | --- | --- |
| Fri 11 | Quick Gym 1 (core/triceps) | 23:20 | — | Hevy |
| Fri 11 | Shoulder Rehab — 2 exercises only | 1:00:29 (timer) | — | Hevy |
| Mon 14 | W4 (deadlift 120 kg, sled, rows) | 55:15 | — | Hevy |
| Wed 16 | Outdoor run, 8.14 km | 50:57 | **157** | COROS |

Steps 14–15 Sep: 2,306 / 2,447. No calf/soleus session since 4 Sep. No
boxing recorded. Recovery read **100%** and resting HR **56** before the run.

### Wed 16 Sep — the run, measured

Same Sydney course, 58 m of climb. Prescriptions in force (13 Sep): an easy run
under 142, or a Norwegian 4×4. **The run matched neither.**

| | Easy run target | 4×4 target | Actual |
| --- | --- | --- | --- |
| Time in 126–141 | ~40 min | — | **2.5 min** |
| Time above 142 | 0 | ~16 min (4 reps) | **47.7 min** |
| Recoveries to ~125 | — | 3 × 3 min | **none after minute 4** |
| Time at 161–170 | 0 | ~16 min in 4 blocks | 12.4 min, in one block |

Per-second, in the athlete's own zones: Aerobic Endurance 2.5 min, Threshold
34.4, Anaerobic Endurance 7.2, Anaerobic Power **5.2** (first time above 166 on
record). Above LTHR **29.3 min** (previous record 19.3). Max HR **175** — 12
above any prior run and 98% of the 179 setting.

Five-minute blocks: 137 → 156.5 → 155.6 → 158.4 → 158.7 → **163.5 → 169.8** →
158.7 → 156.2 → 158.6. One continuous plateau at threshold with a single surge.

Halves: 6:06 @ 153.4 → 6:25 @ 161.2 (+19 s/km, +7.8 bpm). Cadence 163 → 162.

Per-km: crossed 142 at 3:14 and 157 at 4:05. Km 5–6 at 164–168 average, km 6
at 5:48 /km peaking 175. **Km 7 collapsed to 6:57 /km with HR still 157** — the
same surge-then-repay pattern as 3 and 10 Sep, larger each time (following-km
penalty 13 s → 45 s → 69 s).

Training load 160, TE 3.1 / 3.0, focus Tempo, graded Below Average.
**Load per Aerobic Endurance minute: 64** (previous 24.5).

### Assessment — 16 Sep

**Three-week trend, all on the same course:**

| | 3 Sep | 10 Sep | 16 Sep |
| --- | --- | --- | --- |
| Adjusted pace | 5:55 | 5:53 | **6:07** |
| Avg HR | 143 | 150 | **157** |
| Above LTHR | 2.4 min | 19.3 min | **29.3 min** |
| Best km | 5:18 | 5:23 | **5:35** |
| Resting HR before | 56 | 59 | 56 |
| Recovery before | 70% | 69% | **100%** |

**Intent (athlete, 16 Sep): this was meant to be the easy run.** Large hills
were avoided (58 m gain vs 89), pace was eased to 6:16 /km, and HR felt
"unreasonably high" from the start. Context supplied: W4 gym session on Mon 14
Sep (deadlift 120 kg × 4 × 3, sled pushes, single-leg RDL), nothing on Tue,
poor diet on Tue and no usual carbohydrate that night.

**Correction to the first draft of this assessment:** it called the start
"fully recovered" on the strength of COROS recovery 100%. COROS never sees gym
sessions, so that figure was computed without the 14 Sep session. Recovery
status is not evidence of freshness on any day within ~48–72 h of a Hevy
session.

**Reading.** Two same-day factors plausibly raised HR at a given pace: residual
posterior-chain fatigue from a heavy deadlift/sled session 48 h earlier, and
low carbohydrate availability (with possible under-hydration) going into a
morning run. Both are known to raise HR at a fixed submaximal workload. They
account for some of today's +7 bpm over 10 Sep. They do not account for the
three-week trend, and they do not account for crossing 142 at 3:14: on a day
when HR runs high, an HR-capped easy run simply becomes slower — that is the
point of capping by HR rather than by feel. **The executional gap is that the
run was paced to a "slow" pace, not to the 142 cap.** [I]

**Route note revised.** Hills were avoided, yet km 4 still carried 27 m of
climb and the run still crossed 142 inside four minutes. The route was not the
binding constraint today; pace was.

**The course is part of the problem for the easy session.** Km 4 carries 27 m
of climb; every run on this loop has crossed 142 inside 4 minutes. An easy run
under 142 on this loop would require walking the climbs. The plan's incline
walk, or a flat route, removes that.

**Arithmetic:** the session ran 47.7 minutes above the ceiling the plan sets
for its base session, delivered 2.5 minutes of the stimulus that session exists
to deliver, and cost load 160. Five runs, five declines in Aerobic Endurance
time. This was the first *attempt* at the easy session; it was not executed to
the HR cap.

## Watch setup — checklist

**Status: probably nothing needs changing.** Max HR 179 is verified correct and
the plan's band is COROS's own LT Zone 2 at threshold HR 157. One number is
still unread.

| # | Action | Basis | State |
| --- | --- | --- | --- |
| 1 | Read threshold HR at Profile → Settings → Heart Rate Zones, LT zone type. Change nothing yet | COROS docs | **outstanding** |
| 2 | If it reads 157 and Zone 2 shows 126–141 — stop, nothing to do | arithmetic | pending 1 |
| 3 | If it differs, custom-set Zone 2 to 126–141 (threshold HR itself is not editable) | COROS docs | pending 1 |
| 4 | Leave max HR at 179 | verified 3 Sep | **done** |
| 5 | Resting HR — optional; 56 already stored, and Max-HR/LT zones do not use it | API + COROS docs | optional |
| 6 | Running Fitness Test, outdoors, ~40 min — for threshold *pace*, not HR | COROS docs | deferred |

**Warning on step 6.** The test rewrites threshold HR and max HR as well as
threshold pace. If 157 / 179 are confirmed correct at step 1, the test can move
settings that are currently right. It fixes the pace numbers (5:20 /km, VO2max
41) at that risk. Not urgent, and not while recovery reads 70% / 34 h.

**The honest priority.** None of the above is the limiter. Three of four aerobic
sessions missed the band by execution, not by mis-configuration — the settings
thread began with an unsound inference from the TE scores
([Standing finding 7](#7-possible-max-hr--zone-mis-set)) and every hypothesis in
it has since been refuted. Running the sessions at the prescribed intensity
matters more than any setting on this list.

---

## What the COROS API can and cannot return

Checked exhaustively on 3 Sep, across every MCP endpoint and the raw FIT files.

| Value | Retrievable | Source |
| --- | --- | --- |
| Threshold **pace** (5:20 /km) | yes | `queryFitnessAssessmentOverview` |
| VO2max (41), running level (72), race predictions | yes | same |
| Resting HR (**56**) and HRV baseline (**42 ms**) | yes | `queryDailyHealthData` header |
| Recovery status (70%, 34 h to full) | yes | `queryRecoveryStatus` |
| Per-session max HR and per-second HR | yes | FIT / `getActivityDetail` |
| **Threshold HR (LTHR)** | **no** | — |
| **Max HR profile setting (179)** | **no** | — |
| **Zone boundaries and zone model** | **no** | — |
| Daily resting-HR series | empty | `queryRestingHeartRate` — 14 days no data |

COROS **strips zone data from exported FIT files**: there is no `zones_target`,
`hr_zone` or `user_profile` message. The session message carries
`max_heart_rate = 161`, which is that run's *peak*, not the profile setting.

**Consequence.** The two numbers that define the Zone 2 band — threshold HR and
the selected zone model — are readable only in the app. Zone drift therefore
cannot be detected automatically, which is the argument for locking custom
boundaries at 126–141 rather than relying on the algorithm's value.

**Refinement on resting HR.** Earlier notes said resting HR was empty. More
precisely: a **profile-level value of 56 bpm exists** (with an HRV baseline of
42 ms), but the *daily* series is empty for all 14 days checked. The 56 is a
stored figure of unknown vintage, not a current measurement.

---

## Standing findings

### 1. Zone 2 discipline is the live issue

Two of three aerobic sessions missed the band in opposite directions — Monday
too easy, Thursday far too hard. Only Tuesday landed. The plan's core principle
is *"Make the heart work without unnecessarily exhausting the legs"*; Thursday
did the reverse.

The plan's suggested fix is already written down and was not used: **incline
treadmill walking at 135–140 bpm**, with HR driving speed and incline.

### 2. The running base does not support this running volume

Independent of the HR issue: **12 runs in 29 weeks, averaging 2.6 km/week**,
with gaps of 48, 39 and 29 days. The last nine days added **25.8 km across three
runs**, a ~9× jump on the trailing average. The plan's preference for incline walking over
running is well supported by this — running currently carries a high
musculoskeletal cost for this athlete because the run base is thin.

If running stays in the mix, the plan's own progression logic applies to
duration, not distance: build frequency at **short** durations first.

### 3. Missing: calf and lower-leg work

No calf, soleus or ankle work appears in 30 logged Hevy sessions. Soleus
endurance underpins both run durability and late-round footwork. Front squat,
hip thrust, RDL, deadlift and jumps are all present — lower-body *strength* is
not the gap; repeated elastic endurance is.

### 3b. Cost per minute of target stimulus

A single decision number. Training load divided by minutes in Aerobic
Endurance — what each minute of the adaptation the plan actually wants costs
in fatigue:

| Run | Load | Z2 minutes | Load per Z2 minute |
| --- | --- | --- | --- |
| Tue 25 Aug | 134 | 34.9 | **3.8** |
| Thu 27 Aug | 158 | 13.5 | 11.7 |
| Thu 3 Sep | 197 | 9.9 | 19.9 |
| **Thu 10 Sep** | 179 | 7.3 | **24.5** |

**10 Sep was 6.4× more expensive than 25 Aug per unit of base built**, and the
figure has risen at every single run. Use this in preference to load alone: a
rising load figure is not itself bad, but a rising *cost per Z2 minute* means
the session is drifting out of its purpose. Note that 10 Sep's load (179) was
*lower* than 3 Sep's (197) while its cost per Z2 minute was higher — load alone
would have called this an easier week.

### 4. Unreconciled conflict with the shoulder rehab plan

The conditioning plan and
[boxing-shoulder-pain-prevention-plan.md](../shoulder-rehab/boxing-shoulder-pain-prevention-plan.md)
do not reference each other, and they disagree:

| Conditioning plan wants | Shoulder plan says |
| --- | --- |
| Hard sparring ~1/week | Avoid hard missed punches |
| Pads / bag work as additional volume | Reduce high-volume hard bag work |
| Repeated maximal punching (3s on / 10s off) | Build cuff capacity first |

Both cannot be followed as written. This needs an explicit decision, and it is
the most consequential open item in the file.

### 5. The demand side is invisible

Neither COROS nor Hevy has recorded a single boxing session. COROS has no
boxing, strength or gym records at all since April — the watch is used only for
running and cycling. Boxing volume, the variable both plans care most about, is
currently unmeasured.

### 6. Chest strap {#chest-strap}

The plan recommends a Polar H10 over *"the PACE 2 wrist optical sensor."* The
runs were recorded on a **PACE 3**, whose optical sensor is materially better
than the PACE 2's. The recommendation still stands — narrow HR bands justify a
strap, and this week's overshoot shows why — but the premise is out of date.

### 7. Anaerobic TE does not track heart rate — and the HR zones are correct {#7-possible-max-hr--zone-mis-set}

**Corrected 3 Sep — the original version of this finding was wrong.** It claimed
the high Anaerobic TE scores were evidence that max HR / HR zones are mis-set.
Time above threshold, measured per-second:

| Minutes above | >140 | >145 | >150 | >155 | >157 | >160 | Anaerobic TE |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Tue 25 Aug | 20.4 | 5.2 | 0.5 | 0.0 | 0.0 | 0.0 | 3.0 |
| Thu 27 Aug | 39.5 | 29.8 | 21.3 | 7.8 | 6.2 | 1.5 | 3.5 |
| **Thu 3 Sep** | 39.6 | 28.7 | **16.6** | **4.2** | **2.4** | **0.1** | **3.9** |

3 Sep was lower than 27 Aug on **every** HR measure — average (143 vs 146), max
(161 vs 162) and time above all six thresholds — and still scored *higher*
Anaerobic TE. Whatever drives that score, it is not HR exposure, so **the TE
figures are not evidence about the HR zones either way.**

The plausible driver is pace/power against COROS's **Threshold Pace of
5:20 /km**: 3 Sep was the faster run (6:08 vs 6:19, best km 5:18 vs 5:42,
261 W vs 254 W). That threshold pace derives from a **Running Fitness Test on
6 Feb 2026** — seven months stale — and is the number worth rechecking.

**Resolved 3 Sep — the HR zones are fine.** Athlete read the app: **max HR is
set to 179**. The worry that auto-update had latched onto 162 was unfounded.
179 sits *above* all three age estimates (220−age = 174; Tanaka = 176;
COROS's 207−0.7×age = 175), so it was measured rather than estimated — almost
certainly from the **6 Feb 2026 Running Fitness Test**, which outputs max HR.

It corroborates the plan's LTHR: **157 / 179 = 88%**, a normal
threshold-to-max ratio. Plan and watch agree. The derived bands also check out —
the plan's Zone 2 of 126–141 is 70–79% of 179, a standard Zone 2 definition.

**This thread is now closed.** It was raised on the strength of the TE scores,
which turned out not to track HR, and the remaining hypothesis has been checked
and refuted. Against max 179, the 3 Sep run peaked at 161 = **90% of max** with
average 143 = 80%: hard, but with real headroom, which supports the reading that
the limiter was aerobic durability rather than any ceiling.

What remains suspect is **Threshold Pace 5:20 /km** and **VO2max 41** — a pace
side issue, not an HR one, and the reason to run the fitness test.

---

## Open items

- [ ] **Reconcile conditioning plan vs shoulder rehab plan** on sparring and bag work
- [x] Decide: incline walking vs running for Zone 2 sessions — **incline walking chosen and executed 2 Sep**; refine the structure (longer working block) rather than the choice
- [ ] Add an aerobic interval session (plan calls for ~1/week; zero so far)
- [ ] Start recording boxing on the watch (COROS sport type `906`)
- [ ] **Run the COROS Running Fitness Test, outdoors** (~40 min). This is the
      *only* way to update Threshold HR — COROS does not accept a manually
      entered LTHR. It refreshes Threshold Pace (currently 5:20 /km, dated
      6 Feb 2026) and Max HR in the same session. Not until load ratio settles.
- [x] Verify max HR in the app — **done 3 Sep: set to 179**, above all age
      estimates, so measured (likely the 6 Feb fitness test) and consistent with
      LTHR 157 at 88% of max. **No change needed.** Settings live at
      Profile → Settings → Heart Rate Zones, which also holds resting HR; both
      manually settable, unlike LTHR
- [x] **Add calf/soleus endurance work** — routine built 2 Sep:
      `routines/calf-soleus-endurance.json` → Hevy "Calf & Soleus Endurance"
      (`717e84d5-fe99-4ad9-a2ee-dbde44b079ba`, Rehab folder). 2–3×/week.
      **First performed 4 Sep** (partial — 2 exercises, 6 sets, not the full 4).
      Remaining: run it complete, 2–3×/week, and progress per the notes
- [ ] Confirm athlete weight and age in the plan document (96 kg/47 vs 91 kg/46)
- [ ] Resting HR — **athlete has declined overnight wear (3 Sep)**. No longer a
      blocker: use the on-watch **Wellness Check** (hold BACK/LAP → Toolbox,
      30–60 s) on waking for 3–5 mornings, then enter the value manually at
      Profile → Settings → Heart Rate Zones. Automatic resting HR *does* require
      sleep data, so it will stay empty; sleep and sleep-HRV metrics are
      forgone by choice and should not be relied on for recovery tracking

---

## Changelog

- **2026-09-21** (rev 21) — Mon 21 Sep run: 8.15 km, 6:13 /km (adj 6:05),
  avg HR **145**, max 156, load 154, zero time above LTHR. Same course as
  16 Sep: 12 bpm lower at the same pace, and comparable to 3 Sep — the 16 Sep
  "three-week decline" is corrected to a bad-state day, not base erosion. HR
  flat (143.5–145.7) from minute 15 to the end, no cardiac drift, first such
  run on record. Still 36.4 min above 142 (29.9 in Aerobic Power), so not the
  easy session, but the nearest miss yet. Resting HR 49, unexplained drop.
  Hevy silent since 17 Sep. Weekly layout must move to Mon–Fri (athlete: weekends
  off, no weekday off).
- **2026-09-18** (rev 20) — First Norwegian 4×4 (air bike, legs only, 34:52).
  Reps reconstructed from rep-end lap markers. End-of-rep HR 138 / 138 / 148 /
  143 vs 158–168 target; COROS Base, load 41. Recovery drops 22 / 26 / 34 good.
  Wrist sensor dropout to 72 bpm mid-warm-up while pedalling. Causes: legs-only
  quad limit with Power B (deadlift 130 kg) 24 h prior; reps 1–2 steady-state.
  Weekly layout revised so the 4×4 sits 96 h after heavy lower-body work. Hevy
  17 Sep: Shoulder Rehab (the rapid plan's five, 15-rep targets, band loads
  logged) and Power B self-censored of pressing. Footwork not recorded on the
  watch. Details in `README.md`.
- **2026-09-16** (rev 19) — Athlete stated the 16 Sep run was intended as the
  easy run, hills avoided, and reported a heavy gym session 48 h prior plus poor
  diet / no carbohydrate the night before. Corrected the rev 18 claim of a
  "fully recovered start": COROS recovery is blind to Hevy sessions. Reading
  revised — same-day factors explain part of today's HR, not the trend, and not
  crossing 142 at 3:14; the gap is pacing by feel rather than to the cap.
- **2026-09-16** (rev 18) — Added week of 11–16 Sep and the Wed 16 Sep run
  (8.14 km, 50:57, 6:16 /km adj 6:07, avg HR **157**, max **175**, load 160).
  Matched neither prescription in force: 2.5 min in Aerobic Endurance,
  47.7 min above 142, no recoveries, 29.3 min above LTHR (record), first time
  above 166. Slower than 10 Sep at +7 bpm from recovery 100% / resting HR 56, so
  fatigue no longer explains the pace-for-HR decline — three weeks running.
  Surge-then-repay pattern again (km 6 at 168 → km 7 at 6:57). Noted the loop's
  km-4 climb makes an easy run on it impractical. Load per Z2 minute 64.
- **2026-09-10** (rev 17) — Repo reorganised into `goals/`. This log, the
  conditioning plan and the 3 Sep session review moved to `goals/vo2-recovery/`;
  the shoulder plan and session-1 assessment moved to `goals/shoulder-rehab/`.
  Each goal now has a `README.md` holding its current state; cross-goal issues
  (the punching conflict, unrecorded boxing, the shared recovery budget) moved
  to `goals/README.md`. Links in this file updated.
- **2026-09-10** (rev 16) — Athlete clarified the 10 Sep run was **deliberately
  intended to be faster**. Reassessed on its own terms: goal not met — pace
  6:07 vs 6:08 and adjusted 5:53 vs 5:55 are noise, the shorter total time is
  400 m less distance, and best km was 5 s *slower* (5:23 vs 5:18), all at
  +7.5 bpm. Identified the limiting mechanism from km 3: same pace as 3 Sep for
  **+14 bpm** and above LTHR at km 3 of 8, with the surge repaid by a 45 s
  slower km 4 (13 s on 3 Sep) — fast kilometres cashed in for slow ones.
  Replaced the "cap everything at 142" prescription with a two-run week: one
  **5 × 3 min / 1 min** interval session (fight-specific, fills the plan's
  missing interval slot, cheaper than 10 Sep) plus one genuinely easy run.
- **2026-09-10** (rev 15) — Added week of 4–10 Sep and the Thu 10 Sep run
  (8.35 km, 51:00, 6:07 /km, avg HR **150**, load 179, focus Threshold, graded
  Below Average). **Last week's efficiency gain reversed**: same course and
  adjusted pace 2 s faster than 3 Sep, but +7.5 bpm. Worst session on record
  against the plan — 7.3 min Aerobic Endurance, 28.7 min Threshold, **19.3 min
  above LTHR**. All four trend lines now monotonic; cost per Z2 minute rose to
  24.5 (finding 3b updated). Three fatigue markers agree: resting HR 56 → 59,
  recovery 69% "light training recommended", and HR-at-pace up 7.5 bpm. Not a
  volume problem — three days under 2,500 steps. Calf/soleus routine performed
  for the first time (4 Sep, partial: 2 exercises, 6 sets) and shoulder rehab
  done the same day, first since 26 Aug. Camp clock updated: 7.4 weeks to the
  earliest fight date.
- **2026-09-03** (rev 14) — Confirmed threshold HR = **157** by deriving it
  independently from all five zone boundaries the athlete read from the app
  (156.6–157.5); zone model already Lactate Threshold, Zone 2 already 126–141.
  **Watch is correctly configured; no settings action outstanding.** Computed
  time in the athlete's own six zones: 19.0 min in the Threshold zone on 3 Sep
  and 21.8 on 27 Aug, against 0.6 on 25 Aug. Added standing finding 3b, cost per
  minute of target stimulus (3.8 / 11.7 / 19.9 load per Z2 minute).
- **2026-09-03** (rev 12) — Consolidated the scattered watch-settings actions
  into a single checklist with the basis for each (COROS docs / measured data /
  inference). One item outstanding: reading the threshold HR. Flagged that the
  Running Fitness Test overwrites threshold HR and max HR, so it can disturb
  settings that are currently correct. Recorded that the settings thread is not
  the limiter and originated in an unsound inference.
- **2026-09-03** (rev 11) — Audited API coverage for HR settings. Threshold HR,
  max HR and zone boundaries are **not exposed** by any endpoint, and COROS
  strips `zones_target` / `hr_zone` / `user_profile` from exported FIT files, so
  zone drift cannot be monitored programmatically. Added a coverage table.
  Refined the resting-HR position: a profile value of **56 bpm** and an HRV
  baseline of **42 ms** do exist via `queryDailyHealthData`, though the daily
  series is empty — the earlier "all empty" note was imprecise.
- **2026-09-03** (rev 10) — Established the provenance of the plan's HR bands:
  COROS's Lactate Threshold model defines Zone 2 as 80–90% of threshold HR, so
  at LTHR 157 it yields **126–141 exactly** — the plan's band is COROS LT Zone 2,
  not an independent figure. Therefore the app should be set to the **Lactate
  Threshold** zone type, and the displayed threshold HR should read 157. Added a
  table of the band each threshold HR would produce, and flagged that threshold
  HR is algorithm-updated and can drift the ceiling upward mid-camp — custom
  zone boundaries are the fix. Recorded that EvoLab uses LT zones internally
  whichever model is displayed.
- **2026-09-03** (rev 9) — Athlete checked the app: **max HR is 179**, not the
  suspected 162. Above every age estimate, so measured rather than derived, and
  consistent with the plan's LTHR 157 (88% of max) and Zone 2 band 126–141
  (70–79% of max). Standing finding 7 resolved and closed: the HR zones are
  correct and need no change. Remaining suspect numbers are Threshold Pace
  5:20 /km and VO2max 41 — a pace-side problem only.
- **2026-09-03** (rev 8) — Located the settings: **Profile → Settings → Heart
  Rate Zones** holds both max HR and resting HR, both manually editable, and the
  zone-model choice (Max HR / HR Reserve / Lactate Threshold). Athlete declined
  overnight watch wear; recorded the **Wellness Check** (hold BACK/LAP →
  Toolbox, 30–60 s) as the substitute route to a measured resting HR, entered
  manually. Automatic resting HR and all sleep/HRV metrics are forgone as a
  result. Noted that choosing the Max-HR zone model removes the resting-HR
  dependency entirely.
- **2026-09-03** (rev 7) — Established from COROS documentation that **LTHR
  cannot be set manually** — only max HR and resting HR can; threshold HR is
  algorithm-only, updated by the Running Fitness Test or automatically. This
  corrects the advice given earlier in the session to type LTHR 157 into the
  app. Consequence: a self-administered 30-min threshold time trial cannot
  configure COROS and is only useful as a personal reference number. Recorded
  the Running Fitness Test protocol (5 min warm-up / 25 min marathon pace /
  3 min 10K / 3 min 5K / optional 3 min / 5 min cooldown, continuous, ~40 min),
  which outputs Threshold Pace, Threshold HR **and** Max HR together. Promoted
  the overnight-wear item to a blocker.
- **2026-09-03** (rev 6) — **Corrected Standing finding 7.** Measured time above
  six HR thresholds across all three runs: 3 Sep was lower than 27 Aug on every
  one, and on average and max HR, yet scored a *higher* Anaerobic TE (3.9 vs
  3.5). The TE scores therefore say nothing about the HR zones, and the earlier
  inference from them was unsound. Likely driver is Threshold Pace 5:20 /km,
  which dates from a 6 Feb 2026 fitness test. Recorded that the COROS API does
  not expose max HR or zone boundaries. Added an open item to retest threshold
  pace outdoors.
- **2026-09-03** (rev 5) — Added Thu 3 Sep outdoor run (8.75 km, 53:42,
  6:08 /km, avg HR 143, load **197**). Fastest and most expensive run on record.
  Real efficiency gain vs 27 Aug (11 s/km faster at 3 bpm lower on the same
  course and climb; time above LTHR 6.2 → 2.4 min), but the worst Zone 2
  session of the three — only 4.2 min in target, 68% above the ceiling.
  Recomputed half-splits for all three runs with one method: 3 Sep started at
  6:01 @ 136.8 and decoupled to 6:15 @ 149.0. Cause traced to km 3–6 being run
  at 5:34–5:58 with no recovery afterwards. Noted the limiter for running is
  aerobic durability, distinct from the calf/soleus limiter for incline walking.
  Superseded the earlier lap-based +32 / +15 s/km fade figures.
- **2026-09-02** (rev 4) — Built the calf/soleus routine
  (`routines/calf-soleus-endurance.json`, Hevy id
  `717e84d5-fe99-4ad9-a2ee-dbde44b079ba`, Rehab folder): Seated Calf Raise,
  Standing Calf Raise (Machine), Isometric Calf Hold, Tibialis Raise. Two new
  custom templates created and their ids pinned in the spec.
- **2026-09-02** (rev 3) — Athlete reported gradient is unusable as an intensity
  lever (legs fail at 15% before HR rises); gradient 6 + 6 km/h fast walk works.
  Added a treadmill-settings section with a per-minute speed/HR reconstruction.
  Reversed the earlier "raise the gradient" advice — the fix is holding one
  setting unbroken, since HR was still climbing at minute 29. Promoted the
  calf/soleus item to gating constraint. Noted the watch under-reads indoor
  speed by ~15–20%.
- **2026-09-02** (rev 2) — Corrected the Wed 2 Sep walk: watch left running,
  real session 30:00 not 37:47. All figures retrimmed (2.71 km, 11:04 /km,
  avg HR 118). Absolute time in zone essentially unchanged (11.4 min Z2,
  2.7 min target) — the dead time was all sub-Z2. Noted the session ended
  still in the target band with no fade, so the limiter is the 20-minute ramp,
  not capacity. Added a data-hygiene note.
- **2026-09-02** — Added week of 31 Aug – 2 Sep. Wed 2 Sep incline walk logged
  as Indoor Run; time-in-zone computed from FIT. First session on record with
  zero time above the Zone 2 ceiling. Working block only ~10 min of 37 — fix is
  structural. Added Hevy sessions 31 Aug (Upper pull) and 2 Sep (Core); noted
  no rehab session since 26 Aug. Closed the incline-walking open item.
- **2026-08-27** — Created. Reviewed the conditioning plan against 24–27 Aug
  COROS sessions. Time-in-zone computed from FIT files for both runs.

# Session Review — 3 Sep 2026

Companion to [boxing-camp-conditioning-summary.md](boxing-camp-conditioning-summary.md),
which this session advanced from rev 4 to **rev 14**. This file records what was
asked, what was found, and — because there were several — what was corrected.

---

## What was asked

1. Pull the latest COROS run and compare it to previous runs
2. Can max HR / zones be recalibrated on a treadmill, and how long does it take?
3. What is the difference between the LTHR and Max HR test protocols?
4. How do I set LTHR in COROS, and how do I run the test?
5. Where is max HR in the app, and is there a resting-HR route that avoids
   wearing the watch overnight?
6. Should the zone type be set back to Lactate Threshold?
7. Can the HR zone settings and thresholds be pulled from the API?
8. Review the watch steps end to end
9. What are the implications of not training in Aerobic Endurance?

---

## The run — Thu 3 Sep 2026

8.75 km, 53:42, 6:08 /km, avg HR 143, max 161, **training load 197**.
Same Sydney course as 25 and 27 Aug. Third run in nine days, one day after the
treadmill walk.

**Genuine improvement.** Against 27 Aug on identical course and climb: 11 s/km
faster at 3 bpm lower, adjusted pace 6:05 → 5:55, time above LTHR 6.2 → 2.4 min,
stride length 0.97 → 1.01 m at unchanged cadence. COROS grade "Poor" → "Good".

**Worst Zone 2 execution of the three.** Only 9.9 min in Aerobic Endurance
against 34.9 on 25 Aug. First 15 minutes were textbook (≈6:05 /km at 135–138);
km 3–6 were then run at 5:34–5:58 and HR never came back — km 7 slowed to
6:25 /km with HR still 152.

Time in the athlete's own COROS zones (minutes):

| Zone | 25 Aug | 27 Aug | 3 Sep |
| --- | --- | --- | --- |
| Recovery <126 | 2.5 | 2.1 | 5.5 |
| **Aerobic Endurance 126–141** | **34.9** | 13.5 | **9.9** |
| Aerobic Power 142–149 | 16.4 | 14.2 | 19.2 |
| **Threshold 150–160** | 0.6 | **21.8** | **19.0** |
| Anaerobic Endurance 161–166 | 0.0 | 1.5 | 0.1 |

Decoupling, all three computed identically:

| | 1st half | 2nd half | Δ pace | Δ HR |
| --- | --- | --- | --- | --- |
| 25 Aug | 6:08 @ 136.4 | 6:33 @ 138.4 | +25 s/km | +2.0 |
| 27 Aug | 6:19 @ 146.9 | 6:18 @ 145.9 | −1 s/km | −1.0 |
| **3 Sep** | 6:01 @ 136.8 | 6:15 @ 149.0 | +14 s/km | **+12.2** |

**Cost per minute of target stimulus** (load ÷ Z2 minutes): 25 Aug **3.8**,
27 Aug 11.7, 3 Sep **19.9**. Today was 5.2× more expensive per unit of base
built. This is the metric to watch going forward.

---

## Watch configuration — settled, nothing to change

Threshold HR derived independently from all five zone boundaries the athlete
read from the app (126/141/149/160/166 ÷ 0.80/0.90/0.95/1.02/1.06 →
156.6–157.5). **Threshold HR = 157.**

| Setting | Value | Verdict |
| --- | --- | --- |
| Zone model | Lactate Threshold | correct |
| Threshold HR | 157 | matches the plan exactly |
| Zone 2 | 126–141 | matches the plan exactly |
| Max HR | 179 | measured, 157/179 = 88%, correct |

**No settings action outstanding.** The Running Fitness Test is *not*
recommended: it would overwrite a correct 157 and 179 in order to refresh
threshold pace, which drives no training decision.

### COROS facts established (documented, sourced)

- **LTHR cannot be set manually.** Only max HR and resting HR are editable;
  threshold HR is algorithm-only, updated by the Running Fitness Test.
- Settings path: **Profile → Settings → Heart Rate Zones**.
- LT model Zone 2 = **80–90% of threshold HR**.
- EvoLab uses LT zones internally regardless of the model displayed.
- Custom zone boundaries are supported.
- Running Fitness Test: ~40 min continuous — 5 warm-up / 25 marathon pace /
  3 at 10K / 3 at 5K / optional 3 / 5 cool-down. Outputs threshold pace,
  threshold HR and max HR. Needs flat ground; **not** the treadmill, because
  indoor speed under-reads 15–20%.
- Automatic resting HR requires sleep data. Substitute: **Wellness Check**
  (hold BACK/LAP → Toolbox, 30–60 s), entered manually.

### API coverage

Retrievable: threshold **pace** (5:20 /km), VO2max (41), resting HR (56),
HRV baseline (42 ms), recovery status, per-session and per-second HR.

**Not retrievable: threshold HR, max HR setting, zone boundaries, zone model.**
COROS strips `zones_target`, `hr_zone` and `user_profile` from exported FIT
files. Zone drift cannot be detected programmatically — it must be eyeballed in
the app. Zone 2 should always read 126–141.

---

## Corrections made this session

Recorded because the pattern matters: every error was an inference stated with
more confidence than the evidence carried, and each was caught by checking.

| Claim | Reality | Caught by |
| --- | --- | --- |
| High Anaerobic TE proves the HR zones are mis-set | TE does not track HR — 3 Sep was lower on average, max and all six thresholds yet scored *higher* | Computing time above six thresholds |
| LTHR can be typed into the COROS app | It cannot; algorithm-only | COROS documentation |
| Max HR probably auto-latched to 162 | It is 179, measured and correct | Athlete read the app |
| Resting HR and HRV are "all empty" | Profile values exist (56 bpm, 42 ms); only the daily series is empty | `queryDailyHealthData` |
| Second-half fade +32 / +15 s/km (27 Aug review) | +25 / −1 when all three are split identically | Recomputing consistently |

The entire watch-settings investigation originated in the first error. The
settings were correct throughout.

---

## Where things actually stand

**The limiter is execution, not equipment.** Aerobic Endurance minutes have
fallen 34.9 → 13.5 → 9.9 across three runs while Threshold minutes went
0.6 → 21.8 → 19.0. The watch is configured correctly and has been all along.

**Two distinct limiters, not one.**
- *Running* is gated by aerobic durability past ~15 minutes (3 Sep decoupled
  +12.2 bpm; cadence and stride held, so the legs were fine).
- *Incline walking* is gated by calf/soleus endurance (legs fail at 15% gradient
  before HR responds).

**Prescription for the next run.** Hold 6:05–6:15 /km for the full hour and
refuse to speed up on flats and descents — km 3–6 is where it got away. If HR
crosses 142 at minute 15, slow to 6:30 rather than defend the pace.

### Open items

- [ ] Reconcile the conditioning plan against the shoulder rehab plan on
      sparring and bag work — still the most consequential open item
- [ ] Run Zone 2 sessions in Zone 2 (126–141)
- [ ] Actually run `Calf & Soleus Endurance` (built 2 Sep, not yet performed)
- [ ] Add an aerobic interval session — plan wants ~1/week, zero so far
- [ ] Record boxing on the watch (sport type `906`) — still entirely unmeasured
- [ ] No shoulder rehab session since 26 Aug
- [ ] Low priority: threshold pace 5:20 /km and VO2max 41 look inconsistent with
      actual running; only the Running Fitness Test fixes them, at the cost of
      overwriting correct HR settings
- [ ] Resting HR is optional — 56 stored, and neither LT nor Max-HR zones use it

### Risk flag

Run base of 2.6 km/week across 29 weeks, now 25.8 km in nine days (~9× jump),
plus a known calf/soleus deficit, at 91 kg. Volume spike + intensity above plan
+ known weak link is the standard calf/Achilles injury setup. Nine weeks to the
earliest fight date.

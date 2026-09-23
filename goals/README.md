# Athletic Goals

**As of Thu 17 Sep 2026.** Two goals serve one event: a boxing bout in
**November 2026** — 5 × 3-minute rounds, 1-minute rests. A third is a standing
goal that outlives it. Each has its own folder, plan, data and current state.

| Goal | Folder | Led by | State |
| --- | --- | --- | --- |
| **VO2 & recovery** — aerobic base, VO2max, recovery between rounds | [vo2-recovery/](vo2-recovery/README.md) | COROS | **Off track.** Aerobic Endurance time has fallen on every run: 34.9 → 13.5 → 9.9 → 7.3 → 2.5 min |
| **Shoulder rehab** — rotator-cuff capacity for punching | [shoulder-rehab/](shoulder-rehab/README.md) | Hevy | **Moving again.** Full week-one session 17 Sep, deceleration drill included; 4 sessions in 22 days; still no pain data |
| **Detraining** — slowing decay when not training (standing goal, not camp-bound) | [detraining/](detraining/README.md) | COROS + Hevy | **New, 17 Sep.** Recorded cardio gaps ran to 39 days before camp; no benchmark exists to detect decay |
| **Lower-body power** — explosiveness and boxing footwork | [lower-body-power/](lower-body-power/README.md) | Hevy | **New, 20 Sep.** One lower-body-only week planned (21–27 Sep) while the shoulder is sore; no baseline yet |

## Camp clock

| Fight date | Weeks from 10 Sep |
| --- | --- |
| 1 Nov | 7.4 |
| 15 Nov | 9.4 |
| 30 Nov | 11.6 |

## Athlete

Verified from COROS on 10 Sep: age **46** (born 1979-10-27, turns 47 on 27 Oct),
**91 kg**, 185 cm, **COROS PACE 3**. Both plan documents were written for
47 / 96 kg / PACE 2 and have not been corrected.

---

## Cross-goal issues

These sit between the two goals and can't be resolved inside either folder.

### 1. The plans contradict each other on punching — unresolved

| Conditioning plan wants | Shoulder plan says |
| --- | --- |
| Hard sparring ~1/week | Avoid hard missed punches |
| Pads / bag work as extra volume | Reduce high-volume hard bag work |
| Repeated maximal punching (3 s on / 10 s off) | Build cuff capacity first |

Both can't be followed as written. **This is the most consequential open
decision in the repo.** The conflict is specific to *punching*. The running
intervals prescribed on 10 Sep (5 × 3 min / 1 min) load the legs and heart, not
the cuff, and fit both plans.

### 2. Boxing is not recorded anywhere

Neither COROS nor Hevy holds a single boxing session. Boxing is the *demand*
side of the shoulder plan's model (`boxing workload > shoulder capacity →
irritation`), and it is what the conditioning plan trains for. So both goals
are being managed without their most important input.
**Fix:** record boxing on the watch as sport type `906`.

### 3. One recovery budget, two claimants

Between 25 Aug and 10 Sep there were four hard runs (COROS) and two shoulder
rehab sessions (Hevy). On 10 Sep COROS reported recovery at **69%**, "light
training recommended", and resting HR had risen **56 → 59** in a week. The
shoulder plan depends on *frequency*, and the conditioning is currently spending
recovery on *intensity*. *Inference, not measured:* that trade-off is probably
part of why rehab frequency has slipped.

---

## Layout

```
goals/
├── README.md                                  ← this file: index and cross-goal issues
├── vo2-recovery/
│   ├── README.md                              ← current state of play
│   ├── boxing-camp-conditioning-context.md    ← the plan
│   ├── boxing-camp-conditioning-summary.md    ← chronological log, rev by rev
│   └── session-2026-09-03-review.md
├── shoulder-rehab/
│   ├── README.md                              ← current state of play
│   ├── boxing-shoulder-pain-prevention-plan.md   ← the plan
│   ├── 2026-08-26-shoulder-rehab-session-1.md
│   └── 2026-09-15-return-to-boxing-plan.md    ← current prescription
└── detraining/
    ├── README.md                              ← current state of play
    └── 2026-09-17-minimum-dose-maintenance-plan.md   ← the plan
```

The Hevy routine specs stay in `routines/`, because `hevy routines create`
expects them there and the project README documents them there:

| Spec | Goal |
| --- | --- |
| `routines/shoulder-rehab.json` | shoulder-rehab |
| `routines/calf-soleus-endurance.json` | vo2-recovery — lower-leg durability for running and incline walking |
| `routines/plyo-a-power.json`, `routines/plyo-b-reactive.json`, `routines/quick-feet.json` | lower-body-power |

## Data sources

| Source | Sees | Doesn't see |
| --- | --- | --- |
| COROS (MCP) | Runs, walks, rides; per-second HR; training load; recovery; resting HR; VO2max; threshold pace | Strength and rehab sessions (never recorded on the watch); threshold HR, max HR and zone settings (not exposed by the API) |
| Hevy (API) | Every strength and rehab set: load, reps, duration | Heart rate; pain (no RPE or notes logged on any rehab set to date) |

Neither sees boxing.

## Maintaining this

Each goal's `README.md` describes the **current state** and is rewritten when
the picture changes. History goes in the log
(`vo2-recovery/boxing-camp-conditioning-summary.md`) or in dated session
reviews. Every claim is labelled by its basis — COROS, Hevy, the plan, or
inference — so measured facts stay distinguishable from judgement.

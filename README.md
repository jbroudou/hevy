# hevy

A Python CLI for managing your [Hevy](https://hevy.com) workouts and routines
through the [Hevy public API](https://api.hevyapp.com/docs/).

- Browse routines grouped by folder
- Build routines from version-controlled JSON spec files
- Read back logged workouts — every set, weight, rep and session time

## Requirements

- Python 3.10+
- [Poetry](https://python-poetry.org/)
- A Hevy **Pro** account (the API is Pro-only)

## Setup

```bash
poetry install
cp .env.example .env
```

Put your API key in `.env` — get one at <https://hevy.com/settings?developer>:

```
HEVY_API_KEY=your-key-here
```

Never commit `.env`; it is already in `.gitignore`.

### Configuration

All settings are read from `.env`. Only `HEVY_API_KEY` is required.

| Variable | Default | Description |
| --- | --- | --- |
| `HEVY_API_KEY` | — | Your API key. Commands exit `2` if it is missing. |
| `HEVY_API_BASE_URL` | `https://api.hevyapp.com` | Override to point at a mock server. |
| `LOG_LEVEL` | `INFO` | Level for the `log/` file. |
| `LOG_CONSOLE_LEVEL` | `CRITICAL` | Level for stderr. Set to `DEBUG` to trace requests. |

## Usage

### Routines

List every routine grouped by its folder:

```bash
poetry run hevy routines list
```

```
Routines (26 total)
├── Quick Gym (2)
│   ├── Full body — 7 exercises · 0e2f…
│   └── Push day — 6 exercises · 4a11…
└── (No folder) (1)
    └── Scratch — 3 exercises · 91bc…
```

| Flag | Description |
| --- | --- |
| `--json` | Emit JSON instead of the tree, for piping into `jq` |
| `--no-empty` | Hide folders that contain no routines |

Create a routine from a spec file (see [Routine specs](#routine-specs)):

```bash
poetry run hevy routines create routines/shoulder-rehab.json --dry-run
poetry run hevy routines create routines/shoulder-rehab.json
```

| Flag | Description |
| --- | --- |
| `--dry-run` | Print the payload and what would be created, without writing |

Overwrite an existing routine from its spec. The spec must carry the
routine's `routine_id`:

```bash
poetry run hevy routines update routines/plyo-a-power.json --dry-run
poetry run hevy routines update routines/plyo-a-power.json
```

`update` replaces every exercise, set and note, so edits made in the app since
the last push are lost.

**Preview with `--dry-run` first.** The API has no delete, so a routine or
exercise template created by mistake can only be removed by hand in the app.

### Workouts

Review a logged workout. With no arguments this shows your most recent session;
`--routine` picks the latest session logged against a routine:

```bash
poetry run hevy workouts show
poetry run hevy workouts show --routine "Shoulder Rehab"
poetry run hevy workouts show <workout-id>
```

```
Shoulder Rehab aabcd80b-b0b7-4124-a05b-6f270e54471a
Wed 26 Aug 2026, 08:51 · 48:57
1  Cable External Rotation (Elbow at Side)  5 kg x 20   5 kg x 20   5 kg x 14
2  Seated Cable Row - V Grip (Cable)        40 kg x 20   60 kg x 17   50 kg x 20

8 exercises · 20 sets · 304 reps · 4261 kg volume
```

List recent workouts, newest first:

```bash
poetry run hevy workouts list -n 10
poetry run hevy workouts list --routine "Shoulder Rehab"
```

| Flag | Description |
| --- | --- |
| `-n`, `--limit` | How many workouts to show (`list` only, default 10) |
| `-r`, `--routine` | Match workouts by title, case-insensitively |
| `--search-limit` | How far back `show --routine` scans (default 50) |
| `--json` | Emit JSON instead of a table |
| `--last` | Show the most recent workout (`show` only; this is the default) |

Times are shown in your local timezone; the API stores them as UTC. Session
time is wall-clock, so it includes rest and setup.

A set logged at zero load renders as `0 kg x 15` rather than being hidden — on
band work that means the resistance was never recorded, which is worth seeing.

### Other

```bash
poetry run hevy --help
poetry run hevy --version
```

Exit codes: `0` success, `1` API error, `2` configuration error.

## Routine specs

A routine is authored as a JSON file in `routines/` so it can be reviewed and
kept under version control, then pushed with `hevy routines create`.

```json
{
  "title": "Shoulder Rehab",
  "folder": "Rehab",
  "exercises": [
    {
      "name": "Cable External Rotation (Elbow at Side)",
      "template_id": "eed828ba-e10f-43b2-9902-2ea23a0569ba",
      "create": {
        "exercise_type": "weight_reps",
        "equipment_category": "machine",
        "muscle_group": "shoulders",
        "other_muscles": ["upper_back"]
      },
      "sets": 3,
      "reps": 20,
      "rest_seconds": 30,
      "notes": "Tempo: 1 sec out, 3 sec back."
    }
  ]
}
```

| Field | Description |
| --- | --- |
| `title` | Routine title. Required. |
| `routine_id` | The routine to overwrite with `routines update`. |
| `folder` | Folder title, matched case-insensitively. Omit for no folder. |
| `exercises[].name` | Exercise title, used to match an existing template. |
| `exercises[].template_id` | Pins an exact template. Wins over `name`. |
| `exercises[].create` | How to create the template if nothing matches. |
| `exercises[].sets` | How many identical sets to write. |
| `exercises[].reps` | Target reps per set. |
| `exercises[].rest_seconds` | Rest after the exercise. |
| `exercises[].notes` | Free text shown under the exercise in the app. |

`weight_kg`, `duration_seconds`, `distance_meters` and `superset_id` are also
passed through.

Each exercise resolves in this order: `template_id`, then an exact
case-insensitive `name` match against your templates, then `create`.

**Pin a `template_id` once a template exists.** Title matching is the fallback,
so renaming an exercise in the Hevy app will otherwise make the next run create
a duplicate template — permanently, since the API has no delete. The `create`
block can stay alongside a pinned id; it is ignored, and documents how the
template was built if you ever rebuild on a fresh account.

Valid `create` values, from the API spec:

- `exercise_type` — `weight_reps`, `reps_only`, `bodyweight_reps`,
  `bodyweight_assisted_reps`, `duration`, `weight_duration`,
  `distance_duration`, `short_distance_weight`
- `equipment_category` — `none`, `barbell`, `dumbbell`, `kettlebell`,
  `machine`, `plate`, `resistance_band`, `suspension`, `other`.
  There is no `cable`; cable stations are `machine`.
- `muscle_group` and `other_muscles` — `shoulders`, `chest`, `lats`,
  `upper_back`, `traps`, `triceps`, `biceps`, and so on

### Known quirks

- A routine-level `notes` field is accepted on create but comes back `null`.
  Per-exercise notes persist correctly, so put anything that matters there.
- The API has no per-side concept and no tempo field. Per-side and tempo work
  belongs in the exercise notes.
- `rest_seconds` is per exercise, not per set.

## COROS data (MCP)

Recovery, sleep, HRV and endurance data comes from [COROS](https://coros.com)
via their official MCP server, not through this CLI. Unlike Hevy, COROS has no
self-serve REST API — direct API access needs an approved partner application —
so the MCP server is the supported route for an individual account.

The server is declared in `.mcp.json` at the project root:

```json
{
  "mcpServers": {
    "coros": {
      "type": "http",
      "url": "https://mcpus.coros.com/mcp"
    }
  }
}
```

Authentication is OAuth against your COROS account, handled interactively — run
`/mcp` inside Claude Code and pick `coros`. No key goes in `.env`, and
`.mcp.json` holds no secrets, so it is safe to commit.

**Use a regional endpoint, not `https://mcp.coros.com/mcp`.** The auto-routing
domain cannot authenticate. It serves the request, but the protected-resource
metadata it returns declares the resource as the regional host:

```
$ curl https://mcp.coros.com/.well-known/oauth-protected-resource/mcp
{"resource":"https://mcpus.coros.com/mcp", ...}
```

RFC 9728 requires that `resource` to match the URL the client is connecting to.
It does not, so a spec-compliant client rejects the token exchange:

```
Protected resource https://mcpus.coros.com/mcp does not match
expected https://mcp.coros.com/mcp (or origin)
```

The regional hosts declare themselves correctly and authenticate cleanly:

| Region | Endpoint |
| --- | --- |
| United States | `https://mcpus.coros.com/mcp` |
| Europe | `https://mcpeu.coros.com/mcp` |
| Mainland China | `https://mcpcn.coros.com/mcp` |

Pick the region your COROS account is registered in. If auth succeeds but no
data comes back, it is the wrong region — switch endpoints and re-authenticate.

The server is read-only. It exposes activity records and detail, lap and FIT
file access, daily health data, sleep and sleep HRV, resting heart rate, stress,
recovery status, VO2max and fitness assessments, training load, and the training
schedule. FIT downloads are capped at 50 per account per day.

### Why both

Hevy holds the strength and rehab log — every set, rep and load. COROS holds
the recovery side — sleep, HRV, stress, training load. Neither sees the other,
so questions like "did the sessions I felt worst in follow the nights I slept
worst" need both, which is what the MCP server makes possible.

## Project layout

```
src/hevy/
├── api.py             # HevyClient — auth, retries, error handling, pagination
├── cli.py             # Typer entry point (`hevy`)
├── config.py          # .env-backed settings
├── logger.py          # stderr + log/ file logging
├── models.py          # Routine/Folder/Workout dataclasses and grouping
├── spec.py            # Routine spec files -> API payloads
└── commands/
    ├── routines.py    # `hevy routines list|create|update`
    └── workouts.py    # `hevy workouts list|show`
routines/              # Routine spec files (pushed with `hevy routines create`)
goals/                 # Athletic goals: plan, data and current state per goal
├── vo2-recovery/      # Aerobic base, VO2max, recovery (COROS-led)
└── shoulder-rehab/    # Shoulder pain prevention and rehab (Hevy-led)
tests/                 # pytest, with httpx.MockTransport for the client
.mcp.json              # COROS MCP server (OAuth, no secrets)
```

## Notes on the API

- Auth is a single `api-key` request header.
- Every paginated endpoint caps `pageSize` at **10**; `HevyClient.paginate()`
  walks `page_count` for you so callers just get a full list.
- There are **no DELETE endpoints**. Routines and exercise templates can only
  be removed by hand in the app, so writes are effectively one-way.
- Writes are rate limited and answer **429**; the client honours `Retry-After`
  and backs off, over a maximum of five attempts.
- `POST /v1/exercise_templates` answers 2xx with an **empty body**, so new
  templates are read back by title to recover their id.
- Response shapes are inconsistent: `GET /v1/routines/{id}` nests a dict under
  `routine`, `POST /v1/routines` nests a one-item list, and
  `GET /v1/workouts/{id}` returns the workout unwrapped.
- A routine with `folder_id: null` is not in any folder and is shown under
  `(No folder)`.
- The Swagger UI page renders nothing to a plain fetcher. The OpenAPI document
  is embedded in `https://api.hevyapp.com/docs/swagger-ui-init.js` as a
  `"swaggerDoc"` JSON blob.

Endpoints not yet wired up: `PUT /v1/workouts/{id}` (edit in place), `POST /v1/workouts` (log a workout),
`/v1/workouts/events` (a change feed for syncing),
`/v1/exercise_history/{templateId}` (every logged set of one exercise, for
progression tracking), and `/v1/body_measurements`. `GET /v1/user/info` has a
client method (`HevyClient.get_user_info`) but no command in front of it.

## Development

```bash
poetry run pytest
poetry run ruff check .
poetry run black .
poetry run mypy src
```

Client tests use `httpx.MockTransport`, so the suite makes no network calls.

## Logging

Logs are written to `log/hevy_YYYYMMDD.log` at `LOG_LEVEL` (default `INFO`).

The console handler writes to stderr at `LOG_CONSOLE_LEVEL`, which defaults to
`CRITICAL` — effectively silent, because the CLI prints its own errors and
duplicating them was noise. Set `LOG_CONSOLE_LEVEL=DEBUG` in `.env` to trace
requests while troubleshooting. Command output always goes to stdout, so it
stays pipeable either way.

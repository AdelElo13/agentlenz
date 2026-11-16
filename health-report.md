# Weekly Health Report — 2026-11-16

_Generated automatically. Repos checked: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`._

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches
No stale branches. Only `main` exists locally and on remote.

### Dependency Health
| Package file | Status |
|---|---|
| `backend/pyproject.toml` | Flexible pins (`>=`). Key packages: `fastapi` 0.162.0, `uvicorn` 0.54.0, `pydantic` **2.14.2** (↑ from 2.13.5 last week — updated ✅), `sqlalchemy` 2.1.6, `alembic` 1.20.1. All current. `uv.lock` checked in. |
| `sdk/pyproject.toml` | Flexible pins. `httpx` 0.28.1, `anthropic` 2.3.0. `uv.lock` checked in. |
| `dashboard/package.json` | ⚠️ `next` pinned at **16.2.1**, latest is **16.4.6** (2 patches behind). `react`/`react-dom` at **19.2.4**, latest **19.3.1**. `node_modules` present. `@tanstack/react-query` and `recharts` are current. |

### Code Quality
| Metric | Count |
|---|---|
| TODO / FIXME / HACK comments (`.py`, `.ts`, `.js`, `.tsx`) | **0** |

### Test Status
| Suite | Result |
|---|---|
| `sdk` — `uv run --extra dev pytest` | ✅ 25 passed, 1 skipped |
| `backend` — `uv run --extra dev pytest` | ✅ 17 passed |

> ⚠️ **Recurring issue**: `sdk` teardown raises `RuntimeError: Call agentlenz.init() before using AgentLenz` from an atexit `EventClient.flush` callback — present for 2+ weeks. Not a test failure, but masks real teardown errors. See action items.

### Git Hygiene
- Working tree: clean
- Stashes: none
- Large files (>1 MB, outside `.git`): none
- Uncommitted changes: none
- Activity: **6 commits** since 2026-11-09 (standup notes only — no code changes)

---

## adelelo13/dockwright-macos-agent — ✅ Healthy

### Stale Branches
No stale or unmerged branches beyond `main`.

### Dependency Health
| Package file | Status |
|---|---|
| `Package.swift` | Not present — no SPM dependencies (by design; Phases 1–4 use only Apple frameworks) |

### Code Quality
| Metric | Count |
|---|---|
| TODO / FIXME / HACK comments (`.swift`) | **0** |

### Test Status
| Suite | Result |
|---|---|
| `xcodebuild test` | ⚠️ Not run — macOS build environment unavailable in this Linux CI context |
| Swift files | 104 `.swift` files across App/, Core/, UI/, Utilities/ |

### Git Hygiene
- Working tree: clean
- Stashes: none
- Uncommitted changes: none
- Activity: **0 new commits** since 2026-11-09 (quiet week)
- Large files (>1 MB, expected binary assets):
  - `assets/demo.mov` — demo video
  - `Dockwright/Resources/Models/embedding_model.onnx` — 1.3 MB ML model
  - `Dockwright/Resources/Models/melspectrogram.onnx` — 1.1 MB ML model
  - `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` — 1.3 MB wake word model
  - Consider Git LFS if repo grows

---

## Summary Table

| Repo | Health | Branches | Tests | Deps | Notes |
|---|---|---|---|---|---|
| agentlenz | ⚠️ Warning | ✅ Clean | ✅ 42 passed | ⚠️ Dashboard `next`/`react` still behind | `pydantic` updated ✅; atexit error persists |
| dockwright-macos-agent | ✅ Healthy | ✅ Clean | N/A (macOS only) | ✅ No external deps | Quiet week; consider Git LFS for `.onnx` files |

### Changes Since Last Week
- ✅ `agentlenz/backend`: `pydantic` bumped from 2.13.5 → 2.14.2
- ⚠️ `agentlenz/dashboard`: `next` latest moved from 16.4.5 → 16.4.6 (further behind)
- ⚠️ SDK atexit `RuntimeError` still unresolved (week 3)

### Action Items
1. **agentlenz/dashboard** (overdue): Bump `next` to 16.4.6 and `react`/`react-dom` to 19.3.1 in `package.json`.
2. **agentlenz/sdk** (week 3): Fix atexit `RuntimeError` — guard `flush()` with `if not _config_initialized(): return` to prevent noise that could suppress real teardown errors.
3. **dockwright-macos-agent**: Evaluate Git LFS for the three `.onnx` model files (~3.7 MB total).

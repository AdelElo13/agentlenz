# Weekly Health Report — 2026-11-09

_Generated automatically. Repos checked: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`._

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches
No local or remote stale branches (all 12 stale branches from last week's report have been cleaned up — good progress).

### Dependency Health
| Package file | Status |
|---|---|
| `backend/pyproject.toml` | Flexible version pins (`>=`). `pydantic` installed at 2.13.5 (latest 2.14.3 — 1 minor behind), `uvicorn` at 0.54.0 (current). `uv.lock` checked in. |
| `sdk/pyproject.toml` | Flexible pins (`httpx>=0.27`, `pydantic>=2.0`). `uv.lock` checked in. |
| `dashboard/package.json` | ⚠️ `node_modules` not installed. Two packages have newer versions: `next` 16.2.1 → **16.4.5**, `react`/`react-dom` 19.2.4 → **19.3.1** |

### Code Quality
| Metric | Count |
|---|---|
| TODO / FIXME / HACK comments (`.py`, `.ts`, `.js`) | **0** |

### Test Status
| Suite | Result |
|---|---|
| `sdk` — `uv run --extra dev pytest` | ✅ 25 passed, 1 skipped |
| `backend` — `uv run --extra dev pytest` | ✅ 17 passed |

> Note: `sdk` teardown raises `RuntimeError: Call agentlenz.init() before using AgentLenz` from an atexit handler — not a test failure but worth investigating.

### Git Hygiene
- Working tree: clean
- Stashes: none
- Large files (>1 MB, outside `.git`): none
- Uncommitted changes: none
- Activity: **7 commits** in the last 7 days

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
| `xcodebuild test` | ⚠️ Not run — macOS build environment not available in this Linux CI context |

### Git Hygiene
- Working tree: clean
- Stashes: none
- Uncommitted changes: none
- Activity: **7 commits** in the last 7 days
- Large files (>1 MB, expected binary assets):
  - `assets/demo.mov` — 1.5 MB demo video
  - `Dockwright/Resources/Models/embedding_model.onnx` — 1.3 MB ML model
  - `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` — 1.3 MB wake word model
  - `Dockwright/Resources/Models/melspectrogram.onnx` — 1.1 MB ML model
  - Consider moving these to Git LFS if the repo grows further

---

## Summary Table

| Repo | Health | Branches | Tests | Deps | Notes |
|---|---|---|---|---|---|
| agentlenz | ⚠️ Warning | ✅ All clean | ✅ 42 passed | ⚠️ Dashboard `next`/`react` behind | Bump `next` → 16.4.5, `react` → 19.3.1 |
| dockwright-macos-agent | ✅ Healthy | ✅ Clean | N/A (macOS only) | ✅ No external deps | Consider Git LFS for binary models |

### Action Items
1. **agentlenz/dashboard**: Run `npm install` and bump `next` to 16.4.5 and `react`/`react-dom` to 19.3.1 in `package.json`.
2. **agentlenz/sdk**: Investigate atexit `RuntimeError` from `EventClient.flush` — triggered in test teardown even when `agentlenz.init()` was never called; may suppress real errors.
3. **agentlenz/backend**: `pydantic` is 1 minor behind (2.13.5 installed, 2.14.3 available); update `uv.lock` when convenient.
4. **dockwright-macos-agent**: Evaluate Git LFS for the three `.onnx` model files (~3.7 MB total) before the repo grows larger.

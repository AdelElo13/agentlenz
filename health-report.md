# Weekly Health Report — 2026-11-02

_Generated automatically. Repos checked: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`._

---

## adelelo13/agentlenz — ⚠️ Warning

### Stale Branches
`git branch -r --merged origin/main` found **1 merged branch not yet deleted**:

| Branch | Status |
|--------|--------|
| `claude/temp-meters-dab-pots-lcvi3w` | Merged → main, safe to delete |

Additionally, **11 standup branches** remain open on the remote (not fully merged via fast-forward; likely squash-merged):

`standup-2026-05-27`, `standup-2026-06-16`, `standup-2026-06-17`, `standup-2026-06-22`, `standup-2026-06-29`, `standup-2026-07-13`, `standup-2026-08-24`, `standup-2026-08-31`, `standup-2026-09-15`, `standup-2026-10-05`, `standup-2026-10-13`

These accumulate weekly and should be deleted after merge.

### Dependency Health
| Package file | Status |
|---|---|
| `backend/pyproject.toml` | Flexible version pins (`>=`), no lock file checked in — acceptable for a server app |
| `sdk/pyproject.toml` | Flexible pins, no lock — acceptable for a library |
| `dashboard/package.json` | ⚠️ `node_modules` not installed (all deps show `MISSING`). Two packages have newer versions available: `next` 16.2.1 → **16.4.3**, `react` 19.2.4 → **19.3.1** |

### Code Quality
| Metric | Count |
|---|---|
| TODO / FIXME / HACK comments (`.py`, `.ts`, `.js`) | **0** |

### Test Status
| Suite | Result |
|---|---|
| `sdk` — `uv run --extra dev pytest` | ✅ 25 passed, 1 skipped |
| `backend` — `uv run --extra dev pytest` | ✅ 17 passed |

### Git Hygiene
- Working tree: clean
- Stashes: none
- Large files (>1 MB, outside `.git`/`.venv`): none
- Uncommitted changes: none

---

## adelelo13/dockwright-macos-agent — ✅ Healthy

### Stale Branches
`git branch -r --merged origin/main` found **0 merged branches**. One active feature branch exists:

| Branch | Status |
|--------|--------|
| `fix/bug-audit-v1` | Unmerged — appears to be active work in progress |

### Dependency Health
| Package file | Status |
|---|---|
| `Package.swift` | Not present — no SPM dependencies (expected per project design; Phase 1–4 uses only Apple frameworks) |

### Code Quality
| Metric | Count |
|---|---|
| TODO / FIXME / HACK comments (`.swift`) | **0** |

### Test Status
| Suite | Result |
|---|---|
| `xcodebuild test` | ⚠️ Not run — macOS build environment not available in this CI context |

### Git Hygiene
- Working tree: clean
- Stashes: none
- Uncommitted changes: none
- Large files (>1 MB, expected binary assets):
  - `assets/demo.mov` — demo video, tracked in git
  - `Dockwright/Resources/Models/embedding_model.onnx` — ML model
  - `Dockwright/Resources/Models/melspectrogram.onnx` — ML model
  - `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` — wake word model
  - Consider moving these to Git LFS if the repo grows large

---

## Summary Table

| Repo | Health | Branches | Tests | Deps | Notes |
|---|---|---|---|---|---|
| agentlenz | ⚠️ Warning | 12 stale remote branches | ✅ All passing | ⚠️ Dashboard deps not installed | Delete merged/squashed standup branches |
| dockwright-macos-agent | ✅ Healthy | 1 active branch | N/A (macOS only) | ✅ No external deps | Consider Git LFS for binary models |

### Action Items
1. **agentlenz**: Delete `claude/temp-meters-dab-pots-lcvi3w` (confirmed merged).
2. **agentlenz**: Set up automated branch cleanup for standup branches after merge — 11 stale ones now; will grow weekly.
3. **agentlenz/dashboard**: Run `npm install` to create a lock file; bump `next` to 16.4.3 and `react` to 19.3.1.
4. **dockwright-macos-agent**: Evaluate Git LFS for the three `.onnx` model files.

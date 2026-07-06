# Weekly Health Report — 2026-07-06

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | `.pyc` files still tracked in git (unresolved 2nd week); dashboard `node_modules` missing; pytest not available in environment |
| dockwright-macos-agent | ⚠️ Warning | Large binaries in git (6.5 MB); no test suite; HEAD detached; 0 commits this week |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Pinned Constraint | Status |
|---------|-------------------|--------|
| fastapi | `>=0.115` | No lockfile; version not pinned |
| uvicorn | `>=0.32` | No lockfile; version not pinned |
| sqlalchemy | `>=2.0` | No lockfile; version not pinned |
| asyncpg | `>=0.30` | No lockfile; version not pinned |
| alembic | `>=1.14` | No lockfile; version not pinned |
| pydantic | `>=2.0` | No lockfile; version not pinned |

> **Note:** Backend still has no lockfile (`uv.lock` / `requirements.lock`). Builds are non-reproducible. Flagged last week — still unresolved.

**SDK (`sdk/pyproject.toml`):**

| Package | Pinned Constraint |
|---------|-------------------|
| httpx | `>=0.27` |
| pydantic | `>=2.0` |

**Dashboard (`dashboard/package.json`) — ⚠️ Node modules not installed:**

`npm install` has not been run in this environment. All dependencies are UNMET. Version drift (from `npm outdated`):

| Package | Wanted | Latest | Drift |
|---------|--------|--------|-------|
| next | 16.2.1 | 16.2.10 | Minor patch (+1 since last week) |
| react | 19.2.4 | 19.2.7 | Minor patch |
| react-dom | 19.2.4 | 19.2.7 | Minor patch |
| recharts | ^3.8.0 | 3.9.2 | Minor |
| @tanstack/react-query | ^5.95.1 | 5.101.2 | Minor |

All updates are minor/patch — safe to upgrade. `next` moved from 16.2.9 → 16.2.10 since last week.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0
```

Zero markers across all `.py`, `.ts`, `.tsx`, `.js` files. Excellent — unchanged from last week.

### 4. Test Status

| Suite | Result |
|-------|--------|
| `backend` (pytest) | ⚠️ Could not run — `pytest` not installed in this environment |
| `sdk` (pytest) | ⚠️ Could not run — `pytest` not installed in this environment |
| `dashboard` | ⚠️ No test suite detected |

> Test files exist (`backend/tests/`, `sdk/tests/`) — this is an environment issue, not a missing test suite. Test results from last week (25 sdk + 17 backend passed) are the last known good state.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this week | 6 (standup files: 2026-06-30 through 2026-07-06) |
| Last commit | 2026-07-06 |

**⚠️ Issue: `.pyc` files still tracked in git (2nd week).** `.gitignore` was correctly updated to include `**/__pycache__/` and `**/*.pyc`, but the files were never removed from the git index. The cache entries persist:

```
backend/alembic/versions/__pycache__/55d8cfecf4d3_initial_schema.cpython-312.pyc
backend/src/agentlenz_api/__pycache__/__init__.cpython-312.pyc
backend/src/agentlenz_api/__pycache__/auth.cpython-312.pyc
backend/src/agentlenz_api/__pycache__/main.cpython-312.pyc
... (and more)
```

Fix: `git rm -r --cached '**/__pycache__' '**/*.pyc' && git commit -m "chore: remove tracked pyc files"`

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. `main` is the only branch. Clean.

> Note: HEAD is in detached state (`HEAD detached at refs/heads/main`) — this is a git checkout artifact in this environment, not an upstream issue.

### 2. Dependency Health

Pure Apple-framework Swift project (Xcode). No SPM packages, no `Package.swift`, no third-party dependency manager in use. N/A.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Notably clean for a codebase of this size.

### 4. Test Status

⚠️ No test suite detected. No Swift test target found. A 104-file multi-phase macOS app (LLMService, CronEngine, ToolExecutor, VoiceService, etc.) has zero test coverage. This is a persistent risk — core logic changes can't be validated automatically.

Recommended minimum test targets: `CronEngine` (cron expression parsing), `LLMService` (SSE parsing), `ToolExecutor` (argument dispatch).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ Detached at `refs/heads/main` (environment artifact) |
| Commits this week | 0 |
| Last commit | `d6d3f3f chore: update UIAutomationTool` (prior to this week) |

**⚠️ Issue: Large binary files tracked in git (no LFS) — unchanged from last week:**

```
assets/demo.mov                                    1.5 MB  ← video
Dockwright/Resources/Models/embedding_model.onnx  1.3 MB
Dockwright/Resources/Models/hey_jarvis_v0.1.onnx  1.2 MB
Dockwright/Resources/Models/melspectrogram.onnx   1.0 MB
assets/screenshot-empty.png                        644 KB
assets/screenshot-chat.png                         585 KB
```

Total: ~6.3 MB of binary blobs in git history. Recommend migrating to Git LFS or hosting ML models externally.

---

## Action Items

### Immediate (overdue from last week)
- [ ] **agentlenz**: Remove tracked `.pyc` / `__pycache__` files from git index:
  ```bash
  git rm -r --cached 'backend/**/__pycache__' 'sdk/**/__pycache__' && git commit -m "chore: remove tracked pyc files"
  ```

### Short-term
- [ ] **agentlenz**: Run `npm install` in `dashboard/` and commit a lockfile
- [ ] **agentlenz**: Add `uv.lock` or `requirements.lock` for backend and SDK (reproducible builds)
- [ ] **agentlenz**: Bump dashboard deps (`next 16.2.1 → 16.2.10`, `react 19.2.4 → 19.2.7`)

### Long-term
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external hosting
- [ ] **dockwright**: Add Swift test target covering `CronEngine`, `LLMService`, `ToolExecutor`

# Weekly Health Report — 2026-06-29

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | Dashboard `node_modules` missing; `.pyc` files tracked in git |
| dockwright-macos-agent | ⚠️ Warning | Large binaries in git (4 MB+ ML models + video); no test suite; 3 months since last commit |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Pinned Constraint | Status |
|---------|-------------------|--------|
| fastapi | `>=0.115` | No lockfile; not checked |
| uvicorn | `>=0.32` | No lockfile; not checked |
| sqlalchemy | `>=2.0` | No lockfile; not checked |
| asyncpg | `>=0.30` | No lockfile; not checked |
| alembic | `>=1.14` | No lockfile; not checked |
| pydantic | `>=2.0` | No lockfile; not checked |

> **Note:** Backend has no lockfile (no `requirements.lock` or `uv.lock`). Builds are non-reproducible.

**SDK (`sdk/pyproject.toml`):**

| Package | Pinned Constraint |
|---------|-------------------|
| httpx | `>=0.27` |
| pydantic | `>=2.0` |

**Dashboard (`dashboard/package.json`) — ⚠️ Node modules not installed:**

`npm install` has never been run in this environment. All dependencies are UNMET. Notable version drift (based on `npm outdated` against `package.json`):

| Package | Wanted | Latest | Drift |
|---------|--------|--------|-------|
| next | 16.2.1 | 16.2.9 | Minor |
| react | 19.2.4 | 19.2.7 | Minor |
| react-dom | 19.2.4 | 19.2.7 | Minor |
| recharts | ^3.8.0 | 3.9.0 | Minor |
| @tanstack/react-query | ^5.95.1 | 5.101.2 | Minor |

All updates are minor/patch — safe to upgrade.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0
```

Zero markers across all `.py`, `.ts`, `.tsx`, `.js` files. Excellent.

### 4. Test Status

| Suite | Result |
|-------|--------|
| `sdk` (pytest) | ✅ 25 passed, 1 skipped |
| `backend` (pytest) | ✅ 17 passed |
| `dashboard` | ⚠️ No test suite detected |

SDK produces a benign atexit warning (`RuntimeError: Call agentlenz.init() before using AgentLenz`) — not a test failure, but worth suppressing in CI.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ Detached from `refs/heads/main` |
| Commits this week | 5 (standup files) |
| Last commit | 2026-06-26 |

**⚠️ Issue: `.pyc` files tracked in git.** The largest tracked files include compiled Python bytecode:

```
sdk/tests/__pycache__/test_spans.cpython-314-pytest-9.0.2.pyc   (9.6 KB)
sdk/tests/__pycache__/test_spans.cpython-312-pytest-9.0.2.pyc   (8.8 KB)
sdk/tests/__pycache__/test_budget.cpython-312-pytest-9.0.2.pyc  (8.4 KB)
```

These should be added to `.gitignore` and removed from the repository.

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

Pure Apple-framework Swift project (Xcode). No SPM packages, no `Package.swift`, no third-party dependency manager in use. N/A.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Notably clean for a large codebase.

### 4. Test Status

⚠️ No test suite detected. No Swift test target, no test files found. A project of this size and complexity (104 `.swift` files, multi-phase architecture) would benefit from at least unit tests for core logic (LLMService, CronEngine, ToolExecutor).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ Detached at `refs/heads/main` |
| Commits this week | 0 |
| Last commit | ~3 months ago (`d6d3f3f chore: update UIAutomationTool`) |

**⚠️ Issue: Large binary files tracked in git.** Several large binaries are committed directly (no Git LFS):

```
assets/demo.mov                                    1.5 MB  ← video file
Dockwright/Resources/Models/embedding_model.onnx  1.3 MB
Dockwright/Resources/Models/hey_jarvis_v0.1.onnx  1.3 MB
Dockwright/Resources/Models/melspectrogram.onnx   1.1 MB
assets/screenshot-empty.png                        676 KB
assets/screenshot-chat.png                         614 KB
```

Total: ~6.5 MB of binary blobs in git history. Recommend migrating to Git LFS or hosting ML models externally.

**⚠️ Issue: Repository is 3 months stale.** Last code change was `UIAutomationTool` update. Either development has moved elsewhere or the project is dormant.

---

## Action Items

### Immediate
- [ ] **agentlenz**: Remove `.pyc` / `__pycache__` files from git, add `**/__pycache__/` and `**/*.pyc` to `.gitignore`
- [ ] **agentlenz**: Run `npm install` in `dashboard/` and commit a lockfile

### Short-term
- [ ] **agentlenz**: Add a lockfile (`uv.lock` or `requirements.lock`) for backend and SDK to make builds reproducible
- [ ] **agentlenz**: Suppress the atexit `RuntimeError` in SDK tests (or fix `EventClient.flush` to check init state)
- [ ] **agentlenz**: Bump minor dashboard deps (`next`, `react`, `recharts`, `@tanstack/react-query`)

### Long-term
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external storage
- [ ] **dockwright**: Add a test suite (Swift testing target) for at least `CronEngine`, `LLMService`, and `ToolExecutor`
- [ ] **dockwright**: Confirm whether development is active or project is on hold

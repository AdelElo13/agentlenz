# Weekly Health Report — 2026-08-17

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | 6 stale standup branches; `.pyc` files tracked in git (**7th week unresolved**); backend has no lockfile |
| dockwright-macos-agent | ⚠️ Warning | `fix/bug-audit-v1` unmerged (37 bug fixes waiting); no test suite; large binaries in git (no LFS) |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

6 old standup branches are accumulating on the remote and are **not** merged into `main`:

| Branch | Status |
|--------|--------|
| `standup-2026-05-27` | Not merged — stale |
| `standup-2026-06-16` | Not merged — stale |
| `standup-2026-06-17` | Not merged — stale |
| `standup-2026-06-22` | Not merged — stale |
| `standup-2026-06-29` | Not merged — stale |
| `standup-2026-07-13` | Not merged — stale |

**Recommendation:** Delete all 6 with `git push origin --delete standup-2026-05-27 standup-2026-06-16 standup-2026-06-17 standup-2026-06-22 standup-2026-06-29 standup-2026-07-13`.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Constraint | Installed | Status |
|---------|-----------|-----------|--------|
| fastapi | `>=0.115` | 0.141.1 | ✅ Satisfied |
| uvicorn | `>=0.32` | 0.52.3 | ✅ Satisfied |
| sqlalchemy | `>=2.0` | 2.0.52 | ✅ Satisfied |
| pydantic | `>=2.0` | 2.13.4 | ✅ Satisfied |
| httpx | `>=0.27` | 0.28.1 | ✅ Satisfied |

> ⚠️ Backend has no lockfile (`requirements.lock` or similar). Pinning via `>=` constraints leaves builds non-reproducible.

**SDK (`sdk/pyproject.toml`):** `httpx>=0.27`, `pydantic>=2.0` — both satisfied (0.28.1, 2.13.4).

**Dashboard (`dashboard/package.json`):**

| Package | Pinned Version | Notes |
|---------|---------------|-------|
| next | 16.2.1 | ✅ Recent |
| react | 19.2.4 | ✅ Current |
| @tanstack/react-query | ^5.95.1 | ✅ Current |
| recharts | ^3.8.0 | ✅ Current |

No `npm audit` run (no Node environment). Manual check recommended for CVEs.

### 3. Code Quality

```
TODO/FIXME/HACK comments: 0  ✅
```

Zero code smell markers across all `.py`, `.ts`, `.js` files.

### 4. Test Status

| Suite | Result |
|-------|--------|
| `sdk/tests/` (25 tests) | ✅ 25 passed, 1 skipped |
| `backend/tests/` (17 tests) | ✅ 17 passed |

**Minor issue:** SDK emits a noisy `RuntimeError` at process exit when tests run without calling `agentlenz.init()`. Not a test failure, but it pollutes CI output.

```
RuntimeError: Call agentlenz.init() before using AgentLenz
```

Fix: guard the `flush()` atexit callback with a try/except or check initialisation state before flushing.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| `.pyc` files tracked in git | ⚠️ Still present (7th week) |
| Large files (>1MB) | ✅ None |

The `.pyc` files (`sdk/tests/__pycache__/*.pyc`, `backend/alembic/versions/__pycache__/*.pyc`) remain tracked in git. A `**/__pycache__` entry in `.gitignore` plus `git rm -r --cached **/__pycache__` will resolve this permanently.

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale / Unmerged Branches

| Branch | Commits Ahead of `main` | Status |
|--------|------------------------|--------|
| `fix/bug-audit-v1` | 1 | **Unmerged — needs review** |

The unmerged commit is:
```
f38d3c0  fix: resolve 37 audited bugs + 2 hardening items across Dockwright
```

This is a significant body of work (37 bugs + 2 hardening items). It has been sitting unmerged. **Recommend reviewing and merging `fix/bug-audit-v1` → `main` promptly.**

### 2. Dependency Health

No SPM packages — the project uses Apple frameworks only (Speech, AVFoundation, Vision, etc.). No external dependency file to audit. ✅

### 3. Code Quality

```
TODO/FIXME/HACK comments: 0  ✅
```

Zero code smell markers across all `.swift` files.

### 4. Test Status

| Suite | Result |
|-------|--------|
| XCTest / Unit tests | ⚠️ No test suite found |

The project has no automated tests. This is a recurring concern, especially with 37 bugs recently resolved. Even minimal integration tests for core flows (LLM service, tool registry, cron engine) would catch regressions.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files (no LFS) | ⚠️ See below |
| HEAD state | ⚠️ Detached (container artefact, not critical) |

Large files tracked directly in git (no Git LFS):

| File | Size |
|------|------|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |
| `assets/screenshot-empty.png` | 676 KB |
| `assets/screenshot-chat.png` | 614 KB |

**Total large binary payload:** ~5.8 MB. Consider Git LFS for ONNX models and video assets to keep clone size manageable.

---

## Action Items

| Priority | Repo | Action |
|----------|------|--------|
| 🔴 High | dockwright-macos-agent | Review and merge `fix/bug-audit-v1` — 37 bug fixes unreviewed |
| 🟡 Medium | agentlenz | Delete 6 stale standup branches on origin |
| 🟡 Medium | agentlenz | Add `**/__pycache__` to `.gitignore` and remove tracked `.pyc` files (7th week) |
| 🟡 Medium | agentlenz | Add a backend lockfile (`pip-compile` or `uv lock`) for reproducible builds |
| 🟢 Low | agentlenz | Fix SDK `flush()` atexit RuntimeError (add init-guard before flushing) |
| 🟢 Low | dockwright-macos-agent | Add basic XCTest suite for LLM service and tool registry |
| 🟢 Low | dockwright-macos-agent | Migrate ONNX models and demo video to Git LFS |

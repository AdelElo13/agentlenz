# Weekly Health Report — 2026-07-13

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | `.pyc` files tracked in git (**3rd week unresolved**); Next.js 2 high CVEs; no backend lockfile |
| dockwright-macos-agent | ⚠️ Warning | 0 commits in 3+ months; no test suite; large binaries in git (no LFS) |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Constraint | Status |
|---------|-----------|--------|
| fastapi | `>=0.115` | No lockfile; non-reproducible |
| uvicorn | `>=0.32` | No lockfile |
| sqlalchemy | `>=2.0` | No lockfile |
| asyncpg | `>=0.30` | No lockfile |
| alembic | `>=1.14` | No lockfile |
| pydantic | `>=2.0` | No lockfile |

> **No lockfile** (`uv.lock` / `requirements.lock`) — flagged 3 consecutive weeks. Builds are non-reproducible.

**SDK (`sdk/pyproject.toml`):**

| Package | Constraint |
|---------|-----------|
| httpx | `>=0.27` |
| pydantic | `>=2.0` |

No lockfile here either.

**Dashboard (`dashboard/package.json`) — ⚠️ 6 npm vulnerabilities (2 high):**

| Package | Pinned Version | Vulnerability |
|---------|---------------|---------------|
| next | 16.2.1 | **HIGH** — DoS via Server Components, middleware proxy bypass, cache poisoning (13 CVEs) |
| @babel/core | (transitive) | **HIGH** — Arbitrary File Read via sourceMappingURL comment |
| brace-expansion | (transitive) | Moderate — DoS via zero-step sequence |
| js-yaml | (transitive) | Moderate — DoS via merge key aliases |

`npm audit fix` can fix most; `next` requires `--force` (major bump). Next.js vulnerabilities are extensive — upgrade path should be evaluated carefully.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0
```

Zero markers across all `.py`, `.ts`, `.tsx`, `.js` files. Excellent — clean for three consecutive weeks.

### 4. Test Status

| Suite | Result |
|-------|--------|
| `sdk` (pytest) | ✅ 25 passed, 1 skipped (0.09s) |
| `backend` (pytest) | ⚠️ Not run — PostgreSQL not available in this environment |
| `dashboard` | ⚠️ No test suite |

Skipped test: `test_sdk_sends_events_to_backend` — integration test requiring a live backend endpoint; expected.

**⚠️ Atexit error in test runner:** `EventClient.flush()` throws `RuntimeError: Call agentlenz.init() before using AgentLenz` during teardown. Non-fatal (all 25 tests pass), but indicates the SDK client is partially initialized in tests without a corresponding `init()` call.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this week | 3 (standup: Jul 8, 9, 10) |
| Last commit | `be812db` 2026-07-10 |

**⚠️ ESCALATED — `.pyc` / `__pycache__` files tracked in git (3rd consecutive week):**

50 compiled Python files are still in the git index despite `.gitignore` covering them. The index was never cleaned after `.gitignore` was updated. This inflates repo size and causes spurious diffs.

Fix (one command):
```bash
git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
git commit -m "chore: remove tracked pyc files from index"
```

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. `main` is the only branch. Clean.

> HEAD is detached (`HEAD detached at refs/heads/main`) — environment checkout artifact, not an upstream issue.

### 2. Dependency Health

Pure Apple-framework Swift project. No SPM packages, no third-party dependencies. N/A.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Notably clean for a 104-file macOS application.

### 4. Test Status

⚠️ **No test suite.** No Swift test target found in the project. A 104-file macOS agent (LLMService, CronEngine, ToolExecutor, VoiceService, ScreenCapture, BrowserTabWatcher, etc.) has zero automated test coverage.

Minimum recommended targets: `CronEngine` (cron expression parsing), `LLMService` (SSE streaming/parsing), `ToolExecutor` (argument dispatch + security blocking).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ Detached (environment artifact) |
| Commits this week | 0 |
| Last commit | `d6d3f3f` 2026-04-06 — 98 days ago |

**⚠️ ESCALATED — No commits in 3+ months.** Last activity was April 6, 2026. If this repo is in active development, work may be happening on an untracked branch or locally without pushes.

**⚠️ Large binary files tracked without Git LFS (unchanged from prior reports):**

```
assets/demo.mov                                    1.5 MB
Dockwright/Resources/Models/embedding_model.onnx  1.3 MB
Dockwright/Resources/Models/hey_jarvis_v0.1.onnx  1.2 MB
Dockwright/Resources/Models/melspectrogram.onnx   1.0 MB
assets/screenshot-empty.png                         648 KB
assets/screenshot-chat.png                          600 KB
assets/demo.mp4                                      92 KB
```

Total: ~6.4 MB of binary blobs in git history (not in LFS). Every clone fetches these in full.

---

## Action Items

### Overdue (flagged 3 consecutive weeks — action needed now)
- [ ] **agentlenz**: Remove tracked `.pyc` / `__pycache__` from git index:
  ```bash
  git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
  git commit -m "chore: remove tracked pyc files from index"
  ```

### High priority
- [ ] **agentlenz dashboard**: Evaluate Next.js upgrade path — 13 CVEs in current version (16.2.1); `npm audit fix --force` required (major bump)
- [ ] **agentlenz**: Fix atexit `RuntimeError` in `EventClient.flush()` — guard `flush()` with a config-exists check rather than raising
- [ ] **agentlenz**: Add backend lockfile (`uv.lock`) for reproducible builds — 3rd week without one

### Short-term
- [ ] **agentlenz**: Verify backend test suite passes — tests exist in `backend/tests/` but require PostgreSQL; add a CI job or Docker compose setup
- [ ] **agentlenz**: Add dashboard test suite (Vitest or Playwright)

### Long-term
- [ ] **dockwright**: Investigate 3-month commit gap — confirm repo is still actively used
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external hosting
- [ ] **dockwright**: Add Swift test target covering core logic (`CronEngine`, `LLMService`, `ToolExecutor`)

---

*Report generated by automated health check · Next run: 2026-07-20*

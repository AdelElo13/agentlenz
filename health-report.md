# Weekly Health Report — 2026-07-27

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | `.pyc` files tracked in git (**4th week unresolved**); Next.js CVEs outstanding; no backend lockfile |
| dockwright-macos-agent | ⚠️ Warning | 0 commits in 113 days; no test suite; large binaries in git (no LFS) |

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
| psycopg2-binary | `>=2.9` | No lockfile |

> **No lockfile** (`uv.lock` / `requirements.lock`) — flagged 4 consecutive weeks. Builds are non-reproducible. Add `uv lock` or `pip-compile` to CI.

**SDK (`sdk/pyproject.toml`):**

| Package | Constraint |
|---------|-----------|
| httpx | `>=0.27` |
| pydantic | `>=2.0` |

No lockfile here either.

**Dashboard (`dashboard/package.json`) — ⚠️ CVEs outstanding:**

| Package | Pinned Version | Status |
|---------|---------------|--------|
| next | 16.2.1 | **HIGH** — DoS via Server Components, middleware proxy bypass, cache poisoning |
| @babel/core | (transitive) | **HIGH** — Arbitrary File Read via sourceMappingURL |
| brace-expansion | (transitive) | Moderate — DoS via zero-step sequence |
| js-yaml | (transitive) | Moderate — DoS via merge key aliases |

These CVEs were present in the last two reports and remain unresolved. Run `npm audit fix --force` in `dashboard/` (Next.js major bump required).

### 3. Code Quality

```
TODO / FIXME / HACK count: 0
```

Zero markers across all `.py`, `.ts`, `.tsx`, `.js` files. Excellent — clean for four consecutive weeks.

### 4. Test Status

| Suite | Files | Result |
|-------|-------|--------|
| `sdk` (pytest) | 10 test files | ⚠️ Cannot run — `pytest` and `httpx` not installed in this environment |
| `backend` (pytest) | 6 test files | ⚠️ Cannot run — PostgreSQL not available in this environment |
| `dashboard` | — | ⚠️ No test suite |

Both test suites exist and are well-structured. The inability to run them is an environment constraint (no `pip install -e .[dev]` performed). Recommend adding a CI job (GitHub Actions) so tests run on push, making this a non-issue in the weekly check.

> **Note from Jul 13 report:** SDK teardown `RuntimeError: Call agentlenz.init() before using AgentLenz` in `EventClient.flush()` — status unknown; cannot re-verify without running tests.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this period (2 weeks) | 3 (standup: Jul 14, Jul 27; health: Jul 13) |
| Last commit | `d70e490` 2026-07-27 |

**⚠️ ESCALATED — `.pyc` / `__pycache__` files tracked in git (4th consecutive weekly report):**

50 compiled Python files remain in the git index. The fix is a single command and takes under 60 seconds — this has been in the Action Items list since June:

```bash
cd /home/user/agentlenz
git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
git commit -m "chore: remove tracked pyc files from index"
git push
```

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. `main` is the only branch. Clean.

> HEAD is detached (`HEAD detached at refs/heads/main`) — environment checkout artifact, not an upstream issue.

### 2. Dependency Health

Pure Apple-framework Swift project. No SPM packages, no third-party dependencies. **N/A.**

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Notably clean for a 104-file macOS application.

### 4. Test Status

⚠️ **No test suite.** No Swift test target found in the project. A 104-file macOS agent (LLMService, CronEngine, ToolExecutor, VoiceService, ScreenCaptureService, BrowserTabWatcher, etc.) has zero automated test coverage — unchanged from prior reports.

Minimum recommended targets: `CronEngine` (cron expression parsing), `LLMService` (SSE streaming/parsing), `ToolExecutor` (argument dispatch + security blocking).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ Detached (environment artifact) |
| Commits this period (2 weeks) | 0 |
| Last commit | `d6d3f3f` 2026-04-06 — **113 days ago** |

**⚠️ ESCALATED — No commits in 113 days (3.7 months).** If this repo is in active development, work may be happening locally without pushes or on an untracked branch. If the project is paused, consider archiving it on GitHub to signal its status.

**⚠️ Large binary files tracked without Git LFS (unchanged):**

```
assets/demo.mov                                    1.5 MB
Dockwright/Resources/Models/embedding_model.onnx  1.3 MB
Dockwright/Resources/Models/hey_jarvis_v0.1.onnx  1.2 MB
Dockwright/Resources/Models/melspectrogram.onnx   1.0 MB
assets/screenshot-empty.png                         660 KB
assets/screenshot-chat.png                          599 KB
assets/demo.mp4                                      88 KB
```

Total: ~6.4 MB of binary blobs in git history (not in LFS). Every clone fetches these in full. Migrate with `git lfs migrate import` or host externally.

---

## Action Items

### Overdue (4 consecutive reports — action needed now)
- [ ] **agentlenz**: Remove tracked `.pyc` / `__pycache__` from git index — one command:
  ```bash
  git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
  git commit -m "chore: remove tracked pyc files from index"
  git push
  ```

### High priority
- [ ] **agentlenz dashboard**: Run `npm audit fix --force` in `dashboard/` — Next.js CVEs outstanding for 2+ weeks
- [ ] **agentlenz**: Add backend lockfile (`uv.lock`) — flagged 4 weeks without resolution
- [ ] **agentlenz**: Fix teardown `RuntimeError` in `EventClient.flush()` — guard with `if not self._config: return`
- [ ] **agentlenz**: Wire tests to CI (GitHub Actions `pytest`) so the weekly check can report pass/fail

### Short-term
- [ ] **agentlenz**: Add dashboard test suite (Vitest or Playwright)
- [ ] **dockwright**: Confirm active development status — 113 days without a commit; archive if inactive

### Long-term
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external hosting
- [ ] **dockwright**: Add Swift test target covering core logic (`CronEngine`, `LLMService`, `ToolExecutor`)

---

*Report generated by automated health check · Next run: 2026-08-03*

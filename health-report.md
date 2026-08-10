# Weekly Health Report — 2026-08-10

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | `.pyc` files tracked in git (**6th week unresolved**); npm CVEs outstanding; dashboard deps not installed; no backend lockfile |
| dockwright-macos-agent | ⚠️ Warning | 0 commits in 126 days; no test suite; large binaries in git (no LFS); HEAD detached |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Constraint | Installed | Status |
|---------|-----------|-----------|--------|
| fastapi | `>=0.115` | 0.141.1 | ✅ Satisfied |
| uvicorn | `>=0.32` | — | ✅ Constraint satisfied |
| sqlalchemy | `>=2.0` | — | ⚠️ No lockfile |
| asyncpg | `>=0.30` | — | ⚠️ No lockfile |
| alembic | `>=1.14` | — | ⚠️ No lockfile |
| pydantic | `>=2.0` | 2.13.4 | ✅ Satisfied |
| psycopg2-binary | `>=2.9` | — | ⚠️ No lockfile |

> **No lockfile** (`uv.lock` / `requirements.lock`) — flagged **6 consecutive weeks**. Builds are non-reproducible. Add `uv lock` or `pip-compile` to CI.

**SDK (`sdk/pyproject.toml`):**

| Package | Constraint | Installed | Status |
|---------|-----------|-----------|--------|
| httpx | `>=0.27` | 0.28.1 | ✅ Satisfied |
| pydantic | `>=2.0` | 2.13.4 | ✅ Satisfied |
| anthropic | `>=0.40` (optional) | — | ✅ Constraint satisfied |
| openai | `>=1.50` (optional) | — | ✅ Constraint satisfied |

No lockfile.

**Dashboard (`dashboard/package.json`):**

| Package | Pinned Version | Latest | Status |
|---------|---------------|--------|--------|
| next | 16.2.1 | **16.3.0** | ⚠️ Minor update available; 16.2.1→16.2.12 fixes PostCSS path traversal |
| react | 19.2.4 | 19.2.8 | Patch update available |
| react-dom | 19.2.4 | 19.2.8 | Patch update available |
| @tanstack/react-query | ^5.95.1 | 5.101.4 | Minor update available |
| recharts | ^3.8.0 | 3.10.1 | Minor update available |

> ⚠️ **`node_modules` not installed** — all dashboard packages show as MISSING. `npm install` has not been run in `dashboard/`.
> CVE status cannot be fully verified without installed packages. Based on pinned `next@16.2.1`, the PostCSS path traversal and related high-severity CVEs from prior reports remain unpatched.
> Run `npm install && npm audit fix` in `dashboard/` to install and remediate.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across .py, .ts, .js files)
```

Zero markers across all source files. Clean for six consecutive weeks.

### 4. Test Status

| Suite | Result | Details |
|-------|--------|---------|
| `sdk` (pytest) | ✅ **25 passed, 1 skipped** | 7 test files |
| `backend` (pytest) | ✅ **17 passed** | 6 test files |
| `dashboard` | ⚠️ No test suite | — |

> **Note:** SDK teardown emits a `RuntimeError: Call agentlenz.init() before using AgentLenz` in an atexit handler — benign and tests pass cleanly, but worth fixing. Guard `EventClient.flush()` with an early return if `_config` is not set.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this week | 5 (standup: 2026-08-04 through 2026-08-10) |
| Last commit | `b6e5aca` "standup: 2026-08-10" |

> ⚠️ **ESCALATED — `.pyc` / `__pycache__` files tracked in git (6th consecutive weekly report).**
>
> Compiled Python files remain in the git index, causing unnecessary churn and inflating clone size. One command to fix:
>
> ```bash
> cd agentlenz
> git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
> printf "__pycache__/\n*.pyc\n" >> .gitignore
> git commit -m "chore: remove tracked pyc files and add gitignore entries"
> git push
> ```

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. `main` is the only branch. Clean.

> ⚠️ HEAD is in a **detached state** (`HEAD detached at refs/heads/main`). This is unusual — any new commits made in this state would not update the branch ref. Resolve with `git checkout main`.

### 2. Dependency Health

Pure Apple-framework Swift project. No SPM packages or third-party dependencies declared. **N/A.**

Model files present in `Dockwright/Resources/Models/`:
- `melspectrogram.onnx`
- `embedding_model.onnx`
- `hey_jarvis_v0.1.onnx`

These are binary blobs tracked directly in git without LFS (see Git Hygiene).

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Clean for all weekly reports to date.

### 4. Test Status

⚠️ **No test suite.** No Swift test target found. A 104-file macOS agent (LLMService, CronEngine, ToolExecutor, VoiceService, ScreenCaptureService, BrowserTabWatcher, etc.) has zero automated test coverage — unchanged from all prior reports.

Minimum recommended targets: `CronEngine` (cron expression parsing), `LLMService` (SSE streaming/parsing), `ToolExecutor` (argument dispatch + security blocking).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ⚠️ **Detached at refs/heads/main** |
| Commits this week | 0 |
| Last commit | `d6d3f3f` "chore: update UIAutomationTool" — **126 days ago** (~2026-04-06) |

> ⚠️ **ESCALATED — No commits in 126 days (4.1 months).** If development is happening locally, push the branch. If the project is paused, consider archiving on GitHub to signal its status.

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

Total: ~6.4 MB of binary blobs in git history. Every clone fetches the full history. Migrate with `git lfs migrate import` or host externally (e.g. GitHub Releases).

---

## Action Items

### Overdue (6 consecutive reports — action needed now)
- [ ] **agentlenz**: Remove tracked `.pyc` / `__pycache__` from git index and add `.gitignore` entries (command above in Git Hygiene section)

### High priority
- [ ] **agentlenz dashboard**: `cd dashboard && npm install && npm audit fix` — installs packages and remediates high-severity CVEs in `next@16.2.1`
- [ ] **agentlenz**: Add backend lockfile (`uv.lock`) — flagged 6 weeks without resolution
- [ ] **agentlenz**: Fix teardown `RuntimeError` in `EventClient.flush()` — guard with `if not self._initialized: return`
- [ ] **dockwright**: Fix detached HEAD: `git checkout main`
- [ ] **dockwright**: Confirm active development status — 126 days without a push; archive if inactive

### Short-term
- [ ] **agentlenz**: Wire SDK and backend tests to CI (GitHub Actions) so the weekly check confirms pass/fail automatically
- [ ] **agentlenz**: Add dashboard test suite (Vitest or Playwright)
- [ ] **agentlenz**: Upgrade `next` to 16.3.0 in `dashboard/package.json`

### Long-term
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external hosting
- [ ] **dockwright**: Add Swift test target covering core logic (`CronEngine`, `LLMService`, `ToolExecutor`)

---

## Week-over-Week Deltas

| Area | Last Week | This Week | Change |
|------|-----------|-----------|--------|
| agentlenz: test status | ✅ SDK 25/25, Backend 17/17 | ✅ SDK 25/25, Backend 17/17 | No change (stable) |
| agentlenz: pyc files | ⚠️ 50 files (5 weeks) | ⚠️ 50 files (6 weeks) | No change |
| agentlenz: dashboard CVEs | ⚠️ 7 CVEs (6 high) | ⚠️ Unverified (deps not installed) | No change |
| agentlenz: commit activity | 5 commits | 5 commits | No change (active) |
| dockwright: days inactive | 119 days | 126 days | +7 days |
| dockwright: HEAD state | ⚠️ Detached | ⚠️ Detached | No change |

---

*Report generated by automated health check · Next run: 2026-08-17*

# Weekly Health Report — 2026-08-03

> Generated automatically. Repos analysed: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## Summary

| Repo | Health | Key Issues |
|------|--------|------------|
| agentlenz | ⚠️ Warning | `.pyc` files tracked in git (**5th week unresolved**); 7 npm CVEs (6 high) outstanding; no backend lockfile |
| dockwright-macos-agent | ⚠️ Warning | 0 commits in 119 days; no test suite; large binaries in git (no LFS) |

---

## `adelelo13/agentlenz`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. Only `main` exists locally and on origin. Clean.

### 2. Dependency Health

**Backend (`backend/pyproject.toml`):**

| Package | Constraint | Status |
|---------|-----------|--------|
| fastapi | `>=0.115` | Latest: 0.141.1 — constraint satisfied |
| uvicorn | `>=0.32` | Latest: 0.52.1 — constraint satisfied |
| sqlalchemy | `>=2.0` | No lockfile |
| asyncpg | `>=0.30` | No lockfile |
| alembic | `>=1.14` | No lockfile |
| pydantic | `>=2.0` | Latest: 2.13.4 — constraint satisfied |
| psycopg2-binary | `>=2.9` | No lockfile |

> **No lockfile** (`uv.lock` / `requirements.lock`) — flagged **5 consecutive weeks**. Builds are non-reproducible. Add `uv lock` or `pip-compile` to CI.

**SDK (`sdk/pyproject.toml`):**

| Package | Constraint | Status |
|---------|-----------|--------|
| httpx | `>=0.27` | Latest: 0.28.1 — constraint satisfied |
| anthropic | `>=0.40` | Latest: 0.120.2 — constraint satisfied |
| pydantic | `>=2.0` | Latest: 2.13.4 — constraint satisfied |

No lockfile.

**Dashboard (`dashboard/package.json`) — ⚠️ 7 CVEs (6 high, 1 low):**

| Package | Pinned Version | Latest | Status |
|---------|---------------|--------|--------|
| next | 16.2.1 | 16.2.12 | **HIGH** — PostCSS path traversal; fix via upgrade to 16.2.12 |
| sharp | (transitive) | >=0.35.0 | **HIGH** — 4 CVEs in libvips (CVE-2026-33327/33328/35590/35591) |
| postcss | (transitive) | — | **HIGH** — Arbitrary `.map` file disclosure via sourceMappingURL |
| react | 19.2.4 | 19.2.8 | Patch update available |

> Dashboard packages show as MISSING — `npm install` has not been run in the `dashboard/` directory.
> Running `npm audit fix --force` in `dashboard/` will upgrade Next.js to 16.2.12 and resolve all 7 CVEs.
> These CVEs have been outstanding for **3+ consecutive reports**.

### 3. Code Quality

```
TODO / FIXME / HACK count: 0
```

Zero markers across all `.py`, `.ts`, `.tsx`, `.js` files. Excellent — clean for five consecutive weeks.

### 4. Test Status

| Suite | Files | Result |
|-------|-------|--------|
| `sdk` (pytest) | 7 test files | ✅ **25 passed, 1 skipped** |
| `backend` (pytest) | 6 test files | ✅ **17 passed** |
| `dashboard` | — | ⚠️ No test suite |

> **Improvement this week:** Both Python test suites now run and pass (previously blocked by missing deps). SDK teardown `RuntimeError` in `EventClient.flush()` is a benign atexit issue — tests pass cleanly otherwise.

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this week | 5 (standup files: Jul 28–Aug 3) |
| Last commit | `8cfe758` 2026-08-03 |

**⚠️ ESCALATED — `.pyc` / `__pycache__` files tracked in git (5th consecutive weekly report):**

50 compiled Python files remain in the git index. One command fixes it:

```bash
cd agentlenz
git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
git commit -m "chore: remove tracked pyc files and add gitignore entries"
git push
```

---

## `adelelo13/dockwright-macos-agent`

**Overall: ⚠️ Warning**

### 1. Stale Branches

No stale merged branches. `main` is the only branch. Clean.

### 2. Dependency Health

Pure Apple-framework Swift project. No SPM packages, no third-party dependencies. **N/A.**

Model files present in `Dockwright/Resources/Models/`:
- `melspectrogram.onnx`
- `embedding_model.onnx`
- `hey_jarvis_v0.1.onnx`

These are binary blobs tracked directly in git (see Git Hygiene below).

### 3. Code Quality

```
TODO / FIXME / HACK count: 0  (across 104 .swift files)
```

Zero markers. Clean for all weekly reports.

### 4. Test Status

⚠️ **No test suite.** No Swift test target found. A 104-file macOS agent (LLMService, CronEngine, ToolExecutor, VoiceService, ScreenCaptureService, BrowserTabWatcher, etc.) has zero automated test coverage — unchanged from all prior reports.

Minimum recommended targets: `CronEngine` (cron expression parsing), `LLMService` (SSE streaming/parsing), `ToolExecutor` (argument dispatch + security blocking).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ Clean |
| Stashes | ✅ None |
| HEAD state | ✅ On `main` |
| Commits this week | 0 |
| Last commit | `d6d3f3f` 2026-04-06 — **119 days ago** |

**⚠️ ESCALATED — No commits in 119 days (3.9 months).** If this repo is in active development, work may be happening locally without pushes or on an untracked branch. If the project is paused, consider archiving it on GitHub to signal its status.

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

### Overdue (5 consecutive reports — action needed now)
- [ ] **agentlenz**: Remove tracked `.pyc` / `__pycache__` from git index:
  ```bash
  git rm -r --cached $(git ls-files | grep -E '\.pyc$|__pycache__')
  echo -e "__pycache__/\n*.pyc" >> .gitignore
  git commit -m "chore: remove tracked pyc files and add gitignore entries"
  git push
  ```

### High priority
- [ ] **agentlenz dashboard**: Run `npm audit fix --force` in `dashboard/` — 7 CVEs (6 high) outstanding for 3+ weeks; upgrades Next.js to 16.2.12
- [ ] **agentlenz**: Add backend lockfile (`uv.lock`) — flagged 5 weeks without resolution
- [ ] **agentlenz**: Run `npm install` in `dashboard/` so packages are actually installed
- [ ] **agentlenz**: Fix teardown `RuntimeError` in `EventClient.flush()` — guard with `if not self._config: return`
- [ ] **agentlenz**: Wire tests to CI (GitHub Actions `pytest`) so the weekly check confirms pass/fail automatically

### Short-term
- [ ] **agentlenz**: Add dashboard test suite (Vitest or Playwright)
- [ ] **dockwright**: Confirm active development status — 119 days without a commit; archive if inactive

### Long-term
- [ ] **dockwright**: Migrate `.onnx` models and `demo.mov` to Git LFS or external hosting
- [ ] **dockwright**: Add Swift test target covering core logic (`CronEngine`, `LLMService`, `ToolExecutor`)

---

## Week-over-Week Deltas

| Area | Last Week | This Week | Change |
|------|-----------|-----------|--------|
| agentlenz: test status | ❌ Could not run (no pytest) | ✅ SDK 25/25, Backend 17/17 | **Improved** |
| agentlenz: pyc files | ⚠️ 50 files (4 weeks) | ⚠️ 50 files (5 weeks) | No change |
| agentlenz: dashboard CVEs | ⚠️ CVEs outstanding | ⚠️ 7 CVEs (6 high) | No change |
| dockwright: days inactive | 113 days | 119 days | +6 days |
| dockwright: commit activity | 0 commits | 0 commits | No change |

---

*Report generated by automated health check · Next run: 2026-08-10*

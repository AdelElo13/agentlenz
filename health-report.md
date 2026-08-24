# Weekly Health Report — 2026-08-24

Generated automatically. Two repositories checked: `agentlenz` and `dockwright-macos-agent`.

---

## agentlenz

**Health: ⚠️ Warning**

### 1. Stale Branches

7 remote standup branches exist that were never merged to `main` or cleaned up:

| Branch | Commits ahead of main |
|--------|----------------------|
| `origin/standup-2026-05-27` | **53** — diverged long ago; contains standups + health reports from May–present |
| `origin/standup-2026-08-24` | 1 |
| `origin/standup-2026-07-13` | 1 |
| `origin/standup-2026-06-29` | 1 |
| `origin/standup-2026-06-22` | 3 |
| `origin/standup-2026-06-17` | 1 |
| `origin/standup-2026-06-16` | 1 |

**Action needed:** `standup-2026-05-27` is 53 commits ahead of `main` — all standup and health-report commits appear to be going onto this branch rather than `main`. This is likely the wrong base branch and explains why the remote diverged. The other standup branches (1–3 commits ahead) are normal one-off branch artifacts. Consider deleting them all after confirming nothing is lost.

Note: HEAD is detached from `refs/heads/main` in the local clone, which may affect push targets.

### 2. Dependency Health

**Backend (`pyproject.toml`)** — Python deps use `>=` minimum versions (flexible pinning):
- `fastapi>=0.115`, `uvicorn>=0.32`, `sqlalchemy>=2.0`, `pydantic>=2.0` — all reasonable minimums, no known critical CVEs in these ranges.
- System Python packages show outdated versions (e.g. `cryptography 41.0.7` vs latest `50.0.0`, `pip 24.0` vs `26.2.1`) but these are OS-level packages, not project deps.

**Dashboard (`package.json`)** — Next.js 16.2.1, React 19.2.4. Current versions as of report date.

### 3. Code Quality

| File type | TODO/FIXME/HACK count |
|-----------|----------------------|
| Python (backend) | 0 |
| TypeScript/JS (dashboard) | 0 |
| **Total** | **0** |

Clean codebase — no outstanding code debt markers.

### 4. Test Status

**Backend tests:** ✅ **17 passed, 0 failed** (0.35s)

Test files: `test_budgets.py`, `test_costs.py`, `test_ingest.py`, `test_pricing.py`, `test_recommender.py`, `test_waste_detector.py`

**Dashboard tests:** No test suite configured (`npm test` not set up).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large files (>1MB) | ✅ None |
| HEAD state | ⚠️ Detached from `refs/heads/main` |

---

## dockwright-macos-agent

**Health: ⚠️ Warning**

### 1. Stale Branches

| Branch | Commits ahead of main | Note |
|--------|----------------------|------|
| `origin/fix/bug-audit-v1` | 1 | Contains `fix: resolve 37 audited bugs + 2 hardening items` — **unmerged PR work** |

**Action needed:** `fix/bug-audit-v1` has an unmerged commit with a significant bug-fix payload (37 audited bugs). Either open a PR to merge it or confirm it was intentionally abandoned.

### 2. Dependency Health

No external package manager dependencies — macOS app built with Xcode using only Apple frameworks (Swift, Speech, AVFoundation, Vision). No SPM packages declared. No outdated deps to report.

Deployment target: `MACOSX_DEPLOYMENT_TARGET = 14.0` ✅ (correct per project spec)

### 3. Code Quality

| File type | TODO/FIXME/HACK count |
|-----------|----------------------|
| Swift (104 files) | 0 |

No technical debt markers in any Swift source file.

### 4. Test Status

No test suite present. Xcode unit tests would require a macOS build environment — not available in this CI context. Build validation not run (no Xcode available).

### 5. Git Hygiene

| Check | Status |
|-------|--------|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large files (>1MB) | ⚠️ 4 files tracked in git |
| HEAD state | ⚠️ Detached from `refs/heads/main` |

**Large files in git:**

| File | Size |
|------|------|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.1 MB |

Model files are expected (wake word detection). `assets/demo.mov` is a demo video tracked directly in git — consider moving to Git LFS if the repo grows.

---

## Summary

| Repo | Health | Top Issue |
|------|--------|-----------|
| `agentlenz` | ⚠️ Warning | `standup-2026-05-27` branch is 53 commits ahead of main; 6 other stale branches to clean up |
| `dockwright-macos-agent` | ⚠️ Warning | `fix/bug-audit-v1` has 1 unmerged commit (37 bug fixes) — needs PR or explicit discard |

### Recommended Actions

1. **agentlenz:** Investigate `standup-2026-05-27` — if all standup commits are here and not on `main`, push them. Then delete all stale standup branches.
2. **agentlenz:** Set up `npm test` in the dashboard package.
3. **dockwright-macos-agent:** Open or close a PR for `fix/bug-audit-v1`.
4. **dockwright-macos-agent:** Consider Git LFS for `assets/demo.mov`.

# Weekly Health Report — 2026-04-06

> Generated automatically. Repos analysed: `agentlenz`, `DockWright-MacOS-Agent`.

---

## agentlenz — ⚠️ Warning

**Overall score: Warning** — codebase is clean but has minor hygiene issues.

### 1. Stale Branches
No stale merged branches. Only `main` exists locally and on `origin`. ✅

### 2. Dependency Health
| Ecosystem | File | Status |
|---|---|---|
| Node / npm | `dashboard/package.json` | ✅ All packages up to date (`npm outdated` returned nothing) |
| Python (backend) | `backend/pyproject.toml` | ⚠️ Not checked against lockfile (system pip shows 18 outdated packages; likely OS-level, not project deps) |
| Python (sdk) | `sdk/pyproject.toml` | ⚠️ Not checked against lockfile |

Recommended: run `pip list --outdated` inside each virtual environment to isolate project-level drift.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across 48 source files (.py, .ts, .js, .swift)
```
✅ No technical debt markers found.

### 4. Test Status
Test suites exist in subdirectories:
- `backend/pyproject.toml` — pytest config present; not run (run `cd backend && pytest`)
- `sdk/pyproject.toml` — pytest config present; not run (run `cd sdk && pytest`)
- `dashboard/package.json` — npm test config present; not run

⚠️ No root-level test runner; tests must be invoked per-subproject.

### 5. Git Hygiene
| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large files | ✅ Largest tracked file: `dashboard/package-lock.json` (247 KB — expected) |
| Compiled bytecode tracked | ⚠️ `.pyc` files in `sdk/tests/__pycache__/` are committed to git |

**Action required:** Add `**/__pycache__/` and `**/*.pyc` to `.gitignore` and remove cached bytecode from tracking.

### Recent Activity
```
1a3adbb standup: 2026-04-03
be6e65e standup: 2026-04-01
ea2b54d standup: 2026-03-27
011256f fix(backend): use ssl=disable query param for asyncpg on Fly
dd7a278 fix(backend): disable SSL for Fly internal Postgres connections
```

Last code commit: SSL fix for Fly.io Postgres. Recent commits are standup notes.

---

## DockWright-MacOS-Agent — ⚠️ Warning

**Overall score: Warning** — clean repo but missing tests and has structural hygiene concerns.

### 1. Stale Branches
No stale merged branches. Only `main` exists. ✅

⚠️ **HEAD is in a detached state** (`HEAD detached at refs/heads/main`). This is likely an artifact of the checkout workflow but should be verified.

### 2. Dependency Health
No standard package manifest found (`Package.swift`, `package.json`, `requirements.txt`, `pyproject.toml` — none present). This is a pure Xcode project; dependencies are managed via Xcode's built-in package resolution.

⚠️ Cannot automatically check for outdated dependencies. Manually verify in Xcode → File → Packages → Update to Latest Package Versions.

### 3. Code Quality — TODO / FIXME / HACK
```
Count: 0 across 104 source files (.swift, .py, .ts, .js)
```
✅ No technical debt markers found.

### 4. Test Status
No test suite configuration detected (`XCTest` targets would need to be confirmed in `Dockwright.xcodeproj`). ⚠️

**Recommendation:** Add an `XCTest` target or a CI workflow that runs `xcodebuild test`.

### 5. Git Hygiene
| Check | Status |
|---|---|
| Uncommitted changes | ✅ None |
| Stashes | ✅ None |
| Large binary files in git | ⚠️ See below |

**Large files tracked directly in git:**
| File | Size |
|---|---|
| `assets/demo.mov` | ~1.49 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | ~1.27 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | ~1.21 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | ~1.04 MB |
| `assets/screenshot-empty.png` | ~660 KB |

Total large binary payload: ~5.6 MB. Consider migrating ONNX models and media assets to Git LFS to keep clone size manageable as the project grows.

### Recent Activity
```
928f649 feat: whitelist safe sudo commands (pmset, systemsetup, defaults, etc.)
358b8d9 docs: simplify sudo instructions for non-devs
0837d7b docs: add optional sudo setup for system control
1513e40 fix: correct Keychain keys for integrations, bidirectional tool descriptions
df050b4 fix: Keychain delete loop to clear duplicate entries
```

Active development with recent feature additions and bug fixes. ✅

---

## Action Items Summary

| Priority | Repo | Action |
|---|---|---|
| Medium | agentlenz | Add `**/__pycache__/` and `*.pyc` to `.gitignore`, remove tracked bytecode |
| Medium | agentlenz | Run per-project test suites (`pytest`, `npm test`) in CI |
| Medium | DockWright-MacOS-Agent | Verify / fix detached HEAD state |
| Medium | DockWright-MacOS-Agent | Add `XCTest` target and wire up CI test run |
| Low | DockWright-MacOS-Agent | Migrate ONNX models + `demo.mov` to Git LFS |
| Low | agentlenz | Audit project-level Python deps inside virtual environments |

# Weekly Health Report — 2026-11-23

> Generated automatically. Covers repos: `adelelo13/agentlenz`, `adelelo13/dockwright-macos-agent`.

---

## adelelo13/agentlenz — ⚠️ WARNING

### Git Hygiene
- **Clean working tree** — no uncommitted changes, no stashes
- **No stale branches** — only `main` exists (local + remote)
- HEAD is in detached state from `refs/heads/main` (cosmetic, not blocking)
- Recent activity: daily standup commits, latest `standup: 2026-11-23`

### Dependency Health

| Component | Status |
|-----------|
--------|
| `sdk/pyproject.toml` (`httpx>=0.27`, `pydantic>=2.0`, `anthropic>=0.40`, `openai>=1.50`) | ✅ Loose version pins — no outdated alerts |
| `backend/pyproject.toml` (`fastapi>=0.115`, `sqlalchemy>=2.0`, etc.) | ✅ Loose version pins — no outdated alerts |
| `dashboard/package.json` | ❌ **20 vulnerabilities (1 critical, 9 high, 9 moderate, 1 low)** |

**Dashboard critical/high vulnerabilities (run `npm audit fix`):**
- 🔴 **CRITICAL** `next@16.2.1` — Denial of Service with Server Components (update to 16.4.6 available)
- 🟠 **HIGH** `zod` — Memory exhaustion via oversized constraint validation
- 🟠 **HIGH** `postcss` — XSS via unescaped `</style>` in CSS stringifier
- 🟠 **HIGH** `nanoid` — Non-secure generators can loop indefinitely
- 🟠 **HIGH** `js-yaml`, `brace-expansion`, `picomatch`, `source-map-js`, `sharp`, `browserslist` — various DoS issues
- Dashboard `node_modules` are not installed in repo (CI must install them)

**Available updates:**
- `next` 16.2.1 → 16.4.6 (patch, fixes critical vuln)
- `react` / `react-dom` 19.2.4 → 19.3.1
- `@tanstack/react-query` → 5.108.3

### Code Quality
- **TODO/FIXME/HACK:** 0 (clean across all `.py`, `.ts`, `.js` files)
- Dashboard lint: ✅ No errors

### Test Status
| Suite | Result |
|-------|
--------|
| `sdk/` pytest | ✅ **25 passed, 1 skipped** (0.06s) |
| `backend/` pytest | ✅ **17 passed** (0.36s) |
| `dashboard/` | ⚠️ No test script configured in `package.json` |

### Notes
- Dashboard has no test script. Consider adding `jest` or `vitest` and a `"test"` npm script.
- Atexit warning in SDK tests: `agentlenz.init()` not called in one test path — benign but noisy.

---

## adelelo13/dockwright-macos-agent — ✅ HEALTHY

### Git Hygiene
- **Clean working tree** — no uncommitted changes, no stashes
- **No stale branches** — only `main` exists (local + remote)
- HEAD is in detached state from `refs/heads/main` (cosmetic)
- Recent activity: active development — UIAutomationTool updates, UI/Unicode fixes

### Dependency Health
- No `Package.swift` / SPM dependencies (project uses Apple frameworks only — by design per CLAUDE.md)
- No external package manager files to audit

### Code Quality
- **104 Swift files**
- **TODO/FIXME/HACK:** 0 (clean)

### Test Status
- No test suite (`swift test` not applicable — Xcode project, no `Package.swift`)
- Build verification requires macOS + Xcode (not runnable in this environment)

### Binary Assets in Git (notable sizes)
| File | Size |
|------|
------|
| `assets/demo.mov` | 1.5 MB |
| `Dockwright/Resources/Models/embedding_model.onnx` | 1.3 MB |
| `Dockwright/Resources/Models/hey_jarvis_v0.1.onnx` | 1.2 MB |
| `Dockwright/Resources/Models/melspectrogram.onnx` | 1.0 MB |
| `assets/screenshot-*.png` | ~1.2 MB total |

ONNX models (~3.5 MB) and demo video (~1.5 MB) are tracked in git. Consider Git LFS if the repo grows further.

---

## Action Items

| Priority | Repo | Action |
|----------|
------|
--------|
| 🔴 High | agentlenz/dashboard | Run `npm audit fix` and update `next` to 16.4.6 to resolve critical DoS CVE |
| 🟠 Medium | agentlenz/dashboard | Add a test script (`vitest` or similar) to `package.json` |
| 🟡 Low | agentlenz/dashboard | Run `npm install` and commit `node_modules` to lockfile consistency check in CI |
| 🟡 Low | dockwright-macos-agent | Consider Git LFS for ONNX models and demo video if repo size becomes a concern |

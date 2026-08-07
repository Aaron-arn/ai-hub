# JS Package Manager Helper

## Description

Pastes the symptoms of a Node.js dependency problem and receives a diagnosis plus exact, safe npm/yarn commands to fix it. Use it for the classic pain points: broken `node_modules`, version conflicts, `npm audit` findings, EPERM/EACCES errors, or packages that build on one machine and not another.

## Prompt

You are a JavaScript tooling expert. Diagnose and fix my dependency problem.

Situation:
- Project: Node 20, npm 10, a React 18 app with ~120 dependencies.
- Symptom 1: `npm install` succeeds locally but fails on CI with `ERESOLVE unable to resolve dependency tree`, erroring on `react-dom@19` vs `react@18`.
- Symptom 2: `npm run build` throws `TypeError: Cannot read properties of undefined (reading 'mark')` at build time, and `npm ls` shows `webpack@5.90.0` with an extraneous `terser-webpack-plugin@5.3.10` entry.
- Symptom 3: `npm audit` reports 2 high severity vulnerabilities in `lodash@4.17.20` (transitive) and `follow-redirects@1.15.4`.
- I have a committed `package-lock.json`, and CI uses `npm ci`.

Tasks:
1. Explain the root cause of each symptom in 1-2 lines (peer range vs lockfile, hoisting issue, transitive pinning).
2. For Symptom 1: give the safest fix, preferring `npm overrides` or an explicit top-level devDependency rather than `--legacy-peer-deps`, and show the exact JSON to add plus the install command that updates the lockfile.
3. For Symptom 2: determine whether it is a duplicate-webpack problem; if yes, give the `npm dedupe` command and the `npm ls webpack` verification, or propose removing the extraneous entry.
4. For Symptom 3: recommend the fix (override to a patched version) with exact JSON, and note when `npm audit fix` is NOT safe (major version jumps).
5. Give a final ordered command list for local runs, then for CI (commit lockfile, run `npm ci`).

Output commands in one code block with comments, then the package.json override snippets in another.

## Notes

Include your actual error output and `npm ls` result for a precise diagnosis. Mention yarn/pnpm if you use them — the fix steps differ.

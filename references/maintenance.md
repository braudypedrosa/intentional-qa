# Maintenance workflow

Use this only when changing Intentional QA itself.

## Canonical location

`/Users/braudypedorsa/.codex/skills/intentional-qa` is both the active global Codex skill and the Git working copy. Do not maintain a second source copy.

## Update sequence

1. Inspect the current Git status and preserve unrelated or user-authored changes.
2. Modify the global skill using the skill-creator workflow.
3. Keep the suite self-contained. Internal modules and scripts may be added, but do not introduce dependencies on other Codex skills.
4. Validate `SKILL.md` with the bundled skill validator.
5. Test every changed deterministic script with meaningful behavior, not only syntax.
6. Search for unfinished placeholders, stale module routes, broken relative references, and accidental secrets or generated artifacts.
7. Review the diff, then commit all intentional skill changes with a professional message describing behavior and validation.
8. Push the current branch to the configured GitHub remote and verify the remote commit.

Do not commit audit output, screenshots, credentials, tokens, cookies, browser profiles, `.DS_Store`, `__pycache__`, or temporary fixtures.

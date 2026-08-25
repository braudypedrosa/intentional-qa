# Functional Journey Test

Test whether users can complete important goals, not merely whether individual controls exist.

## Select journeys

Derive journeys from navigation, calls to action, requirements, analytics context supplied by the user, and business risk. Prioritize authentication, lead generation, search, filtering, cart/checkout, booking, downloads, account management, and other revenue or data-integrity paths.

For each journey record the start state, actor/role, preconditions, steps, expected outcome, prohibited side effects, and recovery path.

## Execute

- Follow the visible user path with the built-in browser.
- Check navigation, back/forward behavior, deep links, refresh, state persistence, loading, disabled controls, empty results, validation errors, cancellation, and safe retry behavior.
- Exercise alternate paths and one meaningful negative case when safe.
- Observe URL/history, visible state, console errors, and relevant request failures.
- Verify actual end state, not only a success toast. When downstream state requires unauthorized access, mark it Blocked.
- Test role/permission boundaries only with accounts provided for those roles.
- Capture screenshots at visually meaningful checkpoints and at the final visible outcome. Always capture a focused screenshot of a visible journey failure, incorrect destination, missing state, obstructed control, or misleading success/error message.

## Output

Produce a journey matrix with actor, environment, path, result, evidence, screenshot paths where visual confirmation applies, and gaps. Findings should identify the earliest reliable failure point and downstream user impact rather than listing every later symptom.

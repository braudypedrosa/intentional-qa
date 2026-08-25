# Form Test

Test form discovery, usability, validation, accessibility, resilience, and, only when authorized, delivery and downstream effects.

## Inventory

Record each unique form, its page, purpose, fields, submit action, authentication requirement, third-party provider, and potential side effects. Include search, filters, login, registration, checkout, booking, upload, newsletter, contact, and modal forms when present.

## Safe default pass

- Confirm visible labels, required indicators, correct input types, autocomplete hints, sensible defaults, keyboard order, focus visibility, and submit-button state.
- Test blank required fields and safe malformed values such as invalid email, length boundaries, mismatched confirmation, and unsupported file type.
- Check inline error placement, message clarity, association with the field, error recovery, preservation of entered data, loading state, duplicate-click protection, and responsive behavior.
- Inspect console/network behavior during validation without bypassing client rules.
- Verify that hidden required fields, disabled controls, CAPTCHA, consent, and conditional fields behave coherently.

Do not submit a live lead, email, account, order, payment, booking, deletion, upload, or webhook-triggering action without explicit authorization.

## Authorized end-to-end pass

Before submission, record test data, expected integrations, possible analytics/email/CRM/payment effects, cleanup plan, and authorization. Then verify the visible success state, request result, created record or message, downstream delivery, duplicate prevention, and cleanup. Never use real card or personal data unless the user explicitly supplies and authorizes it.

CAPTCHA, mail delivery, payment, and third-party dashboards are Blocked when the required access or safe environment is absent; they are not Pass.

## Output

Use one row per form and state whether discovery, validation, accessibility, responsive behavior, submission, downstream delivery, and cleanup were Pass, Fail, Blocked, or Not run. Confirmed defects need exact field/state and reproduction steps.

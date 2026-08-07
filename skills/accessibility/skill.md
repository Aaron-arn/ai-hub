# Accessibility

You build products usable by everyone: keyboard-only users, screen reader users, and people with low vision, motor, or cognitive impairments.

## Semantics first

- Use native HTML elements and their built-in behavior before reaching for ARIA.
- Use semantic structure: landmarks, headings, lists, tables with headers, forms with labels.
- Add ARIA only where a native equivalent does not exist; incorrect ARIA is worse than none.
- Use `role` truthfully: never override a button's role, never make a div feel interactive without real semantics.
- One page title and one `h1`; heading levels must not skip.

## Keyboard access

- Everything interactive must be reachable and operable by keyboard alone.
- Never trap focus; dialogs and menus must close with Escape and return focus to the trigger.
- Manage focus for modals, toasts, and route changes; focus is a form of announcing state.
- Provide visible focus indicators in every theme; never remove outlines globally.
- Custom widgets (tabs, accordions, comboboxes) must follow their WAI-ARIA authoring patterns: arrow keys, home/end, roving tabindex.
- Avoid long tab sequences; group related controls in landmarks and skip links.

## Screen readers and live regions

- Provide accessible names for every control: label, aria-label, or title.
- Announce dynamic content with `aria-live="polite"` (status changes) or `role="alert"` (errors).
- Do not announce everything; live regions should fire only on meaningful changes.
- Write `alt` text with intent: what the image communicates, not what it depicts.
- Use `aria-describedby` for help text and `aria-invalid` for validation state.
- Test with a real screen reader (NVDA, VoiceOver, JAWS) on a sample of flows.

## Content and design

- Contrast at least 4.5:1 for normal text, 3:1 for large text and UI components.
- Do not rely on color alone to convey meaning; pair with text, icons, or patterns.
- Do not use motion as the only feedback; respect `prefers-reduced-motion`.
- Keep text resizable to 200% without loss of function; no hard-coded tiny fonts.
- Aim for simple layouts and plain language; avoid flashing content over 3 Hz.
- Provide transcripts or captions for media; descriptive audio for informative video.

## Testing

- Run automated checks (axe, WAVE) in CI and treat violations as failures.
- Cover the full keyboard path through every flow before release.
- Test with zoom (200%), screen readers, and switch/eye-gaze input where available.
- Include users with disabilities in usability testing; automated tools miss half the problems.
- Track accessibility debt in the backlog like any other bug; never ship known blockers.
- Follow WCAG 2.1 AA as the minimum bar, and document deviations with a business owner.

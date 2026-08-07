# Frontend Development

You build frontends that work without JavaScript, then enhance; that render correctly at any width; and that pass basic a11y and performance checks.

## Semantic structure

- Use semantic elements (`header`, `nav`, `main`, `section`, `article`, `footer`) over generic divs.
- One `h1` per page; heading levels descend without skipping.
- Use `button` for actions and `a href` for navigation; never fake buttons with divs.
- Use `label` with `for` on every form control; group with `fieldset`/`legend` where needed.
- Keep interactive content in a logical DOM order matching the visual order.
- Use `picture`/`srcset` for responsive images and `loading="lazy"` below the fold.

## CSS and layout

- Use logical properties and `rem` units for spacing and type; avoid px-typed font sizes.
- Design mobile-first with min-width media queries; test at 320px, 768px, and desktop widths.
- Use flexbox or grid for layout; avoid floats and tables for layout.
- Never use `!important` as a habit; fix specificity at the source.
- Keep layout resilient: `overflow-wrap` on long text, `min-width: 0` on grid children.
- Provide `prefers-reduced-motion` fallbacks for animations; keep motion subtle.
- Scope CSS by component; avoid deep descendant selectors that break encapsulation.

## Forms and interaction

- Validate client-side but always validate on the server; never trust the client.
- Show inline, specific error messages near the field that failed.
- Keep buttons and inputs reachable: minimum touch target of 44x44 px where practical.
- Disable the submit button during submission to prevent double submits; show progress.
- Prefer native controls (`select`, `input type=date`) over custom widgets unless design demands otherwise.
- Support keyboard interaction for every custom control: Enter, Escape, arrow keys, focus visible.

## Accessibility

- Provide `alt` text that conveys meaning; empty alt for decorative images.
- Use `aria-label`/`aria-labelledby` only when the accessible name is not already evident.
- Announce dynamic changes with `role="status"`/`aria-live` instead of silent DOM updates.
- Maintain a visible focus indicator; never `outline: none` without replacement.
- Ensure color contrast of 4.5:1 for normal text and 3:1 for large text.

## Performance and quality

- Load only what the view needs: code-split routes, defer non-critical scripts.
- Keep the initial HTML meaningful (no blank shell waiting on JavaScript).
- Optimize images: correct format, dimensions, and lazy loading; avoid huge hero images by default.
- Run Lighthouse (or equivalent) on key pages: target 90+ in performance, accessibility, best practices.
- Use the platform: native dialog element, CSS `:has()`, view transitions where supported.
- Test in at least Chromium and Firefox; use `prefers-color-scheme` for dark mode rather than duplicating CSS.
- Validate HTML with the W3C validator and audit dependencies regularly.

# Frontend Component Builder

## Description

Generates a single-file, accessible React component with a clean props API, keyboard interaction, and no external dependencies. Use it when you need a small UI widget — dropdown, modal, tooltip, tabs, date picker — and want it done right the first time, with ARIA attributes and focus management handled.

## Prompt

You are a senior frontend engineer. Build a reusable, accessible `Dropdown` component in React 18 (function components + hooks, no TypeScript, no external libraries).

Requirements:
1. Props: `options: {value, label}[]`, `value` (controlled), `onChange(newValue)`, `placeholder`, `disabled`, `label` (accessible name), `id`.
2. Rendering: a visible trigger button showing the selected label or placeholder, and a listbox opened on click; close on outside click, on `Escape`, and on selection.
3. Keyboard: the trigger is focusable via Tab; arrow keys move a highlighted active option; `Enter`/`Space` selects; `Home`/`End` jump to first/last. Wrap around at the edges.
4. Accessibility: use `role="listbox"` / `role="option"`, `aria-expanded`, `aria-activedescendant`, and an `aria-labelledby` pointing at the label; each option gets a unique id.
5. Styling: minimal inline CSS classes with a `className` prop passed to the wrapper; the listbox opens below with `position: absolute` and a small drop shadow. No CSS modules or styled-components.
6. Testing notes: add a `data-testid` on the trigger and each option.
7. Cleanup: no memory leaks — remove the document-level click listener on unmount with `useEffect` cleanup.

Output: the full component in one code block (under 150 lines), followed by a short usage example with three options, and a 5-line checklist proving ARIA and keyboard requirements are met.

## Notes

Change the widget name in the first line to get any other component. For TypeScript projects, ask for `.tsx` with strict types instead.

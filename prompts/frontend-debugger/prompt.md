# Frontend Debugger

## Description

Pastes a buggy frontend snippet (HTML, CSS, JS) and its symptom, and receives a diagnosis, the minimal corrected code, and an explanation of the root cause. Use it when a layout breaks, a click handler does nothing, or an event fires at the wrong time and you want to understand why rather than just patch it.

## Prompt

You are a frontend debugging specialist. Here is a minimal reproduction of my bug:

HTML:
```html
<button id="submit">Submit</button>
<div id="status"></div>
```

CSS:
```css
#status { display: none; color: green; }
#submit { background: #eee; padding: 8px; }
```

JavaScript:
```js
const btn = document.querySelector(".submit");
const status = document.getElementById("status");
btn.addEventListener("click", () => {
  status.textContent = "Saved!";
  status.style.display = "block";
  setTimeout(() => status.style.display = "none", 2000);
});
```

Symptoms observed in the browser:
1. Clicking the button does nothing; the console shows `Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')`.
2. After I fix the selector to `#submit`, clicking works, but the message flashes and disappears immediately.
3. The button keeps a gray hover state in Safari but not Chrome.

Tasks:
1. Identify the root cause of each symptom in one or two sentences.
2. Provide the corrected JavaScript (full block) fixing symptoms 1 and 2 — correct selector or delegated listener, and guard the timer with `clearTimeout` for repeated clicks.
3. Explain the CSS cascade reason for symptom 3 and give the fixed CSS (explicit `:hover` and `transition`), noting any Safari quirk.
4. Add a defensive `if` guard checking `status` exists before using it.
5. List in 3 bullets the DevTools steps (elements panel, console stack trace, network tab) to find these issues without reading the code.

Output: the diagnosis numbered 1-3, the corrected JS block, the corrected CSS block, the bullets.

## Notes

Include your own console error text verbatim for precise diagnoses. Ask for the fix as a diff if you want minimal changes to review.

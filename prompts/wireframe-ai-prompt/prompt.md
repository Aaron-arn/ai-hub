# AI Wireframe

## Description

Generate a text wireframe specification for any screen.

## Prompt

Generate a detailed wireframe specification for a {SCREEN_TYPE} screen in {PRODUCT}.

Use ASCII wireframes with box-drawing characters to show the layout, then annotate each zone:

```
+------------------------------------------+
| Header (logo | nav | search | avatar)    |
+------------------------------------------+
| Sidebar  |  Content area (2/3)           |
| (nav,    |  +----------------------+     |
|  filters)|  | Primary card         |     |
|          |  +----------------------+     |
+------------------------------------------+
| Footer                                  |
+------------------------------------------+
```

Then for each zone specify: purpose, key elements, interaction behavior, default/empty/error states, accessibility notes (focus order, labels). List 3 layout alternatives with pros/cons.

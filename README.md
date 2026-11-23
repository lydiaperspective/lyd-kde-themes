# Lyd KDE Themes

Shared KDE Plasma themes and supporting assets maintained independently from the operating-system images that consume them.

## Mystical

The Mystical theme is located in `themes/mystical/` and includes:

- KDE colour scheme
- Plasma Global Theme and splash screen
- Plasma desktop style
- Wallpaper
- Source SVG icon artwork and icon-theme generator
- Installation notes

Supporting assets:

- `scripts/lyd-mystical-first-login` — applies the bundled wallpaper once for a new user
- `konsole/` — matching Konsole colour scheme and profile

## Consumers

Lyd Atomic images fetch this repository at a pinned commit during image builds. This keeps theme assets versioned independently while ensuring reproducible image builds.

## Repository layout

```
themes/mystical/
  colors/
  icons/
  look-and-feel/
  plasma-style/
  wallpaper/
  build-icon-theme.py
scripts/
konsole/
```

## Updating a theme

Commit changes to the theme assets, then update the pinned commit in each consuming image's theme-install script. Avoid tracking a moving branch in production image recipes so that rebuilds remain reproducible.

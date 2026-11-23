# Mystical Plasma Splash

This is the Plasma 6 Look-and-Feel package for the Mystical splash screen.

## Contents

- `metadata.json`: Plasma Look-and-Feel package metadata.
- `contents/splash/Splash.qml`: animated splash layout.
- `contents/splash/images/crescent-moon.svg`: rounded, softly shaded antique-gold crescent.
- `contents/splash/images/moon-glow.svg`: restrained diffuse glow.
- `contents/splash/images/shooting-star.svg`: rounded shooting star and fading trail.

## Install for the current user

From the repository root:

```sh
mkdir -p ~/.local/share/plasma/look-and-feel
cp -a themes/mystical/look-and-feel/org.lydark.mystical.desktop \
  ~/.local/share/plasma/look-and-feel/
```

Then open System Settings → Appearance → Splash Screen, select **Mystical**, and apply it. The package can also be installed system-wide under `/usr/share/plasma/look-and-feel/`.

## Design constraints

The shooting star travels along one open curved sweep above the crescent. Its motion path is not drawn. There are no orbit rings, decorative loops, stray circles, or lines crossing the moon.

The illustration style is cute, rounded, and softly shaded, with antique gold and subtle lavender accents. The splash stays intentionally simple; richer celestial motifs such as triple-moon symbolism, crystals, and botanical details belong in supporting theme artwork rather than cluttering the startup animation.

The splash uses Breeze-compatible Plasma geometry; it does not change desktop widget spacing or sizing.

## Important distinction

This is the **Plasma startup splash** shown while the desktop session starts. It is not the earlier bootloader / Plymouth screen shown before the login manager. A separate Plymouth theme is required for that earlier boot phase.

## Validation status

The package targets the Plasma 6.8.3 version observed in the Lyd Ark desktop image build logs. It has been added to the repository but still needs runtime validation on an installed Lyd Ark system. Plasma is supplied by Arch rolling packages, so recheck compatibility if the image moves to a newer Plasma major version.

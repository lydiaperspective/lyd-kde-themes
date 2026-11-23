#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${1:-$ROOT/build/mystical-boot}"
command -v rsvg-convert >/dev/null 2>&1 || { echo "rsvg-convert is required (librsvg2-tools)." >&2; exit 1; }
command -v xcursorgen >/dev/null 2>&1 || { echo "xcursorgen is required." >&2; exit 1; }
rm -rf "$OUT"
install -d "$OUT/grub" "$OUT/plymouth" "$OUT/cursors/Mystical/cursors"

rsvg-convert -w 1920 -h 1080 "$ROOT/themes/mystical/grub/background.svg" -o "$OUT/grub/background.png"
cp "$ROOT/themes/mystical/grub/theme.txt" "$OUT/grub/theme.txt"
cp /usr/share/grub/unicode.pf2 "$OUT/grub/unicode.pf2"

rsvg-convert -w 180 -h 180 "$ROOT/themes/mystical/plymouth/logo.svg" -o "$OUT/plymouth/logo.png"
for i in 0 1 2 3 4 5 6 7; do
  case "$i" in
    0) shade_x=50 ;; 1) shade_x=35 ;; 2) shade_x=20 ;; 3) shade_x=5 ;;
    4) shade_x=-28 ;; 5) shade_x=95 ;; 6) shade_x=80 ;; 7) shade_x=65 ;;
  esac
  cat > "$OUT/plymouth/moon-$i.svg" <<SVG
<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100" viewBox="0 0 100 100">
<circle cx="50" cy="50" r="39" fill="#E9E1D5"/>
<circle cx="$shade_x" cy="50" r="39" fill="#30203F"/>
<circle cx="50" cy="50" r="39" fill="none" stroke="#B69A55" stroke-width="2"/>
</svg>
SVG
  rsvg-convert -w 100 -h 100 "$OUT/plymouth/moon-$i.svg" -o "$OUT/plymouth/moon-$i.png"
done
cp "$ROOT/themes/mystical/plymouth/lyd-mystical.plymouth" "$OUT/plymouth/"
cp "$ROOT/themes/mystical/plymouth/lyd-mystical.script" "$OUT/plymouth/"

for kind in arrow hand text wait crosshair move not-allowed; do
  rsvg-convert -w 48 -h 48 "$ROOT/themes/mystical/cursors/$kind.svg" -o "$OUT/cursors/$kind.png"
done
cursor_dir="$OUT/cursors/Mystical/cursors"
for spec in "left_ptr:arrow:4:4" "arrow:arrow:4:4" "default:arrow:4:4" "hand2:hand:15:5" "pointer:hand:15:5" "text:text:23:23" "xterm:text:23:23" "watch:wait:24:24" "wait:wait:24:24" "crosshair:crosshair:24:24" "fleur:move:24:24" "move:move:24:24" "not-allowed:not-allowed:24:24" "forbidden:not-allowed:24:24"; do
  IFS=: read -r name source hx hy <<< "$spec"
  printf '48 %s %s %s.png\n' "$hx" "$hy" "$OUT/cursors/$source" > "$OUT/cursors/$name.conf"
  xcursorgen "$OUT/cursors/$name.conf" "$cursor_dir/$name"
done
cp "$ROOT/themes/mystical/cursors/index.theme" "$OUT/cursors/Mystical/index.theme"

echo "Built Mystical GRUB, Plymouth and Xcursor assets in $OUT"

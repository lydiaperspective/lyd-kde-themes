#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT
DESTDIR="${DESTDIR:-}"
bash "$ROOT/scripts/build-mystical-boot-assets.sh" "$WORK/assets"

install -d "$DESTDIR/usr/share/grub/themes/lyd-mystical"
cp -a "$WORK/assets/grub/." "$DESTDIR/usr/share/grub/themes/lyd-mystical/"
install -d "$DESTDIR/usr/share/plymouth/themes/lyd-mystical"
cp -a "$WORK/assets/plymouth/." "$DESTDIR/usr/share/plymouth/themes/lyd-mystical/"
install -d "$DESTDIR/usr/share/icons/Mystical/cursors"
cp -a "$WORK/assets/cursors/Mystical/cursors/." "$DESTDIR/usr/share/icons/Mystical/cursors/"

install -d "$DESTDIR/etc/plymouth"
cat > "$DESTDIR/etc/plymouth/plymouthd.conf" <<'EOF'
[Daemon]
Theme=lyd-mystical
ShowDelay=0
EOF

install -d "$DESTDIR/etc/xdg"
cat > "$DESTDIR/etc/xdg/kcminputrc" <<'EOF'
[Mouse]
cursorTheme=Mystical
EOF

echo "Installed Mystical GRUB, Plymouth and cursor assets."

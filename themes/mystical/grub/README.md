# Mystical GRUB theme

This theme reuses the Mystical KDE wallpaper artwork and palette: midnight plum,
lavender text, and restrained antique-gold accents. The build helper renders the
SVG wallpaper to PNG and creates GRUB's PFF2 font files at build time.

The installed-system helper copies the generated assets to
`/boot/grub/themes/lyd-mystical`, updates `/etc/default/grub`, and runs
`update-grub`. It keeps a timestamped backup of the previous GRUB defaults.

The desktop live ISO uses the theme in its UEFI GRUB menu. The legacy BIOS boot menu
continues to use the live-build Syslinux/ISOLINUX menu; this is a live-build ISO
boot-path limitation and does not affect GRUB installed on the target system.

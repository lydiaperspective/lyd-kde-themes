# Mystical GRUB theme

The GRUB menu uses the Mystical midnight-plum and lavender palette with a static
1920×1080 lunar-night illustration. The artwork is maintained as SVG and rendered
to PNG during image construction because GRUB does not render SVG backgrounds.

The build helper creates the GRUB background, copies the standard Unicode GRUB
font, renders the Plymouth images, and compiles the cursor artwork. The shared
installer places the GRUB theme under
`/usr/share/grub/themes/lyd-mystical`.

On installed Fedora Atomic systems, the one-shot
`lyd-mystical-boot-setup.service` adds the theme path to
`/etc/default/grub` and regenerates `/boot/grub2/grub.cfg` on first boot.
It also selects the Mystical Plymouth theme and rebuilds the initramfs for
subsequent boots. This runtime step is deliberately deferred until the actual
installed system has its boot filesystems mounted.

The unified installer image also includes the theme assets and sets
`GRUB_THEME` in its image configuration. Actual boot-menu rendering must still
be confirmed by booting the resulting ISO in UEFI and legacy BIOS environments.

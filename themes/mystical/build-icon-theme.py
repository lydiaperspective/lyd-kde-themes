#!/usr/bin/env python3
"""Generate the scalable Mystical KDE icon theme from original SVG artwork."""
from pathlib import Path
import sys

OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("icon-theme")
ICONS = {
"apps/system-file-manager": """<path d="M27 47h29l10 10h35v36H27z" fill="#E7C9A0"/><path d="M27 55h74l-7 39H27z" fill="#D6A96F"/><path d="M47 67c7-9 17-9 24 0-7 9-17 9-24 0Z" fill="#9874C4"/><circle cx="59" cy="67" r="4" fill="#F7EFD9"/>""",
"apps/org.kde.dolphin": """<path d="M30 71c4-23 26-39 50-32 13 4 20 16 18 28-2 17-22 28-42 23-13-3-23-9-26-19Z" fill="#B9DCCB"/><path d="M37 66c11-8 22-10 34-7 8 2 15 7 19 14-12 11-31 13-45 5-5-3-8-7-8-12Z" fill="#78B7A2"/><path d="m73 39 10-15 2 21M41 50 29 39l17 3" fill="#D6A96F"/><circle cx="74" cy="59" r="3.5" fill="#30203F"/><path d="M94 69q8 5 12 1" fill="none" stroke="#583477" stroke-width="4"/>""",
"apps/utilities-terminal": """<rect x="27" y="32" width="74" height="62" rx="10" fill="#30203F"/><path d="M27 43h74" stroke="#9874C4" stroke-width="5"/><path d="m43 57 12 10-12 10M61 78h22" fill="none" stroke="#D7C8E8" stroke-width="5" stroke-linecap="round"/>""",
"apps/org.kde.konsole": """<rect x="27" y="32" width="74" height="62" rx="10" fill="#30203F"/><path d="M27 43h74" stroke="#9874C4" stroke-width="5"/><path d="m42 57 13 10-13 10M63 78h21" fill="none" stroke="#B9DCCB" stroke-width="5" stroke-linecap="round"/>""",
"apps/kate": """<path d="M36 25h43l15 15v62H36z" fill="#E9E1D5"/><path d="M79 25v17h15" fill="#D7C8E8"/><path d="M47 56h34M47 68h34M47 80h23" stroke="#9874C4" stroke-width="5" stroke-linecap="round"/><path d="m71 88 25-25 9 9-25 25-12 3z" fill="#B69A55"/>""",
"apps/org.kde.okular": """<path d="M28 31h30q9 0 9 9v55H38q-10 0-10-10z" fill="#E9E1D5"/><path d="M100 31H70q-9 0-9 9v55h19q10 0 10-10z" fill="#D7C8E8"/><path d="M64 42v53M39 51h17M39 63h17M78 51h13M78 63h13" stroke="#9874C4" stroke-width="4" stroke-linecap="round"/>""",
"apps/org.kde.spectacle": """<path d="M36 44h16l8-10h16l8 10h12q8 0 8 8v32q0 8-8 8H36q-8 0-8-8V52q0-8 8-8Z" fill="#D7C8E8"/><circle cx="64" cy="66" r="17" fill="#9874C4"/><circle cx="64" cy="66" r="8" fill="#E9E1D5"/>""",
"apps/org.kde.discover": """<path d="M64 25 76 50l27 4-20 19 5 27-24-13-24 13 5-27-20-19 27-4z" fill="#B69A55"/><circle cx="64" cy="64" r="17" fill="#9874C4"/><path d="m57 64 5 5 10-12" fill="none" stroke="#FFF7E9" stroke-width="5" stroke-linecap="round"/>""",
"apps/firefox": """<circle cx="65" cy="66" r="34" fill="#583477"/><path d="M89 45C80 30 58 25 42 36l11 4-17 9 10 2-8 14c-3 16 10 32 28 34 21 2 37-16 33-36-2-9-6-14-10-18Z" fill="#D6A96F"/><path d="M85 46c-13-4-23 4-26 14-3 10 5 20 17 20 8 0 14-5 17-12 5 19-10 35-28 32-15-2-24-17-19-31 4-12 16-19 27-23Z" fill="#9874C4"/>""",
"apps/preferences-system": """<circle cx="64" cy="64" r="31" fill="#9874C4"/><circle cx="64" cy="64" r="12" fill="#E9E1D5"/><path d="M64 22v12M64 94v12M22 64h12M94 64h12M34 34l9 9M85 85l9 9M94 34l-9 9M43 85l-9 9" stroke="#B69A55" stroke-width="9" stroke-linecap="round"/>""",
"places/folder": """<path d="M20 43q0-7 8-7h27l10 10h35q8 0 8 8v32q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><path d="M21 57h86l-8 34H29Z" fill="#E9C99D"/><path d="M64 63c-10 9-8 20 0 24 8-4 10-15 0-24Z" fill="#9874C4"/>""",
"places/folder-home": """<path d="M20 47h25l10 10h35q8 0 8 8v25H20Z" fill="#D6A96F"/><path d="m44 69 20-17 20 17v20H44Z" fill="#9874C4"/><path d="M59 89V75h10v14" fill="#E9E1D5"/>""",
"places/folder-documents": """<path d="M20 43h36l10 10h34q8 0 8 8v28q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><path d="M46 58h38v34H46z" fill="#E9E1D5"/><path d="M54 69h22M54 78h22" stroke="#9874C4" stroke-width="4" stroke-linecap="round"/>""",
"places/folder-download": """<path d="M20 43h36l10 10h34q8 0 8 8v28q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><path d="M64 57v27m-12-12 12 12 12-12" fill="none" stroke="#583477" stroke-width="7" stroke-linecap="round"/>""",
"places/folder-pictures": """<path d="M20 43h36l10 10h34q8 0 8 8v28q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><rect x="43" y="59" width="42" height="30" rx="4" fill="#E9E1D5"/><circle cx="73" cy="68" r="5" fill="#B69A55"/><path d="m47 85 12-12 9 8 6-5 8 9Z" fill="#78B7A2"/>""",
"places/folder-music": """<path d="M20 43h36l10 10h34q8 0 8 8v28q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><path d="M70 58v23a8 8 0 1 1-5-7V64l19-5v17a8 8 0 1 1-5-7V56Z" fill="#9874C4"/>""",
"places/folder-videos": """<path d="M20 43h36l10 10h34q8 0 8 8v28q0 8-8 8H28q-8 0-8-8Z" fill="#D6A96F"/><rect x="43" y="60" width="42" height="29" rx="5" fill="#30203F"/><path d="m59 66 15 8-15 9Z" fill="#E9E1D5"/>""",
"devices/drive-harddisk": """<rect x="26" y="38" width="76" height="54" rx="10" fill="#A8A1B7"/><path d="M34 69h60v13H34z" fill="#D7C8E8"/><circle cx="85" cy="78" r="4" fill="#78B7A2"/><path d="M42 50h44" stroke="#F7F0E8" stroke-width="4" stroke-linecap="round"/>""",
"devices/drive-removable-media": """<rect x="35" y="30" width="58" height="68" rx="9" fill="#9874C4"/><path d="M48 42h32v22H48z" fill="#D7C8E8"/><path d="M53 76h22" stroke="#E9E1D5" stroke-width="5" stroke-linecap="round"/><circle cx="64" cy="87" r="3" fill="#B69A55"/>""",
"devices/computer": """<rect x="22" y="31" width="84" height="57" rx="8" fill="#30203F"/><rect x="29" y="38" width="70" height="42" rx="3" fill="#9874C4"/><path d="M64 88v10m-18 0h36" stroke="#B69A55" stroke-width="6" stroke-linecap="round"/><path d="M47 62q17-22 34 0-17 22-34 0Z" fill="#D7C8E8"/>""",
"devices/network-server": """<rect x="28" y="27" width="72" height="27" rx="7" fill="#A8A1B7"/><rect x="28" y="61" width="72" height="27" rx="7" fill="#A8A1B7"/><circle cx="43" cy="40" r="4" fill="#78B7A2"/><circle cx="43" cy="74" r="4" fill="#78B7A2"/><path d="M57 40h29M57 74h29" stroke="#E9E1D5" stroke-width="4" stroke-linecap="round"/>""",
"mimetypes/text-x-generic": """<path d="M35 23h42l17 17v66H35z" fill="#E9E1D5"/><path d="M77 23v20h17" fill="#D7C8E8"/><path d="M47 58h35M47 70h35M47 82h27" stroke="#9874C4" stroke-width="5" stroke-linecap="round"/>""",
"mimetypes/application-pdf": """<path d="M35 23h42l17 17v66H35z" fill="#E9E1D5"/><path d="M77 23v20h17" fill="#D7C8E8"/><path d="M47 76q12-23 20-5 6 13 15-3M47 87h35" fill="none" stroke="#C66B79" stroke-width="5" stroke-linecap="round"/>""",
"mimetypes/image-x-generic": """<rect x="29" y="30" width="70" height="66" rx="8" fill="#E9E1D5"/><circle cx="78" cy="48" r="8" fill="#B69A55"/><path d="m37 86 20-23 13 14 9-9 14 18Z" fill="#78B7A2"/>""",
"mimetypes/audio-x-generic": """<path d="M38 57h15l24-19v52L53 72H38z" fill="#9874C4"/><path d="M87 51q15 13 0 26M94 42q25 22 0 44" fill="none" stroke="#B69A55" stroke-width="5" stroke-linecap="round"/>""",
"mimetypes/video-x-generic": """<rect x="27" y="38" width="74" height="53" rx="8" fill="#30203F"/><path d="m55 49 25 15-25 15Z" fill="#E9E1D5"/><path d="M39 30h50" stroke="#B69A55" stroke-width="5" stroke-linecap="round"/>""",
"mimetypes/package-x-generic": """<path d="m64 25 35 18v42l-35 18-35-18V43z" fill="#D6A96F"/><path d="m29 43 35 19 35-19M64 62v41" fill="none" stroke="#F7E9D2" stroke-width="4"/>""",
"mimetypes/application-x-archive": """<path d="m64 25 35 18v42l-35 18-35-18V43z" fill="#9874C4"/><path d="M57 31h14v12H57zm0 17h14v12H57zm0 17h14v12H57zm0 17h14v12H57z" fill="#E9E1D5"/>""",
"mimetypes/text-x-script": """<path d="M35 23h42l17 17v66H35z" fill="#30203F"/><path d="M77 23v20h17" fill="#583477"/><path d="m49 60 10 8-10 8m17 0h16" fill="none" stroke="#B9DCCB" stroke-width="5" stroke-linecap="round"/>""",
"actions/document-open": """<path d="M22 48h33l10 10h41v31H22z" fill="#D6A96F"/><path d="M64 35v36m-14-14 14 14 14-14" fill="none" stroke="#E9E1D5" stroke-width="7" stroke-linecap="round"/>""",
"actions/document-save": """<path d="M31 25h58l10 10v68H31z" fill="#D7C8E8"/><path d="M43 25v27h34V25M43 103V68h42v35" fill="#9874C4"/><path d="M50 78h28v25H50z" fill="#E9E1D5"/>""",
"actions/edit-copy": """<path d="M47 28h48v62H47z" fill="#B9DCCB"/><path d="M32 42h48v62H32z" fill="#E9E1D5"/><path d="M43 59h26M43 70h26M43 81h18" stroke="#9874C4" stroke-width="4" stroke-linecap="round"/>""",
"actions/edit-paste": """<path d="M44 30h40v12h12v61H32V42h12z" fill="#E9E1D5"/><path d="M49 28h30v18H49z" fill="#9874C4"/><path d="M45 61h38M45 73h38M45 85h26" stroke="#B69A55" stroke-width="4" stroke-linecap="round"/>""",
"actions/edit-delete": """<path d="M33 42h62l-5 60H38z" fill="#D7C8E8"/><path d="M27 34h74M49 34v-9h30v9M52 55v33M76 55v33" fill="none" stroke="#583477" stroke-width="5" stroke-linecap="round"/>""",
"actions/go-home": """<path d="m23 62 41-34 41 34" fill="none" stroke="#583477" stroke-width="9" stroke-linecap="round"/><path d="M35 58v43h58V58L64 35z" fill="#D6A96F"/><path d="M55 101V75h18v26" fill="#9874C4"/>""",
"actions/view-refresh": """<path d="M93 54a31 31 0 0 0-55-11l-8 10m0-18v18h18M35 75a31 31 0 0 0 55 11l8-10m0 18V76H80" fill="none" stroke="#9874C4" stroke-width="7" stroke-linecap="round"/><path d="M64 46v36m-13-13 13 13 13-13" fill="none" stroke="#B69A55" stroke-width="5" stroke-linecap="round"/>""",
"actions/system-shutdown": """<path d="M64 25v39" stroke="#B69A55" stroke-width="9" stroke-linecap="round"/><path d="M45 38a34 34 0 1 0 38 0" fill="none" stroke="#9874C4" stroke-width="9" stroke-linecap="round"/>""",
"status/network-wireless": """<path d="M25 51q39-34 78 0M37 65q27-24 54 0M49 79q15-13 30 0" fill="none" stroke="#9874C4" stroke-width="7" stroke-linecap="round"/><circle cx="64" cy="94" r="7" fill="#B69A55"/>""",
"status/audio-volume-high": """<path d="M25 53h17l26-21v64L42 75H25z" fill="#9874C4"/><path d="M82 49q19 15 0 30m8-42q30 27 0 54" fill="none" stroke="#B69A55" stroke-width="6" stroke-linecap="round"/>""",
"status/battery-full": """<rect x="30" y="40" width="64" height="48" rx="8" fill="#E9E1D5"/><path d="M94 54h8v20h-8" fill="#B69A55"/><rect x="38" y="48" width="48" height="32" rx="4" fill="#78B7A2"/>""",
"status/dialog-warning": """<path d="m64 25 43 76H21z" fill="#E8C77F"/><path d="M64 51v25" stroke="#583477" stroke-width="7" stroke-linecap="round"/><circle cx="64" cy="88" r="4" fill="#583477"/>""",
"categories/utilities": """<path d="M64 25c-20 0-35 16-35 35 0 23 22 43 35 43s35-20 35-43c0-19-15-35-35-35Z" fill="#9874C4"/><path d="M48 62c0-12 8-20 16-20s16 8 16 20-8 21-16 21-16-9-16-21Z" fill="#E9E1D5"/><path d="m57 64 7-10 7 10-7 10z" fill="#B69A55"/>""",
"categories/settings": """<circle cx="64" cy="64" r="30" fill="#9874C4"/><circle cx="64" cy="64" r="10" fill="#E9E1D5"/><path d="M64 22v12m0 60v12M22 64h12m60 0h12M34 34l9 9m42 42 9 9m0-60-9 9M43 85l-9 9" stroke="#B69A55" stroke-width="8" stroke-linecap="round"/>""",
"categories/graphics": """<rect x="27" y="31" width="74" height="65" rx="10" fill="#E9E1D5"/><path d="m35 85 20-24 15 16 12-12 12 20" fill="#78B7A2"/><circle cx="78" cy="48" r="8" fill="#B69A55"/>""",
"categories/multimedia": """<path d="M31 42q0-9 9-9h48q9 0 9 9v44q0 9-9 9H40q-9 0-9-9z" fill="#30203F"/><path d="m53 49 27 15-27 15z" fill="#E9E1D5"/><path d="M40 27h48" stroke="#B69A55" stroke-width="5" stroke-linecap="round"/>""",
"categories/development": """<path d="m47 43-22 21 22 21m34-42 22 21-22 21M72 34 56 94" fill="none" stroke="#9874C4" stroke-width="8" stroke-linecap="round"/><circle cx="64" cy="64" r="47" fill="none" stroke="#B69A55" stroke-width="3" stroke-dasharray="4 8"/>""",
}

def render(name, glyph):
    group, key = name.split("/", 1)
    label = key.replace("-", " ").replace(".", " ").title()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-labelledby="title desc">
<title id="title">Mystical {label}</title>
<desc id="desc">Original pastel cartoon {label.lower()} icon for the Mystical KDE icon theme.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#49305F"/><stop offset="1" stop-color="#21152E"/></linearGradient><linearGradient id="shine" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#FFF8EA" stop-opacity=".38"/><stop offset="1" stop-color="#FFF8EA" stop-opacity="0"/></linearGradient></defs>
<rect x="12" y="12" width="104" height="104" rx="27" fill="url(#bg)"/>
<path d="M31 22q30-17 63 1" fill="none" stroke="url(#shine)" stroke-width="5" stroke-linecap="round"/>
<g stroke="#583477" stroke-width="3.8" stroke-linecap="round" stroke-linejoin="round">{glyph}</g>
<path d="m96 25 3 7 7 3-7 3-3 7-3-7-7-3 7-3z" fill="#B69A55"/>
</svg>
'''

for name, glyph in ICONS.items():
    target = OUT / "scalable" / (name + ".svg")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(render(name, glyph), encoding="utf-8")

# Desktop files and toolkits use several equivalent icon names. Provide
# explicit aliases so the Mystical artwork is selected consistently.
ALIASES = {
    "apps/dolphin": "apps/org.kde.dolphin",
    "apps/konsole": "apps/org.kde.konsole",
    "apps/org.kde.kate": "apps/kate",
    "apps/okular": "apps/org.kde.okular",
    "apps/spectacle": "apps/org.kde.spectacle",
    "apps/discover": "apps/org.kde.discover",
    "apps/systemsettings": "apps/preferences-system",
    "apps/org.kde.systemsettings": "apps/preferences-system",
    "places/user-home": "places/folder-home",
    "places/folder-downloads": "places/folder-download",
    "actions/edit-delete-shred": "actions/edit-delete",
    "mimetypes/application-x-pdf": "mimetypes/application-pdf",
    "mimetypes/application-x-shellscript": "mimetypes/text-x-script",
    "devices/drive-removable-media-usb": "devices/drive-removable-media",
}
for alias, original in ALIASES.items():
    source = OUT / "scalable" / (original + ".svg")
    target = OUT / "scalable" / (alias + ".svg")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())

contexts = {"apps":"Applications","places":"Places","devices":"Devices","mimetypes":"MimeTypes","actions":"Actions","status":"Status","categories":"Categories"}
directories = [f"scalable/{folder}" for folder in contexts]
index = ["[Icon Theme]", "Name=Mystical", "Comment=Cozy lunar and botanical icon theme for KDE Plasma", "Inherits=Breeze,hicolor", "Directories=" + ",".join(directories), "Example=system-file-manager", "DesktopDefault=48", "ToolbarDefault=22", "MainToolbarDefault=22", "SmallDefault=16", "PanelDefault=22", "DialogDefault=32", ""]
for folder, context in contexts.items():
    index += [f"[scalable/{folder}]", "Size=128", "Type=Scalable", "MinSize=16", "MaxSize=512", f"Context={context}", ""]
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "index.theme").write_text("\n".join(index), encoding="utf-8")
print(f"Generated {len(ICONS)} Mystical scalable icons in {OUT}")

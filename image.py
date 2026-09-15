# swap_photo.py
import base64, re, pathlib

img = pathlib.Path("dp.PNG").read_bytes()
b64 = base64.b64encode(img).decode()
new_href = f'href="data:image/png;base64,{b64}"'

for name in ("dark.svg", "light.svg"):
    p = pathlib.Path(name)
    svg = p.read_text(encoding="utf-8")
    svg, n = re.subn(r'href="data:image/[^"]+"', new_href, svg, count=1)
    if n == 0:
        print(f"!! no embedded image found in {name}")
    else:
        p.write_text(svg, encoding="utf-8")
        print(f"updated {name}")
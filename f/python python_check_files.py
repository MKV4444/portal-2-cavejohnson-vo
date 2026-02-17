from pathlib import Path
import re

BASE_DIR = Path(__file__).parent   # = f/
TARGET_DIR = BASE_DIR              # ไม่ต้อง / "f"
README = TARGET_DIR / "README.md"

files = {p.stem for p in TARGET_DIR.glob("*.wav")}

lines = README.read_text(encoding="utf-8").splitlines()
out = []

pattern = re.compile(r"- \[( |x)\] (.+)")

for line in lines:
    m = pattern.match(line)
    if m:
        name = m.group(2).strip()
        if name in files:
            out.append(f"- [x] {name}")
        else:
            out.append(f"- [ ] {name}")
    else:
        out.append(line)

README.write_text("\n".join(out), encoding="utf-8")
print("✔ updated f/README.md")

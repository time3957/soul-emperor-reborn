#!/usr/bin/env python3
"""รวมเล่มนิยายจากไฟล์รายบท (novel/ คือแหล่งข้อมูลหลัก)."""

from pathlib import Path

# ลำดับอ่าน: บทแทรกอยู่ระหว่างบท 8 กับบท 9
ORDER = [
    "00-prologue.md",
    "01-awakening-year-18.md",
    "02-lucky-survivor.md",
    "03-unreported.md",
    "04-return-to-campus.md",
    "05-the-old-textbook.md",
    "06-unexpected-progress.md",
    "07-lose-but-unbroken.md",
    "08-perfect-control.md",
    "08a-interlude-three-worlds.md",
    "09-zone17-field-mission.md",
    "10-wsc-offer.md",
]


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    chapter_dir = root / "novel"
    output = root / "dist" / "BOOK.md"

    # ไม่สร้างบทปลอม หรือข้ามไฟล์หายไปเงียบ ๆ
    missing = [name for name in ORDER if not (chapter_dir / name).is_file()]
    if missing:
        raise FileNotFoundError("Missing chapters: " + ", ".join(missing))

    contents = [
        "# ฟงชาง — จักรพรรดิวิญญาณคืนสู่โลก\n\n"
        "> ไฟล์รวมเล่มสร้างอัตโนมัติจาก novel/ — ห้ามแก้ไขโดยตรง\n\n---"
    ]
    for chapter in ORDER:
        text = (chapter_dir / chapter).read_text(encoding="utf-8").strip()
        contents.append(text)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n\n---\n\n".join(contents) + "\n", encoding="utf-8")
    print(f"Built {output} ({len(ORDER)} sections)")


if __name__ == "__main__":
    main()

import os
import shutil
from pathlib import Path

# ============================
# FILE DAN FOLDER YANG DI-EXCLUDE
# ============================
EXCLUDE_FILES = ["main.py", "tools.py"]
EXCLUDE_FOLDERS = [
    "__pycache__", 
    ".git", 
    "Organized",
    "Music", "Videos", "Images", 
    "Documents", "Archives", "Others"
]


# ============================
# KATEGORI FILE
# ============================
FILE_TYPES = {
    "Music": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt"],
    "Archives": [".zip", ".rar", ".7z"],
}


def detect_category(ext):
    ext = ext.lower()
    for category, exts in FILE_TYPES.items():
        if ext in exts:
            return category
    return "Others"


# ============================
# SMART ORGANIZER (PDF, DLL)
# ============================
def smart_file_organizer(path, extension):
    p = Path(path)

    if not p.exists() or not p.is_dir():
        print("[ERROR] Path tidak ditemukan:", path)
        return []

    organized_dir = p / "Organized"
    organized_dir.mkdir(exist_ok=True)

    moved = []
    ext = extension.lower().lstrip(".")

    for f in p.iterdir():
        if f.is_file() and f.suffix.lower().lstrip(".") == ext:

            # Skip file program
            if f.name in EXCLUDE_FILES:
                continue

            target = organized_dir / f.name

            if target.exists():
                base = target.stem
                i = 1
                while True:
                    candidate = organized_dir / f"{base}_{i}{f.suffix}"
                    if not candidate.exists():
                        target = candidate
                        break
                    i += 1

            shutil.move(str(f), str(target))
            moved.append(str(target))

    return moved


# ============================
# AUTO SORT + AUTO RENAME
# ============================
def auto_sort_and_rename(path="."):
    p = Path(path)

    if not p.exists() or not p.is_dir():
        print("[ERROR] Path tidak ditemukan:", path)
        return []

    moved_files = []

    for f in p.iterdir():

        # Abaikan folder exclude
        if f.is_dir() and f.name in EXCLUDE_FOLDERS:
            continue

        if f.is_file():

            # Abaikan file program
            if f.name in EXCLUDE_FILES:
                continue

            ext = f.suffix.lower()
            category = detect_category(ext)
            target_folder = p / category
            target_folder.mkdir(exist_ok=True)

            # Hitung jumlah file di folder kategori
            count = len([x for x in target_folder.iterdir() if x.is_file()]) + 1

            # Generate format rename
            new_name = f"{category}_{count:04d}{ext}"
            target_path = target_folder / new_name

            shutil.move(str(f), str(target_path))
            moved_files.append(str(target_path))

    return moved_files
# ============================
# LIST FILES DI PATH
# ============================
def list_files(path="."):
    p = Path(path)
    if not p.exists():
        return []
    return [str(x.name) for x in p.iterdir() if x.is_file()]
# ============================
# LIST FOLDERS DI PATH
# ============================
def list_folders(path="."):
    p = Path(path)
    if not p.exists():
        return []
    return [str(x.name) for x in p.iterdir() if x.is_dir()]



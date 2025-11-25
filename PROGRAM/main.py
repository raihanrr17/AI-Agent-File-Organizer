import os
from tools import (
    auto_sort_and_rename,
    smart_file_organizer,
    list_files,
    list_folders,
)

# ============================
# WARNA TERMINAL
# ============================
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


# ============================
# AI PARSER & EXECUTOR
# ============================
def ai_parse_and_execute(user_input: str):
    ui = user_input.lower().strip()

    print(f"{YELLOW}[AI Thinking...] {RESET}")

    # ================
    # EXIT COMMANDS
    # ================
    if ui in ["exit", "quit", "keluar", "stop"]:
        print(f"{CYAN}AI: Program dihentikan.{RESET}")
        exit()

    # ================
    # AUTO SORT KOMPLIT
    # ================
    if "auto" in ui and ("sort" in ui or "deteksi" in ui or "detect" in ui):
        moved = auto_sort_and_rename(".")
        print(f"{CYAN}AI: Auto-sort selesai. {len(moved)} file dipindahkan.{RESET}")
        return

    # ================
    # RAPIKAN PDF
    # ================
    if "rapikan" in ui and "pdf" in ui:
        moved = smart_file_organizer(".", "pdf")
        print(f"{CYAN}AI: Berhasil merapikan {len(moved)} file PDF.{RESET}")
        return

    if "pdf" in ui and "folder" in ui:
        moved = smart_file_organizer(".", "pdf")
        print(f"{CYAN}AI: Semua file PDF dipindahkan: {len(moved)} file.{RESET}")
        return

    # ================
    # CEK FILE
    # ================
    if ("cek" in ui or "lihat") and "file" in ui:
        files = list_files(".")
        print(f"{CYAN}AI: Ditemukan {len(files)} file:{RESET}")
        for f in files[:20]:
            print(f"  - {f}")
        return
    # ================
    # CEK FOLDER
    # ================
    if ("cek" in ui or "lihat") and ("folder" in ui or "foldernya" in ui):
        folders = list_folders(".")
        print(f"{CYAN}AI: Ditemukan {len(folders)} folder:{RESET}")
        for d in folders:
            print(f"  - {d}")
    return

    # ================
    # DEFAULT
    # ================
    print(f"{CYAN}AI: Maaf, perintah tidak dikenali. Coba: 'auto sort', 'rapikan pdf', 'cek file'.{RESET}")


# ============================
# REPL (Chat Mode)
# ============================
def repl():
    print(f"{CYAN}=== Terminal AI Agent (File Organizer) ==={RESET}")
    print("Ketik perintah, misalnya:")
    print(" - auto sort semua file")
    print(" - rapikan file PDF")
    print(" - cek file di folder ini")
    print(" - cek folder di path ini")
    print(" - exit")
    print()

    while True:
        try:
            user = input(f"{GREEN}You> {RESET}")
            ai_parse_and_execute(user)
        except KeyboardInterrupt:
            print(f"\n{CYAN}AI: Program dihentikan.{RESET}")
            break


# ============================
# MAIN
# ============================
if __name__ == "__main__":
    repl()

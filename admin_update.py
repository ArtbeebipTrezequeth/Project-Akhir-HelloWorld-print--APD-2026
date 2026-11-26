import os
from data_awal import katalog_permen

def update_admin():
    os.system("cls")
    print("=== ADMIN - KELOLA STOK ===")
    if not katalog_permen:
        print("Belum ada menu untuk diupdate.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, item in enumerate(katalog_permen, start=1):
        status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
        print(f"{i}. {item['nama']} | Stok: {item['stok']} pcs | Status: {status}")
    print("0. Keluar / Batal")

    while True:
        raw_idx = input("Pilih nomor menu yang ingin diupdate stoknya: ").strip()
        if not raw_idx:
            print("Input tidak boleh kosong.")
            continue
        try:
            no_menu = int(raw_idx)
            if no_menu == 0:
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if 1 <= no_menu <= len(katalog_permen):
                idx = no_menu - 1
                break
            print("Nomor menu tidak ditemukan.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    while True:
        raw_stok = input("Masukkan jumlah stok baru (-1 untuk batal): ").strip()
        if not raw_stok:
            print("Input tidak boleh kosong.")
            continue
        try:
            stok_baru = int(raw_stok)
            if stok_baru == -1:
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if stok_baru >= 0:
                break
            print("Stok tidak boleh negatif.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    katalog_permen[idx]["stok"] = stok_baru
    print("Stok berhasil diupdate.")
    input("\nTekan Enter untuk lanjut...")
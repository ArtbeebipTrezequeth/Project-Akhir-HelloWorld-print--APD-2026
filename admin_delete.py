import os
from data_awal import jenis_permen, katalog_permen

def delete_admin():
    os.system("cls")
    print("=== ADMIN - HAPUS MENU ===")
    print("1. Hapus Salah Satu Menu")
    print("2. Hapus Salah Satu Variasi Rasa")
    print("3. Hapus Semua Menu")
    print("0. Keluar / Batal")

    while True:
        raw_pilih = input("Pilih (1/2/3/0): ").strip()
        if not raw_pilih:
            print("Input tidak boleh kosong.")
            continue
        try:
            pilih = int(raw_pilih)
            if pilih in (1, 2, 3, 0):
                break
            print("Pilihan harus 1, 2, 3, atau 0.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    if pilih == 0:
        print("Tindakan dibatalkan.")
        input("\nTekan Enter untuk lanjut...")
        return

    if pilih == 1:
        if not katalog_permen:
            print("Katalog menu sudah kosong.")
            input("\nTekan Enter untuk lanjut...")
            return
        for i, item in enumerate(katalog_permen, start=1):
            print(f"{i}. {item['nama']} ({item['varian']})")
        print("0. Batal")

        while True:
            raw_no = input("Pilih nomor menu yang dihapus: ").strip()
            if not raw_no:
                print("Input tidak boleh kosong.")
                continue
            try:
                no_menu = int(raw_no)
                if no_menu == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= no_menu <= len(katalog_permen):
                    katalog_permen.pop(no_menu - 1)
                    print("Menu berhasil dihapus.")
                    break
                print("Nomor menu tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    elif pilih == 2:
        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j}: {', '.join(jenis_permen[j])}")
        print("0. Batal")

        while True:
            raw_j = input("Pilih nomor jenis permen: ").strip()
            if not raw_j:
                print("Input tidak boleh kosong.")
                continue
            try:
                no_j = int(raw_j)
                if no_j == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= no_j <= len(daftar_jenis):
                    jenis_dipilih = daftar_jenis[no_j - 1]
                    break
                print("Nomor jenis tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

        varians = jenis_permen[jenis_dipilih]
        if not varians:
            print("Tidak ada varian pada jenis ini.")
            input("\nTekan Enter untuk lanjut...")
            return

        for i, v in enumerate(varians, start=1):
            print(f"{i}. {v}")
        print("0. Batal")

        while True:
            raw_v = input("Pilih nomor varian yang dihapus: ").strip()
            if not raw_v:
                print("Input tidak boleh kosong.")
                continue
            try:
                no_v = int(raw_v)
                if no_v == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= no_v <= len(varians):
                    varians.pop(no_v - 1)
                    print("Variasi rasa berhasil dihapus.")
                    break
                print("Nomor varian tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    elif pilih == 3:
        while True:
            raw_konf = input("Ketik 1 untuk konfirmasi hapus SEMUA menu atau 0 untuk batal: ").strip()
            if not raw_konf:
                print("Input tidak boleh kosong.")
                continue
            try:
                konf = int(raw_konf)
                if konf == 0:
                    print("Penghapusan semua menu dibatalkan.")
                    break
                if konf == 1:
                    katalog_permen.clear()
                    print("Semua menu berhasil dihapus.")
                    break
                print("Masukkan 1 atau 0.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    input("\nTekan Enter untuk lanjut...")
import os
from data_awal import katalog_permen, shopping_list

def delete_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - DELETE SHOPPING LIST ===")
    if not shopping_list:
        print("Shopping list kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    print("1. Hapus Salah Satu Kategori Pilihan Menu Tertentu")
    print("2. Hapus Semua Belanjaan")
    print("0. Keluar / Batal")

    while True:
        raw_pilih = input("Pilih (1/2/0): ").strip()
        if not raw_pilih:
            print("Input tidak boleh kosong.")
            continue
        try:
            pilih = int(raw_pilih)
            if pilih in (1, 2, 0):
                break
            print("Pilihan harus 1, 2, atau 0.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    if pilih == 0:
        print("Tindakan dibatalkan.")
        input("\nTekan Enter untuk lanjut...")
        return

    if pilih == 1:
        daftar_kategori = []
        for entry in shopping_list:
            kat = katalog_permen[entry["menu_index"]]["jenis"]
            if kat not in daftar_kategori:
                daftar_kategori.append(kat)

        for i, kat in enumerate(daftar_kategori, start=1):
            print(f"{i}. {kat}")
        print("0. Batal")

        while True:
            raw_kat = input("Pilih nomor kategori menu yang ingin dihapus: ").strip()
            if not raw_kat:
                print("Input tidak boleh kosong.")
                continue
            try:
                no_kat = int(raw_kat)
                if no_kat == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= no_kat <= len(daftar_kategori):
                    kategori = daftar_kategori[no_kat - 1].lower()
                    sisa = [
                        entry for entry in shopping_list
                        if katalog_permen[entry["menu_index"]]["jenis"].lower() != kategori
                    ]
                    shopping_list.clear()
                    shopping_list.extend(sisa)
                    print("Item sesuai kategori berhasil dihapus dari shopping list.")
                    break
                print("Nomor kategori tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    elif pilih == 2:
        while True:
            raw_konf = input("Ketik 1 untuk konfirmasi hapus SEMUA belanjaan atau 0 untuk batal: ").strip()
            if not raw_konf:
                print("Input tidak boleh kosong.")
                continue
            try:
                konf = int(raw_konf)
                if konf == 0:
                    print("Penghapusan semua belanjaan dibatalkan.")
                    break
                if konf == 1:
                    shopping_list.clear()
                    print("Semua belanjaan berhasil dihapus.")
                    break
                print("Masukkan 1 atau 0.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    input("\nTekan Enter untuk lanjut...")
import os
from data_awal import jenis_permen, katalog_permen, shopping_list

def update_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - KELOLA BELANJAAN ===")
    if not shopping_list:
        print("Belanjaan kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, entry in enumerate(shopping_list, start=1):
        item = katalog_permen[entry["menu_index"]]
        print(f"{i}. {item['nama']} | Varian: {entry['varian']} | Qty: {entry['qty']}")
    print("0. Keluar / Batal")

    while True:
        raw_idx = input("Pilih nomor item belanjaan: ").strip()
        if not raw_idx:
            print("Input tidak boleh kosong.")
            continue
        try:
            no_item = int(raw_idx)
            if no_item == 0:
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if 1 <= no_item <= len(shopping_list):
                idx = no_item - 1
                break
            print("Nomor item tidak valid.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    entry = shopping_list[idx]
    item = katalog_permen[entry["menu_index"]]

    print("1. Atur Kuantitas")
    print("2. Ubah Varian Rasa")
    print("0. Batal")

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
        while True:
            raw_qty = input(f"Masukkan kuantitas baru (maks {item['stok']}, 0 untuk batal): ").strip()
            if not raw_qty:
                print("Input tidak boleh kosong.")
                continue
            try:
                qty_baru = int(raw_qty)
                if qty_baru == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= qty_baru <= item["stok"]:
                    entry["qty"] = qty_baru
                    print("Kuantitas berhasil diubah.")
                    break
                print(f"Kuantitas harus antara 1 sampai {item['stok']}.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    elif pilih == 2:
        varians = jenis_permen.get(item["jenis"], [item["varian"]])
        for i, v in enumerate(varians, start=1):
            print(f"{i}. {v}")
        print("0. Batal")

        while True:
            raw_v = input("Pilih nomor varian baru: ").strip()
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
                    entry["varian"] = varians[no_v - 1]
                    print("Varian rasa berhasil diubah.")
                    break
                print("Nomor varian tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

    input("\nTekan Enter untuk lanjut...")
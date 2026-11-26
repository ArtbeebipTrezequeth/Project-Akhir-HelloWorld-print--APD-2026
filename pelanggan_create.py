import os
from data_awal import jenis_permen, katalog_permen, shopping_list

def create_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - TAMBAH BELANJAAN ===")
    if not katalog_permen:
        print("Menu toko kosong.")
        input("\nTekan Enter untuk lanjut...")
        return

    for i, item in enumerate(katalog_permen, start=1):
        status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
        print(f"{i}. {item['nama']} | Rp{item['harga']:,}".replace(",", ".") + f"/pcs | Stok: {item['stok']} | {status}")
    print("0. Keluar / Batal")

    while True:
        raw_idx = input("Pilih nomor menu: ").strip()
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
            print("Nomor menu tidak valid.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    item = katalog_permen[idx]
    if item["stok"] <= 0:
        print("Stok menu sedang habis.")
        input("\nTekan Enter untuk lanjut...")
        return

    varians = jenis_permen.get(item["jenis"], [item["varian"]])
    for i, v in enumerate(varians, start=1):
        print(f"{i}. {v}")
    print("0. Batal")

    while True:
        raw_v = input("Pilih nomor varian rasa: ").strip()
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
                varian_dipilih = varians[no_v - 1]
                break
            print("Nomor varian tidak valid.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    while True:
        raw_qty = input(f"Masukkan jumlah beli (maks {item['stok']}, 0 untuk batal): ").strip()
        if not raw_qty:
            print("Input tidak boleh kosong.")
            continue
        try:
            qty = int(raw_qty)
            if qty == 0:
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if 1 <= qty <= item["stok"]:
                break
            print(f"Jumlah beli harus antara 1 sampai {item['stok']}.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    shopping_list.append({
        "menu_index": idx,
        "varian": varian_dipilih,
        "qty": qty,
    })
    print("Berhasil ditambahkan ke shopping list.")
    input("\nTekan Enter untuk lanjut...")
# Data Awal
Nama_admin = ["Bip", "Hanif", "Cinta", "Mulan"]
Pw_admin = "Tokopermen123"

Stok_permen_coklat = 10
Stok_permen_vanila = 10
Stok_permen_stroberi = 10
Stok_permen_mint = 10
Stok_permen_kopi = 10
Stok_permen_lemon_tea = 10

harga_permen_coklat = 3000
harga_permen_vanila = 2000
harga_permen_stroberi = 2000
harga_permen_mint = 2000
harga_permen_kopi = 2000
harga_permen_lemon_tea = 3000

jenis_permen = {
    "Lunak": ["Coklat", "Vanila", "Stroberi"],
    "Keras": ["Mint", "Kopi", "Lemon Tea"],
}

katalog_permen = [
    {
        "nama": "Permen Coklat",
        "harga": harga_permen_coklat,
        "stok": Stok_permen_coklat,
        "jenis": "Lunak",
        "varian": "Coklat",
    },
    {
        "nama": "Permen Vanila",
        "harga": harga_permen_vanila,
        "stok": Stok_permen_vanila,
        "jenis": "Lunak",
        "varian": "Vanila",
    },
    {
        "nama": "Permen Stroberi",
        "harga": harga_permen_stroberi,
        "stok": Stok_permen_stroberi,
        "jenis": "Lunak",
        "varian": "Stroberi",
    },
    {
        "nama": "Permen Mint",
        "harga": harga_permen_mint,
        "stok": Stok_permen_mint,
        "jenis": "Keras",
        "varian": "Mint",
    },
    {
        "nama": "Permen Kopi",
        "harga": harga_permen_kopi,
        "stok": Stok_permen_kopi,
        "jenis": "Keras",
        "varian": "Kopi",
    },
    {
        "nama": "Permen Lemon Tea",
        "harga": harga_permen_lemon_tea,
        "stok": Stok_permen_lemon_tea,
        "jenis": "Keras",
        "varian": "Lemon Tea",
    },
]

shopping_list = []



# Menu Login
from login import admin, pengguna
import os
import inquirer

def MenuUtama():
    os.system("cls")
    print("============ Selamat datang di toko permen =============")
    pilihan = [
        inquirer.List(
            "login",
            message="Login Sebagai",
            choices=["admin", "pelanggan"],
        ),
    ]
    logins = inquirer.prompt(pilihan)

    if (logins["login"]) == "admin":
        logmin()
        os.system("cls")
    elif (logins["login"]) == "pelanggan":
        pengguna()
        os.system("cls")

def logmin():
    os.system("cls")
    try:
        print("=========================")
        user = input("Masukkan Username: ").strip()
        password = input("Masukkan Password: ")
        print("=========================")
        if not ((user in Nama_admin and password == Pw_admin)):
            raise ValueError
    except ValueError:
        os.system("cls")
        logcoba()

    else:
        os.system("cls")
        if (user in Nama_admin and password == Pw_admin):
            admin()

def logcoba():
    pilihan = [
        inquirer.List(
            "pilih",
            message="Login Gagal",
            choices=["coba lagi", "kembali ke menu awal"],
        ),
    ]
    step = inquirer.prompt(pilihan)
    os.system("cls")
    if (step["pilih"]) == "coba lagi":
        logmin()
    elif (step["pilih"]) == "kembali ke menu awal":
        MenuUtama()

if __name__ == "__main__":
    MenuUtama()



# Login
import os
import inquirer

def admin():
    jalan = True
    while jalan:
        os.system("cls")
        menu = [
            inquirer.List(
                "aksi",
                message="Menu Admin",
                choices=[
                    "Tambah Menu",
                    "Lihat Data Menu",
                    "Kelola Stok",
                    "Hapus Menu",
                    "keluar",
                ],
            )
        ]
        pilih = inquirer.prompt(menu)
        if pilih["aksi"] == "Tambah Menu":
            create_admin()
        elif pilih["aksi"] == "Lihat Data Menu":
            read_admin()
        elif pilih["aksi"] == "Kelola Stok":
            update_admin()
        elif pilih["aksi"] == "Hapus Menu":
            delete_admin()
        elif pilih["aksi"] == "keluar":
            jalan = keluar_admin()

def pengguna():
    jalan = True
    while jalan:
        os.system("cls")
        menu = [
            inquirer.List(
                "aksi",
                message="Menu Pelanggan",
                choices=[
                    "Tambah Belanjaan",
                    "Lihat Belanjaan",
                    "Kelola Belanjaan",
                    "Hapus Belanjaan",
                    "Bayar",
                    "keluar",
                ],
            )
        ]
        pilih = inquirer.prompt(menu)
        if pilih["aksi"] == "Tambah Belanjaan":
            create_pelanggan()
        elif pilih["aksi"] == "Lihat Belanjaan":
            read_pelanggan()
        elif pilih["aksi"] == "Kelola Belanjaan":
            update_pelanggan()
        elif pilih["aksi"] == "Hapus Belanjaan":
            delete_pelanggan()
        elif pilih["aksi"] == "Bayar":
            bayar_pelanggan()
        elif pilih["aksi"] == "keluar":
            jalan = keluar_pelanggan()


# Admin Tambah
import os

def create_admin():
    os.system("cls")
    print("=== ADMIN - TAMBAH ===")
    print("1. Tambah Menu Pilihan Baru")
    print("2. Tambah Jenis Variasi Rasa")
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
        while True:
            nama = input("Nama Permen (atau ketik 0 untuk batal): ").strip()
            if nama == "0":
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if nama:
                break
            print("Nama permen tidak boleh kosong.")

        while True:
            raw_harga = input("Harga Permen (angka, 0 untuk batal): ").strip()
            if not raw_harga:
                print("Harga tidak boleh kosong.")
                continue
            try:
                harga = int(raw_harga)
                if harga == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if harga > 0:
                    break
                print("Harga harus lebih dari 0.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

        while True:
            raw_stok = input("Jumlah Stok (angka, -1 untuk batal): ").strip()
            if not raw_stok:
                print("Stok tidak boleh kosong.")
                continue
            try:
                stok = int(raw_stok)
                if stok == -1:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if stok >= 0:
                    break
                print("Stok tidak boleh negatif.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j}")
        print("0. Batal")

        while True:
            raw_j = input("Pilih nomor jenis permen: ").strip()
            if not raw_j:
                print("Pilihan tidak boleh kosong.")
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

        daftar_varian = jenis_permen[jenis_dipilih]
        for i, v in enumerate(daftar_varian, start=1):
            print(f"{i}. {v}")
        print("0. Batal")

        while True:
            raw_v = input("Pilih nomor varian rasa: ").strip()
            if not raw_v:
                print("Pilihan tidak boleh kosong.")
                continue
            try:
                no_v = int(raw_v)
                if no_v == 0:
                    print("Tindakan dibatalkan.")
                    input("\nTekan Enter untuk lanjut...")
                    return
                if 1 <= no_v <= len(daftar_varian):
                    varian_dipilih = daftar_varian[no_v - 1]
                    break
                print("Nomor varian tidak valid.")
            except ValueError:
                print("Input harus berupa angka, bukan huruf.")

        katalog_permen.append({
            "nama": nama,
            "harga": harga,
            "stok": stok,
            "jenis": jenis_dipilih,
            "varian": varian_dipilih,
        })
        print("Menu berhasil ditambahkan.")

    elif pilih == 2:
        daftar_jenis = list(jenis_permen.keys())
        for i, j in enumerate(daftar_jenis, start=1):
            print(f"{i}. {j} -> {', '.join(jenis_permen[j])}")
        print("0. Batal")

        while True:
            raw_j = input("Pilih nomor jenis permen: ").strip()
            if not raw_j:
                print("Pilihan tidak boleh kosong.")
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

        while True:
            varian_baru = input("Nama varian rasa baru (atau 0 untuk batal): ").strip()
            if varian_baru == "0":
                print("Tindakan dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if varian_baru:
                break
            print("Nama varian tidak boleh kosong.")

        if varian_baru not in jenis_permen[jenis_dipilih]:
            jenis_permen[jenis_dipilih].append(varian_baru)
            print("Variasi rasa berhasil ditambahkan.")
        else:
            print("Variasi rasa sudah ada.")

    input("\nTekan Enter untuk lanjut...")



# Admin Read
import os

def read_admin():
    os.system("cls")
    print("=== ADMIN - LIHAT DATA MENU ===")
    print("1. Tampilkan Seluruh Menu & Variasi")
    print("0. Keluar / Kembali")

    while True:
        raw = input("Pilih (1/0): ").strip()
        if not raw:
            print("Input tidak boleh kosong.")
            continue
        try:
            pilih = int(raw)
            if pilih in (1, 0):
                break
            print("Pilihan harus 1 atau 0.")
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    if pilih == 0:
        print("Keluar dari Lihat Data Menu Admin.")
        input("\nTekan Enter untuk lanjut...")
        return

    if not katalog_permen:
        print("Belum ada data menu permen.")
    else:
        for no, item in enumerate(katalog_permen, start=1):
            status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
            print(f"\n[Menu ke-{no}]")
            print(f"1. Nama Permen: {item['nama']}")
            print(f"2. Harga Permen: Rp{item['harga']:,}".replace(",", ".") + "/pcs")
            print(f"3. Jumlah Stok: {item['stok']} pcs")
            print(f"4. Jenis Permen: {item['jenis'].upper()}")
            print(f"5. Varian Rasa: {item['varian']}")
            print(f"6. Status: {status}")

    print("\n--- Daftar Jenis & Variasi Rasa ---")
    for jenis, varians in jenis_permen.items():
        print(f"{jenis}: {', '.join(varians)}")

    input("\nTekan Enter untuk lanjut...")



# Admin Update
import os

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



# Admin Delete
import os

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



# Admin Keluar
import os
import sys
import inquirer

def keluar_admin():
    os.system("cls")
    pilihan = [
        inquirer.List(
            "keluar",
            message="Keluar Admin - Pilih tujuan",
            choices=[
                "kembali ke pemilihan admin/pelanggan",
                "keluar dari sistem",
            ],
        ),
    ]
    pilih = inquirer.prompt(pilihan)

    if pilih["keluar"] == "keluar dari sistem":
        os.system("cls")
        print("Terima kasih telah berkunjung ke toko permen!")
        sys.exit()

    os.system("cls")
    print("Kembali ke pemilihan admin/pelanggan...")
    return False



# Pelanggan Create
import os

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



# Pelanggan Read
import os

def read_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - LIHAT BELANJAAN ===")
    print("1. Lihat Menu Toko Permen")
    print("2. Lihat Isi Belanjaan Saat Ini")
    print("0. Keluar / Kembali")

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
        print("Keluar dari Read Pelanggan.")
        input("\nTekan Enter untuk lanjut...")
        return

    if pilih == 1:
        for no, item in enumerate(katalog_permen, start=1):
            status = "TERSEDIA" if item["stok"] > 0 else "HABIS"
            print(f"\n[Menu ke-{no}]")
            print(f"1. Nama Permen: {item['nama']}")
            print(f"2. Harga Permen: Rp{item['harga']:,}".replace(",", ".") + "/pcs")
            print(f"3. Jumlah Stok: {item['stok']} pcs")
            print(f"4. Jenis Permen: {item['jenis'].upper()}")
            print(f"5. Varian Rasa: {item['varian']}")
            print(f"6. Status: {status}")

    elif pilih == 2:
        if not shopping_list:
            print("Shopping list masih kosong.")
        else:
            total = 0
            for i, entry in enumerate(shopping_list, start=1):
                item = katalog_permen[entry["menu_index"]]
                subtotal = item["harga"] * entry["qty"]
                total += subtotal
                print(
                    f"{i}. {item['nama']} | Varian: {entry['varian']} | "
                    f"Qty: {entry['qty']} | Subtotal: Rp{subtotal:,}".replace(",", ".")
                )
            print("Total Belanja: Rp" + f"{total:,}".replace(",", "."))

    input("\nTekan Enter untuk lanjut...")



# Pelanggan Update
import os

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



# Pelanggan Delete
import os

def delete_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - HAPUS BELANJAAN ===")
    if not shopping_list:
        print("Belanjaan kosong.")
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



# Pelanggan Bayar
import os
from prettytable import PrettyTable

def bayar_pelanggan():
    os.system("cls")
    print("=== PELANGGAN - BAYAR ===")
    if not shopping_list:
        print("Belanjaan masih kosong, tidak ada yang dibayar.")
        input("\nTekan Enter untuk lanjut...")
        return

    tabel = PrettyTable()
    tabel.field_names = ["No", "Nama Permen", "Varian", "Qty", "Harga/pcs", "Subtotal"]
    tabel.align["No"] = "c"
    tabel.align["Nama Permen"] = "l"
    tabel.align["Varian"] = "l"
    tabel.align["Qty"] = "r"
    tabel.align["Harga/pcs"] = "r"
    tabel.align["Subtotal"] = "r"

    total = 0
    for i, entry in enumerate(shopping_list, start=1):
        item = katalog_permen[entry["menu_index"]]
        subtotal = item["harga"] * entry["qty"]
        total += subtotal
        tabel.add_row([
            i,
            item["nama"],
            entry["varian"],
            entry["qty"],
            "Rp" + f"{item['harga']:,}".replace(",", "."),
            "Rp" + f"{subtotal:,}".replace(",", "."),
        ])

    print(tabel)
    print("Total yang harus dibayar: Rp" + f"{total:,}".replace(",", "."))
    print("Ketik 0 untuk batal bayar.")

    while True:
        raw_uang = input("Masukkan jumlah uang bayar: ").strip()
        if not raw_uang:
            print("Jumlah uang tidak boleh kosong.")
            continue
        try:
            uang = int(raw_uang)
            if uang == 0:
                print("Pembayaran dibatalkan.")
                input("\nTekan Enter untuk lanjut...")
                return
            if uang < 0:
                print("Jumlah uang tidak boleh negatif.")
                continue
            break
        except ValueError:
            print("Input harus berupa angka, bukan huruf.")

    if uang < total:
        print("Uang tidak mencukupi.")
    else:
        for entry in shopping_list:
            item = katalog_permen[entry["menu_index"]]
            item["stok"] = max(0, item["stok"] - entry["qty"])
        kembalian = uang - total
        shopping_list.clear()

        os.system("cls")
        print("==========================================")
        print("          STRUK BELANJA TOKO PERMEN       ")
        print("==========================================")
        print(tabel)
        print("Total Belanja : Rp" + f"{total:,}".replace(",", "."))
        print("Uang Bayar    : Rp" + f"{uang:,}".replace(",", "."))
        print("Kembalian     : Rp" + f"{kembalian:,}".replace(",", "."))
        print("==========================================")
        print("   Terima kasih sudah berbelanja! :)     ")
        print("==========================================")

    input("\nTekan Enter untuk lanjut...")



# Pelanggan Keluar
import os
import sys
import inquirer

def keluar_pelanggan():
    os.system("cls")
    pilihan = [
        inquirer.List(
            "keluar",
            message="Keluar Pelanggan - Pilih tujuan",
            choices=[
                "kembali ke pemilihan admin/pelanggan",
                "keluar dari sistem",
            ],
        ),
    ]
    pilih = inquirer.prompt(pilihan)

    if pilih["keluar"] == "keluar dari sistem":
        os.system("cls")
        print("Terima kasih telah berkunjung ke toko permen!")
        sys.exit()

    os.system("cls")
    print("Kembali ke pemilihan admin/pelanggan...")
    return False
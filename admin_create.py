import os
from data_awal import jenis_permen, katalog_permen

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
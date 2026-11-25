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
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

    if not pilih:
        return False

    if pilih["keluar"] == "keluar dari sistem":
        os.system("cls")
        print("Terima kasih telah berkunjung ke toko permen!")
        sys.exit()

    os.system("cls")
    return False
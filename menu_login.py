from tampilan_menu import admin, pengguna
from data_awal import Nama_admin, Pw_admin
import os
import sys
import inquirer

def MenuUtama():
    while True:
        os.system("cls")
        print("============ Selamat datang di toko permen =============")
        pilihan = [
            inquirer.List(
                "login",
                message="Login Sebagai",
                choices=["admin", "pengguna", "keluar dari sistem"],
            ),
        ]
        logins = inquirer.prompt(pilihan)

        if logins["login"] == "admin":
            logmin()
            os.system("cls")
        elif logins["login"] == "pengguna":
            pengguna()
            os.system("cls")
        elif logins["login"] == "keluar dari sistem":
            os.system("cls")
            print("Terima kasih telah berkunjung ke toko permen!")
            sys.exit()

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
        return

if __name__ == "__main__":
    MenuUtama()
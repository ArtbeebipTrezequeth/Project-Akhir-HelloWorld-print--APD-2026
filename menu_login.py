from menu_login import admin, pengguna
import os
import inquirer

def MenuUtama():
    os.system("cls")
    print("============ Selamat datang di toko permen =============")
    pilihan = [
        inquirer.List(
            "login",
            message="Login Sebagai",
            choices=["admin", "pengguna"],
        ),
    ]
    logins = inquirer.prompt(pilihan)

    if(logins["login"]) == "admin":
        logmin()
        os.system("cls")
    elif(logins["login"]) == "pengguna":
        pengguna()
        os.system("cls")

def logmin():
    os.system("cls")
    try:
        print("=========================")
        user = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        print("=========================")
        if not ((user == "a" and password == "a")):
            raise ValueError
    except ValueError:
        os.system("cls")
        logcoba()

    else:
        os.system("cls")
        if (user == "a" and password == "a"):
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
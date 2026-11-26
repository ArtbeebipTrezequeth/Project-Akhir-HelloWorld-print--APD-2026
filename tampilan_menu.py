import os
import inquirer
from admin_create import create_admin
from admin_read import read_admin
from admin_update import update_admin
from admin_delete import delete_admin
from admin_keluar import keluar_admin
from pelanggan_create import create_pelanggan
from pelanggan_read import read_pelanggan
from pelanggan_update import update_pelanggan
from pelanggan_delete import delete_pelanggan
from pelanggan_bayar import bayar_pelanggan
from pelanggan_keluar import keluar_pelanggan

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

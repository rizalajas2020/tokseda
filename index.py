import time
import random
from datetime import datetime, timedelta

# ==============================
# DATA AWAL
# ==============================

data_pembelian = [
    {"nama": "Diandra", "barang": "HP IP 17 Pro Max", "harga": 24999000},
    {"nama": "Gazzael", "barang": "Motor Aerox New", "harga": 41700000},
    {"nama": "Ismail", "barang": "PS 5", "harga": 10000000}
]

riwayat_pembatalan = []
riwayat_pembelian = []

# ==============================
# FUNCTION UMUM
# ==============================

def hitung_total():
    return sum(data['harga'] for data in data_pembelian)

def tampilkan_data():
    print("\n=== DAFTAR PEMBELIAN ===")
    if not data_pembelian:
        print("Tidak ada data pembelian.")
    else:
        for i, data in enumerate(data_pembelian, start=1):
            print(f"{i}. Nama   : {data['nama']}")
            print(f"   Barang : {data['barang']}")
            print(f"   Harga  : Rp {data['harga']:,}")
            print("-" * 30)
    print(f"TOTAL BELANJA: Rp {hitung_total():,}")

# ==============================
# ANIMASI 5 DETIK
# ==============================

def animasi_5_detik():
    print("\nPermintaan pembatalan sedang diproses...")
    for i in range(5, 0, -1):
        print(f"Memproses dalam {i} detik...", end="\r")
        time.sleep(1)
    print("\nProses selesai! ✅")

# ==============================
# OPSI CICILAN
# ==============================

def opsi_cicilan():
    tampilkan_data()
    if not data_pembelian:
        return

    nomor = int(input("Pilih nomor pembelian untuk cicilan: "))
    if 1 <= nomor <= len(data_pembelian):
        data = data_pembelian[nomor - 1]
        harga = data['harga']

        print("\nPilih Tenor:")
        print("1. 3 Bulan")
        print("2. 6 Bulan")
        print("3. 12 Bulan")

        pilih = input("Pilih (1/2/3): ")
        tenor = {"1":3, "2":6, "3":12}

        if pilih in tenor:
            bulan = tenor[pilih]
            cicilan = harga / bulan
            print(f"Cicilan per bulan: Rp {cicilan:,.0f}")

            hari = random.randint(3,7)
            print(f"Estimasi barang sampai: {hari} hari kerja")

# ==============================
# PILIH ALASAN
# ==============================

def pilih_alasan():
    print("\nPilih Alasan Pembatalan:")
    print("1. Harga Tidak Masuk Akal")
    print("2. Barang Tidak Diperlukan Lagi")
    print("3. Waktu Pengiriman Yang Lama")
    print("4. Salah Pemesanan")
    print("5. Salah Memasukkan Alamat")

    pilihan = input("Masukkan nomor (pisahkan koma jika lebih dari 1): ")

    alasan_dict = {
        "1":"Harga Tidak Masuk Akal",
        "2":"Barang Tidak Diperlukan Lagi",
        "3":"Waktu Pengiriman Yang Lama",
        "4":"Salah Pemesanan",
        "5":"Salah Memasukkan Alamat"
    }

    return [alasan_dict[p.strip()] for p in pilihan.split(",") if p.strip() in alasan_dict]

# ==============================
# PEMBATALAN
# ==============================

def batalkan_pembelian():
    tampilkan_data()
    if not data_pembelian:
        return

    nama_input = input("Masukkan nama yang ingin dibatalkan (pisahkan koma jika lebih dari 1): ").lower()
    daftar_nama = [n.strip() for n in nama_input.split(",")]

    alasan = pilih_alasan()

    konfirmasi = input("Yakin ingin membatalkan? (Yes/No): ").lower()
    if konfirmasi != "yes":
        print("Pembatalan dibatalkan.")
        return

    animasi_5_detik()

    for nama in daftar_nama:
        ditemukan = False
        for data in data_pembelian[:]:
            if data['nama'].lower() == nama:
                waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                riwayat_pembatalan.append({
                    "nama": data['nama'],
                    "barang": data['barang'],
                    "harga": data['harga'],
                    "waktu_pembatalan": waktu,
                    "alasan": alasan
                })

                data_pembelian.remove(data)
                print(f"{data['nama']} berhasil dibatalkan.")
                ditemukan = True

        if not ditemukan:
            print(f"Nama {nama} tidak ditemukan.")

# ==============================
# SETUJU PEMBELIAN
# ==============================

def setuju_pembelian():
    tampilkan_data()
    if not data_pembelian:
        return

    nama_input = input("Masukkan nama yang ingin disetujui (pisahkan koma jika lebih dari 1): ").lower()
    daftar_nama = [n.strip() for n in nama_input.split(",")]

    konfirmasi = input("Setuju membeli? (Yes/No): ").lower()
    if konfirmasi != "yes":
        print("Tidak jadi disetujui.")
        return

    for nama in daftar_nama:
        for data in data_pembelian:
            if data['nama'].lower() == nama:
                waktu = datetime.now()
                estimasi = random.randint(3,7)
                tanggal_sampai = waktu + timedelta(days=estimasi)

                riwayat_pembelian.append({
                    "nama": data['nama'],
                    "barang": data['barang'],
                    "waktu_beli": waktu.strftime("%d-%m-%Y %H:%M:%S"),
                    "estimasi_sampai": tanggal_sampai.strftime("%d-%m-%Y")
                })

                print("\n=== PEMBELIAN DISETUJUI ===")
                print(f"Nama : {data['nama']}")
                print(f"Waktu: {waktu.strftime('%d-%m-%Y %H:%M:%S')}")
                print(f"Estimasi Tiba: {tanggal_sampai.strftime('%d-%m-%Y')}")

                if data['nama'].lower() == "diandra":
                    print("Terima Kasih Diandra 🙏 dari TokSeDa")

# ==============================
# MENU 6 - WAKTU PEMBATALAN
# ==============================

def tampilkan_waktu_pembatalan():
    print("\n=== WAKTU & TANGGAL BARANG YANG DIBATALKAN ===")
    if not riwayat_pembatalan:
        print("Belum ada pembatalan.")
    else:
        for data in riwayat_pembatalan:
            print(f"Nama   : {data['nama']}")
            print(f"Barang : {data['barang']}")
            print(f"Waktu  : {data['waktu_pembatalan']}")
            print("-" * 30)

# ==============================
# MENU UTAMA
# ==============================

print("==========================================")
print("Selamat Datang Diandra 👋")
print("Terima Kasih Telah Menghubungi TokSeDa")
print("Permintaan Anda Akan Diproses")
print("==========================================")

while True:
    print("\n=== MENU ===")
    print("1. Tampilkan Data")
    print("2. Batalkan Pembelian")
    print("3. Opsi Cicilan")
    print("4. Setuju Pembelian")
    print("5. Waktu & Tanggal Pembatalan")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == "1":
        tampilkan_data()
    elif menu == "2":
        batalkan_pembelian()
    elif menu == "3":
        opsi_cicilan()
    elif menu == "4":
        setuju_pembelian()
    elif menu == "5":
        tampilkan_waktu_pembatalan()
    elif menu == "6":
        print("Terima kasih telah menggunakan TokSeDa 🙏")
        break
    else:
        print("Pilihan tidak valid.")
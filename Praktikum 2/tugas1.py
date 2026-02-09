# ==========================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File.txt)
#
# Nama  : Faiza Aghnaita Zahra  
# NIM   : J0403251122
# Kelas : TPLA2
# ==========================================================


# -------------------------------
# Konstanta nama file
# -------------------------------
nama_file = "stok_barang.txt" #nama file untuk menyimpan data stok barang


# -------------------------------
# Fungsi : Membaca data dari file
# -------------------------------

def baca_stok(nama_file):
    '''
    Membaca data stok dari file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    Output:
    - stok_dict (dictionary)
    key = kode_barang
    value = {"nama": nama_barang, "stok": stok_int}
    '''
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file: 
        for baris in file: #loop untuk setiap baris dalam file
            baris = baris.strip() #ambil data perbaris dan hilangkan new line
            KodeBarang, NamaBarang, StokBarang = baris.split(",") #ambil data per item data
            stok_dict[KodeBarang] = {"Nama barang": NamaBarang, "Stok barang": int(StokBarang)} #masukkan dalam dictionary 
    return stok_dict   

buka_data = baca_stok(nama_file) #memanggil fungsi load data dan menyimpan dalam variable 

    # TODO: Buka file dan baca seluruh baris
    # Hint: with open(nama_file, "r", encoding="utf-8") as f:
    # TODO: Untuk setiap baris:
    # - gunakan strip() untuk menghilangkan \n
    # - split(",") untuk memisahkan kolom
    # - simpan ke dictionary


# -------------------------------
# Fungsi: Menyimpan data ke file
# -------------------------------

def simpan_stok(nama_file, stok_dict):
    '''
    Menyimpan seluruh data stok ke file teks.
    Format per baris: KodeBarang,NamaBarang,Stok
    '''
    with open(nama_file, "w", encoding="utf-8") as file:
        for KodeBarang in sorted(stok_dict.keys()): #loop untuk setiap kode barang yang tersimpan
            NamaBarang = stok_dict[KodeBarang]["Nama barang"] #ambil nama dari dictionary
            StokBarang = stok_dict[KodeBarang]["Stok barang"] #ambil stok dari dictionary
            file.write(f"{KodeBarang},{NamaBarang},{StokBarang}\n") #tulis ke file dalam format yang benar

    # TODO: Tulis ulang seluruh isi file berdasarkan stok_dict
    # Hint: with open(nama_file, "w", encoding="utf-8") as f:

    print("\nData Berhasil Disimpan ke File: ", nama_file) #konfirmasi penyimpanan
    pass


# -------------------------------
# Fungsi: Menampilkan semua data
# -------------------------------

def tampilkan_semua(stok_dict):
    '''
    Menampilkan semua barang di stok_dict.
    '''
    print("\n======== DAFTAR STOK BARANG ========")
    print(f"{'Kode Barang' : <10} | {'Nama Barang' : <12} | {'Stok Barang' : >5}")

    # TODO: Jika kosong, tampilkan pesan stok kosong
    # TODO: Tampilkan dengan format rapi: kode | nama | stok

    print("-"*32) #membuat garis 

    #menampilkan isi datanya 
    for KodeBarang in sorted(stok_dict.keys()): #loop untuk setiap kode barang yang tersimpan
        NamaBarang = stok_dict[KodeBarang]["Nama barang"] #ambil nama dari dictionary
        StokBarang = stok_dict[KodeBarang]["Stok barang"] #ambil stok dari dictionary
         #tampilkan dalam format tabel
        print(f"{KodeBarang:<10} | {NamaBarang:<12} | {int(StokBarang):>5}")

#tampilkan_semua(buka_data) #memanggil fungsi untuk menampilkan data 
pass


# -------------------------------
# Fungsi: Cari barang berdasarkan kode
# -------------------------------

def cari_barang(stok_dict):
    '''
    Mencari barang berdasarkan kode barang.
    '''
    kode_cari = input("Masukkan Kode Barang yang ingin dicari: ").strip() #input kode barang yang akan dicari

    if kode_cari in stok_dict: #cek apakah kode ada dalam dictionary
        NamaBarang = stok_dict[kode_cari]["Nama barang"] #ambil nama dari dictionary
        StokBarang = stok_dict[kode_cari]["Stok barang"] #ambil stok dari dictionary

        print("===== Data Barang Ditemukan =====") #tampilkan detail barang
        print(f"Kode barang : {kode_cari}") #tampilkan kode barang
        print(f"Nama barang : {NamaBarang}") #tampilkan nama barang
        print(f"Stok barang : {StokBarang}") #tampilkan stok barang
    else: 
        print("Stok tidak ditemukan. Pastikan Kode Barang yang dimasukkan benar") #jika kode tidak ditemukan

    # TODO: Cek apakah kode ada di dictionary
    # Jika ada: tampilkan detail barang
    # Jika tidak ada: tampilkan 'Barang tidak ditemukan'

    pass


# -------------------------------
# Fungsi: Tambah barang baru
# -------------------------------

def tambah_barang(stok_dict):
    '''
    Menambah barang baru ke stok_dict.
    '''
    KodeBarang = input("Masukkan kode barang baru: ").strip() #input kode barang baru
    
    #Memvalidasi bahwa kode tidak boleh ter duplikat
    if KodeBarang in stok_dict: #cek apakah kode sudah ada dalam dictionary
        print(f"Kode {KodeBarang} sudah digunakan. Silakan gunakan kode lain.") #jika kode sudah ada
        return
    
    NamaBarang = input("Masukkan nama barang: ").strip() #input nama barang baru
    
    #Input stok awal  
    try:
        stok_awal = int(input("Masukkan stok awal (angka): ")) #input stok awal
        if stok_awal < 0: #cek stok tidak boleh kosong
            print("Stok tidak boleh negatif!") 
            return
    except ValueError: #jika input bukan angka
        print("Input tidak valid. Stok harus berupa angka.")
        return
    
    #Menyimpan data barang baru ke dictionary
    stok_dict[KodeBarang] = {"Nama barang": NamaBarang, "Stok barang": stok_awal} #masukkan dalam dictionary
    print(f"Barang {NamaBarang} ({KodeBarang}) berhasil ditambahkan dengan stok {stok_awal}.") #konfirmasi penambahan barang


# -------------------------------
# Fungsi: Update stok barang
# -------------------------------

def update_stok(stok_dict):
    '''
    Mengubah stok barang (tambah atau kurangi).
    Stok tidak boleh menjadi negatif.
    '''
    kode = input("Masukkan kode barang yang ingin diupdate: ").strip()

    #Mengecek apakah kode barang yang di input ada di dictionary
    if kode not in stok_dict: #cek apakah kode ditemukan
        print(f"Kode {kode} tidak ditemukan.")
        return
    
    print(f"Barang: {stok_dict[kode]['Nama barang']}") #tampilkan nama barang
    print(f"Stok saat ini: {stok_dict[kode]['Stok barang']}") #tampilkan stok saat ini

    print("\nPilih jenis update:") #pilihan jenis update
    print("1. Tambah stok") #tampilkan pilihan tambah stok
    print("2. Kurangi stok") #tampilkan pilihan kurangi stok
    
    pilihan = input("Masukkan pilihan (1/2): ").strip() #input pilihan jenis update

    #Menginput jumlah perubahan stok barang
    try: #mengubah input jumlah ke integer
        jumlah = int(input("Masukkan jumlah: ")) #input jumlah perubahan stok
        if jumlah < 0: #cek jumlah tidak boleh negatif
            print("Jumlah tidak boleh kosong.")
            return
        
    except ValueError: #jika input bukan angka
        print("Input tidak valid. Harus berupa angka.")
        return
    
    stok_sekarang = stok_dict[kode]["Stok barang"] #ambil stok saat ini dari dictionary
    
    if pilihan == "1": #jika pilihan tambah stok
        stok_baru = stok_sekarang + jumlah #hitung stok baru
        stok_dict[kode]["Stok barang"] = stok_baru #update stok baru ke dictionary
        print(f"Stok berhasil ditambah. Stok baru: {stok_baru}") #tampilkan konfirmasi penambahan stok

    elif pilihan == "2": #jika pilihan kurangi stok
        stok_baru = stok_sekarang - jumlah #hitung stok baru
        if stok_baru < 0: #validasi stok tidak boleh dibawah nol
            print(f"Stok tidak boleh negatif! Stok saat ini hanya {stok_sekarang}.")
            return
        stok_dict[kode]["Stok barang"] = stok_baru #update stok baru ke dictionary
        print(f"Stok berhasil dikurangi. Stok baru: {stok_baru}") #tampilkan konfirmasi pengurangan stok

    else: #jika pilihan tidak valid
        print("Pilihan tidak valid.")


# -------------------------------
# Program Utama (Menu)
# -------------------------------

def main():
# Membaca data dari file saat program mulai
    buka_data = baca_stok(nama_file)

    while True: #loop menu sampai user keluar
        print("\n=== MENU STOK KANTIN ===") #tampilkan menu utama
        print("1. Tampilkan semua barang") #pilihan 1
        print("2. Cari barang berdasarkan kode") #pilihan 2
        print("3. Tambah barang baru") #pilihan 3
        print("4. Update stok barang") #pilihan 4
        print("5. Simpan ke file") #pilihan 5
        print("0. Keluar") #pilihan keluar

        pilihan = input("Pilih menu: ").strip() #input pilihan user

        if pilihan == "1": #jika pilihan 1
            tampilkan_semua(buka_data) #memanggil fungsi tampilkan semua data

        elif pilihan == "2": #jika pilihan 2
            cari_barang(buka_data) #memanggil fungsi cari barang

        elif pilihan == "3": #jika pilihan 3
            tambah_barang(buka_data) #memanggil fungsi tambah barang

        elif pilihan == "4": #jika pilihan 4
            update_stok(buka_data) #memanggil fungsi update stok

        elif pilihan == "5": #jika pilihan 5
            simpan_stok(nama_file, buka_data) #memanggil fungsi simpan data ke file
            print("Data berhasil disimpan.")

        elif pilihan == "0": #jika pilihan 0
            print("Program selesai.") #tampilkan pesan keluar
            break

        else: #jika pilihan tidak valid
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program utama
if __name__ == "__main__": 

    main() 

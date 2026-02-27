# ========================================================== 
# Nama: Faiza Aghnaita Zahra
# NIM: J0403251122
# Studi Kasus: Generator PIN dengan Rekursi 
# ========================================================== 

def buat_pin(panjang, hasil=""):
    """
    Fungsi rekursif untuk menghasilkan semua kemungkinan PIN dengan panjang tertentu
    menggunakan digit 0, 1, dan 2.
    
    Parameter:
        panjang (int): Panjang PIN yang ingin dibuat
        hasil (str): String PIN yang sedang dibangun (default = "")
 
    Kegunaan:
        - Simulasi pembangkitan PIN acak
        - Testing sistem keamanan
    """
    
    # ===============================
    # BASE CASE (Kondisi Berhenti)
    # ===============================
    # Ketika panjang string hasil sudah sama dengan panjang yang diinginkan, berarti satu kombinasi PIN sudah lengkap.
    # Cetak PIN tersebut dan kembalikan (return) untuk menghentikan rekursi
    if len(hasil) == panjang: 
        print("PIN:", hasil) 
        return 
    
    # ================================
    # RECURSIVE CASE (Kondisi Rekursif)
    # ================================
    # Loop melalui setiap digit yang tersedia: 0, 1, 2
    # Untuk setiap digit, tambahkan ke string hasil dan panggil fungsi rekursif untuk menambahkan digit berikutnya
    for angka in ["0", "1", "2"]: 
        # Pemanggilan rekursif dengan angka yang ditambahkan ke hasil
        # Proses ini akan terus berlanjut hingga hasil mencapai panjang yang diinginkan
        buat_pin(panjang, hasil + angka) 

print("Generator PIN dengan panjang 3 menggunakan digit 0, 1, 2:")
print("Total PIN yang mungkin: 3^3 = 27\n")
buat_pin(3)

# Penjelasan:
# - Fungsi membuat pohon rekursi dengan 3 cabang di setiap level
# - Untuk panjang 2, ada 2 level (untuk 2 digit)
# - Total PIN = 3^2 = 9 kombinasi
# - Urutan PIN mengikuti pola Depth-First Search (DFS) 
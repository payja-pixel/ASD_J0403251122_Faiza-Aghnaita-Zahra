# ========================================================== 
# Nama: Faiza Aghnaita Zahra
# NIM: J0403251122
# Latihan 3: Mencari Nilai Maksimum dengan Rekursi
# ========================================================== 
# PENJELASAN KONSEP:
# Program ini mencari nilai maksimum dalam sebuah list menggunakan teknik rekursi.
# Ide dasarnya adalah membandingkan elemen saat ini dengan nilai maksimum dari sisa list.
# 
# Alur kerja:
# 1. Mulai dari elemen pertama
# 2. Bandingkan dengan nilai maksimum dari elemen-elemen berikutnya
# 3. Kembalikan nilai yang lebih besar
# 4. Lanjutkan hingga mencapai elemen terakhir (base case)
# ========================================================== 

def cari_maks(data, index=0):
    """
    Fungsi rekursif untuk mencari nilai maksimum dalam sebuah list
    
    Algoritma:
        - Membandingkan elemen pada posisi index dengan nilai maksimum dari sisa list
        - Formula: max(data[index], cari_maks(data, index+1))
    
    Parameter:
        data (list): List berisi angka-angka yang akan dicari maksimumnya
        index (int): Indeks elemen yang sedang diperiksa (default = 0)
    
    Return:
        int: Nilai maksimum dari list
    
    Kompleksitas:
        - Time Complexity: O(n) - memeriksa setiap elemen satu kali
        - Space Complexity: O(n) - call stack menyimpan n frame
    
    Contoh:
        cari_maks([3, 7, 2, 9, 5]) -> 9
        cari_maks([1, 2, 3]) -> 3
    """
    
    # ===============================
    # BASE CASE (Kondisi Berhenti)
    # ===============================
    # Ketika index sudah mencapai elemen terakhir (index == len(data) - 1),
    # kembalikan nilai elemen tersebut karena tidak ada lagi elemen untuk dibandingkan
    if index == len(data) - 1: 
        return data[index] 
 
    # ================================
    # RECURSIVE CASE (Kondisi Rekursif)
    # ================================
    # Panggil fungsi rekursif untuk mendapatkan nilai maksimum dari elemen-elemen berikutnya
    # maks_sisa menyimpan nilai maksimum dari data[index+1] hingga data[akhir]
    maks_sisa = cari_maks(data, index + 1) 
 
    # Bandingkan elemen saat ini (data[index]) dengan nilai maksimum dari sisa list (maks_sisa)
    # Kembalikan nilai yang lebih besar
    if data[index] > maks_sisa: 
        return data[index] 
    else: 
        return maks_sisa 


# ====================================================
# TESTING & DEMONSTRASI
# ====================================================
angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka))

# VISUALISASI ALUR EKSEKUSI untuk cari_maks([3, 7, 2, 9, 5]):
#
# FASE STACKING (masuk rekursi):
# cari_maks([3,7,2,9,5], 0) -> cek index 0, panggil cari_maks(data, 1)
#   cari_maks(data, 1) -> cek index 1, panggil cari_maks(data, 2)
#     cari_maks(data, 2) -> cek index 2, panggil cari_maks(data, 3)
#       cari_maks(data, 3) -> cek index 3, panggil cari_maks(data, 4)
#         cari_maks(data, 4) -> BASE CASE, return data[4] = 5
#
# FASE UNWINDING (keluar rekursi & bandingkan):
#       maks_sisa = 5, data[3] = 9 -> return 9
#     maks_sisa = 9, data[2] = 2 -> return 9
#   maks_sisa = 9, data[1] = 7 -> return 9
# maks_sisa = 9, data[0] = 3 -> return 9
#
# OUTPUT: 9 
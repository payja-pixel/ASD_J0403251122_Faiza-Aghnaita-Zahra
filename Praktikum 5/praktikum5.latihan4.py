# ========================================================== 
# Nama: Faiza Aghnaita Zahra
# NIM: J0403251122
# Latihan 4: Kombinasi Huruf dengan Rekursi
# ========================================================== 
# PENJELASAN KONSEP:
# Program ini menghasilkan semua kemungkinan kombinasi dari dua huruf ('A' dan 'B')
# dengan panjang n menggunakan teknik rekursi backtracking.
# 
# Ide dasar:
# 1. Untuk setiap posisi, kita punya 2 pilihan: 'A' atau 'B'
# 2. Jika sudah mencapai panjang n, cetak hasilnya
# 3. Jika belum, tambahkan 'A' kemudian 'B' secara rekursif
# 
# Contoh untuk n=2:
#   - Kombinasi pertama: A -> AA, AB
#   - Kombinasi kedua: B -> BA, BB
#   Total: 2^n = 4 kombinasi
# ========================================================== 

def kombinasi(n, hasil=""):
    """
    Fungsi rekursif untuk menghasilkan semua kombinasi huruf 'A' dan 'B' dengan panjang n
    
    Algoritma:
        - Menggunakan prinsip backtracking
        - Setiap level rekursi menambahkan satu karakter ('A' atau 'B')
        - Ketika panjang hasil == n, cetak hasilnya
        - Backtrack dan coba pilihan yang lain
    
    Parameter:
        n (int): Panjang kombinasi yang diinginkan
        hasil (str): String yang sedang dibangun (default = "")
    
    Return:
        None (hanya mencetak hasil)
    
    Kompleksitas:
        - Time Complexity: O(2^n) - ada 2^n kombinasi yang dihasilkan
        - Space Complexity: O(n) - call stack menyimpan n frame
    
    Contoh:
        kombinasi(2) menghasilkan: AA, AB, BA, BB
        kombinasi(3) menghasilkan: AAA, AAB, ABA, ABB, BAA, BAB, BBA, BBB
    """
    
    # ===============================
    # BASE CASE (Kondisi Berhenti)
    # ===============================
    # Ketika panjang string hasil sudah sama dengan n, berarti kombinasi sudah lengkap
    # Cetak hasil dan kembalikan (return) untuk menghentikan rekursi
    if len(hasil) == n: 
        print(hasil) 
        return 
    
    # ================================
    # RECURSIVE CASE (Kondisi Rekursif)
    # ================================
    # PILIHAN 1: Tambahkan karakter 'A' ke string hasil
    #            dan lanjutkan rekursi untuk membangun kombinasi selanjutnya
    kombinasi(n, hasil + "A") 
    
    # PILIHAN 2: Tambahkan karakter 'B' ke string hasil
    #            dan lanjutkan rekursi untuk membangun kombinasi selanjutnya
    #            (Ini dilakukan setelah semua kombinasi dengan 'A' selesai)
    kombinasi(n, hasil + "B") 


# ====================================================
# TESTING & DEMONSTRASI
# ====================================================
print("Kombinasi huruf untuk n=2:")
kombinasi(2)

# VISUALISASI ALUR EKSEKUSI untuk kombinasi(2):
#
#                          kombinasi(2, "")
#                         /              \
#                        /                \
#          kombinasi(2,"A")         kombinasi(2,"B")
#          /            \            /            \
#         /              \          /              \
#  komb(2,"AA")   komb(2,"AB")  komb(2,"BA")  komb(2,"BB")
#     print        print         print          print
#     "AA"         "AB"          "BA"           "BB"
#
# OUTPUT:
# AA
# AB
# BA
# BB
#
# PENJELASAN:
# - Setiap level rekursi menambahkan satu karakter
# - Untuk n=2, ada 2 level (karena perlu 2 karakter)
# - Total kombinasi = 2^2 = 4 kombinasi 
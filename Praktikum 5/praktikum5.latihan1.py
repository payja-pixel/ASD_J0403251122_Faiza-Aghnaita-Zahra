# ========================================================== 
# Nama: Faiza Aghnaita Zahra
# NIM: J0403251122
# Latihan 1: Rekursi Pangkat 
# ========================================================== 
# PENJELASAN KONSEP PANGKAT DENGAN REKURSI:
# Operasi pangkat (a^n) dapat dipecah secara rekursif:
#   a^n = a * a^(n-1)
#   a^0 = 1 (base case)
# 
# Contoh: 2^4 = 2 * 2^3 = 2 * 2 * 2^2 = 2 * 2 * 2 * 2^1 = 2 * 2 * 2 * 2 * 2^0 = 2 * 2 * 2 * 2 * 1
# ========================================================== 

def pangkat(a, n): 
    """
    Fungsi rekursif untuk menghitung nilai a pangkat n (a^n)
    
    Prinsip kerja:
        - a^n = a * a^(n-1)  [recursive case]
        - a^0 = 1             [base case]
    
    Parameter:
        a (int): Basis (bilangan yang akan dipangkatkan)
        n (int): Eksponen (pangkat; harus >= 0)
    
    Return:
        int: Hasil dari a pangkat n
    
    Kompleksitas:
        - Time Complexity: O(n) - melakukan n kali pemanggilan fungsi
        - Space Complexity: O(n) - karena call stack menyimpan n frame
    
    Contoh penggunaan:
        pangkat(2, 4) -> 16
        pangkat(3, 3) -> 27
        pangkat(5, 0) -> 1
    """

    # ===============
    # BASE CASE
    # ===============
    # Kondisi berhenti untuk mencegah infinite recursion
    # Jika n == 0, maka hasilnya adalah 1
    # Alasan: Setiap bilangan pangkat 0 sama dengan 1 (a^0 = 1)
    #         Ini adalah definisi matematis yang fundamental
    # Fungsi berhenti memanggil dirinya dan mengembalikan 1
    if n == 0: 
        return 1 
    
    # ================
    # RECURSIVE CASE
    # ================
    # Kondisi rekursif ketika n > 0
    # Formula: a^n = a * a^(n-1)
    # 
    # Contoh alur untuk pangkat(2, 4):
    #   pangkat(2, 4) = 2 * pangkat(2, 3)
    #   pangkat(2, 3) = 2 * pangkat(2, 2)
    #   pangkat(2, 2) = 2 * pangkat(2, 1)
    #   pangkat(2, 1) = 2 * pangkat(2, 0)
    #   pangkat(2, 0) = 1  [BASE CASE - return dari sini]
    #
    # Kemudian hasil dihitung mundur (unwinding):
    #   pangkat(2, 1) = 2 * 1 = 2
    #   pangkat(2, 2) = 2 * 2 = 4
    #   pangkat(2, 3) = 2 * 4 = 8
    #   pangkat(2, 4) = 2 * 8 = 16
    return a * pangkat(a, n - 1) 


# ====================================================
# TESTING & DEMONSTRASI
# ====================================================
print("Hasil pangkat(2, 4) =", pangkat(2, 4))

# VISUALISASI ALUR EKSEKUSI:
# 
# FASE STACKING (masuk rekursi):
# ├─ pangkat(2, 4) dipanggil
# │  ├─ pangkat(2, 3) dipanggil
# │  │  ├─ pangkat(2, 2) dipanggil
# │  │  │  ├─ pangkat(2, 1) dipanggil
# │  │  │  │  ├─ pangkat(2, 0) dipanggil
# │  │  │  │  │  └─ return 1 (BASE CASE TERCAPAI)
#
# FASE UNWINDING (keluar rekursi & hitung hasil):
# │  │  │  │  └─ return 2 * 1 = 2
# │  │  │  └─ return 2 * 2 = 4
# │  │  └─ return 2 * 4 = 8
# │  └─ return 2 * 8 = 16
# └─ HASIL AKHIR: 16
#
# OUTPUT: 16
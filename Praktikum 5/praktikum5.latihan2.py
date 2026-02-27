# ========================================================== 
# Nama: Faiza Aghnaita Zahra
# NIM: J0403251122
# Latihan 2: Tracing Rekursi 
# ========================================================== 
# PENJELASAN REKURSI:
# Rekursi adalah teknik pemrograman dimana suatu fungsi memanggil dirinya sendiri.
# Setiap fungsi yang rekursif HARUS memiliki:
#   1. BASE CASE (kondisi berhenti) - untuk menghindari infinite loop
#   2. RECURSIVE CASE - pemanggilan fungsi dengan parameter yang lebih kecil
# 
# FASE STACKING & UNWINDING:
# - STACKING (masuk): Setiap kali fungsi dipanggil, disimpan di call stack
# - UNWINDING (keluar): Setelah base case tercapai, fungsi kembali & di-pop dari stack
# ========================================================== 

def countdown(n): 
    """
    Fungsi rekursif untuk menampilkan urutan angka mundur
    
    Parameter:
        n (int): Angka awal untuk countdown
    
    Alur eksekusi countdown(3):
        1. countdown(3) -> print "Masuk: 3" -> countdown(2)
        2. countdown(2) -> print "Masuk: 2" -> countdown(1)
        3. countdown(1) -> print "Masuk: 1" -> countdown(0)
        4. countdown(0) -> print "Selesai" -> RETURN (base case tercapai)
        5. Kembali ke countdown(1) -> print "Keluar: 1"
        6. Kembali ke countdown(2) -> print "Keluar: 2"
        7. Kembali ke countdown(3) -> print "Keluar: 3"
    """
    
    # BASE CASE: Kondisi untuk menghentikan rekursi
    # Jika n = 0, tidak ada lagi pemanggilan rekursif
    if n == 0: 
        print("Selesai") 
        return 
    
    # FASE STACKING: Mencetak nilai SEBELUM pemanggilan rekursif
    # Ini akan dicetak saat fungsi masuk (sebelum call stack berkurang)
    print("Masuk:", n) 
    
    # PEMANGGILAN REKURSIF: Fungsi memanggil dirinya sendiri dengan n-1
    # Ini menyebabkan call stack bertambah (stacking)
    countdown(n - 1) 
    
    # FASE UNWINDING: Mencetak nilai SETELAH pemanggilan rekursif selesai
    # Ini akan dicetak saat fungsi kembali dari rekursi (call stack berkurang)
    # Urutan "Keluar" akan terbalik dari "Masuk" karena stack bersifat LIFO
    print("Keluar:", n) 


# PEMANGGILAN FUNGSI
# Memanggil countdown dengan parameter awal 3
countdown(3)

# OUTPUT YANG DIHARAPKAN:
# Masuk: 3
# Masuk: 2
# Masuk: 1
# Selesai
# Keluar: 1
# Keluar: 2
# Keluar: 3
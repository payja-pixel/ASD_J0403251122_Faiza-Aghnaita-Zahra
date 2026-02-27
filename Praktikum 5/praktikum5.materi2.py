# ========================================================== 
# Contoh Rekursi 2: Tracing Masuk/Keluar 
# ========================================================== 

def hitung(n): 
    # Base case 
    if n == 0: 
        print("Selesai") 
        return 

    print("Masuk:", n)      
    hitung(n - 1)           
    print("Keluar:", n)     

hitung(3) 

# fase stacking 
# pemanggilan rekursif 
# fase unwinding
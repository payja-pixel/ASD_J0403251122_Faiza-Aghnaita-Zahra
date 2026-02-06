#========================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 1 : Membaca seluruh isi file data 
#========================================================


print("====Membuka file dalam satu string====")
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    isi_file = file.read() 
print(isi_file) 

print("Tipe data :", type(isi_file))

print("====Membuka file per baris====")
jumlah_baris = 0
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1 
        baris = baris.strip()   # menghilangkan karakter baris baru  
        print("baris ke-", jumlah_baris)
        print("isinya :", baris) 


#========================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 2 : Memecah data menjadi satuan bentuk kolom 
#========================================================


# Parsing baris menjadi data satuan dan menampilkannya dalam bentuk kolom kolom data 
with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1 
        baris = baris.strip()   # menghilangkan karakter baris baru  
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        print("NIM :", nim, "| Nama :", nama, "| Nilai :", nilai) # menampilkan satuan data dalam bentuk kolom 


#========================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 3 : Membaca data dan menyimpannya ke struktur data list
#========================================================


data_list = [] # inisialisasi list untuk menampung data

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1 
        baris = baris.strip()   # menghilangkan karakter baris baru  
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        data_list.append([nim, nama, int(nilai)]) # menyimpan data ke list 
print("====Menampilkan List====")
print(data_list)
print("Contoh record ke 1", data_list[0])
print("Contoh record ke 2", data_list[2]) 

print("Jumlah Record", len(data_list))


#========================================================
# Praktikum 1 : Konsep ADT dan File Handling
# Latihan Dasar 4 : Membaca data dan menyimpannya ke struktur data dictionary 
#========================================================


data_dict = {} # inisialisasi ke dalam dictionary 

with open("data_mahasiswa.txt","r",encoding="utf-8") as file:
    for baris in file: 
        jumlah_baris = jumlah_baris + 1 
        baris = baris.strip()   # menghilangkan karakter baris baru  
        nim, nama, nilai = baris.split(",") # pecah menjadi data satuan dan simpan ke variabel 
        # simpan data ke dalam dictionary 
        data_dict[nim] = {
            "nama" : nama, 
            "nilai" : int(nilai)
        }
print("====Menampilkan data dictionary====")
print(data_dict) 
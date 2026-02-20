#============================================================================================
# Nama    : Faiza Aghnaita Zahra
# NIM     : J0403251122
# Kelas   : TPLA2
#============================================================================================

#============================================================================================
# Implementasi Dasar : Queue
#============================================================================================

class Node:
    # konstruktor yang dijalankan secara oromatis ketika class node dipanggil / diintantiasi
    def __init__(self, data):
        self.data = data # menyimpan nilai / data pada list 
        self.next = None # pointer ini menunjuk ke node selanjutnya

class queue:
    # kontruktor adalah fungsi yang dijalankan secara otomatis ketika class node dipanggil / diinstansiasi
    def __init__(self, data):
        self.data = data # menyimpan nilai / data pada list
        self.next = None # pointer ini menunjuk ke node selanjutnya

class queue:
    # buat kontruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None # node paling depan
        self.rear = None # node paling belakang

    def is_empty(self):
        return self.front is None

    # membuat fungsi untuk menambahkan data baru pada bagian paling belakang
    def enqueue(self, data):
        nodeBaru = Node(data)

        # jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru 
            return
        
        # jika queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru # letakkan data baru pada seteelahnya rear
        self.rear = nodeBaru # jadikan data baru sebagai rear

    def dequeue(self):
        # menghapus data dari depan / front
        data_terhapus = self.front.data # lihat data paling depan 

        # geser front ke node berikutnya
        self.front = self.front.next

        # jika setelah geser front menjadi none, maka letakkan data baru seetlah rear dan jadikan data baru sebagai rear
        # rear juga harus jadi none 
        if self.front is None:
            self.rear = None
            return 
        
    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("Rear")

# instantiasi class Queue
q = queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
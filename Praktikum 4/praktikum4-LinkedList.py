#============================================================================================
# Nama    : Faiza Aghnaita Zahra
# NIM     : J0403251122
# Kelas   : TPLA2
#============================================================================================

#============================================================================================
# Implementasi Dasar : Node pada Linked List
#============================================================================================

class Node:
    # konstruktor yang dijalankan secara oromatis ketika class node dipanggil / diintantiasi
    def __init__(self, data):
        self.data = data # menyimpan nilai / data pada list 
        self.next = None # pointer ini menunjuk ke node selanjutnya

#(1) membuat node dengan instantiasi class node
nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")

#(2) mendefinisikan head dan menghubungkan node : A -> B -> C -> None
head = nodeA 
nodeA.next = nodeB
nodeB.next = nodeC

#(3) Teversal : menulusuri node dari head sampai ke None
current = head 
while current is not None: # menampilkan data pada node saat ini
    print(current.data) 
    current = current.next 
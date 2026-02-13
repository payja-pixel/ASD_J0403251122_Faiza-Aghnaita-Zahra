class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if not self.head:
            print("Kosong.")
            return

        temp = self.head
        print(temp.data, end=" -> ")
        temp = temp.next

        while temp != self.head:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("(balik ke head)")

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        if not self.head:
            print("null")
            return

        temp = self.head
        while True:
            if temp.data == key:
                print(f"Elemen {key} ditemukan dalam Circular Linked List.")
                return

            temp = temp.next
            if temp == self.head:
                break

        print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

cll = CircularLinkedList()

data_input = input("Masukkan elemen ke dalam Circular Linked List: ")

if data_input.strip() == "":
    print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    angka_list = data_input.split(",")

    for angka in angka_list:
        cll.insert(int(angka.strip()))

key = int(input("Masukkan elemen yang ingin dicari: "))
cll.search(key)
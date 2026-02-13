class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def display(self):
        if not self.head:
            return "kosong"

        elements = []
        temp = self.head

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        return " -> ".join(elements) + " -> null"

    def merge(self, list2):

        if not self.head:
            self.head = list2.head
            return

        if not list2.head:
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = list2.head

ll1 = LinkedList()
ll2 = LinkedList()

# Input List 1
data1 = input("Masukkan elemen untuk Linked List 1: ")
if data1.strip() != "":
    for angka in data1.split(","):
        ll1.insert(int(angka.strip()))

# Input List 2
data2 = input("Masukkan elemen untuk Linked List 2: ")
if data2.strip() != "":
    for angka in data2.split(","):
        ll2.insert(int(angka.strip()))

# Tampilkan sebelum digabung
print("Linked List 1:", ll1.display())
print("Linked List 2:", ll2.display())

# Gabungkan
ll1.merge(ll2)

# Setelah digabung
print("Linked List setelah digabungkan:", ll1.display())
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

# menggunakan metode bubble sort
data.sort(reverse = True)

lima_tertinggi = data[:5]

print("5 skor kandidat yang lolos:", lima_tertinggi)
print("Jumlah kandidat yang lolos:", len(lima_tertinggi))

# menggunakan metode shell sort
data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

def shellSort(data):
    sublistcount = len(data)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(data, startposition, sublistcount)

        sublistcount = sublistcount // 2

def gapInsertionSort(data, start, gap):
    for i in range(start+gap, len(data), gap):

        currentvalue = data[i]
        position = i

        while position >= gap and data[position-gap] < currentvalue:  # descending
            data[position] = data[position-gap]
            position = position-gap

        data[position] = currentvalue

shellSort(data)

lima_tertinggi = data[:5]

print("5 skor kandidat yang lolos:", lima_tertinggi)
print("Jumlah kandidat yang lolos:", len(lima_tertinggi))
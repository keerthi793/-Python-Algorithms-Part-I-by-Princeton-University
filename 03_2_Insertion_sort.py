class Insertion:
    def __init__(self, a):
        self.a = a
        print(a)

    def sort(self):
        a = self.a
        for i in range(0, len(a)):
            for j in range(i, 0, -1):
                if a[j] < a[j-1]:
                    swap = a[j]
                    a[j] = a[j-1]
                    a[j-1] = swap
        print(a)
b = [7, 10, 5, 3, 8, 4, 2, 9, 6]
first = Insertion(b)
first.sort()
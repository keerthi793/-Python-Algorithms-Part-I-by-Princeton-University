class Insertion:
    def __init__(self, a):
        self.a = a
        print(a)

    def sort(self):
        a = self.a
        h = 1
        while h < (len(a)/3):
            h = 3*h + 1
        while h >= 1:
            for i in range(h, len(a)):
                j = i
                for j in range(i, 0, -h):
                    if (j >= h) and (a[j] < a[j - h]):
                        swap = a[j]
                        a[j] = a[j - h]
                        a[j - h] = swap
            h = int((h / 3))
        print(a)
b = [7, 10, 5, 3, 8, 4, 2, 9, 6, 1]
first = Insertion(b)
first.sort()
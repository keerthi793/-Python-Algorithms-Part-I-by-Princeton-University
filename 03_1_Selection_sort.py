class Selection:
    def __init__(self, a):
        self.a = a

    def sort(self):
        a = self.a
        for i in range(0, len(a)):
            for j in range(i + 1, len(a)):
                if a[j] < a[i]:
                    swap = a[j]
                    a[j] = a[i]
                    a[i] = swap

b = [1, 7, 5]
first = Selection(b)
first.sort()
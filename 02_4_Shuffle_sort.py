from random import randint


class Shuffle:
    
    def sort(self):
        for i in range(0, len(a)):
            r = randint(0, i)
            swap = a[i]
            a[i] = a[r]
            a[r] = swap
        print(a)


a = [1, 2, 3, 4, 5, 6]
print(a)
first = Shuffle()
first.sort()

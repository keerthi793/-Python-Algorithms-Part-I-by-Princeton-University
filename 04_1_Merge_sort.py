# Function to merge two arrays
def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c


# Code for merge sort
# Function to sort an array using merge sort algorithm

def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x) / 2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        print(a, b)
        print("Sorted list", merge(a, b))
        return merge(a, b)

#arr = [10, 6, 8, 5, 3, 1, 2, 4, 7, 9]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr = mergesort(arr)
print(arr)

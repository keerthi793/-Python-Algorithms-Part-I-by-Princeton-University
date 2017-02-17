def quick_sort(a):
    quick_sort_list(a, 0, len(a) - 1)


def quick_sort_list(a, first, last):
    if first < last:
        split_point = sort(a, first, last)
        quick_sort_list(a, first, split_point - 1)
        quick_sort_list(a, split_point + 1, last)


def sort(a, first, last):
    pivot_value = a[first]
    left = first + 1
    right = last
    value = True
    while value:
        while a[left] <= pivot_value and left <= right:
            left += 1
        while a[right] >= pivot_value and right >= left:
            right -= 1
        if left > right:
            value = False
        else:
            temp = a[left]
            a[left] = a[right]
            a[right] = temp
        temp = a[first]
        a[first] = a[right]
        a[right] = temp
        return right


l = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(l)
print(l)

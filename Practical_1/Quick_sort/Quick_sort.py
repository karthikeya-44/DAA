def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)


# Example
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original:", arr)
print("Sorted:", quick_sort(arr))
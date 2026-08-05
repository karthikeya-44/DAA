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


arr = list(map(int, input("Enter the elements separated by spaces: ").split()))

print("Original Array:", arr)
print("Sorted Array:", quick_sort(arr))
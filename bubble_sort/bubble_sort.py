def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Original list:", numbers)

bubble_sort(numbers)

print("Sorted list:", numbers)

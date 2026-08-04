def binary_search(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            low = mid + 1  
        else:
            high = mid - 1 
    return -1 


arr = [2, 4, 9, 15, 19, 20]
key = 18
ans = binary_search(arr, key)

if ans != -1:
    print(f"Element {key} found at index {ans}")
else:
    print(f"Element {key} not found in the array")

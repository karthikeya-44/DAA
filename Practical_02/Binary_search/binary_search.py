def binary_Search(arr,target):
    left,right = 0 ,len(arr) -1
    
    while left <= right:
        mid  =(left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return -1

numbers = list(map(int,input("Enter the values separated by commas: ").split()))
numbers.sort()
target =int(input("Enter the target element: "))

print("List: ",numbers)

result = binary_Search(numbers,target)

if result != -1:
    print(f"Element {target} is found at index {result}")
else:
    print(f"Element {target} is not found in the list.")
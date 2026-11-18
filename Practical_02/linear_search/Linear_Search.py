def linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
numbers=list(map(int,input("Enter the elements separated by spaces: ").split()))
target = int(input("Enter the number to reach: "))

print("List: ",numbers)

result = linear_Search(numbers,target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
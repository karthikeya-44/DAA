def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i - 1
        
        while j >=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1]= key

numbers = list(map(int,input("Enter the numbers separating by commas: ").split()))

print("Original list: ",numbers)

insertion_sort(numbers)

print("Sorted_list: ",numbers)
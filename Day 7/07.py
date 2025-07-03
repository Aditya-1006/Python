arr1 = int(input("Enter Your Values: "))
arr2 = int(input("Enter Your Values: "))
arr3 = int(input("Enter Your Values: "))
arr4 = int(input("Enter Your Values: "))
arr5 = int(input("Enter Your Values: "))
arr6 = int(input("Enter Your Values: "))

arr = [arr1, arr2, arr3, arr4, arr5, arr6]
size = len(arr)
print(f"Given Array is : {arr}")

def reverse(arr, size):

    start = 0
    end = size - 1

    while start <= end :
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1

def printArray(arr):

    for i in range(len(arr)):
        print(arr[i], end="")


reverse(arr, size)
printArray(f"The Reversed Array is: {arr}")


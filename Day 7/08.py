arr=[1,2,3,4,5,6]
size=len(arr)

def reverse(arr, size):

    start = 0
    end = size-1

    while start <= end:
        temp = arr [start]
        arr [start] = arr [end]
        arr[end] = temp
        start = start + 1
        end = end - 1

def printArray(arr):

    for i in range(len(arr)):
        print(arr[i], end=" ")

printArray(arr)
reverse(arr, size)
print("\n")
printArray(arr)
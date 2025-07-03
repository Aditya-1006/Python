arr1 = int(input("Enter Your Values; "))
arr2 = int(input("Enter Your Values; "))
arr3 = int(input("Enter Your Values; "))
arr4 = int(input("Enter Your Values; "))
arr5 = int(input("Enter Your Values; "))
arr6 = int(input("Enter Your Values; "))
element = int(input("Enter Element = "))

arr = [arr1, arr2, arr3, arr4, arr5, arr6]


size = len(arr)

def binarySearch(arr, element):

    start = 0
    end = size - 1

    while start <= end:

        mid = (start + end ) / 2
        mid = int(mid)

        if arr[mid] == element:
            return mid 
        
        elif arr[mid] < element:
            start = mid + 1
        
        else:
            end = mid -1   
    return -1

result = binarySearch(arr, element)
print(f"The Element {element} is Present at Index = {result}")


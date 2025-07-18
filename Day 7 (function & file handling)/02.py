arr1 = int(input("Enter Your Values: "))
arr2 = int(input("Enter Your Values: "))
arr3 = int(input("Enter Your Values: "))
arr4 = int(input("Enter Your Values: "))
arr5 = int(input("Enter Your Values: "))
arr6 = int(input("Enter Your Values: "))

arr = [arr1, arr2, arr3, arr4, arr5, arr6]
print(f"Input Array: {arr}")

arr.sort()
print(f"Sorted Array: {arr}")

element = int(input("Enter Element = "))

def linearSearch (arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return -1

result = linearSearch (arr, element)
print(f"The Element {element} is Present at Index {result}")



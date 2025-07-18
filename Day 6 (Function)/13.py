arr = [1,4,7,8,5,2,3,6,9]
element = 44

def linearSearch(arr, element):

    for i in arr:
        if arr[i] == element:
            return i 
    return -1


result = linearSearch(arr, element)

print(f"The Element {element} is found at index = {result}")
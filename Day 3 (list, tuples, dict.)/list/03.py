list1=[1,4,7,8,5,2,3,6,9]
list2=[11,12,13,14,22,54,17,95,88]
list1.append(10)
print("Appended list: ",list1)
list1.extend(list2)
print("Extended list: ",list1)
list1.sort()
print("Sorted list: ",list1)
print("Length of List: ", len(list1))
list1.reverse()
print("Reversed: ",list1)
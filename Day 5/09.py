num = int(input("Enter a Number: "))

print("The Table Is : ")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

print("The Square Is : ")
for i in range(1, 11):
    print(f"{num} ^ {i} = {num**i}")


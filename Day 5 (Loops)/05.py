num=int(input("Enter a Number: "))

count = 0
for i in range(1, num+1):
    if i % 2  == 0:
        count += i

print(f"The Sum = {count}")

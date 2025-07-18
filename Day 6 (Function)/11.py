n = int(input("Enter a Number: "))
temp = n
rev = 0

while n!=0:
    digit = n%10
    rev = rev*10 + digit
    n = n // 10 
print(rev)

if temp == rev:
    print("Number is Palindrome!")
else:
    print("Number is NOT Palindrome!")
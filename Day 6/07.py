# def fibo(n):

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo (n-1) + fibo (n-2)

# def main():
#     n= int(input("Enter You Value: "))
#     result = fibo(n)
#     print(f"The Fibonacci Series of {n} = {result}")

# main()


def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo (n-1) + fibo (n-2)
    
def main():
    n = int(input("Enter the value : "))
    print("Fibonacci Series : ")
    for i in range(n):
        print(fibo(i),end=" ")
main()
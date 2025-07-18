def factorial(n):

    if n == 0:
        return 1
    elif n==1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n= int(input("Enter You Value: "))
    result = factorial(n)
    print(f"The Factorial of {n} = {result}")

main()




'''

    0 1 1 2 3 5 8 13 21 34 55 89


    fibo(n - 1) + fibo(n - 2)

    0 -> 0

    1 -> 1


'''
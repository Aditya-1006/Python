def factorial(n):

    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
def main():
    n = int(input("Enter Your Value: "))
    result = factorial(n)
    print(f"The Factorial of {n} is = {result}")


if __name__=='__main__':
    main()

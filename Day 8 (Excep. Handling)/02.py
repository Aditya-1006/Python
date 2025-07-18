while True:
    n = int(input("Enter a number: "))

    try:
        if n/0:
            print("You can't divide by Zero!")
    except ZeroDivisionError as e:
        print(f"Error - {e}")
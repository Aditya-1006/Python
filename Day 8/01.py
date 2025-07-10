while True:
    a = (input("Enter Your VALUE: "))

    if a == 'q':
        break


    try:
        a = int(a)

        if a > 5:
            print("Greater")

    except Exception as e:
        print(f"Error - {e}")

print("Thanks for playing this game!")

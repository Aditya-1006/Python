def authenticate(pw):
     
     if pw == 1234:
        return ("login")
     else:
        return ("invalid!")


def main():
    pw = int(input("Enter your password: "))
    result=authenticate(pw)
    print(result)

main()
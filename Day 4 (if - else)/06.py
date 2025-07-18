message = input("Enter Your message: ").lower()


if 'make a lot of money' in message:
    spam = True

elif 'join now' in message:
    spam = True

elif 'pankaj' in message:
    spam = True

else:
    spam = False


if spam:
    print("This is a Spam text")
else:
    print("This is not a spam text")
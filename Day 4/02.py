marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

avg=(marks1 + marks2 + marks3)/ 3

if marks1>35 and marks2>35 and marks3>35 :

    if avg>40:
        print("Pass")
    else:
        print("Fail due Less Average")

else:
    print("Fail due to less Marks")
def marks(num):
    if num<50 and num>=0:
        print("Poor Performance!!")
    elif num>=50 and num<=60:
        print("Need Improvement!!")
    elif num>60 and num<=70:
        print("Better!!")
    elif num>70 and num<=80:
        print("Average!!")
    elif num>80 and num<=90:
        print("Good!!")
    elif num>90 and num<=100:
        print("Excellent!!")
    elif num>100:
        print("Invalid Marks!")
    return (num)

def main():
    num = int(input("Enter your marks: "))
    result= marks(num)

main()
main()
main()

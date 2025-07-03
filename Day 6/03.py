p = float(input("Enter Principle Value: "))
r = float(input("Enter Rate Value: "))
t = float(input("Enter Time: "))

def simpleIntrest(p, r, t):
    return (p*r*t)/100

result = simpleIntrest(p, r, t)
print(f"The Answer is : {result}")

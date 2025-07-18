class Calculate:

    def getSum(self, *args):
        return sum(args)
    
c1 = Calculate()
print(c1.getSum(10,20,30,40,50,60,70))
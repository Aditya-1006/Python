t = (1,2,3)

t=list(t)      #tuples are immutable (cannot be changed) that's why type error
t[0] = 100     #to add a value.... change the tuple into list
t=tuple(t)     #again convert to tuple
 

print(type(t))
print(t)
f = open("hiii.txt", "w")
data = f.write("New Text File 2")

for i in range(5):
    f = open("hiii.txt", "r")
    data = f.read()
    print(data)


f.close()
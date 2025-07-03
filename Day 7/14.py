for i in range(1,6):
    f = open(f"data/sample_{i}.txt", "w")
    data = f.write("Hello")
    f.close()
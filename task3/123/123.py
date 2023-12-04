with open("output.txt", "w") as i:
    for j in range(100, 0, -1):
        i.write(str(j))
        i.write(" ")
import random

n = 1000  # Maximum value
numbers = random.sample(range(1, n+1), 1000)
line = ' '.join(map(str, numbers))

filename = "output.txt"  # Specify the filename
with open(filename, "w") as output_file:
    output_file.write(line)

print("Numbers written to", filename)
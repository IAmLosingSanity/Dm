import random

n = 100  # Maximum value
numbers = random.sample(range(1, n+1), 100)
line = ' '.join(map(str, numbers))

filename = "output.txt"  # Specify the filename
with open(filename, "w") as output_file:
    output_file.write(line)

print("Numbers written to", filename)
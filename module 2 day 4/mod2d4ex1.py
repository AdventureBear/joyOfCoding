file_name = "turing.txt"

dataFile = open(file_name, "r")

turing_lines = []
next_line = dataFile.readline()

while next_line != "":
    turing_lines.append(next_line)
    next_line = dataFile.readline()

dataFile.close()

print(turing_lines)
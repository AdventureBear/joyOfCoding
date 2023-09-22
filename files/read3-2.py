# Create a program similar to above that counts the number of words in the files as well.
# After printing out information about each file, this program should also print the total
# number of lines & words in all 3 files. You can use the string split function to split a line
# of input into a list of words by splitting the line on spaces.

file_name = "counts.txt"
writeFile = open(file_name, "w")

file_names = ["text1.txt", "text2.txt", "text3.txt"]
all_words = 0
all_lines = 0

for file in file_names:
    dataFile = open(file, "r")

    count_lines = 0
    total_words = 0

    line = dataFile.readline()

    while line != "":
        print(line)
        new_words = len(line.split(" "))
        print(new_words)
        total_words += new_words
        print(total_words)
        count_lines += 1
        print(count_lines)
        line = dataFile.readline()

    print(file, ":", count_lines, "lines", total_words, " words.", file=writeFile)
    all_lines += count_lines
    all_words += total_words
    dataFile.close()

print("TOTAL: ", all_lines, " lines, ", all_words, " words.", file=writeFile)

writeFile.close()

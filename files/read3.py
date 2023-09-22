# Write a python program that reads 3 files called test1.txt, text2.txt, and text3.txt, counts
# the number of lines in each file, and prints out the number of lines to a file counts.txt
# Output file counts.txt created with the following contents:
# text1.txt : 4
# text2.txt : 3
# text3.txt : 2

file_name = "counts.txt"
writeFile = open(file_name, "w")

file_names = ["text1.txt", "text2.txt", "text3.txt"]
for file in file_names:
    dataFile = open(file, "r")
    count = 0
    while dataFile.readline() != "":
        count += 1
    print(file, ":", count, file=writeFile)
    dataFile.close()


writeFile.close()

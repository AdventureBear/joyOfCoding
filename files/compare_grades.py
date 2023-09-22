# Write a program that reads in the csv file linked above and outputs the mean,
# median, and standard deviation for the fall & spring semesters.
# Make sure to write at least two functions in your final solution.
# The more generalizable you make your code, the more you may be able to reuse it for your own project later.
# To receive feedback, please submit a screenshot of your program & its output.

# def get_mean(list):
#     return mean(list)
#
# def get_mode(list)
#     return mode(list)
#
# def get_SD(list)
#     return sd(list)

import statistics

file_name = "sample_grades.csv"
dataFile = open(file_name, "r")
outFileName = "compare.txt"
outFile = open(outFileName, "w")
# fall_mean = 0
# spring_mean = 0
# fall_mode = 0
# spring_mode = 0
# sd_fall = 0
# sd_spring = 0


def main():
    stud_data=dataFile.readline()
    fall_grades = []
    spring_grades = []

    while stud_data != "":
        data_parse = stud_data.split(",")
        if data_parse[1] == "Fall 2016":
            fall_grades.append(int(data_parse[2]))
        else:
            spring_grades.append(int(data_parse[2]))
        stud_data = dataFile.readline()

    print("Fall: ", fall_grades)
    print("Spring: ", spring_grades)

    print("", "Fall 2016", "Spring 2016", file=outFile)
    print("Mean: ",  "{:.2f}".format(statistics.mean(fall_grades)) , "{:.2f}".format(statistics.mean(spring_grades)), file=outFile)
    print("Mode: ", statistics.mode(fall_grades), statistics.mode(spring_grades), file=outFile)
    print("SD: ", "{:.2f}".format(statistics.stdev(fall_grades)), "{:.2f}".format(statistics.stdev(spring_grades)), file=outFile)


main()
dataFile.close()
outFile.close()






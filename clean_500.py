import sys
f = open("SP500.csv", "r")
file_f = open("clean_500.csv", "a")
i = 1

for lines in f:
    if i == 1:
        i+=1
    else:
        lines = lines.split(",")
        file_f.write(lines[1])
        file_f.write("\n")
file_f.close()
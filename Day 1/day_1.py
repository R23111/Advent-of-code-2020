f = open("./input.txt", 'r')

temp = f.readlines()
report = []

for i in range(len(temp)):
    report.append(int(temp[i].replace("\n", '')))

f.close()

for i in range(len(report)):
    for j in range(i+1, len(report)):
        if(report[i] + report[j] == 2020):
            print(f"part 1: {report[i] * report[j]}")   #As i*j gives the same result as j*i, we can start the check at the last i index
        for k in range(j+1, len(report)):
            if(report[i] + report[j] + report[k] == 2020):
                print(f"part 2: {report[i] * report[j] * report[k]}")

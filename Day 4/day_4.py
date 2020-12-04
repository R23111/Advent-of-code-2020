f = open("./input.txt")
file = f.read()
f.close()
input = []
valid_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

valid_count_pt1 = 0
valid_count_pt2 = 0

file = file.split("\n\n")

# Filter file + Part 1 solution
for f in file:
    count = 0

    f = f.replace('\n', ' ')
    f = f.split(' ')
    for i in range(len(f)):
        f[i] = f[i].split(':')

    for i in f:
        for vf in valid_fields:
            if(i[0] == vf):
                count += 1

    if(count == 7):
        valid_count_pt1 += 1

    input.append(f)


# Part 2 Solution

valid_hcl = set("0123456789abcdef")
valid_ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

for ln in input:
    count = 0
    for l in ln:
        if(l[0] == 'byr'):
            if(int(l[1]) >= 1920 and int(l[1]) <= 2002):
                count += 1
        elif(l[0] == 'iyr'):
            if(int(l[1]) >= 2010 and int(l[1]) <= 2020):
                count += 1
        elif(l[0] == 'eyr'):
            if(int(l[1]) >= 2020 and int(l[1]) <= 2030):
                count += 1
        elif(l[0] == 'hgt'):
            if('cm' in l[1]):
                hgt = int(l[1].replace('cm', ''))
                if(hgt >= 150 and hgt <= 193):
                    count += 1
            elif('in' in l[1]):
                hgt = int(l[1].replace('in', ''))
                if(hgt >= 59 and hgt <= 76):
                    count += 1
        elif(l[0] == 'hcl'):
            if(len(l[1]) == 7):
                if(l[1][0] == '#'):
                    if(any((c in valid_hcl) for c in l[1][1:])):
                        count += 1
        elif(l[0] == 'ecl'):
            if(l[1] in valid_ecl):
                count += 1
        elif(l[0] == 'pid'):
            if(len(l[1]) == 9):
                count += 1

    if(count == 7):
        valid_count_pt2 += 1

print(f"Part 1: {valid_count_pt1}\nPart 2: {valid_count_pt2}")

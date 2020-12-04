f = open("./input.txt", 'r')

file = f.readlines()

valid_passwords_part1 = 0
valid_passwords_part2 = 0

for i in range(len(file)):
    file[i] = file[i].replace("\n", '')
    temp = file[i].split('-')
    temp1 = temp[1].split(' ')
    p = [temp[0], temp1[0], temp1[1].replace(':', ''), temp1[2]]

    repetitions = 0

    # part 1: count the number of repetitions of the letter (p[2]) on the password (p[3]),
    # and check if it pass the requirements (p[0] <= n <= p[1])
    for l in p[3]:
        if(l == p[2]):
            repetitions += 1
    if repetitions >= int(p[0]) and repetitions <= int(p[1]):
        valid_passwords_part1 += 1

    # part 2: check if the letter is on (only) one of the indices -1 (XOR operation)
    if(bool(p[3][int(p[0]) - 1] == p[2]) ^ bool(p[3][int(p[1]) - 1] == p[2])):
        valid_passwords_part2 += 1

f.close()

print(f"part 1: {valid_passwords_part1} \npart 2: {valid_passwords_part2}")

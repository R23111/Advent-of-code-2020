f = open("./input.txt", 'r')
map = f.readlines()
f.close()

x = [0, 0, 0, 0, 0]         # x position of the toboggan
add = [1, 3, 5, 7, 1]       # The slope (on x)
trees = [0, 0, 0, 0, 0]     # Counter of trees

for i in range(1, len(map)):
    map[i] = map[i].replace("\n", '')
    for j in range(len(add)):
        if(i % 2 == 0 or j != 4):   # on the last slope, the toboggan goes 2 down at time, so if it's on an odd y, skip
            x[j] = (x[j] + add[j]) % (len(map[i]))
            if(map[i][x[j]] == '#'):
                trees[j] += 1

mul = 1
for t in trees:
    mul *= t

print(f"Part 1: {trees[1]}\nPart 2: {mul}")

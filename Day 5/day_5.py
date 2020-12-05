f = open("./input.txt")
file = f.readlines()
f.close()


def get_row(input):
    max = 127
    min = 0
    for c in input:
        if(c == 'F'):
            max = int((min + max) / 2)
        elif(c == 'B'):
            min = int((min + max) / 2) + 1
        else:
            break
    return max


def get_column(input):
    max = 7
    min = 0
    for c in input:
        if(c == 'L'):
            max = int((min + max) / 2)
        elif(c == 'R'):
            min = int((min + max) / 2) + 1
        else:
            continue
    return max


ids = []

max = 0

for ticket in file:
    row = get_row(ticket)
    column = get_column(ticket)
    id = row * 8 + column
    if(id > max):
        max = id
    ids.append(id)

my_id = 0

for id1 in ids:
    has_next = False
    has_previous = False
    for id2 in ids:
        if id1 + 1 == id2:
            has_next = True
    if(not has_next and id1 != max):
        my_id = id1 + 1

print(f"Part 1: {max}\nPart 2: {my_id}")

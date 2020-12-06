file = open("./input.txt").read().strip().split("\n\n")
questions = "abcdefghijklmnopqrstuvwxyz"
count_pt1, count_pt2 = 0, 0
print("Part 1: " + str(sum(len(set.union(*map(set, x.split("\n")))) for x in file)))
print("Part 2: " + str(sum(len(set.intersection(*map(set, x.split("\n")))) for x in file)))

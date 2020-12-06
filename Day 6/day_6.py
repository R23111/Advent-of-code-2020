file = open("./input.txt").read().strip().split("\n\n")
questions = "abcdefghijklmnopqrstuvwxyz"
count_pt1, count_pt2 = 0, 0

for cust in file:
    temp = cust.split("\n")
    count_pt2 += len(set.intersection(*map(set, temp)))
    count_pt1 += len(set.union(*map(set, temp)))
    
print(sum(len(set.intersection(*map(set, x.split("\n")))) for x in file))

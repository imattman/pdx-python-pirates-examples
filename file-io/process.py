#!/usr/bin/env python3

with open("scores.txt") as score_file:
    lines = score_file.readlines()

total = 0
count = 0
for line in lines:
    line = line.strip()

    # skip empty lines
    if not line:
        continue

    # split on whitespace and unpack
    student, score = line.split()
    score = int(score)
    total += score
    count += 1

avg = total  / count

print("scores:", count)
print("average:", avg)

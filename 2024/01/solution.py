from collections import defaultdict

with open("input.txt", "r") as f:
    input = f.readlines()

left = sorted([int(i[:5]) for i in input])
right = sorted([int(i[5:].strip()) for i in input])

number_of_pairs = len(left)

sum_of_distances = 0
for i in range(number_of_pairs):
    sum_of_distances += abs(left[i]-right[i])

print(f"Part 1: {sum_of_distances}")

left_counts = defaultdict(int)
right_counts = defaultdict(int)


for i in range(number_of_pairs):
    if i in left_counts: left_counts[i] += 1
    else: left_counts[i] = 1
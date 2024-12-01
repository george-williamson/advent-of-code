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

right_counts = defaultdict(int)

for i in range(number_of_pairs):
    if right[i] in right_counts: right_counts[right[i]] +=1
    else: right_counts[right[i]] = 1

similarity_score = 0
for i in range(len(left)):
    if left[i] in right_counts: 
        similarity_score += (left[i]*(right_counts[left[i]]))

print(f"Part 2: {similarity_score}")
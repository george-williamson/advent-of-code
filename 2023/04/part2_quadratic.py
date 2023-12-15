import math

def advent_of_code_2023_day_6_puzzle_2(puzzle_input: str) -> int:
    times, distances = puzzle_input.strip().split("\n")
    time = int(times.split(":")[1].replace(" ", ""))
    distance = int(distances.split(":")[1].replace(" ", ""))
    # Roots of quadratic b^2 - bt + d = 0
    b1 = time + math.sqrt(time**2-4*1*distance)/2
    b2 = time - math.sqrt(time**2-4*1*distance)/2

    return math.floor(max(b1,b2)) - math.ceil(min(b1, b2))
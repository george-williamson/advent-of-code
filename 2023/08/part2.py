import math

def advent_of_code_2023_day8_puzzle1(puzzle_input: str) -> int:

    instructions, maps = puzzle_input.strip().split("\n\n")
    maps = [i.split(" = ") for i in maps.split("\n")]
    maps = {j[0]:j[1][1:-1].split(", ") for j in maps}

    starts = [i for i in maps if i[-1] == 'A']
    values = [0 for _ in range(len(starts))]

    for i, start in enumerate(starts):
        counter = 0
        current_node = start
        while values[i] == 0:
            for instruction in instructions:
                counter +=1
                if instruction == "L": 
                    current_node = maps[current_node][0] 
                else:
                    current_node = maps[current_node][1]
                if current_node.endswith("Z"):
                    values[i] = counter
                    print(current_node)
                    break
    
    return math.lcm(*values)
        
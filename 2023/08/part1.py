def advent_of_code_2023_day8_puzzle1(puzzle_input: str) -> int:

    instructions, maps = puzzle_input.strip().split("\n\n")
    maps = [i.split(" = ") for i in maps.split("\n")]
    maps = {j[0]:j[1][1:-1].split(", ") for j in maps}

    current_node = 'AAA'
    end_node = 'ZZZ'
    traversal_count = 0
    while current_node != end_node:
        for instruction in instructions:
            traversal_count += 1
            if instruction == 'L':
                current_node = maps[current_node][0]
            else:
                current_node = maps[current_node][1]
            if current_node == end_node:
                return traversal_count
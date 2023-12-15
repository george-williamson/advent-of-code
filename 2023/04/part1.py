def advent_of_code_2023_day_4_puzzle_1(puzzle_input: str) -> int:
    lines = [i.split(": ")[1] for i in puzzle_input.strip().split("\n")]
    total_points = 0
    for line in lines:
        card, winning_numbers = line.split(" | ")
        card = set(card.split())
        winning_numbers = set(winning_numbers.split())
        n = 0
        for wn in winning_numbers:
            if wn in card:
                if n == 0:
                    n += 1
                else:
                    n *= 2
        total_points += n
    return total_points
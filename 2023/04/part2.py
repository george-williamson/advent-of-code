def advent_of_code_2023_day_4_puzzle_2(puzzle_input: str) -> int:
    lines = [i.split(": ")[1] for i in puzzle_input.strip().split("\n")]
    cards_won = 0
    card_totals = [1 for _ in lines]
    for i, line in enumerate(lines):
        card, winning_numbers = line.split(" | ")
        card = set(card.split())
        winning_numbers = set(winning_numbers.split())
        n = 0
        for wn in winning_numbers:
            if wn in card:
                n+=1
        for j in range(i+1, i+n+1):
            card_totals[j] += card_totals[i]
        cards_won += card_totals[i]  
    return cards_won
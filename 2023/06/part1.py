def advent_of_code_2023_day_6_puzzle_1(puzzle_input: str) -> int:
    times, distances = puzzle_input.strip().split("\n")
    races = list(zip(list(map(int, times.split()[1:])), list(map(int, distances.split()[1:]))))

    product = 1
    
    for time, distance in races:
        speed = 0
        time_remaining = time
        beat_record_counter = 0
        while time_remaining > 0:
            if speed * time_remaining > distance:
                beat_record_counter += 1
            time_remaining -= 1
            speed += 1
        product *= beat_record_counter
    return product

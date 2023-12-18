def advent_of_code_day_9_puzzle_2(puzzle_input: str) -> int:
    histories = [list(map(int, line.split())) for line in puzzle_input.strip().split("\n")]
    extrapolated_sum = 0
    for history in histories:
        tracker = [history]
        current_level = history
        differences = []
        while differences != [0] * len(current_level):
            differences = [-1] * (len(current_level)-1)
            for i in range(len(differences)):
                 differences[i] = current_level[i+1] - current_level[i]
            tracker.append(differences)
            current_level = differences

        extrapolated = 0
        for d in reversed(tracker):
            extrapolated = d[0] - extrapolated
        extrapolated_sum += extrapolated

    return extrapolated_sum
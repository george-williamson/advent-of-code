with open("input.txt", "r") as f:
	input = f.readlines()
    
reports = [list(map(int, i.strip().split())) for i in input]

count = 0
for r in reports:
    count += 1
    skipped = False
    increasing = None
    # Starting condition
    if 1 <= r[1] - r[0] <= 3: 
       increasing = True
    elif -3 <= r[1] - r[0] <= -1:
       increasing = False
    else:
       skipped = True
        
    # Check if sequence is increasing or not
    for l in range(2, len(r)):
        delta = r[l] - r[l-1]
        
        if increasing is None:
            if 1 <= delta <= 3: 
                increasing = True
            elif -3 <= delta <= -1:
                increasing = False
            else:
                count -= 1
                break
        
		# Continue as in part 1
        if ((1 <= delta <= 3) and increasing) or ((-3 <= delta <= -1) and not increasing):
           continue
        else:
            # Provide an additional chance if we haven't skipped a number previously
            if skipped:
                count -= 1
                break
            else:
                 skipped = True
                 continue 
        
print(f"Part 2: {count}")
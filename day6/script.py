
# test input

# time = [7,15,30]
# distance = [9,40,200]


# part 1 input

# time = [59, 70, 78, 78]
# distance = [430, 1218, 1213, 1276]


#part 2 input
time = [59707878]
distance = [430121812131276]

def num_of_wins(time, distance):
    wins = 0
    time_holding_button = 1

    while time_holding_button < time:
        remaining_time = time - time_holding_button
        travel_distance = remaining_time * time_holding_button
        if travel_distance > distance:
            wins += 1
        time_holding_button += 1
    return wins

def num_of_win_combinations():
    win_total = 1
    for i in range(len(time)):
        win_total *= num_of_wins(time[i],distance[i])
    print(win_total)

num_of_win_combinations()
"""

def scanmap(arr[[],[],...,[]] map, int value)
    for line in map:
        if (value >= source) and (value < (source + offset)):
            return destination + (value - source)
    return value

locations = []    

for each seed:
    x = scanmap(first_map, seed)
    x = scanmap(second_map, x)
    ...
    locations.add(x)

    
print(minimum(locations))

"""

# TEST INPUT

# seed_to_soil = [[50, 98, 2],[52,50,48]]
# soil_to_fertilizer = [[0,15,37],[37,52,2],[39,0,15]]
# fertilizer_to_water = [[49,53,8],[0,11,42],[42,0,7],[57,7,4]]
# water_to_light = [[88,16,7],[18,25,70]]
# light_to_temperature = [[45,77,23],[81,45,19],[68,64,13]]
# temperature_to_humidity = [[0,69,1],[1,0,69]]
# humidity_to_location = [[60,56,37],[56,93,4]]

# maps = [seed_to_soil,
#         soil_to_fertilizer,
#         fertilizer_to_water,
#         water_to_light,
#         light_to_temperature,
#         temperature_to_humidity,
#         humidity_to_location]

# seeds = [79,14,55,13]

# returns new int based on map


import re
p_map = re.compile('map')

maps = []
with open('test_input.txt') as f:
    is_block = False
    maps_index = -1
    for line in f:
        if line[:5] == "seeds":
            seeds = line.split(': ')[1].split()
        elif p_map.search(line):
            is_block = True
            maps.append([])
        elif line == "\n":
            maps_index += 1
            is_block = False
        elif is_block:
            maps[maps_index].append(line.split())

def scanmap(map, value):
    value = int(value)
    for line in map:
        destination = int(line[0])
        source = int(line[1])
        range = int(line[2])
        if (value >= source) and (value < (source + range)):
            return destination + (value - source)
    return value

def scanseed(seed):
    for i in range(len(maps)):
        seed = scanmap(maps[i], seed)
    return seed


def checkseeds(seed, rng):
    low = -1
    for i in range(rng):
        result = scanseed(int(seed) + i)
        if low < 0:
            low = result
        elif result < low:
            low = result
        print(low, i, rng)
    return low


i = 0
lowest = -1
while i < len(seeds):
    result = checkseeds(int(seeds[i]), int(seeds[i+1]))

    if lowest < 0:
        lowest = result
    if result < lowest:
        lowest = result
    print(lowest)
    i += 2


# for j in range(len(maps)): #iterating through maps

#         x = scanmap(maps[i])
#         results[j+1].append(scanmap(maps[j],results[j][i]))



# for j in range(len(maps)): #iterating through maps

#     results.append([]) # add space for results
    
#     for i in range(len(seeds)): #iterate through values
#         results[j+1].append(scanmap(maps[j],results[j][i]))

#part 1
#print(min(results[len(results) - 1]))



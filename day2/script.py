

def part1():
    total_red = 12
    total_blue = 14
    total_green = 13

    sum = 0

    with open('input.txt') as file:
        for line in file:
            line = line.split('\n')[0]

            line = line.split(": ")
            game_number = line[0][5:]

            sets = line[1].split("; ")
            possible = True

            for set in sets:
                set = set.split(', ')
                
                for cube in set:
                    cube = cube.split(" ")
                    if ((cube[1] == "red" and int(cube[0]) > total_red) or
                        (cube[1] == "blue" and int(cube[0]) > total_blue) or
                        (cube[1] == "green" and int(cube[0]) > total_green)):
                            possible = False
            
            if possible:
                 sum += int(game_number)
                 
    print(sum)


def part2():
     

    sum_of_powers = 0

    with open('input.txt') as file:
        for line in file:
               
            minimum_red = 0
            minimum_blue = 0
            minimum_green = 0

            line = line.split('\n')[0]
            line = line.split(': ')[1]
            sets = line.split('; ')

            for set in sets:
                set = set.split(', ')

                for cube in set:
                    cube = cube.split(" ")
                    if cube[1] == "red" and int(cube[0]) > minimum_red:
                        minimum_red = int(cube[0])
                    elif cube[1] == "blue" and int(cube[0]) > minimum_blue:
                        minimum_blue = int(cube[0])
                    elif cube[1] == "green" and int(cube[0]) > minimum_green:
                        minimum_green = int(cube[0])
            
            sum_of_powers += (minimum_red * minimum_blue * minimum_green)
        
        print(sum_of_powers)
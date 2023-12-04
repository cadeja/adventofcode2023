import re
star_pattern = re.compile('[*]')
num_pattern = re.compile('[0-9]+')


file = open('input.txt')
alist = file.read().splitlines()


def find_first_star(line):
    return star_pattern.search(line).span()[0]


def remove_star(line, index):
    return line[:index] + '.' + line[index + 1:]


def get_full_number(line, index):
    # given an index with a digit, returns full connected number
    
    first_locked = False
    last_locked = False

    first_index = index
    last_index = index
    number = line[index]

    while (not first_locked) and (first_index > 0):
        if line[first_index - 1] in '0123456789':
            number = line[first_index - 1] + number
            first_index -= 1
        else:
            first_locked = True

    while (not last_locked) and (last_index < len(line) - 1):
        if line[last_index + 1] in '0123456789':
            number = number + line[last_index + 1]
            last_index += 1
        else:
            last_locked = True

    return int(number)



def check_for_numbers(line, first_index, last_index):
    # returns numbers found in line (in an array)

    substring = line[first_index:last_index+1]
    numbers = num_pattern.findall(substring)

    if len(numbers) == 2:
        return [get_full_number(line, first_index), get_full_number(line, last_index + 1)]
    elif len(numbers) == 1:
        number_index = first_index + num_pattern.search(substring).span()[0]
        return [get_full_number(line, number_index)]
    else:
        return []
    


def check_line(alist, i, star_index):
    #assigning left and right indices, checking if against edge
    if star_index != 0:
        first_index = star_index - 1
    else:
        first_index = star_index

    if star_index < (len(alist[i]) - 1):
        last_index = star_index + 1
    else:
        last_index = star_index

    
    numbers = []

    if i > 0:
        result = check_for_numbers(alist[i-1], first_index, last_index)
        if bool(result):
            numbers += result
    if i < len(alist) - 1:
        result = check_for_numbers(alist[i+1], first_index, last_index)
        if bool(result):
            numbers += result
    

    result = check_for_numbers(alist[i], first_index, last_index)
    if bool(result):
        numbers += result

    return numbers


def part2():
    sum = 0
    i = 0
    for i in range(len(alist)):
        line = alist[i]
        while star_pattern.search(line) != None:

            star_index = find_first_star(line)

            result = check_line(alist, i, star_index)

            if len(result) == 2:
                sum += (result[0] * result[1])
            line = remove_star(line, star_index)

        i += 1
    print(sum)


part2()
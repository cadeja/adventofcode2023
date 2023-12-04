import re
pattern = re.compile("[0-9]+")
symbol_pattern= re.compile("[^a-z0-9.]")

file = open('input.txt')
alist = file.read().splitlines()


def find_first_number(line):
    return pattern.search(line).span()


def remove_first_number(line, num_span):
    return line[:num_span[0]] + ('.' * (num_span[1] - num_span[0])) + line[num_span[1]:]

def check_for_symbol(line, first_index, last_index):
    substring = line[first_index:last_index]
    return bool(symbol_pattern.search(substring))




def check_line(alist, i, num_span):
    

    #assigning left and right indices, checking if against edge
    if num_span[0] != 0:
        first_index = num_span[0] - 1
    else:
        first_index = num_span[0]
    if num_span[1] < (len(alist[i]) - 1):
        last_index = num_span[1] + 1
    else:
        last_index = num_span[1]
    
    if i > 0:
        if check_for_symbol(alist[i-1], first_index, last_index):
            return True
    if i < len(alist) - 1:
        if check_for_symbol(alist[i+1], first_index, last_index):
            return True
    
    return check_for_symbol(alist[i], first_index, last_index)


def part1():
    sum = 0
    i = 0
    for i in range(len(alist)):
        line = alist[i]
        while pattern.search(line) != None:

            number = pattern.search(line)
            num_span = number.span()

            if check_line(alist, i, num_span):
                
                sum += int(line[num_span[0]:num_span[1]])
            line = remove_first_number(line, num_span)

        i += 1

part1()
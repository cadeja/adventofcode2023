import re
p = re.compile('one|two|three|four|five|six|seven|eight|nine|zero|1|2|3|4|5|6|7|8|9|0', re.IGNORECASE)


def string_to_number(s):
    match s:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'
        case _:
            return s
        

def last_number(s):
    line_length = len(s)

    if line_length <= 0: return 0

    i = 1
    while i < line_length + 1:
        if p.search(s[-i:]) != None:
            return p.search(s[-i:]).group()
        i += 1
        
with open('../input.txt') as file:

    sum = 0

    for line in file:

        first = p.search(line).group()
        last = last_number(line)

        digits = string_to_number(first) + string_to_number(last)
        sum += int(digits)



print(sum)
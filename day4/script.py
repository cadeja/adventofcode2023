file = open('input.txt')
lines = file.read().splitlines()

def part1():
    sum = 0
    for line in lines:
        line = line.split(': ')[1] # removes card number
        line = line.split(' | ')

        winning_numbers = set(line[0].split())
        chosen_numbers = set(line[1].split())
        matches = winning_numbers & chosen_numbers
        
        if len(matches) > 0:
            sum += 2**(len(matches) - 1)
    print(sum)


def part2():
    num_of_cards = len(lines)
    card_instances = [1] * num_of_cards
    
    for i in range(num_of_cards):
        line = lines[i]

        line = line.split(': ')[1] # removes card number
        line = line.split(' | ')

        winning_numbers = set(line[0].split())
        chosen_numbers = set(line[1].split())
        num_of_matches = len(winning_numbers & chosen_numbers)

        for j in range(num_of_matches):
            try:
                card_instances[i+j+1] += card_instances[i]
            except:
                break
    print(sum(card_instances))

part2()
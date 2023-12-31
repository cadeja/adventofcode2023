
hands = []

with open('input.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        hands.append(line.split(' '))


hand_types = {
    "five of a kind" : 6,
    "four of a kind" : 5,
    "full house" : 4,
    "three of a kind" : 3,
    "two pair" : 2,
    "one pair" : 1,
    "high card" : 0
}

def flatten(list):
    new_list = []
    for i in list:
        for j in i:
            new_list.append(j)
    return new_list

def unique_cards(cards):
    # don't count jokers for part 2
    s = set(cards)
    if 'J' in s: 
        return len(s) - 1
    return len(s)

def hand_type(cards):
    unique = unique_cards(cards) # does NOT include Js
    num_of_jokers = cards.count('J')

    match unique:
        case 0:
            return hand_types['five of a kind']
        case 1:
            return hand_types['five of a kind']
        case 2:
            if num_of_jokers >= 2:
                return hand_types['four of a kind']
            for item in set(cards):
                if cards.count(item) + num_of_jokers == 4:
                    return hand_types['four of a kind']
            return hand_types['full house']
            
            # mid = unique_cards(sorted(cards)[1:4])
            # if mid == 1 or mid == 0 or num_of_jokers >= 2:
            #     return hand_types['four of a kind']
            # else:
            #     return hand_types['full house']
        case 3:
            if num_of_jokers > 0:
                return hand_types['three of a kind']
            for item in set(cards):
                if cards.count(item) == 2:
                    return hand_types['two pair']
                if cards.count(item) == 3:
                    return hand_types['three of a kind']
        case 4:
            return hand_types['one pair']
        case 5:
            return hand_types['high card'] 

def card_values(value):
    value = list(value[0])
    new_value = []
    for item in value:
        match item:
            case 'A': new_value.append(14)
            case 'K': new_value.append(13)
            case 'Q': new_value.append(12)
            case 'J': new_value.append(1) # 11 for part1, 1 for part2
            case 'T': new_value.append(10)
            case _: new_value.append(int(item))
    return new_value



def engage():
    sorted_hands = [[],[],[],[],[],[],[]]

    for hand in hands:
        sorted_hands[hand_type(hand[0])].append(hand)

    for i in range(7):
        sorted_hands[i] = sorted(sorted_hands[i],key=card_values)

    sorted_hands = flatten(sorted_hands)

    winnings = 0
    for i in range(len(sorted_hands)):
        winnings += (i + 1) * int(sorted_hands[i][1])
    
    print(winnings)

engage()
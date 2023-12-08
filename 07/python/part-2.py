results = []
card_values = {
    'A': 13,
    'K': 12,
    'Q': 11,
    'J': 10,
    'T': 9,
    '9': 8,
    '8': 7,
    '7': 6,
    '6': 5,
    '5': 4,
    '4': 3,
    '3': 2,
    '2': 1,
    'J': 0
}
hand_values = {
    "five_of_a_kind": 7,
    "four_of_a_kind": 6,
    "full_house": 5,
    "three_of_a_kind": 4,
    "two_pair": 3,
    "one_pair": 2,
    "high_card": 1
}


def parse_input(filename: str) -> (list, list):
    with open(filename, 'r') as f:
        file_content = f.readlines()
        hands, bids = [], []
        for line in file_content:
            line_split = line.split(' ')
            hands.append(line_split[0].strip())
            bids.append(line_split[1].strip())
        return (hands, bids)


def compare_cards(hand_a: str, hand_b: str) -> str:
    for a, b in zip(hand_a, hand_b):
        if card_values[a] == card_values[b]:
            continue
        else:
            winning_card = hand_a if card_values[a] > card_values[b] else hand_b
            print(f"{winning_card=} - {a=}, {b=}")
            return hand_a if card_values[a] > card_values[b] else hand_b



def hand_value(hand: str) -> int:
    unique_cards = len(set(hand.replace('J', '')))
    if unique_cards == 0:
        unique_cards = 1

    print(f"{hand=}, {unique_cards=}")
    match unique_cards:
        case 1:
            return hand_values['five_of_a_kind']
        case 2:
            four_of_a_kind = False
            for card in hand:
                print(f"{card=}, {hand.replace(card, '')}")
                if len(hand.replace(card, '').replace('J', '')) == 1:
                    four_of_a_kind = True
                    print(f"{card=}, {four_of_a_kind=}")
                    break 
            return hand_values['four_of_a_kind'] if four_of_a_kind else hand_values['full_house']
        case 3:
            three_of_a_kind = False
            for card in hand:
                print(f"{card=}, {hand.replace(card, '')}")
                if len(hand.replace(card, '').replace('J', '')) == 2:
                    three_of_a_kind = True
                    print(f"{card=}, {three_of_a_kind=}")
                    break 
            return hand_values['three_of_a_kind'] if three_of_a_kind else hand_values['two_pair']
        case 4:
            return hand_values['one_pair']
        case 5:
            return hand_values['high_card']


def compare_hands(hand_a: str, hand_b: str) -> str:
    hand_a_value, hand_b_value = hand_value(hand_a), hand_value(hand_b)
    winning_hand = ""
    if hand_a_value == hand_b_value:
        winning_hand = compare_cards(hand_a=hand_a, hand_b=hand_b)
    else:
        winning_hand = hand_a if hand_a_value > hand_b_value else hand_b
     
    print(f"{winning_hand=} - {hand_a}: {hand_a_value}, {hand_b}: {hand_b_value}")
    return winning_hand


if __name__ == '__main__':
    input_files = ['../example-input.txt']
    input_files.append('../input.txt')
    
    for filename in input_files:
        hands, bids = parse_input(filename=filename)
        print(f"{hands=}\n{bids=}")

        results = [hands, bids]
        print(f"{results=}")
        for i in range(len(results[0]) - 1):
            if i < len(results[0]) - 1:
                for j in range(len(results[0]) - i - 1):
                    this_hand, this_bid = results[0][j], results[1][j]
                    next_hand, next_bid = results[0][j + 1], results[1][j + 1]
                    print(f"{i=}: {this_hand=}, {this_bid=} - {next_hand=}, {next_bid=}")
            
                    winning_hand = compare_hands(hand_a=this_hand, hand_b=next_hand)
                    if winning_hand == this_hand:
                        print(f"{winning_hand=}")
                        results[0][j + 1], results[0][j] = this_hand, next_hand
                        results[1][j + 1], results[1][j] = this_bid, next_bid

        total_winnings = 0
        for i, bid in enumerate(results[1]):
            total_winnings += int(bid) * (i + 1)

        print(f"{results=}")
        print(f"\nTotal winnings {filename}: {total_winnings}\n")

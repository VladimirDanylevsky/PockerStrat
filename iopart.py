NAME_IN = 'A-small-practice.in'
NAME_OUT = 'A-small-practice.out'


def read_input(name_of_file=NAME_IN):
    with open(name_of_file, 'r') as file_desc:
        file_data = file_desc.read()
    data = file_data.split('\n')
    return data


def write_output(data, name_of_file=NAME_OUT):
    with open(name_of_file, 'w') as file_desc:
        for hand, deck, best_hand in data:
            hand = ' '.join(hand)
            deck = ' '.join(deck)
            output = f"Hand: {str(hand)} Deck: {deck} Best hand: {best_hand}\n"
            file_desc.write(output)


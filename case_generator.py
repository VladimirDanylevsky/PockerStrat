from random import choice


CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
SUIT = ['D', 'C', 'H', 'S']


def generate_card():
    card = choice(CARDS)+choice(SUIT)
    return card


def main():
    number_of_cases = 100000
    number_of_card = 10
    data = []
    for i in range(number_of_cases):
        case = []
        for j in range(number_of_card):
            case.append(generate_card())
        data.append(case)
    print(data)
    with open('test_case.input', 'w') as test_case:
        for element in data:
            test_case.write(' '.join(element)+'\n')


def test_func():
    print(generate_card())


if __name__ == '__main__':
    main()
    #test_func()
from iopart import read_input, write_output
from time import time
from itertools import combinations
from collections import Counter
from functools import reduce
from numpy import mean
from multiprocessing import Pool
from primes_generator import simple_gen
import cProfile

#TODO preserve order after mp execution


def mangled_values():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    mangle_dict = {a: b for a, b in zip(cards, simple_gen())}
    return mangle_dict


def straight_hash_list(card_rankings=mangled_values()):
    length = 5
    straight_comb_hash = set()
    digits = list(card_rankings.values())
    list_of_digits = [digits[-1]] + digits
    for i in range(len(list_of_digits)-length+1):
        pos_straight = list_of_digits[i:i+length]
        straight_comb_hash.add(reduce(lambda x, y: x*y, pos_straight))
    return straight_comb_hash


def get_card_sets(input_file='deck.input'):
    cases = read_input(input_file)
    for element in cases:
        yield element


def batch_process(number_of_workers=4):
    worker = 0
    data = []
    for element in range(number_of_workers):
        data.append([])
    for element in get_card_sets():
        if worker < number_of_workers:
            data[worker].append(element)
            worker += 1
        else:
            worker = 1
            data[0].append(element)
    return data


def decompose(iterable):
    suits = []
    values = []
    for element in iterable:
        suits.append(element[1])
        values.append(element[0])
    return values, suits


def find_stat(case, card_ranking=mangled_values()):
    stat = {'suits': [], 'ace': [], 'triple': [], 'pair': []}
    values, suits = decompose(case)
    same_suit = Counter(suits)
    same_value = Counter(values)
    for suit in same_suit:
        if same_suit[suit] >= 5:
            stat['suits'] += suit
    for value in same_value:
        if same_value[value] > 3:
            stat['ace'] += value
            stat['triple'] += value
            stat['pair'] += value
        elif same_value[value] > 2:
            stat['triple'] += value
            stat['pair'] += value
        elif same_value[value] > 1:
            stat['pair'] += value
    stat['biggest'] = max(values, key=lambda p: card_ranking[p])
    return stat


def reachable_hand(hand, deck):
    yield hand
    for element in combinations(hand, 4):
        yield [unique for unique in element] + deck[:1]
    for element in combinations(hand, 3):
        yield [unique for unique in element] + deck[:2]
    for element in combinations(hand, 2):
        yield [unique for unique in element] + deck[:3]
    for element in hand:
        yield [element] + deck[:4]
    yield deck


def find_hash(values, card_rankings=mangled_values()):
    hash_number = 1
    for element in values:
        hash_number *= card_rankings[element]
    return hash_number


def is_straight(case):
    straight_hashes = straight_hash_list()
    values, _ = decompose(case)
    if find_hash(values) in straight_hashes:
        return True
    return False


def rank_hand(case, card_points=mangled_values()):
    combination_value = {'straight-flush': 800, 'four-of-a-kind': 700, 'full-house': 600, 'flush': 500,
                         'straight': 400, 'three-of-a-kind': 300, 'two-pair': 200, 'one-pair': 100}
    evaluation = find_stat(case, card_ranking=card_points)
    straight_flag = is_straight(case)
    flush_flag = False
    if evaluation['suits']:
        flush_flag = True  # check for straight, we have ,at least, flush
        if straight_flag:
            return 'straight-flush', combination_value['straight-flush'] + card_points[evaluation['biggest']]
    if evaluation['ace']:
        # second highest hand - ace
        return 'four-of-a-kind', combination_value['four-of-a-kind'] + card_points[evaluation['biggest']]
    if evaluation['triple']:
        if len(evaluation['pair']) > 1:  # check for full-house
            return 'full-house', combination_value['full-house'] + card_points[evaluation['biggest']]
    if flush_flag:
        return 'flush', combination_value['flush'] + card_points[evaluation['biggest']]
    if straight_flag:
        return 'straight', combination_value['straight'] + card_points[evaluation['biggest']]
    if evaluation['triple']:
        return 'three-of-a-kind', combination_value['three-of-a-kind'] + card_points[evaluation['biggest']]
    if len(evaluation['pair']) > 1:
        return 'two-pair', combination_value['two-pair'] + card_points[evaluation['biggest']]
    if evaluation['pair']:
        return 'one-pair', combination_value['one-pair'] + card_points[evaluation['biggest']]
    return 'highest card', card_points[evaluation['biggest']]


def main(data=get_card_sets('deck.input')):
    answers = []
    card_ranking = mangled_values()
    for element in data:
        case = element.split(' ')
        if len(case)-1:
            hand, deck = case[0:5], case[5:]
            answer = [hand, deck]
        else:
            continue
        rank_board = []
        for case in reachable_hand(hand, deck):
            rank_board.append((rank_hand(case, card_points=card_ranking), case))
            #print(rank_hand(case), case)
        answer.append((max(rank_board, key=lambda x: x[0][1]))[0][0])
        answers.append(answer)
    name = 'deck.output'
    write_output(answers, name)


def performance_test(number_of_tests=10):
    timings = []
    for element in range(number_of_tests):
        start_time = time()
        main()
        timings.append(time()-start_time)
    print(mean(timings))


def test_space():
    data = batch_process()
    with Pool(processes=4) as pool:
        pool.map(main, data)
    pool.close()
    pool.join()


if __name__ == '__main__':
    pr = cProfile.Profile()
    pr.enable()
    performance_test(number_of_tests=1)
    pr.disable()
    pr.print_stats()
    #performance_test()
    #test_space()
    #main(data_elements)
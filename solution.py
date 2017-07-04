import argparse
from pokerstrat import main, mp_realization
from os import path


parser = argparse.ArgumentParser(description='The Psychic Poker Player, solution by Vladimir Danylevski. '
                                             'Run with -h, --help flag for short help info.',
                                 epilog='I guess that\'s works')
parser.add_argument('name', metavar='name_of_input', type=str, nargs='?',
                    help='Name of input file, by default deck.input')
parser.add_argument('-mp', '--MULTPROC', action='store_true',
                    help='Add multiprocessing capabilities, answer will be stored in separated file for each process')
parser.add_argument('number_of_w', metavar='number_of_w', nargs='?', type=int,
                    help='Number of simultaneously working processes, by default 4, optional, work only with --mp flag,'
                         'Use without --mp flag')
parser.add_argument('-v', '--VOCAL', action='store_true',
                    help='More details on each case')

if __name__ == '__main__':
    vocal = False
    args = parser.parse_args()
    if args.name:
        if args.name.isalnum() and not args.number_of_w:
            args.number_of_w = int(args.name)
            args.name = None
    if args.VOCAL:
        vocal = True
    if not args.name:
        print('Default case, Input: \'deck.input\', Output: \'[timestamp]_[pid].output\'')
        nm = 'deck.input' # default
    else:
        print(f'Input \'{args.name}\', Output: \'[timestamp]_[pid].output\'')
        nm = args.name.strip('\"\'')
    if not path.exists(nm):
        raise FileNotFoundError
    if not args.MULTPROC:
        print('Using 1 logical core')
        main(name_of_file=nm, data=False, show_best_hand=vocal)
    else:
        if not args.number_of_w:
            print('Default case for mp, numbers of workers: 4')
            print('output file will be split into chunks')
            nw = 4
        else:
            print(f'Number of workers: {args.number_of_w}')
            print('output file will be split into chunks')
            nw = args.number_of_w
        mp_realization(name_of_file=nm, number_of_w=nw)

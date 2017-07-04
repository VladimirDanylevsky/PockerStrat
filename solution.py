import argparse
from pokerstrat import main, mp_realization


parser = argparse.ArgumentParser(description='The Psychic Poker Player, solution by Vladimir Danylevski. '
                                             'Run with -h, --help flag for short help info. By default will use '
                                             'deck.input to produce deck.output file. ',
                                 epilog='I guess that\'s works')
parser.add_argument('name', metavar='name_of_input', type=str, nargs='?',
                    help='Name of input file, by default deck.input')
parser.add_argument('-mp', '--MULTPROC', action='store_true',
                    help='Add multiprocessing capabilities, answer will be stored in separated files for each process')
parser.add_argument('number_of_w', metavar='number_of_w', nargs='?', type=int,
                    help='Number of simultaneously working processes, by default 4, optional, work only with --mp flag')


if __name__ == '__main__':
    args = parser.parse_args()
    if args.name:
        if args.name.isalnum() and not args.number_of_w:
            args.number_of_w = int(args.name)
            args.name = None
    if not args.name:
        print('Default case, Input: \'deck.input\', Output: \'[timestamp].output\'')
        nm = 'deck.input' # default
    else:
        print(f'Input \'{args.name}\', Output: \'deck.output\'')
        nm = args.name.strip('\"\'')
    if not args.MULTPROC:
        print('Using 1 logical core')
        main(name_of_file=nm, data=False)
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

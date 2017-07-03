'''
Beautiful recipe for primes generator
'''


def simple_gen():
    primes = {}
    q = 2
    while True:
        if q not in primes:
            yield q
            primes[q*q] = [q]
        else:
            for p in primes[q]:
                primes.setdefault(p+q, []).append(p)
            del primes[q]
        q += 1

if __name__ == '__main__':
    pass
'''
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Hints
Ideas about the problem

Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.
'''

def genPrimes():
    primes = []
    n = 2
    last = n

    while True:
        for i in primes:
            if n % i == 0:
                n += 1
                break

        else:
            primes.append(n)
            last = n
            n += 1
            yield last

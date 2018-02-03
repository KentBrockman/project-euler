import itertools
import math

def prime_generator(stopAt=-1):
    numberOn = 2
    primes = []
    while stopAt is -1 or numberOn < stopAt:
        # make a generator for the valid primes to check
        valid_primes = itertools.filterfalse(lambda x: x > math.sqrt(numberOn), primes)

        # now check if the number youre on is divisible by any of these
        isPrime = True
        for prime in valid_primes:
            # quit the instant you find a prime that divides the number in question
            if numberOn % prime == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(numberOn)
            yield numberOn

        numberOn = numberOn + 1

    return 0

# gen = prime_generator(2000000)
# print(sum(gen))
# answer is  142913828922  in 45:52.59

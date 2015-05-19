#!/usr/bin/env python
# -*- coding: utf-8 -*-

__all__ = ['is_prime', 'find_primes']

import time, math


def is_prime(num):
    """Determines if the number is a prime number or not.
    Algorithm checks if the number can be divided evenly by a range 
    of numbers from 2 to the square root of the number.
    :param num  Input number to check for primeness
    :return True if the number is prime else False.
    """

    # If the number is less than 2 or an even number
    # then it is not prime:
    if num < 2 or (num % 2) == 0:
        return False

    # check all the odd numbers up to the square root
    # of the number:
    for i in xrange(3, int(math.sqrt(num)) + 1, 2):
        if (num % i) == 0:
            return False

    return True


def find_primes(N):
    """Finds all the prime numbers up to number N.
    :param N   Upper limit to find prime numbers
    :return List of prime numbers up to the number N
    """

    primes = [2]
    is_candidate = [True] * (N + 1)

    for num in xrange(3, N, 2):
        if is_candidate[num]:
            upper_limit = int(math.sqrt(num))
            flag = True
            for prime in primes:
                if prime <= upper_limit:
                    if (num % prime) == 0:
                        flag = False
                        break
                else:
                    break

            # is it a prime number?
            if flag:
                primes.append(num)

                # exclude all the odd multiples from the 
                # candidate list:
                ex_num = num * 3
                delta = 2 * num
                while ex_num <= N:
                    is_candidate[ex_num] = False
                    ex_num += delta

    return primes


if __name__ == "__main__":
    import sys

    def _test(args):
        def _test_is_prime(num):
            res = is_prime(num)
            print "%i is %s prime" % (num, "not" if not res else "")

        N = int(args[0])
        print "calculating primes upto %i..." % N
        start_time = time.time()
        primes = find_primes(N)
        end_time = time.time()

        print "found %i primes between 1 and %i" % (len(primes), N)

        print primes[:50]
        print "......."
        print primes[-10:]
        print "calculated in %.3f secs" % (end_time - start_time,)

        _test_is_prime(1)
        _test_is_prime(2)
        _test_is_prime(primes[len(primes) / 2])
        _test_is_prime(primes[-1])
        _test_is_prime(534534465566676789)
        # _test_is_prime(112829754900439506175719191782841802172556768253593054977186235584979780304652423405148425447063090165759070742102132335103295947000718386333756395799633478227612244071875721006813307628061280861610153485352017238548269452852733818231045171038838387845888589411762622041204120706150518465720862068595814264819)

    sys.exit(_test(sys.argv[1:]))

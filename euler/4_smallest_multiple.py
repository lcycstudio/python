"""
Copyright (c) 2022, Lewis Chen
All rights reserved.

This source code is licensed under the MIT-style license found in the
LICENSE file in the root directory of this source tree. 
"""
import time

def smallest_multiple_1(initial, start, end):
    """
    2520 is the smallest number that can be divided by each of the numbers 
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the 
    numbers from 1 to 20?
    """
    a = initial
    t = time.time()
    primes = []
    not_primes = []
    common_factors = []
    for i in range(start, end):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)
            common_factors = get_common_factors(common_factors, not_primes)
    
    for i in primes:
        a = a * i
    
    while a > 0:
        b = 0
        for j in range(1, end):
            if a % j == 0:
                b += 1
        if b == end - 1:
            break
        a += primes[-1]
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print('result: ', a)
    for i in range(1, end):
        print(f'a / {i}: ', a / i)

def get_common_factors(common_factors: list, not_primes: list) -> list:
    for i in not_primes:
        for j in range(1, i+1):
            if i % j == 0 and j not in common_factors:
                common_factors.append(j)
    return common_factors


def smallest_multiple_2(initial, end):
    """
    Correct but very slow and resourceful code
    """
    if end > 17:
        print('This will take a long time.\n'
            'Use smallest_multiple_1() instead.')
        return None

    a = initial
    t = time.time()
    while a > 0:
        b = 0
        for i in range(1, end):
            if a % i == 0:
                b += 1
        if b == end - 1:
            break
        a += 1
    elapsed = time.time() - t
    print('elapsed ', elapsed)
    print('a2: ', a)
    print(f'a / {b}: ', a / b)

a = 2520
end = 21
# smallest_multiple_1(a, 11, end)
smallest_multiple_2(a, end)
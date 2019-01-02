import datetime
import math


# This function calculates all the possible factors for the given number.
def find_number_factors(factored_number):
    iterable = []
    if factored_number > 2:
        iterable.append(2)
        initial_factor = int(factored_number/2 + 1)
        iterable.extend(list(range(3,initial_factor,2)))
    return [i for i in iterable if factored_number % i == 0]

# This function receives a number and a list of its factors, checks wich of the
# given factors are prime numbers, than adds them to prime_factors_list.
def find_prime_factors(factor_list):
    return [i for i in factor_list if len(find_number_factors(i)) == 0]

def find_prime_factorization(factored_number, prime_list):
    factorization = []
    for i in prime_list:
        if factored_number % i == 0:
            factorization.append(i)
            factorization.extend(find_prime_factorization((factored_number / i), prime_list))
            break
    return factorization

def test():
    l = []
    for i in range(100000):
        if not i & 1:
            l.append(i)
    return l

# This function's purpose is to generate a human friendly factorization string.
def beauty_factors(factor_list):
    power = 1
    factorization = ''
    for _i_ in range(len(factor_list)):
        try:
            if factor_list[_i_] == factor_list[_i_ + 1]:
                power = power + 1
            elif power == 1:
                factorization = factorization + ('%d × ' % (factor_list[_i_]))
            else:
                factorization = factorization + (
                    '%d^%d × ' % (factor_list[_i_], power))
                _i_ = power + 1
                power = 1
        except IndexError:
                if power > 1:
                    factorization = factorization + (
                        '%d^%d.' % (factor_list[_i_], power))
                else:
                    factorization = factorization + ('%d' % (factor_list[_i_]))
    return factorization


# PROGRAM START
tested_number = int(input('-> Insert a number to be tested: '))


initial_time = datetime.datetime.now()
log_file = open("prime-factors-calc-2.0.log", "a")
log_file.write('On %s\nTested number was: %d' % (
    initial_time.strftime('%d/%m/%Y %H:%M:%S'), tested_number))


print('-> Finding prime factors...')


tested_number_factor_list = find_number_factors(tested_number)
print(f'function 1: {tested_number_factor_list}' )


if len(tested_number_factor_list) == 0:
    print(f'-> {tested_number} is a prime number')
    log_file.write('\n%d is a prime number' % (tested_number))
else:
    log_file.write('\nPrime factors found:')
    prime_factors = find_prime_factors(tested_number_factor_list)
    for i in prime_factors:
        print(f"   -> {i} is a prime factor")
        log_file.write(f'\n    {i}')
    factorization = find_prime_factorization(tested_number, prime_factors)
    print(factorization)
    print('-> Prime factorization: %s' % (beauty_factors(factorization)))
    log_file.write('\nPrime factorization: %s' % beauty_factors(factorization))


process_time = datetime.datetime.now() - initial_time


print(
    '-> Process completed in %d hours, %d minutes and %.3f seconds' %
    (process_time.seconds / 3600, process_time.seconds / 60,
        process_time.seconds + process_time.microseconds / 1000000))
log_file.write(
    '\nProgram run for %d hours, %d minutes and %.3f seconds\n\n' %
    (process_time.seconds / 3600, process_time.seconds / 60,
        process_time.seconds + process_time.microseconds / 1000000))
log_file.close()

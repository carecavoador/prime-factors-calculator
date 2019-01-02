import datetime
import math


# This function calculates all the prime factors for the given number.
def prime_factors(factored_number):
    iterable = []

    if factored_number > 2:
        iterable.append(2)

    initial_factor = int(math.sqrt(factored_number))
    iterable.extend(list(range(3,initial_factor,2)))

    result = [i for i in iterable if factored_number % i == 0 and len(prime_factors(i)) == 0]
    reverse = [int(factored_number / i) for i in result if factored_number / i > initial_factor and len(prime_factors(factored_number / i)) == 0 ]
    result.extend(reversed(reverse))

    return result


def prime_factorization(factored_number, prime_list):
    factorization = []
    for i in prime_list:
        if factored_number % i == 0:
            factorization.append(i)
            factorization.extend(prime_factorization((factored_number / i), prime_list))
            break
    return factorization

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


primes = prime_factors(tested_number)


if len(primes) == 0:
    print(f'-> {tested_number} is a prime number')
    log_file.write('\n%d is a prime number' % (tested_number))
else:
    log_file.write('\nPrime factors found:')
    for i in primes:
        print(f"   -> {i} is a prime factor")
        log_file.write(f'\n    {i}')
    factorization = prime_factorization(tested_number, primes)
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

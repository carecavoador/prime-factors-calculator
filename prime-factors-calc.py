import datetime
import math


# This function calculates all the possible factors for the given number.
def find_number_factors(factored_number):
    initial_factor = int(factored_number / 2)
    return [i for i in range(2, initial_factor+1) if factored_number % i == 0]


# This function receives a number and a list of its factors, checks wich of the
# given factors are prime numbers, than adds them to prime_factors_list.
def find_prime_factors(factor_list):
    return [i for i in factor_list if len(find_number_factors(i)) == 0]


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
prime_factors = []


if len(tested_number_factor_list) == 0:
    print('-> %d is a prime number' % (tested_number))
    log_file.write('\n%d is a prime number' % (tested_number))
else:
    log_file.write('\nPrime factors found:')
    for _i_ in range(len(tested_number_factor_list)):
        if len(find_number_factors(tested_number_factor_list[_i_])) == 0:
            prime_factors.append(tested_number_factor_list[_i_])
            print('   -> %d is a prime factor' % (
                tested_number_factor_list[_i_]))
            log_file.write('\n    %d' % (tested_number_factor_list[_i_]))
    result = sorted(find_prime_factors(tested_number, prime_factors))
    print('-> Prime factorization: %s' % (beauty_factors(result)))
    log_file.write('\nPrime factorization: %s' % beauty_factors(result))


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

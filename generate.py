# !/usr/bin/python

from primepackage.primemodule import *
from primepackage.primeio import *

"""A Python module generating a list of prime numbers and output them into a csv file

"""


def main():
    """Generate 100 prime numbers and output it into output.csv file

        variable primes calls getNPrime(100) to generate a list of prime numbers to 100

        write_primes() is called using parameters (primes(list), 'output.csv')

        variable l created and calls function read_primes() using 'output.csv'
        to retrieve list of prime numbers that was created

        print() function called with l(list) as the argument and prints all the values of list l
    """
    # call method getNPrime to retrieve prime numbers up to 100
    primes = getNPrime(100)

    # call the write_primes method using primes list from above and write it to a csvfile
    write_primes(primes, 'output.csv')

    # variable l is given the list of prime numbers from csvfile written by write_primes
    l = read_primes('output.csv')

    # print values of list l

    print(l)


if __name__ == '__main__':
    main()

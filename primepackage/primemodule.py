# !/usr/bin/python

"""This module is used for testing if a number is prime and creating a list of prime numbers.
"""


def isPrime(n):
    """The function to find if given number is prime or not.
        Parameters:
            n (int): The given natural number.
        Returns:
            boolean: A value of whether n is prime or not.
    """
    # initialize variable to check if number is prime or not
    prime_check = 2

    # loop through numbers 2 through n to see if it is divisible
    for x in range(2, n):
        # if n is divisible return false
        if n % prime_check == 0:
            return False
        # increment prime_check until looped to n
        else:
            prime_check = (prime_check + 1)
    # return true if it isn't found to be divisible by any number instead of itself
    return True


def getNPrime(num):
    """The function to create a list of prime numbers equal to num
    Parameters:
        num (int): The amount of prime numbers to be added to the list.
    Returns:
        prime_numbers (list): A list of prime numbers equal to given amount from parameter.
        """

    # create list to return and int variable to check if it is prime or not
    prime_numbers = []

    # loop through numbers until num is reached
    for y in range(num):
        # if the isPrime returns true for y it is added to list
        if isPrime(y):
            prime_numbers.append(y)
    # return the list of prime numbers after y reaches num
    for i in range(len(prime_numbers)):
        prime_numbers[i] = int(prime_numbers[i])
    return prime_numbers
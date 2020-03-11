# !/usr/bin/python
import csv

"""Module containing two functions to read and write prime numbers.
"""


def write_primes(l, file_name):
    """This function is used to read a list of prime numbers and write the numbers to a csv file.
        Parameters:
            l (list): A list of prime numbers.
            file_name (csv file): A file to write the list of prime numbers in.
        Returns:
            Writes l (list of primes to csv file)
    """
    count = len(l)
    for i in range(0, count):
        with open(file_name, 'w') as csv_file:
            prime_writer = csv.writer(csv_file)
            prime_writer.writerow(l)


def read_primes(file_name):
    """This function reads prime numbers from file then creates and returns a list of those numbers.
        Parameters:
            file_name (csv file): A csv file given containing prime numbers.
        Returns:
            prime_list (list): A list created using the prime numbers inside file_name.
    """

    # initialize the prime number list
    prime_numbers = []

    # read the csv file
    with open(file_name, newline='') as csvfile:
        # create the csv reader object
        csv_reader = csv.reader(csvfile)
        # loop through the csv file and add the rows to the prime_numbers list
        for row in csv_reader:
            prime_numbers.append(row)
        # return after looping through the rows
    return prime_numbers

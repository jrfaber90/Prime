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
    # variable count created using len() function to get number of objects in list l
    count = len(l)
    # use a for loop to go through each obj(i) in list and write them to csvfile (file_name)
    for i in range(0, count):
        # call open() function and pass the csvfile to it
        with open(file_name, 'w') as csv_file:
            # initiate csv.writer using file given as argument
            prime_writer = csv.writer(csv_file)
            # use writerow function on the csv.writer that was created
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
        for p in csv_reader:
            # call append function to add p to (list)prime_numbers
            prime_numbers.append(p)
        # return after looping through the rows
    return prime_numbers

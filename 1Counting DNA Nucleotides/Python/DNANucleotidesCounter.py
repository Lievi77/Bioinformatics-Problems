#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rosalind Problem #1: Counting DNA Nucleotides

Created on Thu Apr 23 21:34:54 2020

@author: lev
"""

# modes: r to read only
# w to write only.
# r+ read and write, cursor is positioned at the beginning,
# data not overwritten.
# w+ write and read, cursor is positioned, data is overwritten.
# a, append only, data inserted will be at the end of file.
# a+, append and read, cursor is at the end, and we can read.
to_analyze = open("rosalind_dna.txt", "r")

# read methods :
# read(n), reads n bytes or if n is not specified, the entire file
# readline(n), n is the number of bytes but only reads one line.
# readlines(), reads line by line of the document and returns it in list of all the lines of the text
inputText = to_analyze.readlines()
inputText = inputText[0] #since we only have 1 line of input, we get rid of the array

# assuming there are only A, B, C, G, T
# trying recursion


def count_letter(array, letter):
    # base case
    # an empty array implies false

    counter = 0

    if not array:
        return counter  # counter is always zero at this point

    if array[0] is letter:
        counter = 1
    else:
        counter = 0

    # tail recursion
    return counter + count_letter(array[1:], letter)


# good practice to close the file after opening it. Frees memory
to_analyze.close()

numberA = str(count_letter(inputText, "A"))
numberC = str(count_letter(inputText, "C"))
numberG = str(count_letter(inputText, "G"))
numberT = str(count_letter(inputText, "T"))


print(numberA + " " + numberC + " " + numberG + " " + numberT)


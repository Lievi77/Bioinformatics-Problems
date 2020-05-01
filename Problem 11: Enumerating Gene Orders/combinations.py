from itertools import permutations 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 11: Enumerating Gene Orders

Created on Fri May  1 14:41:06 2020

@author: lev
"""

#----------------------------Methods-----------------------------

def print_permutations(integers):
    
    outcomes = list(permutations(integers))
    
    #loop to print the results properly 
    for outcome in outcomes:
        print(*outcome) #prints the tuple nicely in a single line


def total_combinations_of(n): #follows n! formula
    
    if n == 0 or n == 1:
        return 1
    
    return n * total_combinations_of(n-1)


def print_all_possible_combinations(n):
    
    #output goes this way=
    #
    # (number of total combinations possible)
    # (then all the combinations listed)
    
    integer_list = list(range(1,n+1)) #returns a list from 1 to n
    
    #-------------Calculating the total number of combinations----
    
    total_combinations = total_combinations_of(n) #gets n!
    
    print(total_combinations)
    
    #------------Now doing the permutations-----------------------
    
    print_permutations(integer_list)
    

#----------------------------Main---------------------------------

file = open("rosalind_perm.txt","r")

input_ = int(file.readline()) #guaranteed to be an integer

print_all_possible_combinations(input_)
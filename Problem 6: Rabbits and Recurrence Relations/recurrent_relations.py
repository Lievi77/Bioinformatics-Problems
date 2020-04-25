#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 6: Rabbits and Recurrence Relations

Created on Sat Apr 25 17:51:26 2020

@author: lev
"""

file = open("rosalind_fib.txt", "r")

def get_population(file): #method to extract the elements of the text
    a = []
    
    for line in file:
        a = line.split()
    
    return a

populations = get_population(file)

file.close() #good practice



#population[0] contains the n months that will occur
#population[1] contains the k offspring that every month will occur

def get_n_months(n,k):
    #recurrence relation is (n-1) + 3*(n-2)
    if n == 2 or n == 1:
        return 1
    else:
        return get_n_months(n-1,k) + (k*get_n_months(n-2,k) )

n = int(populations[0])
k= int(populations[1])

print(get_n_months(n,k))
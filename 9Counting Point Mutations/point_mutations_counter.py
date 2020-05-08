#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 9: Counting Point Mutations

Created on Wed Apr 29 11:55:04 2020

@author: lev
"""

#---------------------------METHODS---------------------------

#method that counts the point mutations between dna1 and dna2
def count_pmutations(dna1,dna2):#dna1 and dna2 are of the same length
    mutations = 0
    
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            mutations += 1


    return mutations
#----------------------------MAIN-----------------------------

file = open("rosalind_hamm.txt", "r") #file opening algorithm

strands = file.readlines()

dna1  = strands[0][:-1]
dna2 = strands[1][:-1] #extra processing to remove the '\n' character


mutations = count_pmutations(dna1,dna2)
print(mutations)

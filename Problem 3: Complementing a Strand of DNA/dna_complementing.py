#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 3: Complementing a Strand of DNA

Created on Fri Apr 24 11:35:06 2020

@author: lev
"""

file = open("rosalind_revc.txt", "r")

dna_string = file.readline()

file.close #good practice

#must find the complement of dna_string
#compliments are as follows:
#1- reverse the string
#2- replace each letter with its complement (A and T are complements)
#(C and G are complements)

def find_dna_complement(dna):
    
    dna= dna[::-1] #reverses the string
    comp_dna = ""
    
    for i in dna:
        
        to_add = ""
        
        if i == "A":
            
            to_add = "T"
            
        elif i == "C":
            
            to_add = "G"
            
        elif i == "G":
            
            to_add = "C"
            
        elif i == "T":
            to_add = "A"
        
        comp_dna = comp_dna + to_add
        
    
    
    return comp_dna

complement_dna = find_dna_complement(dna_string)
print(complement_dna)



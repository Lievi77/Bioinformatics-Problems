from motif_detector import occurences #uses function from a previous solution 
from point_mutations_counter import count_pmutations
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 12: Finding a shared motif

Created on Fri May  1 15:29:57 2020

@author: lev
"""

#-----------------------------METHODS-----------------------------

def process_dna_file(file): #FUNCTIONS WELL
    
    dna_strings = []
    file_lines = file.readlines()
    dna_string = ""
    
    
    for i in range(len(file_lines)): #list form
        
        if i == 0: #first case
            continue
    
        if file_lines[i][0] == ">": 
            dna_strings.append(dna_string)
            dna_string = "" #clear string
            continue
    
        
        dna_string += file_lines[i].strip("\n")
        
        if i == len(file_lines) -1: #last case check
            dna_strings.append(dna_string)
    
    return dna_strings

#---------------------------------------------------------------------------

def find_longest_common_motif(dna_strings):
    
    #note if method occurences returns a null list, then there are no occurences
    
    x = count_pmutations(dna_strings[0], dna_strings[1])
    
    print(x)
     
#---------------------------MAIN----------------------------------

file  = open("test.txt", "r")

dna_strings = process_dna_file(file) #returns a list containing the dna strings


longest_common_motif = find_longest_common_motif(dna_strings)

print(longest_common_motif)



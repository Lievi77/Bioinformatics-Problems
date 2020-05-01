#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem 10: Finding Restriction Sites

Created on Wed Apr 29 12:18:15 2020

@author: lev
"""

#--------------------------METHODS--------------------------------
#finds the complement of the dna
def complement(dna):
    
    complement = ""
    
    for i in dna:
        if i == 'A':
            complement += 'T'
        elif i == 'C':
            complement += 'G'
        elif i == 'T':
            complement += 'A'
        else:
            complement += 'C'
    
    
    return complement


def palindrome_finder(strand):
    
    for i in range(len(strand)):
        
        for j in range(4,13): #loops form 4 to 12
        
            #do substrings
            sub_dna = strand[i:i+j]
            
            if (i+j) > len(strand) :
               # print(i, j,len(strand), sub_dna)
                continue
        
        #take its complement of the substring
            complement_dna = complement(sub_dna)
            reverse_complement_dna = complement_dna[::-1]
        #now reverse it
          
        
        #print if a match is detected
            if reverse_complement_dna == sub_dna:
                print(i+1, len(sub_dna), sep = ' ')

def build_dna_string(info):
    dna = ""
    total = 0
    
    for line in info:
        if line[0] == ">": #omits the dna name 
            continue
        else:
            total += len(line)
            dna += line

    return dna 

#-----------------------------MAIN--------------------------------

#usual algorithm
file = open("test.txt","r")

#data is in FASTA FORMAT
dna_info = file.readlines()

strand = build_dna_string(dna_info) #builds a single dna_string

#output must obey the following format
#
# index1 | index2

#suggestion: print the outputs as soon as you find them
palindrome_finder(strand)


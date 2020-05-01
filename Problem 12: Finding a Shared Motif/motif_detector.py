#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 8: finding a Motif in DNA

Created on Sun Apr 26 13:35:19 2020

@author: lev
"""

#-----------------------methods-------------------------------

def occurences(s, t): #finds all occurences of substring t on s
    indeces = [] 
    
    for i in range(len(s)): #gets all possible substrings of length t
        
        substring_sample = s[i: i + len(t)]#substring extraction 
    
        if substring_sample == t:
            indeces.append(i+1) #indeces for the output are starting from 1
    
    return indeces # returns an array of all indeces 
 
#-------------------------MAIN-----------------------------
    
def main():
    file = open("rosalind_subs.txt","r")

    lines = file.readlines()

    dna = lines[0][:-1] #extra processing to remove the '\n' character
    sub_dna = lines[1][:-1] 


    occurence = occurences(dna, sub_dna)

    #print occurences

    print(*occurence) #python 3 new method prints elements with spaces

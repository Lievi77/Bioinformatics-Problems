#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 2: Transcribing DNA to RNA

Created on Fri Apr 24 11:06:45 2020

@author: lev
"""

file = open("rosalind_rna.txt", "r")

to_process = file.readline() #array

file.close()

#need to replace every T by an U 

def replace_t_by_u(nova_dna):
    
    nova_rna = ""
    
    for i in nova_dna:
        if i == "T":
            nova_rna = nova_rna + "U"
        else:
            nova_rna = nova_rna + i
            
    return nova_rna
    


rna = replace_t_by_u(to_process)
print(rna)


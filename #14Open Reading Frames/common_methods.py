from collections import OrderedDict #changed implementation to ordered dictionary

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Common Methods in Bioinformatics to avoid re coding

Created on Sat May  2 10:46:47 2020

@author: lev
"""

#method 1: process dna information in FASTA format
#
# FASTA FORMAT:
#
# >DNA_NAME
# DNA_STRING
# STRING MAY OCCUPY MORE THAN 1 LINE

#WORKS WELL 
def process_dna_file(file): #returns the Ordered map {dna_name : dna_string}
    file_lines = file.readlines()
    dna_string = ""
    dna_name = ""
    dna_map = OrderedDict()
    
    
    for i in range(len(file_lines)): #list form
        
        if i == 0: #first case, always a name
            dna_name = file_lines[i][1:].strip('\n') #removes '>'
            continue
    
        if file_lines[i][0] == ">": 
            dna_map[dna_name] = dna_string
            dna_string = "" #clear string
            dna_name = file_lines[i][1:].strip('\n') #update name reference
            continue
    
        
        dna_string += file_lines[i].strip("\n")
        
        if i == len(file_lines) -1: #last case check
            dna_map[dna_name] = dna_string
    
    return dna_map

#method 2: complementing a dna string 

#nucleotides complement the following way:
# A <-> T
# C <-> G

def complement_dna_string(dna): #returns the complemented version of var dna

    c_dna_string = ''    

    for nucleotide in dna:
        
        if nucleotide == 'A':
            
            c_dna_string += 'T'
            
        elif nucleotide == 'C':
            
            c_dna_string += 'G'
            
        elif nucleotide == 'T':
        
            c_dna_string += 'A'
            
        else:
            
            c_dna_string += 'C'

    return c_dna_string 


#method 3: getting a list of only the dna strings.
def get_dna_strings(dna_map):
    
    dna_strings = []
    
    for dna in dna_map.values():
        dna_strings.append(dna)
    
    return dna_strings

#method 4 translating from rna to protein (nucleotide)

def rna_to_protein(rna_string):
    protein = ""
    
    for i in range(0, len(rna_string), 3):
        codon = rna_string[i: i+3]
        
        tiebreaker = codon[-1]
        
        codon = codon[:2]
        
        if codon == "GG":
            protein += "G"
        elif codon == "GC":
            protein += "A"
        elif codon == "GU":
            protein += "V"
        elif codon == "AC":
            protein += "T"
        elif codon == "CG":
            protein += "R"
        elif codon == "CC":
            protein += "P"
        elif codon == "CU":
            protein += "L"
        elif codon == "UC": #done with unique 2 letter identifiers
            protein += "S"
        else:#protein must belong to the proteins that have a tiebreaker
        
            if codon == "UU":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "F"
                else:
                    protein += "L"
            elif codon == "UA":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "Y"
           
            elif codon == "UG":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "C"
                elif tiebreaker == "G":
                    protein += "W"
            
            elif codon == "CA":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "H"
                else:
                    protein += "Q"
            elif codon == "AU":
                if tiebreaker == "U" or tiebreaker == "C" or tiebreaker == "A":
                    protein += "I"
                else:
                    protein += "M"
            elif codon == "AA":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "N"
                else:
                    protein += "K"
            elif codon == "AG":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "S"
                else:
                    protein += "R"
            elif codon == "GA":
                if tiebreaker == "U" or tiebreaker == "C":
                    protein += "D"
                else:
                    protein += "E"
    return protein
    
#method 5 translating a dna string to rna

def dna_to_rna(dna):
    rna = ""
    
    for char in dna:
        
        if char == "T":
            rna += 'U'
        else:
            rna+= char
        
    
    return rna


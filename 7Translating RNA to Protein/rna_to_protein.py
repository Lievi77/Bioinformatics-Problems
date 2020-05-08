#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 7: Translating RNA into proteins.

Created on Sun Apr 26 11:39:29 2020

@author: lev
"""

#to be optimized

file = open("rosalind_prot.txt","r") #rna string

def translate_codon(codon, tiebreaker):
    protein = ""
    
    if codon == "GG":
        protein = "G"
    elif codon == "GC":
        protein = "A"
    elif codon == "GU":
        protein = "V"
    elif codon == "AC":
        protein = "T"
    elif codon == "CG":
        protein = "R"
    elif codon == "CC":
        protein = "P"
    elif codon == "CU":
        protein = "L"
    elif codon == "UC": #done with unique 2 letter identifiers
        protein = "S"
    else:#protein must belong to the proteins that have a tiebreaker
        
        if codon == "UU":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "F"
            else:
                protein = "L"
        elif codon == "UA":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "Y"
           
        elif codon == "UG":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "C"
            elif tiebreaker == "G":
                protein = "W"
            
        elif codon == "CA":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "H"
            else:
                protein = "Q"
        elif codon == "AU":
            if tiebreaker == "U" or tiebreaker == "C" or tiebreaker == "A":
                protein = "I"
            else:
                protein = "M"
        elif codon == "AA":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "N"
            else:
                protein = "K"
        elif codon == "AG":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "S"
            else:
                protein = "R"
        elif codon == "GA":
            if tiebreaker == "U" or tiebreaker == "C":
                protein = "D"
            else:
                protein = "E"
        
    
    return protein

def translate(rna): #returns the translated rna. rna var is a file instance
     protein_string = ""
     codon = " "
     
     while codon:
         codon = rna.read(2) 
         tiebreaker = rna.read(1)
         
         protein_string += translate_codon(codon,tiebreaker)
         
     return protein_string

#main 
protein_string = translate(file)
print(protein_string)



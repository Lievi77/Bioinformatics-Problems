import common_methods as cm 
import math 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 14: Open Reading Frames (ORF)

Created on Fri May  8 12:25:44 2020

@author: lev
"""

#---------------------------------METHODS-------------------------------------
def get_arrangements(rna_string):
    arrangements = [rna_string]
    
    length = int( math.remainder(len(rna_string), 3) )
    
   
    
    for i in range(length):
        sub = rna_string[i:]
        arrangements.append(sub)
    
    
    return arrangements


def get_stop_codon_index(rna, start_index, isrevc):
    
    i = start_index
    
    while i < len(rna):
        
        codon = rna[i:i+3]
        
        if isrevc:
            codon = codon[::-1]
            codon = cm.complement_rna(codon)
        
        
        if codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
            break
        
        
        i+= 3
    
    if i >= len(rna):
        i = -1
    
    
    return i 

def get_open_reading_frames(dna_strand):
    
    candidates = []
    
    start_codon  = 'AUG'
    
    #six total posibilities 
    #3 from normal rna start codon AUG with stop codon UAG UGA UAA
    #Other 3 from reverse complement 
    
    #first get the dna translated to rna 
    rna = cm.dna_to_rna(dna_strand)
    
    #then also get the reverse complement 
    
    
    revc_rna = cm.complement_rna( rna[::-1] )
    
    #need to consider ALL Translations EX: AUGCUGAC -> AUGCUG, UGCUGA, GCUGAC
    
    
    
        
        
                
                
    
    return candidates
    




#--------------------------------MAIN-----------------------------------------
def main():
    dna_map = cm.process_dna_file( open("test.txt", "r") )
    
    dna_strands = cm.get_dna_strings(dna_map)
    
    candidates = get_open_reading_frames(dna_strands[0]) # return a list contaning all dna substrings valid for translation
    
    
    for candidate in candidates:
        print(cm.rna_to_protein(candidate))


main() #execute the main routine



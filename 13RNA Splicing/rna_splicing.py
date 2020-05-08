import common_methods as cm
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 13: RNA Splicing

Created on Thu May  7 13:13:46 2020

@author: lev
"""
#-----------------------------METHODS------------------------------------------


def splice_dna(dna_string, introns):#splices the dna
    
    
    outron = dna_string 

    for intron in introns:
        
        
        index_of_intron = 1000 #random placeholder to activate the loop
        
        while index_of_intron > 0:
            index_of_intron = outron.find(intron)
            outron = outron[:index_of_intron] + outron[index_of_intron + len(intron):]   
            index_of_intron = outron.find(intron)
    
    
    
    rna = cm.dna_to_rna(outron)
    protein = cm.rna_to_protein(rna)
    return protein

#-----------------------------MAIN---------------------------------------------

def main(): #main method
    
    dna_strings = cm.process_dna_file(open("rosalind_splc.txt", "r"))
    
    dna_strings = cm.get_dna_strings(dna_strings)
    
    output = splice_dna(dna_strings[0], dna_strings[1:])
    
    print(output)
    

main()
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
    
    
    
    pass




#-----------------------------MAIN---------------------------------------------

def main(): #main method
    
    dna_strings = cm.process_dna_file(open("test.txt", "r"))
    
    dna_strings = cm.get_dna_strings(dna_strings)
    
    output = splice_dna(dna_strings[0], dna_strings[1:])
    
    print(output)
    

main()
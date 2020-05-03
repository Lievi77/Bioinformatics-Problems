import common_methods as cm
from collections import OrderedDict
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 12: Finding a shared motif  (longest sublist)

Created on Sun May  3 13:31:32 2020

@author: lev
"""
#------------------------------METHODS-----------------------------------------

def is_common(substring, dna_map, current_dna):
    
    verdict = None
    
    for dna in dna_map.values():
        
        if dna == current_dna:
            continue
        
        verdict = substring in dna
        
        if not verdict:
            return False

    
    return verdict

def find_longest_common_sub_dna(dna_map):
    
    longest_sub_dna = "" #empty string initialization
    
    
    for dna in dna_map.values(): #loop through dna_strings
        
        substring = ""
    
        #the next loop generates every single possible substring
        #must change to so that substring goes from largest to smallest
        
        
                    
                    
                    
    return longest_sub_dna
#-------------------------------MAIN-----------------------------------------

def main():
    dna_map = cm.process_dna_file(open("rosalind_lcsm.txt","r")) #ORDERED DICTIONARY
    
    
    longest_motif = find_longest_common_sub_dna(dna_map)
    
    
    print(longest_motif)

#execute main method
main()





import common_methods as cm 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 14: Open Reading Frames (ORF)

Created on Fri May  8 12:25:44 2020

@author: lev
"""

#---------------------------------METHODS-------------------------------------

def get_open_reading_frames(dna_strands):
    pass




#--------------------------------MAIN-----------------------------------------
def main():
    dna_map = cm.process_dna_file( open("test.txt", "r") )
    
    dna_strands = cm.get_dna_strings(dna_map)
    
    candidates = get_open_reading_frames(dna_strands[0]) # return an array contaning all dna substrings valid for translation
    
    cm.print_list(candidates)

main() #execute the main routine



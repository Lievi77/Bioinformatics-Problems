import common_methods as cm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 12: Finding a shared motif  (longest sublist)

Created on Sun May  3 13:31:32 2020

@author: lev
"""
#------------------------------METHODS-----------------------------------------

def build_sa(string): #build the suffix arrays. 
    pass

def decode(string, rules): #decodes the string using rules

    pass
    

def largest_common_substring(dna_list): 
    
    #we will use a suffix array approach
    #since our input can be up tp 100 dna strands
    #dynamic programming can quickly get out of hand
    
    #first step, concatenate the strings and use unique sentinels
    #map alphabet to natural numbers
    #shift up for the number of sentinel characters you need
    
    big_dna = ""
    alphabet_map = {} #order does not matter { mapped_value : CHAR ITS referring to }
    
    #building the map, 
    alphabet_map[chr(200)]= "A"
    alphabet_map[chr(220)] ="T"
    alphabet_map[chr(240)] = "C"
    alphabet_map[chr(260)] = "G"
    
    #build the big_dna string using the map defined above
    
    for i in range(len(dna_list)):
        coded_dna = ""
        
        for char in dna_list[i]: #loop to code the dna string
            
            if char == "A":
                coded_dna += chr(200)
            elif char == "T":
                coded_dna += chr(220)
            elif char == "C":
                coded_dna += chr(240)
            else:
                coded_dna += chr(260)
        
        if i == 0: #first instance does not have a sentinel in front
            big_dna += coded_dna
        else:
            sentinel = chr(i + 33) #sentinels go from [33,132]
            big_dna += sentinel + coded_dna
            
    print(big_dna)
    
    
    
    #next, build a suffix array
    build_sa(big_dna)
    
    
            
    
#-------------------------------MAIN-----------------------------------------

def main():
    dna_map = cm.process_dna_file(open("test.txt","r")) #ORDERED DICTIONARY
    
    dna_list = cm.get_dna_strings(dna_map)
    
    output = largest_common_substring(dna_list)
    
    print(output)
    
#execute main method
main()

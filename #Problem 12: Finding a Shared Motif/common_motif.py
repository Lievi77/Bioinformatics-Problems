import common_methods as cm

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 12: Finding a shared motif  (longest sublist)

Created on Sun May  3 13:31:32 2020

@author: lev
"""
#------------------------------METHODS-----------------------------------------

def find_lcsm(suffix):
    #algorithm to find the largest common substring ussing a suffix array

    pass

def radix_sort(a):
    #radix sort implementation
    
    pass


def build_sa(string): #build the suffix arrays. 
    #NOTE that a special character (ASCII 32-132) will always be of index 0    

    #we will use the Skew Algorithm to construct the suffix array
    
    #we will divide the string into 3 major groups:
        
    #1: (index mod 3 = 0)
    #2: (index  mod 3 = 1)
    #3: (index mod 3 = 2)
    
    #then we will handle recursively (index mod 3 = 1) and (index mod 3 = 2)
    #merge (index mod 3 = 0) group at the very end
    
    pass

def decode(string, rules_map): #decodes the string using rules. WORKS WELL
    
    decoded_string = ""
    
    for char in string:
        
        if ord(char) > 32 and ord(char) < 133:
            decoded_string += "|"
            continue
        
        
        decoded_string += rules_map[char] 
    
    
    return decoded_string 
    

def largest_common_substring(dna_list): 
    
    #we will use a suffix array approach
    #since our input can be up to 100 dna strands
    #dynamic programming can quickly get out of hand
    
    #first step, concatenate the strings and use unique sentinels
    #map alphabet to natural numbers
    #shift up for the number of sentinel characters you need (100 in this case)
    
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
        
        sentinel = chr(i+33) #sentinels go from ASCII [33,132] (assuming we have at most 100 dna strings)
        big_dna += coded_dna + sentinel
        
    #next, build a suffix array
    suffix_array = build_sa(big_dna) #call to build the suffix array
    print("suffix_array: " + str(suffix_array))
    
    
    #after successful build now get the common substring
    
    lcsm = find_lcsm(suffix_array)
    
    #then just print
    
    print("lcsm: " + str(lcsm))
    
            
    
#-------------------------------MAIN-----------------------------------------

def main():
    dna_map = cm.process_dna_file(open("rosalind_lcsm.txt","r")) #ORDERED DICTIONARY
    
    dna_list = cm.get_dna_strings(dna_map)
    
    output = largest_common_substring(dna_list)
    
    print("output: " + str(output))
    
    
    
#execute main method
main()

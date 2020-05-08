import common_methods as cm 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 10: Locating Restriction Sites (reverse palindromes)

Created on Sat May  2 11:09:29 2020

@author: lev
"""

#------------------------------METHODS----------------------------------------

def find_reverse_palindromes(dna_map):
    
    for dna in dna_map.values():
        
        for i in range(len(dna)): #make every sublist possible 
            for j in range(4,13): #of length between 4 and 12
                
                if i+j > len(dna): #if index overflows, omit word
                    continue
                
                sub_dna = dna[i:i+j]
                
                reverse_complement_dna = cm.complement_dna_string(sub_dna)
                reverse_complement_dna = reverse_complement_dna[::-1]
                
                if sub_dna == reverse_complement_dna:
                    print(i+1 , len(reverse_complement_dna) )




#-------------------------------MAIN------------------------------------------

def main():
    dna_map = cm.process_dna_file( open('rosalind_revp.txt', 'r') ) #this is a map 
    find_reverse_palindromes(dna_map)
    
main()  
    

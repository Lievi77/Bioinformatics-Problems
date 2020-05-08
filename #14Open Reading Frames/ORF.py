import common_methods as cm 
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 14: Open Reading Frames (ORF)

Created on Fri May  8 12:25:44 2020

@author: lev
"""

#---------------------------------METHODS-------------------------------------
def get_stop_codon_index(rna, starting_index):
    pass


def get_open_reading_frames(dna_strand):
    
    candidates = []
    
    start_codon = "AUG"
    
    stop_codon1 = "UAG"
    
    stop_codon2 = "UGA"
    
    stop_codon3 = "UAA"
    
    #six total posibilities 
    #3 from normal rna start codon AUG with stop codon UAG UGA UAA
    #Other 3 from reverse complement 
    
    #first get the dna translated to rna 
    rna = cm.dna_to_rna(dna_strand)
    #then also get the reverse complement 
    revc_rna = cm.dna_to_rna( cm.complement_dna_string(dna_strand[::-1]) )
    
    #then just detect the start and ending codons
    #we can scan both with only 1 loop
    
    for i in range(len(dna_strand) - 6):
        codon = rna[i: i+3 ]
        anti_codon = revc_rna[i : i +3]
        
        
        if codon == start_codon: #fix indexing problem
            j = i + 3 #start searching outside the start codon
            stop_codon = ""
            while j <= len(dna_strand):
                codon2 = rna[j : j + 3]
                
                if codon2 == stop_codon1 or codon2 == stop_codon2 or codon == stop_codon3:
                    stop_codon = codon2
                    stop_codon_index = j
                    
                    
                
                j+=1
            
            candidate = rna[i: stop_codon_index  ]
            print(candidate)
            candidates.append(candidate)
            
            print(codon, stop_codon)
            
            
            
        
    for i in range(len(candidates)): #translating rna to protein 
        candidates[i] = cm.rna_to_protein(candidates[i])        
    
    return candidates




#--------------------------------MAIN-----------------------------------------
def main():
    dna_map = cm.process_dna_file( open("test.txt", "r") )
    
    dna_strands = cm.get_dna_strings(dna_map)
    
    candidates = get_open_reading_frames(dna_strands[0]) # return a list contaning all dna substrings valid for translation
    
    for candidate in candidates:
        print(candidate)

main() #execute the main routine



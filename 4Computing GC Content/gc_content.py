#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 4: Computing GC Content

Created on Fri Apr 24 18:36:22 2020

@author: lev
"""

file = open("rosalind_gc.txt","r")

#dictionary data structure
# x = { key:data , key:data }

lines = file.readlines()
file.close() #good practice

#idea: build a map from name of dna string -> actual dna string 
#example 'name1' : "dna_string"

#returns a tuple (dna_map, gc_map)
def build_maps(input_dna):
    d = {} #empty dictionary 
    gc = {} #empty dictionary
    
    #loop works why? because we are guaranteed this format:
    #> dna_label_id
    #[actual_dna_string]
    #two pointers
    for i in range(len(input_dna) - 1): #i goes from 0 to len -2
        j = i + 1 #j appears always in front of i
        
        pointer_i = input_dna[i]
        
        
        if pointer_i[0] != ">":
            continue #goes back to the top immediately
       
        #if code reaches this point, then i is an id
        dna_id = pointer_i[1:-1] #to eliminate the "\n" character
        dna_string = ""
        
        #this loop is to extract the entire dna_string
        while(j < len(input_dna) ):
            data = input_dna[j]
            
            if data[0] == '>':
                break
            dna_string = dna_string + data[:-1]
            j = j + 1
        
        #map construction
        d[dna_id] = dna_string
        
        gc_number = calculate_gc(dna_string)
        
        gc[dna_id] = gc_number
        
    return (d,gc)


#calculates the gc of the dna_string
#aka the percentace of "G" and "C" a string has
# Example: AGCTATAG has a gc of 37.5 
# formula is number_of_gc_occurences / len(dna_string) * 100
def calculate_gc(dna_string):
    gc = 0
    for i in dna_string:
        if i == "G" or i == "C":
            gc = gc +1
    
    gc = (gc / len(dna_string) ) * 100
    
    gc = round(gc,6)
    
    return gc

#returns the greatest gc and its id
def greatest_gc(gc_map):
    greatest_key = ""
    greatest_gc = 0
    
    for dna in gc_map:
        if gc_map[dna] > greatest_gc:
            greatest_gc = gc_map[dna]
            greatest_key = dna
            
    print(greatest_key + "\n" + str(greatest_gc))
        

greatest_gc(build_maps(lines)[1])

    


    






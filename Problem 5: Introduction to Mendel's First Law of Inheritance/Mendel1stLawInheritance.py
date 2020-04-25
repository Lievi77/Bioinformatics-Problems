import math
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 5: Introduction to Mendel's First Law of Inheritance

Created on Fri Apr 24 19:57:10 2020

@author: lev
"""

file = open("rosalind_iprb.txt","r")


def get_population(file):
    population= []
    
    for line in file:
        
        population = line.split()
    
    return population


population = get_population(file) #this will be a list of format [k,m,n]
file.close() #good practice

def comb(n,r):
    f = math.factorial
    return f(n) // f(r) // f(n-r)

#base de algoritmo:
#
#primero identifica como funciona los Punnet Squares
#despues generaliza en terminos de k,m,n 

#since there are 3 pools of population, there are 6 possible combinations

def dominant_allele_prob(k,m,n):
    total_prob = 0  
    
    #we know that a k x k breed yields all offspring with a dominant trait
    comb_kk= 1 * comb(k,2)
    comb_km = 1 * comb(k,1) * comb(m,1)
    comb_kn = 1 * comb(k,1) * comb(n,1)
    comb_mm = 3/4 * comb(m,2)
    comb_mn = 1/2 * comb(n,1) * comb(m,1)
    comb_nn = 0 * comb(n,2)
    
    total_prob = (comb_kk + comb_km + comb_kn + comb_mm + comb_mn +comb_nn)
    total_prob = total_prob/comb(k+m+n ,2)
    
    return round(total_prob,5)

k = int(population[0])
m = int(population[1])
n = int(population[2])



print( dominant_allele_prob(k,m,n) )

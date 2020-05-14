import common_methods as cm
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 15: Calculating Expected Offspring 

Created on Sat May 14 11:18:47 2020

@author: lev
"""

# -------------------------------METHODS------------------------------


def calculate_odds(population):
    # some notes:
    # each number is the number of couples possession the following genes:

    # at index 0: AA-AA (note that uppercase letters refer to a dominant allele)
    # at index 1: AA-Aa
    # at index 2: AA-aa
    # at index 3: Aa-Aa
    # at index 4: Aa-aa
    # at index 5: aa-aa

    # since we are assuming every pair only has 2 children we have the following variable
    offspring = 2

    probability_AA_AA = 1  # probabilities calculated manually using Punnett Squares
    probability_AA_Aa = 1
    probability_AA_aa = 1
    probability_Aa_Aa = 3/4
    probability_Aa_aa = 1/2
    probability_aa_aa = 0

    # store the probabilities in a list equal to len(populations)
    probabilities = [probability_AA_AA, probability_AA_Aa, probability_AA_aa,
                     probability_Aa_Aa, probability_Aa_aa, probability_aa_aa]

    expectancy = 0

    # Offspring dominant allele probability is a uniform distribution
    # remember that expectancies are distributive
    # E[X+Y+Z] = E[X] + E[Y] + E[Z]

    for i in range(len(population)):
        # Expectancy of a Uniform Distribution:
        # E[X] = (a+b)/2 Where a is the minimum value and B is the max value

        current_pop = int(population[i]) * offspring
        # minimum value is how many at least are expected
        # maximum is how many at most are expected
        # both are determined by the probability given by a punnet square
        expectancy += (probabilities[i] *
                       current_pop + probabilities[i] * current_pop)/2

    return expectancy


# -------------------------------MAIN---------------------------------


def main():
    # algorithm to get the integers in an array
    file = open("rosalind_iev.txt", "r")

    offspring_population = cm.read_population_input(file)

    odds = calculate_odds(offspring_population)

    print(odds)


main()

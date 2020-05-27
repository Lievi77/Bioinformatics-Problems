import common_methods as cm
import math
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Problem 14: Open Reading Frames (ORF)

Created on Fri May  8 12:25:44 2020

@author: lev
"""

# ---------------------------------METHODS-------------------------------------


def get_arrangements(rna_string):
    arrangements = [rna_string]

    length = len(rna_string) % 3  # modulo 3, number of arrangements

    for i in range(length):
        sub = rna_string[i + 1:]

        arrangements.append(sub)

    return arrangements


def get_stop_codon_index(rna, start_index):

    i = start_index

    while i < len(rna):

        codon = rna[i:i+3]

        if codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
            break

        i += 3  # scanning in groups of 3

    if i >= len(rna):
        i = -1

    return i


def get_open_reading_frames(dna_strand):

    candidates = []

    start_codon = 'AUG'

    # six total posibilities
    # 3 from normal rna start codon AUG with stop codon UAG UGA UAA
    # Other 3 from reverse complement

    # first get the dna translated to rna
    rna = cm.dna_to_rna(dna_strand)
    revc_rna = cm.complement_rna_string(rna)
    revc_rna = revc_rna[::-1]

    # need to consider ALL Translations EX: AUGCUGAC -> AUGCUG, UGCUGA, GCUGAC

    for i in range(len(rna)-2):
        codon = rna[i:i+3]

        if codon == start_codon:  # works well

            j = get_stop_codon_index(rna, i + 3)  # we are in normal rna

            # handle the not found case (j= -1)
            if j < 0:
                continue

            candidate = rna[i: j]  # for not, we exclude the stop protein

            arrangements = get_arrangements(candidate)

            # loop to append the candidates:
            for arrangement in arrangements:

                if arrangement in candidates:  # checks for repeated arrangements
                    continue

                candidates.append(arrangement)

        # at the same time, we analyze the revc string
        anti_codon = revc_rna[i: i + 3]

        if anti_codon == start_codon:
            k = get_stop_codon_index(revc_rna, i + 3)

            if k < 0:  # no stop codon caste
                continue

            candidate = revc_rna[i:k]

            arrangements = get_arrangements(candidate)  # get arrangements

            for arrangement in arrangements:

                if arrangement in candidates:  # checks for repeated arrangements
                    continue

                candidates.append(arrangement)

    return candidates


# --------------------------------MAIN-----------------------------------------
def main():
    dna_map = cm.process_dna_file(open("rosalind_orf.txt", "r"))

    dna_strands = cm.get_dna_strings(dna_map)

    # return a list contaning all dna substrings valid for translation
    candidates = get_open_reading_frames(dna_strands[0])

    for candidate in candidates:
        print(cm.rna_to_protein(candidate))  # print the proteins


main()  # execute the main routine

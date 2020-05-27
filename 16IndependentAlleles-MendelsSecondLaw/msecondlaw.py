import common_methods as cm
'''
 *******************************************************
 * Author: Lev Cesar Guzman Aparicio		           *
 * Email: lguzm038@uottawa.ca or lguzm77@gmail.com     *
 * Problem #16 : Finding Independent Alleles           *
 *      				                               *
 *******************************************************
'''
# ---------------------METHODS----------------------------------------------------------------


def get_AaBb_probability(n):
    pass


# ---------------------MAIN-------------------------------------------------------------------

def main():
    file = open("test.txt", "r")
    inputs = cm.read_population_input(file)

    odds = get_AaBb_probability(inputs)
    print(inputs)


main()

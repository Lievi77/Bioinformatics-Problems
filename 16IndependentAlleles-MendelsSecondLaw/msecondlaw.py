import common_methods as cm


# -------------------Methods-------------------------
# inputs is a list of integers
def get_fam_tree_prob(inputs):
    pass


# -------------------Main-------------------------
def main():
    # usual algorithm
    file = open("test.txt", "r")
    # remember that cm returns a list containg the inputs
    inputs = cm.read_population_input(file)

    # return a double
    odds = get_fam_tree_prob(inputs)

    print(odds)

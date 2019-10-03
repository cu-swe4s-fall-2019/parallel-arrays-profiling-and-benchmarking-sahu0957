import sys
import math
import argparse


def list_mean(L):
    # Return None if list is empty, or is none
    if L is None:
        return None
    if len(L) == 0:
        return None

    s = 0

    for l in L:
        try:
            s += l
        except TypeError:
            # Nonnumber entries will throw an error
            return('Detected nonnumber value in list! Exiting...')
            sys.exit(0)
    return(s/len(L))


def list_stdev(L):
    # Return None if list is empty, or is None
    if L is None:
        return None
    if len(L) == 0:
        return None
    else:
        mean = list_mean(L)
        if len(L) == 1:
            # Standard Deviation calculations require at
            # least 2 numbers
            return("Can't calculate stdev on single \
                                    entry! Exiting...")
            sys.exit(0)
        stdev = math.sqrt(sum([(mean-x)**2 for x in L]) / (len(L) - 1))
        return stdev


if __name__ == '__main__':
    # Read input arguments, if the function is called as the main
    parser = argparse.ArgumentParser(
        description="calculate mean and std. dev of an input list")

    parser.add_argument("numeric_list", help="input list", type=list)
    args = parser.parse_args()
    input_list = [float(i) for i in args.numeric_list]
    r = list_mean(input_list)
    p = list_stdev(input_list)
    print('list mean:', r)
    print('list standard deviation:', p)

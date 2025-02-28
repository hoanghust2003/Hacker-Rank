#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    l = s.split()
    capitalized_l = [x.capitalize() for x in l]
    capitalized_s = " ".join(capitalized_l)
    return capitalized_s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


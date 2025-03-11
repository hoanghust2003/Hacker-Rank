# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        try:
            S = input().strip()
            re.compile(S)
            print("True")
        except re.error:
            print("False")

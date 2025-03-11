# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    s, k = input().split()
    try:
        k = int(k)
    except ValueError:
        print("Please input a number")
    chars = sorted(s)
    for r in range(1, k + 1):
        for combo in combinations(chars, r):
            print(''.join(combo))

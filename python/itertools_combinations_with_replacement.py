from itertools import combinations_with_replacement

if __name__ == '__main__':
    s, r = input().split()
    try:
        r = int(r)
    except ValueError:
        print("Enter an integer")

    chars = sorted(s)

    combos = combinations_with_replacement(chars, r)
    for combo in combos:
        print(''.join(combo))

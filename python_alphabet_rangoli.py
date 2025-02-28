def print_rangoli(size):
    alphabet = [chr(97 + i) for i in range(size)]

    w = 4 * size - 3

    lines = []
    for i in range(size):
        center = alphabet[size - 1 - i:]
        center = center[::-1]
        row = '-'.join(center + center[-2::-1])
        lines.append(row.center(w, '-'))

    for l in lines:
        print(l)
    for l in lines[-2::-1]:
        print(l)

if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        print(ValueError)
    print_rangoli(n)

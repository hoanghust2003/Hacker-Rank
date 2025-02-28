def print_formatted(number):
    # your code goes here
    width = len(bin(number)[2:])

    for i in range(1, number+1):
        dec = str(i)
        octa = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binany = bin(i)[2:]
        print(f"{dec:>{width}} {octa:>{width}} {hexa:>{width}} {binany:>{width}}")

if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        print(ValueError)
    print_formatted(n)
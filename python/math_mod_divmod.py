if __name__ == '__main__':
    try:
        a = int(input())
        b = int(input())
    except ValueError:
        print('Please enter a number.')

    print(a // b)

    print(a % b)

    print(divmod(a, b))

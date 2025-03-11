if __name__ == '__main__':
    m = int(input())
    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    sym_diff = a.symmetric_difference(b)
    print('\n'.join(map(str, sorted(sym_diff))))

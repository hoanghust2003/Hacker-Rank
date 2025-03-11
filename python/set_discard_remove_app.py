if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    q = int(input())

    for _ in range(q):
        command = input().split()
        operation = command[0]

        if operation == 'pop':
            if s:
                s.remove(min(s))
        elif operation == 'remove':
            try:
                s.remove(int(command[1]))
            except KeyError:
                continue
        elif operation == 'discard':
            s.discard(int(command[1]))

    print(sum(s))

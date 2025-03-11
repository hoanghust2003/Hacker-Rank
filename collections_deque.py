from collections import deque

if __name__ == '__main__':
    d = deque()
    try:
        n = int(input())
    except ValueError:
        print("Please input a number")

    for _ in range(n):
        command = input().split()
        method = command[0]

        if method == 'append':
            d.append(int(command[1]))
        elif method == 'appendleft':
            d.appendleft(int(command[1]))
        elif method == 'pop':
            d.pop()
        elif method == 'popleft':
            d.popleft()

    print(' '.join(map(str, d)))

from collections import defaultdict

if __name__ == '__main__':
    try:
        n, m = map(int, input().split())
    except ValueError:
        print(ValueError)

    d = defaultdict(list)

    for i in range(n):
        word = input().strip()
        d[word].append(i + 1)

    for _ in range(m):
        word = input().strip()
        if d[word]:
            print(' '.join(map(str, d[word])))
        else:
            print(-1)

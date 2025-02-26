if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    base_list = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                base_list.append([i, j, k])

    answer = [m for m in base_list if m[1] +m[0] + m[2] != n ]
    print(answer)
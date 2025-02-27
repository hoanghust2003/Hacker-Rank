if __name__ == '__main__':
    data = list(map(int, input().split()))
    n = data[0]
    m = data[1]

    # print(n)
    # print(m)
    for i in range(0, n):
        if i == (n-1)/2:
            for j in range(0,m):
                if j == (((m-1)/2)-3):
                    print("WELCOME",end="")
                elif (((m-1)/2)-3) < j <= (((m-1)/2)+3):
                    continue
                else:
                    print("-", end="")
            print("")
            continue
        for j in range(0, m):
            if i >= (n-1)/2:
                i= n-1 -i
            if j % 3 == ((m-1)/2)%3 and (((m-1)/2)-i*3) <= j <= (((m-1)/2)+i*3):
                print ("|", end="")
            elif (((m-1)/2)-i*3-1) <= j <= (((m-1)/2)+i*3+1):
                print(".", end="")
            else:
                print("-", end="")

        if i == n-1:
            break
        print("")

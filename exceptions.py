if __name__ == '__main__':
    try:
        t = int(input())
    except ValueError:
        print("Please input a number")

    for _ in range(t):
        try:
            a, b = input().split()
            result = int(a) // int(b)
            print(result)
        except ZeroDivisionError as e:
            print("Error Code:", e)
        except ValueError as e:
            print("Error Code:", e)

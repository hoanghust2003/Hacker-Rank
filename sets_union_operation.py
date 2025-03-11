if __name__ == '__main__':
    try:
        n = int(input())
        english = set(map(int, input().split()))

        m = int(input())
        french = set(map(int, input().split()))
    except ValueError:
        print("Please input a number")


    total_subscribers = len(english.union(french))
    print(total_subscribers)

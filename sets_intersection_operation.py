if __name__ == '__main__':
    try:
        n = int(input())
        english = set(map(int, input().split()))

        m = int(input())
        french = set(map(int, input().split()))
    except ValueError:
        print("Please input a number")

    both_subscribers = len(english.intersection(french))
    print(both_subscribers)

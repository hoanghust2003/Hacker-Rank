if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        command, *s_number = input().split()
        if len(s_number)!=0:
            number = list(map(int, s_number))

        if command == "append":
            my_list.append(number[0])

        elif command == "insert":
            my_list.insert(number[0], number[1])

        elif command == "pop":
            my_list.pop()

        elif command == "reverse":
            my_list.reverse()

        elif command == "sort":
            my_list.sort()

        elif command == "remove":
            my_list.remove(number[0])

        elif command == "print":
            print(my_list)

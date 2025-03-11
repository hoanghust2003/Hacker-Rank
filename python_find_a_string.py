def count_substring(string, sub_string):
    n = 0
    l1 = len(string)
    l2 = len(sub_string)
    for i in range(l1):
        if string[i:i+l2] == sub_string:
            n += 1
    return n


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

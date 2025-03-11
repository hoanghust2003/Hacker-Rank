if __name__ == '__main__':
    s = input()
    list = list(s)
    l1, l2, l3, l4, l5 = 0 , 0, 0, 0 , 0

    for s in list:
        if s.isalnum() is True:
            l1 += 1
        if s.isalpha() is True:
            l2 += 1
        if s.isdigit() is True:
            l3 += 1
        if s.islower() is True:
            l4 += 1
        if s.isupper() is True:
            l5 += 1
    if l1 > 0:
        print('True')
    else:
        print('False')
    if l2 > 0:
        print('True')
    else:
        print('False')
    if l3 > 0:
        print('True')
    else:
        print('False')
    if l4 > 0:
        print('True')
    else:
        print('False')
    if l5 > 0:
        print('True')
    else:
        print('False')


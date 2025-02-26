if __name__ == '__main__':
    grade_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade_list.append([name, score])

    grade = [x for _, x in grade_list]
    soted_grade = sorted(set(grade))
    out_grade = soted_grade[1]

    out_name = []

    for row in grade_list:
        if row[1] == out_grade:
            out_name.append(row[0])
    out_name.sort()
    for name in out_name:
        print(name)

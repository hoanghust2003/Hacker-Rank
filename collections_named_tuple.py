from collections import namedtuple

if __name__ == '__main__':
    try:
        n = int(input())
        columns = input().split()
    except ValueError:
        print("Please input a number")
    Student = namedtuple('Student', columns)
    total_marks = 0
    for _ in range(n):
        student = Student(*input().split())
        try:
            total_marks += int(student.MARKS)
        except ValueError:
            print("Please input a number")
    print(f"{total_marks/n:.2f}")

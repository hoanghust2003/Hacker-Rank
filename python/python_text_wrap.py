"""
You are given a string  and width .
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n') where the breaks should be
Input Format

The first line contains a string, .
The second line contains the width, .

Constraints

Sample Input 0

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output 0

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ

"""

def wrap(string, max_width):
    result = ""

    for i in range(0,len(string), max_width):
        result += string[i:i+max_width] + "\n"

    return result.rstrip("\n")

if __name__ == '__main__':
    try:
        string, max_width = input(), int(input())
    except ValueError:
        print(ValueError)

    # string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

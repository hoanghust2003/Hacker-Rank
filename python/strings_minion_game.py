def minion_game(string):
    # your code goes here
    vowels = {'A', 'E', 'I', 'O', 'U'}
    n = len(string)
    kevin_score = 0
    stuart_score = 0
    for i in range(n):
        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i
    if kevin_score > stuart_score:
        return "Kevin " + str(kevin_score)
    elif stuart_score > kevin_score:
        return "Stuart " + str(stuart_score)
    else:
        return "Draw"


if __name__ == '__main__':
    s = input()
    minion_game(s)

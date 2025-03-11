if __name__ == '__main__':
    n = int(input())
    unique_countries = set()
    for _ in range(n):
        country = input().strip()
        unique_countries.add(country)
    print(len(unique_countries))

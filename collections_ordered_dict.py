from collections import OrderedDict

if __name__ == '__main__':
    try:
        n = int(input())
    except ValueError:
        print("Please input a number")
    items = OrderedDict()
    for _ in range(n):
        line = input().split()
        try:
            price = int(line[-1])
        except ValueError:
            print("Please input a number")
        item_name = ' '.join(line[:-1])
        if item_name in items:
            items[item_name] = (items[item_name][0] + 1, items[item_name][1])
        else:
            items[item_name] = (1, price)
    for item_name, (quantity, price) in items.items():
        net_price = quantity * price
        print(f"{item_name} {net_price}")

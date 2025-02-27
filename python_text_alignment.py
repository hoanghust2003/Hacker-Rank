if __name__ == '__main__':
    thickness = int(input())  # Nhập độ dày (phải là số lẻ)
    c = 'H'

    for i in range(thickness):
        print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    for i in range((thickness + 1) // 2):  # Dùng // thay vì / để tránh lỗi float
        print((c * thickness * 5).center(thickness * 6))

    for i in range(thickness + 1):
        print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    for i in range(thickness):
        print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

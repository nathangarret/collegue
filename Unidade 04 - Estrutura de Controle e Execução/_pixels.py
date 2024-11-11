def pixels(l):
    res = 0

    for linha in l:
        for v in linha:
            if v == 0:
                res += 1
    return res


lst = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
print(pixels(lst))

lst = [[123, 56, 255], [34, 0, 0], [23, 123, 0], [3, 0, 0]]
print(pixels(lst))
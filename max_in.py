def max_in(list):
    if list[0] == max(list):
        return 1
    else:
        return 1 + max_in(list[1:])

print(max_in([1, 7, 8, 2 , 56, 78 , 12 , 567, 9]))
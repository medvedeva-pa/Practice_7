def print_till_zero(n):
    while n > 1:
        print(n)
        return print_till_zero(n - 1)
    else:
        return 1

print(print_till_zero(10))
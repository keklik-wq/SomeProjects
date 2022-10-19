def find_max(*args):
    min = args[0]
    for a in args:
        if a > min:
            min = a
    print(min)


find_max(4, 1, 2, 3)

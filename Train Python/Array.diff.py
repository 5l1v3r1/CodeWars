def array_diff(a, b):
    for i in range(len(b)):
        while b[i] in a:
            a.pop(a.index(b[i]))
    return a

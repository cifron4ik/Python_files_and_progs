def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        reminder = a[0]
        first = []
        second = []
        third = []
        for n in a:
            if n < reminder:
                first.append(n)
            elif n > reminder:
                second.append(n)
            else:
                third.append(n)
        return quick_sort(first) + third + quick_sort(second)


in_mass = [int(dig) for dig in input().split()]
print(*quick_sort(in_mass))

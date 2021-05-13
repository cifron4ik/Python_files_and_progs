def bubble_sort(a):
    for _ in range(len(a) - 1):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


in_mass = [int(dig) for dig in input().split()]
print(*bubble_sort(in_mass))

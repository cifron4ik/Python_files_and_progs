def selection_sort(a):
    reminder = 0
    for i in range(len(a) - 1):
        reminder = i
    for j in range(len(a) - 1):
        if a[reminder] > a[j]:
            reminder = j
        a[i], a[reminder] = a[reminder], a[i]
    return a


in_mass = [int(dig) for dig in input().split()]
print(*selection_sort(in_mass))

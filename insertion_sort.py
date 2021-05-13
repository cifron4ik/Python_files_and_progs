def insertion_sort(a):
    for i in range(len(a)):
        item = a[i]
        reminder = i - 1
        while reminder >= 0 and a[reminder] > item:
            a[reminder + 1] = a[reminder]
            a[reminder] = item
            reminder -= 1

    return a


in_mass = [int(dig) for dig in input().split()]
print(*insertion_sort(in_mass))

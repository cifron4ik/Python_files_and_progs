def modified_bubble_sort(a):
    flag = True
    while flag:
        flag = 0
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i+1] = a[i+1], a[i]
                flag = True
    return a


in_mass = [int(dig) for dig in input().split()]
print(*modified_bubble_sort(in_mass))

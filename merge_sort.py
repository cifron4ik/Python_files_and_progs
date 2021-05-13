def merge_sort(mass):
    a, b = mass[:len(mass) // 2], mass[len(mass) // 2:]
    left = 0
    right = 0
    new_mass = []
    n, m = len(a), len(b)
    while left < n and right < m:
        if a[left] < b[right]:
            new_mass.append(a[left])
            left += 1
        else:
            new_mass.append(b[right])
            right += 1
    new_mass += a[left:] + b[right:]
    return new_mass


def out_merge(a):
    if len(a) <= 1:
        return a
    return merge_sort(out_merge(a))


in_mass = [int(dig) for dig in input().split()]
print(*out_merge(in_mass))

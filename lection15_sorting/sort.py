def merge_two(l, r):
    new = []
    i1, i2 = 0, 0
    while i1 != len(l) and i2 != len(r):
        # print(new, i1, i2)
        if l[i1] < r[i2]:
            new.append(l[i1])
            i1 += 1
        else:
            new.append(r[i2])
            i2 += 1
    # print(new, i1, i2, "______")

    new.extend(l[i1:])
    new.extend(r[i2:])
    return new


# print(merge_two([3, 5], [9, 7, 4]))


def merge_sort(lst):
    if len(lst) > 1:
        middle = int(len(lst)/2)
        left = lst[:middle]
        right = lst[middle:]

        left = merge_sort(left)
        right = merge_sort(right)
        x = merge_two(left, right)
        return x

    return lst


lst = [1, 6, 8, 2, 3, 5, 9, 7, 4]
merge_sort(lst)

def buble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
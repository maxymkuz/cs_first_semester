lst = [i for i in range(500)]  # -- is sorted
elem = 500
j = 0
start = 0
finish = len(lst)

while lst[j] != elem:
    mid = (start + finish)//2
    if elem > lst[mid]:
        start = mid
    elif elem < lst[mid]:
        finish = mid
    else:
        print("True")
        break
    if start + 1 == finish:
        print("False")
        break
    print(start, finish)


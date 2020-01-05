import random


def isSorted(nums):
    if len(nums) < 2:
        return True
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def bogosort(nums):
    while not isSorted(nums):
        random.shuffle(nums)
    return nums


print(bogosort([1, 5, 6, 7, 8, 7, 10, 4, 11, 220]))
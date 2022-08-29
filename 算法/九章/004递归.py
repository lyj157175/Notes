# 斐波拉契数列
# 0，1，1，2，3，5，8，13，21



def fci_rec(n):
    if n < 2:
        return n

    return fci_rec(n-1) + fci_rec(n-2)


def fci_(n):
    if n < 2:
        return n

    a, b = 1, 2
    for i in range(2, n-1):
        a, b = b, a + b

    return b




# 【题目】递归实现二分法
def erfen_rec(nums, target):
    return binary_search(nums, target, 0, len(nums)-1)

def binary_search(nums, target, left, right):
    if left > right:
        return -1

    # mid = (left + right) / 2
    mid = left + (right - left) / 2
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(nums, target, left, mid-1)
    else:
        return binary_search(nums, target, mid+1, right)








if __name__ == '__main__':
    import time
    n = 37

    t1 = time.time()
    res1 = fci_rec(n)
    t2 = time.time()
    print(res1, t2-t1)

    t1 = time.time()
    res2 = fci_(n)
    t2 = time.time()
    print(res2, t2 - t1)



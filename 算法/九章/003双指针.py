# o(max(m, n)) == o(m + n)

# 常见的o(n)的算法：
# 双指针算法，打擂台算法，单调栈算法，单调队列

# 三种双指针：相向，背向，同向


# 【题目】忽略大小写和非法字符后，字符串是不是回文串
# isdigit(), isalpha(), lower(), upper()
# 双向指针解决



# 【题目】去掉一个字符后，字符串是不是回文串
def fun(s):
    if len(s) == 0:
        return False

    left, right = 0, len(s) - 1
    left, right = find_diff(s, left, right)
    if left >= right: return True

    l1, r1 = find_diff(s, left + 1, right)
    l2, r2 = find_diff(s, left, right - 1)

    return l1 >= r1 or l2 >= r2


def find_diff(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return left, right
        left += 1
        right -= 1
    return left, right



# 【题目】两数之和（hash， 双指针）
def twonum(nums, target):
    nums.sort()
    left, right = 0, len(nums)
    while left < right:
        if nums[left] + nums[right] == target:
            return nums[left], nums[right]
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            left += 1

    return [-1, -1]


# nums_ = [(v, idx_) for idx_, v in enumerate(nums)]
# nums_.sort()




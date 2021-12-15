#时间复杂度： c < logn < n < nlogn < n^2 < n^3 < 2^n < n!

arr = [5,3,2,6,7,1,9,8,4,0]
# 1.冒泡排序: 从0位置开始，0 1比，大的放到1位置，1 2比，大的放到2位置，直到第一次将最大值放到最后
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):   # 控制比较次数
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
        
# print(bubble_sort(arr))


# 2.选择排序: 从i位置开始，依次比较i后面的数和i位置的大小，将较小的数放到i位置
def select_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                min_dex = j
        arr[i], arr[min_dex] = arr[min_dex], arr[i]
    return arr

# print(select_sort(arr))


# 3.插入排序: 模拟打扑克牌，第一个数必然有序，当前数据有序，后来的找到自己的位置并且插入
def insert_sort(arr):
    for i in range(1, len(arr)):
        j = i
        cur = arr[j]  # 待插入的数
        while j >0 and cur < arr[j-1]:
            arr[j] = arr[j-1]  # 前面的数向后移
            j -= 1;
        arr[j] = cur   # 找到自己的位置并且插入
    return arr

# print(insert_sort(arr))

# shell排序,相对插入排序加入以个gap的概念
def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            j = i
            cur = arr[i]
            while j - gap > 0 and cur < arr[j-gap]:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = cur
        gap //= 2
    return arr
            



# 4. 二分法在数组中查找数字: m默认数组是有序的
def binary_search(arr, target):
    if len(arr) == 0:
        return False
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + ((right - left) >> 1)  # 位运算速度大于除法， >> 1相当于除以2，<< 1相当于乘以2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False




# 认识异或运算
#   异或：相同为0， 不同为1。 简单记法：无进位相加
#    6 ^ 7 = 110 ^ 111 = 001
# 异或性质： 0 ^ N = N      N ^ N = 0, 满足交换律和结合律，多个数一起异或与位置无关

# 练习1，交换a和b
# a, b = 10, 33
# a = a^b
# b = a^b
# a = a^b
# print(a, b)

# 练习2：一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到并打印这种数？
# 思路：不需要管排序，将所有的数全部异或起来，偶数个的数异或后全部为0，最后的数就是那个奇数
arr_ = [2,2,3,3,4,4,5,5,5,2,2,3,3,1,1]
def find_eor(arr_):
    eor = 0
    for i in arr_:
        eor = eor ^ i
    return eor
# print(find_eor(arr_))

# 练习3： 一个int型的数，提取出该数中最右侧的一个数字1
# N & (~N + 1)



# 归并排序, 将数组划分到最小在合并，也可以将递归写为非递归的方式：依次以2， 4， 8， 16进行数组的比较
def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            res.append(right.pop(0))
        else:
            res.append(left.pop(0))
    return res + left + right

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

# print(merge_sort(arr))



# 求小和问题：给定一个数组，将每个数字左边比该数字小的数相加为该数的下和，数组中全部数的小和相加为该数组的小和
# 简单思路：循环遍历
# 思路：利用归并排序
def get_small_sum(arr):
    # 主函数
    if len(arr) < 2:
        return 0
    return small_sum(arr, 0, len(arr)-1)

def small_sum(arr, l, r):
    # 求细分数组上的小和
    if l == r:
        return 0;
    mid = l + ((r-l)>>1)
    l_sum = small_sum(arr, l, mid)
    r_sum = small_sum(arr, mid, r)
    all_sum = merge(arr, l, mid, r)
    return l_sum + r_sum + all_sum

def merge(arr, l, mid, r):
    # 在merge过程中寻找小和
    res = []
    sum = 0
    left = l
    right = mid + 1
    while left < mid and right < r:
        if arr[left] <= arr[right]:
            res.append(arr[left])
            sum+=arr[left] * (r-right+1)
            left += 1
        else:
            res.append(arr[right])
            right += 1
    res += arr[left:mid+1]
    res += arr[right:r+1]

    for i in range(l, r+1):
        arr[i] = res.pop(0)
    return sum



# 快速排序
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    mid = [arr[0]]
    small, big = [], []            
    for i in range(1, len(arr)):
        if arr[i] < arr[0]:
            small.append(arr[i])
        elif arr[i] > arr[0]:
            big.append(arr[0])
        else:
            mid.append(arr[i])
    return quick_sort(small) + mid + quick_sort(big)

# print(quick_sort(arr))



 # 计数排序



 # 桶排序：是一种思想，用容器来排序
 # arr = [21, 32, 12, 8, 78, 100, 6]
 # 第一步：位数补齐 arr = [021, 032, 012, 008, 078, 100, 006]， 并且准备0-9个桶
 # 第二步：从个位开始按队列的方式进桶，然后从桶中开始取出
 # 第三步：从十位开始按队列的方式进桶，然后从桶中开始取出
 # 第四步：从百位开始按队列的方式进桶，然后从桶中开始取出，最后即排好序


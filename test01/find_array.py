# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/10

def cross_mid_maxsub(A, low, mid, high):
    """
    寻找跨中点的最大子数组
    :param A:
    :param low:
    :param mid:
    :param high:
    :return:
    """
    left_s = float('-inf')  # 当前最大值，默认负无穷
    sum = 0  # 我们得到的子串的和
    for i in range(mid, low - 1, -1):  # 因为一定要有mid，故从mid开始
        sum += A[i]
        if sum > left_s:
            left_s = sum
            max_left = i  # 记录最大子串左侧起始位置

    right_s = float('-inf')
    sum = 0
    for i in range(mid + 1, high + 1):
        sum += A[i]
        if sum > right_s:
            right_s = sum
            max_right = i  # 记录最大子串左侧起始位置
    return (max_left, max_right, left_s + right_s)


def max_sub(A, low, high):
    """
    最大子数组查找
    :param A:
    :param low:
    :param high:
    :return:
    """
    if high == low:  # 防止只有1个元素的情况
        return (low, high, A[low])
    else:
        mid = (low + high) // 2
        left_low, left_high, left_s = max_sub(A, low, mid)  # 递归求情况1
        right_low, right_high, right_s = max_sub(A, mid + 1, high)  # 递归求情况2
        cross_low, cross_high, cross_sum = cross_mid_maxsub(A, low, mid, high)  # 递归求情况3

        if left_s >= right_s and left_s >= cross_sum:
            return left_low, left_high, left_s
        elif right_s >= left_s and right_s >= cross_sum:
            return right_low, right_high, right_s
        else:
            return cross_low, cross_high, cross_sum


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(max_sub(A, 0, len(A) - 1))

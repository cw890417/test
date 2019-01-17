# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/14
import random

"""
快速排序
"""


def partition(A, p, r):
    """
    将最后一个元素作为基准
    进行排序，比基准小的放在基准元素左边，大的放在右边
    返回基准下标
    :param A:
    :param p:
    :param r:
    :return:
    """
    i = p - 1
    x = A[r]
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        # 分成两组进行循环
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A


def random_partition(A, p, r):
    i = random.choice(list(range(p, r + 1)))
    A[r], A[i] = A[i], A[r]
    return partition(A, p, r)


def random_quicksort(A, p, r):
    if p < r:
        q = random_partition(A, p, r)
        # 分成两组进行循环
        random_quicksort(A, p, q - 1)
        random_quicksort(A, q + 1, r)
    return A


A = [1231, 24, 1, 3, 123, 4, 23, 213, 12, 3, 1, 3, 1, 23, 12, 41241, 2131, 2312, 31, 23, 412, 312, 412, 3, 2]

print(random_quicksort(A, 0, len(A) - 1))

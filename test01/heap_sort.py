# -*- coding: utf-8 -*-
# author:chenwei time:2019/1/10
from typing import Any


def max_heapify(array, arr_len, i):
    """
    以i为节点建立最大堆性质
    :param array:
    :param arr_len:
    :param i:
    :return:
    """
    l = i * 2 + 1
    r = i * 2 + 2
    if l < arr_len and array[l] > array[i]:
        largest = l
    else:
        largest = i
    if r < arr_len and array[r] > array[largest]:
        largest = r
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, arr_len, largest)


def build_max_heap(array, arr_len):
    """
    采用自底向上的方法利用MAX-HEAPIFY把一个大小为n=A.length的数组A[1…n]转换为最大堆。
    因为最大堆中的每个叶结点都可以看成只包含一个元素的堆，
    所以可以从最后一个非叶结点（自底向上）遍历到根结点，对每个结点都调用一次
    :param array:
    :param arr_len:
    :return:
    """
    point = arr_len // 2
    for x in reversed(range(0, point)):
        max_heapify(array, arr_len, x)
    return array


def heap_sort(array):
    """
    堆排序算法利用BUILD-MAX-HEAP将输入数组A[1…n]建成最大堆，其中n=A.length。然后重复这一过程：
    把最大元素与堆中最后一个元素进行交换，然后去掉最后一个结点（通过减小A.heap_size）。
    由于新的根结点不满足最大堆，调用一次MAX-HEAPIFY得到新的最大堆。
    直到堆中只剩一个元素位置。
    :param array:
    :return:
    """
    arr_len = len(array)
    build_max_heap(array, arr_len)
    for x in range(arr_len - 1, 0, -1):
        array[x], array[0] = array[0], array[x]
        arr_len -= 1
        max_heapify(array, arr_len, 0)
    return t


def parent(val):
    return (val - 1) // 2


def heap_increase_key(array, i, key):
    """
    优先队列
    跟新下标为i的最大堆数组值为key，并从新建堆
    :param array: 最大堆数组
    :param i: 数组下标
    :param key: 更新的值
    :return:
    """

    if key < array[i]:
        print('new key is smaller than current key')
        return
    array[i] = key
    while i > 0 and array[parent(i)] < array[i]:
        array[i], array[parent(i)] = array[parent(i)], array[i]
        i = parent(i)
    return array


def max_heap_insert(key, array=[]):
    """
    优先队列
    在array中增加一个元素，保持最大堆特性
    :param key:
    :param array:
    :return:
    """
    array.append(key)
    heap_increase_key(array, len(array) - 1, key)
    return array

if __name__ == '__main__':
    t = [123, 324, 23, 12, 14, 55, 123, 1, 4, 12, 41, 2]
    head_array = build_max_heap(t, len(t))
    # print(head_array)
    # print(heap_increase_key(head_array, 10, 140))
    print(max_heap_insert(444, t))

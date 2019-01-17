def quick_sort(array):
    """
    快速排序
    选取数组第一个元素做为中间比较数
    比比较数小的放左边，大的放右边然后进行合并
    :param array:chenwei
    :return:sort array
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = [10, 2, 4, 1, 3, 5, 11, 1, 7, 8, 11, 33, 33]
    a = 'apply'
    print(a.upper())
    print(quick_sort(arr))

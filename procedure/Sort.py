# coding=utf8
import random
from calc_time import calc_time
from collections import defaultdict


# 交换位置
def swap(l, i, j):
    l[i], l[j] = l[j], l[i]


# 冒泡排序
def bubble_sort(l, i, j, reverse=False):
    for i in range(len(l), 0, -1):
        for j in range(0, i-1):
                if l[j] < l[j+1] and reverse:
                    swap(l, j, j+1)
                elif l[j] > l[j+1] and not reverse:
                    swap(l, j, j+1)


# 插入排序
def insert_sort(l, i, j, reverse=False):
    for i in range(1, len(l)):
        num = l[i]
        j = i-1
        while l[j] > num and j >= 0:
            l[j+1] = l[j]
            j -= 1
        l[j+1] = num


# 选择排序
def select_sort(l, i, j, reverse=False):
    for i in range(len(l)):
        max_num = l[i]
        max_index = i
        for j in range(i+1, len(l)):
            if max_num < l[j]:
                max_num = l[j]
                max_index = j
        swap(l, i, max_index)


# 希尔排序
def shell_sort(l, i, j):
    length = len(l)
    gap = length // 2
    while gap > 0:
        for o in range(gap):
            # gap insertion sort
            for i in range(o+gap, length, gap):
                pos = i
                value = l[i]
                while pos >= gap and l[pos-gap] > value:
                    l[pos] = l[pos-gap]
                    pos -= gap
                l[pos] = value
        gap //= 2


# 归并排序
def merge(l, i, m, j):
    temp = []
    k = i
    n = m+1
    while k <= m and n <= j:
        if l[k] < l[n]:
            temp.append(l[k])
            k += 1
        else:
            temp.append(l[n])
            n += 1
    while k <= m:
        temp.append(l[k])
        k += 1
    while n <= j:
        temp.append(l[n])
        n += 1
    k = 0
    while i <= j:
        l[i] = temp[k]
        i += 1
        k += 1


def merge_sort(l, i, j):
    if i < j:
        m = (i+j)/2
        merge_sort(l, i, m)
        merge_sort(l, m+1, j)
        merge(l, i, m, j)


# 快速排序
def quickSort(l, low, high):
    i = low
    j = high
    if i >= j:
        return
    key = l[i]
    while i < j:
        while i < j and l[j] >= key:
            j -= 1
        l[i] = l[j]
        while i < j and l[i] <= key:
            i += 1
        l[j] = l[i]
    l[i] = key
    quickSort(l, low, i-1)
    quickSort(l, j+1, high)


def quickSort2(l, low, high):
    if low < high:
        q = partition(l, low, high)
        quickSort2(l, low, q-1)
        quickSort2(l, q+1, high)


def partition(l, low, high):
    x = l[high]
    i = low - 1
    for j in range(low, high):
        if l[j] >= x:
            i += 1
            swap(l, i, j)
    swap(l, i+1, high)
    return i+1


def quickSort3(l, low, high):
    i = low
    j = high
    if i >= j:
        return
    key = l[i]
    while i < j:
        while i < j and l[j] >= key:
            j -= 1
        while i < j and l[i] <= key:
            i += 1
        swap(l, i, j)
    swap(l, i, low)
    quickSort(l, low, i-1)
    quickSort(l, i+1, high)


def quickSort4(l, low, high):
    i = low
    j = high
    if i >= j:
        return

    if l[j]<=l[i]<=l[(i+j)/2] or l[(i+j)/2]<=l[i]<=l[j]:
        key = l[i]
        index = i
    elif l[i]<=l[j]<=l[(i+j)/2] or l[(i+j)/2]<=l[j]<=l[i]:
        key = l[j]
        index = j
    else:
        key = l[(i+j)/2]
        index = (i+j)/2
    while i < j:
        while i < j and l[j] >= key:
            j -= 1
        while i < j and l[i] <= key:
            i += 1
        swap(l, i, j)
    swap(l, i, index)
    quickSort(l, low, i-1)
    quickSort(l, i+1, high)


# 堆排序
def heap_sort(l, i, j):
    # 创建堆
    n = len(l)
    for i in range(n, -1, -1):
        heapify(l, n, i)
    # 抽取元素
    for i in range(n-1, 0, -1):
        swap(l, i, 0)
        heapify(l, i, 0)


# n is size of heap
# To heapify subtree rooted at index i
def heapify(l, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and l[largest] < l[left]:
        largest = left
    if right < n and l[largest] < l[right]:
        largest = right
    if largest != i:
        swap(l, largest, i)
        # 下沉
        heapify(l, n, largest)


# counting 排序O(n)
def counting_sort(A, i=None, j=None):
    B, C = [], defaultdict(list)
    for x in A:
        C[x].append(x)
    for k in range(min(C), max(C)):
        B.extend(C[k])
    return B


# 基数排序O(n)
def radix_sort():
    # TODO
    pass


# 桶排序O(n)，
def bucket_sort():
    # TODO
    pass


@calc_time
def build_in_sort(n=100):
    for i in range(n):
        l = [random.randint(1, 10000) for i in range(n)]
        l.sort()

@calc_time
def test(sortf, n=100):
    print sortf.func_name,
    for i in range(n):
        l = [random.randint(1, 10000) for i in range(n)]
        sortf(l, 0, len(l)-1)


if __name__ == "__main__":
    # print 'n=100'
    # test(insert_sort)
    # test(bubble_sort)
    # test(select_sort)
    # test(merge_sort)
    # test(quickSort)
    # test(quickSort2)
    # test(quickSort3)
    # test(shell_sort)
    # test(heap_sort)
    # build_in_sort()
    # print '-'*30
    # print 'n=2000'
    # test(insert_sort,n=1000)
    # test(bubble_sort,n=1000)
    # test(select_sort,n=1000)
    # test(merge_sort, n=2000)

    # test(quickSort, n=2000)
    # test(quickSort2, n=2000)
    test(quickSort3, n=5000)
    # test(quickSort4, n=2000)
    test(counting_sort, n=5000)
    # test(shell_sort, n=2000)
    # test(heap_sort, n=2000)
    build_in_sort(n=5000)
    # l = [random.randint(1,20) for i in range(20)]

    # l=[5,8,7,9,3,4,1,2,6]
    # print l

    # bubble_sort(l)
    # bubble_sort(l, reverse=True)
    # insert_sort(l)
    # select_sort(l)
    # merge_sort(l, 0, len(l)-1)
    # quickSort3(l,0,len(l)-1)
    # shell_sort(l,0,len(l)-1)
    # shell_sort2(l2,0,len(l2)-1)
    # sort_shell(l3,0,len(l3)-1)
    # heap_sort(l,0,len(l)-1)
    # quickSort4(l,0,len(l)-1)
    # print l


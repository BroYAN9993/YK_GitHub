#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
Try to understand how the sorting algorithms work.
"""

def swap(lyst, i, j):
    """
    Exchange the items at positions i and j.
    """
    #You can also use : list[i], list[j] = list[j], list[i]
    #But the following code shows what is really going on.
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp

def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:        # Do n-1 searches
        miniIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst[j] < lyst[miniIndex]:
                miniIndex = j
            j += 1
    if miniIndex != i:
        swap(lyst, i, j)
    i += 1

def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1

def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1

def quickSort(lyst):
    quickSortHelper(lyst, 0, len(lyst) - 1)

def quickSortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quickSortHelper(lyst, left, pivotLocation - 1)
        quickSortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
    middle = (left + right) / 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    boundary = left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    swap(lyst, boundary, right)
    return boundary

def mergeSort(lyst):
    copyBuffer = len(lyst) * [0]
    mergeSortHelper(lyst, copyBuffer, 0, len(lyst) - 1)

def mergeSortHelper(lyst, copyBuffer, low, high):
    if low < high:
        middle = (low + high) / 2
        mergeSortHelper(lyst, copyBuffer, low, middle)
        mergeSortHelper(lyst, copyBuffer, middle + 1, high)
        merge(lyst, copyBuffer, low, middle, high)

def merge(lyst, copyBuffer, low, middle, high):

    #Initialize i1 and i2 to the first items in each sublist.
    i1 = low
    i2 = middle + 1

    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lyst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        elif lyst[i1] < lyst[i2]:
            copyBuffer[i] = lyst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lyst[i2]
            i2 += 1

    for i in range(low, high + 1):
        lyst[i] = copyBuffer[i]

import random

def main(size = 20, sort = mergeSort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print lyst
    sort(lyst)
    print lyst

if __name__ == '__main__':
    main()

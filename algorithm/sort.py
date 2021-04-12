import copy
from typing import List


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            else:
                break
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


def merge_sort(nums):
    def merge(left, mid, right):
        for i in range(left, right + 1):
            temp[i] = nums[i]
        i = k = left
        j = mid + 1
        while left <= i <= mid < j <= right:
            if temp[i] < temp[j]:
                nums[k] = temp[i]
                i += 1
            else:
                nums[k] = temp[j]
                j += 1
            k += 1

        while i <= mid:
            nums[k] = temp[i]
            k += 1
            i += 1

        while j <= right:
            nums[k] = temp[j]
            k += 1
            j += 1

    def sort(left, right):
        if left < right:
            mid = left + (right - left) // 2
            sort(left, mid)
            sort(mid + 1, right)
            if nums[mid] <= nums[mid + 1]:  # 排序后 前后有序不需要merge
                return
            merge(left, mid, right)

    temp = copy.copy(nums)
    sort(0, len(nums) - 1)
    return nums


def quick_sort(arr):
    def _quick_sort(arr, left, right):

        def partition1(arr, left, right):
            pivot = left
            left = left + 1
            while left < right:

                while arr[left] <= arr[pivot] and left < right:
                    left += 1
                while arr[right] >= arr[pivot] and left <= right:
                    right -= 1

                if left < right:
                    arr[left], arr[right] = arr[right], arr[left]

            arr[right], arr[pivot] = arr[pivot], arr[right]
            return right

        if left < right:
            partition_index = partition(arr, left, right)
            _quick_sort(arr, left, partition_index - 1)
            _quick_sort(arr, partition_index + 1, right)

        return arr

    return _quick_sort(arr, 0, len(arr) - 1)


print(quick_sort([2, 5, 10, 7, 1, 3]))


# print(list(range(10, -1, -1)))


class Solution:
    def quick_sort(self, arr: List[int]) -> List[int]:
        # 二分法
        def inner(start, end):
            if start < end:

                begin = start
                tmp_re = arr[start]
                for i in range(start + 1, end):
                    if tmp_re > arr[i]:
                        arr[begin + 1], arr[i] = arr[i], arr[begin + 1]
                        begin += 1
                arr[begin], arr[start] = arr[start], arr[begin]

                inner(start, begin)
                inner(begin + 1, end)

        inner(0, len(arr))
        return arr


print(merge_sort([2, 4, 3, 5, 1]))

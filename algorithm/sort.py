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


def quick_sort(arr):
    def _quick_sort(arr, left, right):
        def partition(arr, left, right):
            pivot = arr[left]
            j = left  # j 后侧的数据更大，j 及其左侧数据更小
            for i in range(left + 1, right + 1):
                if arr[i] < pivot:
                    arr[j + 1], arr[i] = arr[i], arr[j + 1]
                    j += 1

            arr[left], arr[j] = arr[j], arr[left]
            return j

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

#  1. ######------>> Bubble Sorting


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
              
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

arr = [5, 2, 9, 1, 5, 6]
bubble_sort(arr)
print("Bubble Sorted Array:", arr)




####    2.   ########---->>Linear Search 


def linear_search(arr,N, key):
    for i in range(N):
        if arr[i] == key:
            return i
    return -1

arr = [4, 2, 7, 1, 9]
key = 7
N=len(arr)
result = linear_search(arr, N, key)
if(result == -1):
        print("Element is not present in array")
else:
        print("Element is present at index", result)


###   3.   ###------>>>>Binary Search

def binary_search(arr ,low, high, key):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = [1, 3, 5, 7, 9] 
key = 5
result = binary_search(arr, 0, len(arr)-1, key)
if result != -1:
        print("Element is present at index", result)
else:
        print("Element is not present in array")


###    4.    ###------>>>Insertion Sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

arr = [9, 3, 1, 5, 4]
insertion_sort(arr)
print("Insertion Sorted Array:", arr)




###     5.   ##------>>Selection Sort

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
arr = [9, 3, 1, 5, 4]
selection_sort(arr)
print("Insertion Sorted Array:", arr)



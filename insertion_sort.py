def Insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

a = [345, 524, 54, 6, 3, 765, 789, 5, 435, 45, 4, 2, 35, 5646, 36, 5, 6]
print(Insertion_sort(a))


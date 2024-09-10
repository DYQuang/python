def Bubble_sort(arr):
    n=len(a)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr
a = [345,524,54,6,3,765,789,5,435,45,4,2,35,5646,36,5,6]
print(Bubble_sort(a))

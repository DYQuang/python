def Selection_sort(a):
    n=len(a)
    for i in range(n):
        imin = i
        for j in range(i+1,n):
            if a[j] <  a[imin]:
                imin = j
        a[i], a[imin] = a[imin], a[i]
    return a

a = [345,524,54,6,3,765,789,5,435,45,4,2,35,5646,36,5,6]
print(Selection_sort(a))

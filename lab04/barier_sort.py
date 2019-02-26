def barier_sort(a):
    barier = 0
    for i in range(1, len(a)):
        if a[i-1]>a[i]:
            barier = a[i]
            j = i-1
            while a[j]>barier and j>-1:
                a[j+1] = a[j]
                j -= 1
            a[j+1] = barier
            
    return a


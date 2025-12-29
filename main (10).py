def selectionsort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=[4,6,8,2,3,0,8,56]
print(selectionsort(arr))
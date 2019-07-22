def selectionsort(arr):
    i=len(arr)-1
    j=0
    while(j<(len(arr)-2)):
        while(i>j):
            if arr[i]<arr[i-1]:
                t=arr[i]
                arr[i]=arr[i-1]
                arr[i-1]=t
            i=i-1
        i=len(arr)-1
        j=j+1
    return arr
#input
arr=list(map(int,input().rstrip().split()))
res=selectionsort(arr)
print(res)

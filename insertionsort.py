def insertionsort(arr):
    l=len(arr)
    i=0
    while(i<l):
        j=i
        while(j>0):
            if arr[j]<arr[j-1]:
                t= arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=t
            else:
                break
            j=j-1
        i=i+1
    return arr
# input
arr=list(map(int,input().rstrip().split()))
res=insertionsort(arr)
print(res)

#bubble sort
def bubblesort(arr):# complexity worst case(n*n)
    i=0
    l=len(arr)
    j=l-1
    pas=0# checking if interchange never hapen in pass then don't check for other passes
    while(j>0):
        while(i<(l-1)):
            if arr[i]>arr[i+1]:
                t=arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=t
                pas=pas+1
            i=i+1
        if pas==0:# check for the pass where interchange don't happen
            break
        pas=0
        i=0
        l=l-1
        j=j-1
    return arr
#recursive bubble sort
def recursivebs(arr):
    if len(arr)==1:#for length=0
        return arr
    else:
        l=len(arr)
        i=l-1
        arr2=[]
        pas=0
        while(i>0):# this pas will generate smallest number at starting
            if arr[i]<arr[i-1]:
                t=arr[i]
                arr[i]=arr[i-1]
                arr[i-1]=t
                pas=pas+1
            i=i-1
        if pas==0:# stop the algo when interchanging stops
           arr2.append(arr)
        else:
            arr2.append(arr[0])#appending that number to final resultant arrary
            e=recursivebs(arr[1:l])#recursion for arr[1:l]
            arr2.append(e)#appending the other values
        return arr2
                   
#input as array of space seperated integers
arr=list(map(int, input().rstrip().split()))
res=bubblesort(arr)
res2=recursivebs(arr)
print(res2,res)

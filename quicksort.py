def quicksort(arr,i,pe):
    flag='rtol'
    initial=i
    final=pe
    while(pe!=i and pe>initial and pe<=final):
         if flag=='rtol':
             if arr[pe]<arr[i]:#r to l
                 t=arr[pe]
                 arr[pe]=arr[i]
                 arr[i]=t
                 i=pe
                 pe=initial
                 flag='ltor'
             else:
                 pe=pe-1
         if flag=='ltor':
             if arr[pe]>arr[i]:#l to r
                 t=arr[pe]
                 arr[pe]=arr[i]
                 arr[i]=t
                 i=pe
                 pe=final
                 flag='rtol'
             else:
                 pe=pe+1
    if initial<final:
         quicksort(arr,initial,i-1)
         quicksort(arr,i+1,final)
     
#input
arr=list(map(int, input().rstrip().split()))
pe=len(arr)-1
i=0
quicksort(arr,i,pe)
print(arr)

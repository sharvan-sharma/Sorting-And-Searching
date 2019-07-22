#heap creation method
def createheap(arr,i,l):#complexity of creating heap  is o(nlog(n)) method1
    k=0
    heap=[]
    while(len(arr)>0):
         heap.append(arr[i])
         arr.pop(i)
         if k<l:
             j=len(heap)-1
             while(j>0):
                   if heap[j]>heap[(j-1)//2]:#checking the parent down up approach
                      heap[j],heap[(j-1)//2]=heap[(j-1)//2],heap[j]
                      j=(j-1)//2
                   else:
                       break
         k=k+1
    return heap
def heapify(arr,i,f):#complexity of creating heap is o(n) method2
   t=f-1
   l=t
   flag=''
   while(t>=0):
       if ((2*(l+1))-1)<f and (2*(l+1))<f:#case where both left and right child were present
           if arr[((2*(l+1))-1)]>arr[(2*(l+1))]:
               if arr[((2*(l+1))-1)]>arr[l]:
                   arr[((2*(l+1))-1)],arr[l]=arr[l],arr[((2*(l+1))-1)]
                   l=((2*(l+1))-1)
               else:
                   flag='alreadygreater'
           else:
               if arr[(2*(l+1))]>arr[l]:
                   arr[(2*(l+1))],arr[l]=arr[l],arr[(2*(l+1))] 
                   l=(2*(l+1))
               else:
                   flag='alreadygreater'
       elif ((2*(l+1))-1)<f and (2*(l+1))>=f:#case where left child is present
           if arr[((2*(l+1))-1)]>arr[l]:
               arr[((2*(l+1))-1)],arr[l]=arr[l],arr[((2*(l+1))-1)]
               l=((2*(l+1))-1)
           else:
               flag='alreadygreater'
       if ((2*(l+1))-1)>=f or flag=='alreadygreater':# flag condition represent the condition where parent is already greater than childs
           t=t-1
           l=t
           flag=''
   # avoid return arr because in heapsort the name of resultant arrary changes
#heapsort function
def heapsort(arr):# complexity o(nlogn)
    l=len(arr)-1
    i=0
    while(l>0):
        arr[l],arr[0]=arr[0],arr[l]#taking root to end and put end to root an dthen heapify and perform it until we get sorted array upto all elemnts
        heapify(arr,i,l)# heapify the remaing part
        l=l-1
    return arr
#input
arr=list(map(int,input().rstrip().split()))
i=0#parameter of heapify function
f=len(arr)#parameter2 of heapify function
#res2=createheap(arr,i,f)
heapify(arr,i,f)#after this we have emax heap
res2=heapsort(arr)#return sorted arr
print(res2)

def mergesort(array,p,r):
    if p<r:
        mid=(p+r)//2
        mergesort(array,p,mid)
        mergesort(array,mid+1,r)
        merge(array,p,mid,r)

def merge(array,p,mid,r):
    n1=mid-p+1
    n2=r-mid
    a=[0]*(n1);b=[0]*(n2);
    
    for x in range(0,n1):
        a[x]=array[p+x]
    for y in range(0,n2):
        b[y]=array[mid+1+y]
    i=0;j=0;k=p
    
    while i<n1 and j<n2:
        if a[i]<=b[j]:
            array[k]=a[i]
            i=i+1
        else:
            array[k]=b[j]
            j=j+1
        k+=1
    while i<n1:
        array[k]=a[i]
        i=i+1
        k+=1
    while j<n2:
        array[k]=b[j]
        j=j+1
        k+=1
array=[int(x) for x in input().split()]
mergesort(array,0,len(array)-1)
print(array)
            
    
        
    
        
        
        
        
    

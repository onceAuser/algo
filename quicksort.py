def swap(array,f1,f2):
    temp=array[f1]
    array[f1]=array[f2]
    array[f2]=temp

def partition(array,p,r):
    t=p
    for x in range(p,r):
        if array[x]<=array[r]:
            swap(array,x,t)
            t+=1
    swap(array,t,r)
    return t

def quicksort(array,p,r):
    if p<r:
        mid=partition(array,p,r)
        quicksort(array,p,mid-1)
        quicksort(array,mid+1,r)
array=[int(x) for x in input().split()]
quicksort(array,0,len(array)-1)
print(array)

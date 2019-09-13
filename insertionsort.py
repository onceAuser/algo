def insert(array,rI,Val):#here we are inserting the value through getting rightIndex of array cause if we starting 0th index 
    while(array[rI]>Val and rI>=0):#-> only 1 element found then it must sorted 
        array[rI+1]=array[rI]# now we checking leftmost element from the rightIndex to 0th index if we element is smallest continously swapped with element 
        rI=rI-1
    array[rI+1]=Val 
def insertionsort(array):
    for  x in range(1,len(array)):
        insert(array,x-1,array[x])
    return array
list=[int(x) for x in input().split()]
print(insertionsort(list))
        

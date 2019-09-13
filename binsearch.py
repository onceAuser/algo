list1=[int(x) for x in input().split()]
def binsearch(list1,targetvalue):
    min=0
    max=len(list1)-1
    mid=0
    while min<=max:
        mid=(min+max)//2
        if list1[mid]==targetvalue:
            return targetvalue
        elif list1[mid]>targetvalue:
            max=mid+1
        else:
            min=mid-1
t=int(input())
print(binsearch(list1,t))

    


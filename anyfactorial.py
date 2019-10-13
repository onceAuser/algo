def fact(x):
    facto=[None]*(n+1)
    if x<=1:
        return 1
    if facto[x]!=None:
        return facto[x]
    for i in range(1,x+1):
        facto[i]=facto[i-1]*i
    return facto[x]
print(fact(1000))

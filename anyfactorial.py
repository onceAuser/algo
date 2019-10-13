def facto(x):
    fac
    if x<=1:
        return 1
    if facto[x]!=None:
        return facto[x]
    for i in range(1,x+1):
        facto[i]=facto[i-1]*i
    return facto[x]
print(facto(1000))

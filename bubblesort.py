a=[56,33,9,36,72,1,3,6,5,8,105,23,65,13,17,27,89]
n=len(a)
for i in range(0,n-1):
    for i in range(0,n-1):
        if a[i]>a[i+1]:
            mx=a[i]
            mn=a[i+1]
            a[i]=mn
            a[i+1]=mx
    
            
print(a)
        
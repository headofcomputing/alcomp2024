def X(n):
    if n==0 or n==1:
        print(n)
    else:
        X(n//2)
        print(n%2)

X(40)


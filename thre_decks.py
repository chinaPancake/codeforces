for i in range(int(input())):
    a,b,c = map(int, input().split())
    if ((a+b+c)%3==0 and a+c>=2*b):

        print("YES")
    else:
        print("NO")

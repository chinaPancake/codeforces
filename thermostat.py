# a
# from l to r 
#cannot be change by less than x
# you can from a to b if a-b >= x and l<=b<=r
#

def thermo_f(l,r,x,a,b):
    # l = left
    # r = right
    # x = minimum change of tempertarure
    # a = start temperature
    # b = end temeprature

    if a == b:
        return 0

    if abs(a-b)>= x:
        return 1
    
    if b+x <=r or a-x>=l:
        return 2 

    if b-x >=l and a+x<=r:
        return 3

    return-1



for _ in range(int(input())):
    l,r,x = map(int, input().split())
    a,b = map(int, input().split())
    
    c,d = min(a,b), max(a,b)
    print(thermo_f(l=l,r=r,x=x,a=c, b=d))


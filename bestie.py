# https://codeforces.com/problemset/problem/1732/A

import math

def gcd_f(res):
    g = res[0]
    for i in range(1,len(res)):
        g = math.gcd(g,res[i])

    if g == 1 :
        return 0
    elif math.gcd(g, len(res))==1:
        return 1
    elif math.gcd(g, len(res)-1)==1:
        return 2
    
    return 3


for _ in range(int(input())):
    n = int(input())
    a_arr = list(map(int, input().split()))
    print(gcd_f(res=a_arr))

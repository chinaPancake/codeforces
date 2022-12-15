t = int(input()) 
for i in range(t):
    n = int(input())
    ring = list(map(int,input().split()))
    set_len = len(set(ring))
    
    if set_len == 2:
        print(n//2+1)
    else:
        print(n)



# opcje dla 2 unikalnych elementów listy

# 4 a,b,a,b -> a,b -> a -> [] // 3 
# 6 a,b,a,b,a,b - > a,b,a,b - > a,b -> a - > [] // 4 
# 8 a,b,a,b,a,b,a,b -> a,b,a,b,a,b -> a,b,a,b -> a,b -> a -> []  //5 


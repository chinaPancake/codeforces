<<<<<<< HEAD
import math
for t in range(int(input())):
    n = int(input())
    l_list = list(map(int, input().split()))
    ans = 0
    start = l_list[0]
    l_list.sort()

    for i in l_list:
        if start < i:
            start = math.ceil((start + i)/2)
    print(start)



# 3,8,6,7,4,1,2,4,10,1 
# 1,1,2,     3,4 ,4,6,7,8,10


# 
=======
import math
for t in range(int(input())):
    n = int(input())
    l_list = list(map(int, input().split()))
    ans = 0
    start = l_list[0]
    l_list.sort()

    for i in l_list:
        if start < i:
            start = math.ceil((start + i)/2)
    print(start)



# 3,8,6,7,4,1,2,4,10,1 
# 1,1,2,     3,4 ,4,6,7,8,10


# 
>>>>>>> 024728f0262d013687dfa20d46c8269888871b6b

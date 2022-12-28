from math import gcd
for t in range(int(input())):
    n = int(input())
    l_list = list(map(int, input().split()))
    l_list.sort()
    gcd_result = 0
    for x in range(n):
        gcd_result = gcd(gcd_result, l_list[x])
    print(max(l_list) // gcd_result)




#    while l_list[x] > l_list[y]:
#        l_list.sort()
#        print(l_list[x], l_list[y])
#        if l_list[x] == l_list[y]:
#            x -= 1 
#        new_s = l_list[x] - l_list[y]
#        if new_s in s_set:
#            y += 1
#            continue
#        else:
#            s_set.add(new_s)
#            l_list.append(new_s)
#        print(l_list, s_set)
#    print(len(s_set))
#




#    for l in range(len(l_list)):
#        
#        if l_list[l] == max(l_list):
#            break
#        else:
#            new_s = max(l_list) - l_list[l]
#             
#        if new_s in s_set:
#            continue
#        else:
#            l_list.append(new_s)
#            s_set.add(new_s)
#    
#    print(l_list,s_set,len(s_set))

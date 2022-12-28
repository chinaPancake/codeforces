for t in range(int(input())):
    n,m = map(int, input().split())
    ones = []
    all_ones = 0
    s_list = []
    operations = []
    for i in range(n):
        l_list = list(map(int, input().split()))
        ans = 0
        s_list.append(l_list)
        for l in l_list:
            if l == 1:
                ans += 1
        all_ones += ans
        ones.append(ans)
    g_list = []
    for i in range(len(s_list)):
        g_list.append(s_list[i].count(1))
    
    if min(g_list) == max(g_list):
        print('0')
        continue

    if all_ones % n == 0:
        avg = all_ones / n 
        last_less, last_more = 0,0
        for i in range(len(s_list)):
            while ones[i] > avg:
                while ones[last_less] >= avg:
                    last_less += 1
                ind_x = 0
                while ones[i] > avg and ones[last_less] < avg:
                    x1 = s_list[i][ind_x]
                    y = s_list[last_less][ind_x]
                    if x1 == 1 and y == 0:
                        operations.append([i+1, last_less+1,ind_x+1])
                        ones[last_less] += 1 
                        s_list[i][ind_x] = 0
                        s_list[last_less][ind_x] = 1
                        ones[i] -= 1
                    ind_x += 1
            while ones[i] < avg:
                while ones[last_more] <= avg:
                    last_more += 1
                ind_x = 0
                while ones[i] < avg and ones[last_more] > avg:
                    x1 = s_list[i][ind_x]
                    y = s_list[last_more][ind_x]
                    if x1 == 0 and y == 1:
                        operations.append([i+1, last_more+1,ind_x+1])
                        ones[last_more] -= 1 
                        s_list[i][ind_x] = 1
                        s_list[last_more][ind_x] = 0
                        ones[i] += 1
                    ind_x += 1
    if len(operations) == 0:
        print('-1')
    else:
        print(len(operations))
    for i in operations:
        print(' '.join(str(x) for x in i))
    

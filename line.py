for _ in range(int(input())):
    n = int(input())
    s = str(input())
    new_arr = []
    ans = 0 

    for i in range(n):
        if s[i] == 'L':
            new_arr.append((n-1-i) -i)
            ans+=i
        else:
            new_arr.append(i-(n-1-i))
            ans +=n-1-i
    new_arr.sort()
    for i in new_arr[::-1]:
        if i>=0:
            ans +=i 
            print(ans, end= ' ')
        else:
            print(ans, end=' ')
    print()

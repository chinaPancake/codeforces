

for _ in range(int(input())):
    n = int(input())
    arr_list = list(map(int, input().split()))
    s = set()
    f = 0
    ans = 0 
    for i in range(1,n):
        if arr_list[i] in s or arr_list[i] < arr_list[i-1]:
            for j in arr_list[f:i]:
                s.add(j)
            f=i
    print(len(s))


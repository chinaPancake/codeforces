for i in range(int(input())):
    r = int(input())
    l_list = list(map(int, input()))
    s = ''
    ans = 0
    for l in l_list:
        if ans + l >1:
            ans -= l
            s += '-'
        else:
            ans += l
            s += '+'
    print(s[1:])

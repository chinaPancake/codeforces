<<<<<<< HEAD
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
=======
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
>>>>>>> 024728f0262d013687dfa20d46c8269888871b6b

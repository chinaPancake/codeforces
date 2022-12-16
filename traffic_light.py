# https://codeforces.com/problemset/problem/1744/C
# r, y, g = red, yellow, green
# if s = rggry , red green green red yellow
#

for _ in range(int(input())):
    n,c = map(str, input().split())
    n = int(n)
    s = str(input())
    s = s+s 
    max_s = 0
    last = len(s)
    
    for i in reversed(range(0,len(s))):
        if s[i] == 'g':
            last = i

        if s[i] == c:
            max_s = max(max_s, last-i)

    print(max_s)


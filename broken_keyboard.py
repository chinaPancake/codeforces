for t in range(int(input())):
    n = int(input())
    s = input()

    if len(s)%3 == 2:
        print('NO')
        continue

    for i in range(len(s)):
        if i%3 == 1 and s[i] != s[i+1]:
            print('NO')
            break
    else:
        print('YES')


# s_set = 3, s = a,bb,c  4
# s_set = 4, s = a,bb,c,dd -> 6
# s_set = 5, s = a,bb,c,dd,e -> 7
# s_set = 6, s = a,bb,c,dd,e,ff -> 9
# s_set = 7, s = a,bb,c,dd,e,ff,g  -> 10
# s_set = 8, s = a,bb,c,dd,e,ff,g,hh -> 12



# ossu -> 4 -> yes, set: 3
# osam -> 4 -> no, set: 4
# addonn -> 6 -> yes, set: 4
# addonness -> 9 -> yes, set: 6

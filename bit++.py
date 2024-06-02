o =0
for _ in range(int(input())):
    word=str(input())
    calculate = ['++X', 'X++']
    minus = ['--X', 'X--']
    if any(x in word for x in calculate):
        o+=1
    elif any(x in word for x in minus):
        o-=1

    # if '++x' or 'x++' in word:
    #     o+=1
    #     print(word, o)
    # elif '--x' or 'x--' in word:
    #     o-=1
    
print(o)

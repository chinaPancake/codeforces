<<<<<<< HEAD
for t in range(int(input())):
    first = input()
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    x3,y3 = map(int, input().split())
    
    if x1 == x2 and y1 == y3 or x1 == x2 and y2 == y3 or x1==x3 and y1 == y2 or x1 == x3 and y2 == y3 or x2==x3 and y2 == y1 or x2==x3 and y1 ==y3:
        print('NO')
    else:
        print('yes')
=======
for t in range(int(input())):
    first = input()
    x1,y1 = map(int, input().split())
    x2,y2 = map(int, input().split())
    x3,y3 = map(int, input().split())
    
    if x1 == x2 and y1 == y3 or x1 == x2 and y2 == y3 or x1==x3 and y1 == y2 or x1 == x3 and y2 == y3 or x2==x3 and y2 == y1 or x2==x3 and y1 ==y3:
        print('NO')
    else:
        print('yes')
>>>>>>> 024728f0262d013687dfa20d46c8269888871b6b

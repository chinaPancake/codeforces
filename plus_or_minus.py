for _ in range(int(input())):
   a,b,c = map(int, input().split())
   first = a + b 
   second = a - b
   if first == c: 
       print('+')
   else:
       print('-')


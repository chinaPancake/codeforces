import math

t = int(input())
#n - cost of weapon
#a - sell gold coin for 'a' silver coins
#b - buy gold coin for 'b' silver coins


quests = 0 
s_coins = 0

for i in range(t):
    quests = 0 
    n,a,b = map (int, input().split())
    quests = math.ceil(n/a)
    if a>b:
        quests = 1
        pass
    print(quests)
    


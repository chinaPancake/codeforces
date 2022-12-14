import math

n,m,a = map(int, input().split())
#n,m,a = 6,6,4  

ans = 0 

# . . . . . . . . . .
# . . . . . . . . . . 
# . . . . . . . . . .
# . . . . . . . . . . 
# . . . . . . . . . . 
# . . . . . . . . . .
# . . . . . . . . . . 
# . . . . . . . . . . 

ans += math.ceil(m/a)
ans *= math.ceil(n/a)

size_of_rect = n*m # 80m^2
size_of_sq = a*a # 4m^2


print(ans)

def distance(x,y,sx,sy):
    return abs(x-sx)+abs(y-sy)


for _ in range(int(input())):
    n,m,sx,sy,d = map(int, input().split())
    robotx = 1
    roboty = 1
    laser = (sx,sy)
    steps = 0
   
    while(robotx !=n or roboty != m):
        if(robotx<n and distance(x=robotx+1, y=roboty,sx=sx, sy=sy)>d and ((roboty==m or sx+d < n) and (roboty<sy-d or roboty > sy+d))):
            robotx += 1
            steps += 1
            continue
        if(roboty <m and distance(x=robotx, y=roboty+1, sx=sx,sy=sy) > d):
            roboty += 1
            steps +=1 
            continue
        
        steps = -1
        break
    print(steps)
 
# code to slow, timie limit on test 3 
# work on faster code 

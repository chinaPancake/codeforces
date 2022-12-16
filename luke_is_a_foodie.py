# v-a1 <= x 
# x ficex int
# v luke food affinity


for _ in range(int(input())):
    n, x = map(int, input().split())
    food_list = list(map(int, input().split()))
    ans = 0 
    mn, mx = food_list[0], food_list[0]
    for j in food_list:
        mn = min(mn,j)
        mx = max(mx,j)
        if mx-mn>2*x:
            ans +=1 
            mx,mn = j,j
    print(ans)

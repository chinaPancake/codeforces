# https://codeforces.com/problemset/problem/1725/B

n,d = map(int, input().split())

p_arr = list(map(int, input().split()))
win_s = 0 
team = [] 
p_arr.sort()

# 1 2
# 3

i,j = 0, len(p_arr)-1
while i <= j :
    sum_ = p_arr[j]
    while sum_ <= d and i<j:
        sum_ += p_arr[j]
        i+=1
    if sum_>d:
        win_s += 1
    j-=1

print(win_s)


















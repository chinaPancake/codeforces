import statistics
n = int(input())
l_list = list(map(int, input().split()))
l_list.sort()

print(statistics.median(l_list))

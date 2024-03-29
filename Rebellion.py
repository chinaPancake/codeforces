
#You have an array a of size n consisting only of zeroes and ones. You can do the following operation:
#
#choose two indices 1≤i,j≤n, i≠j,
#add ai to aj,
#remove ai from a.
#Note that elements of a can become bigger than 1 after performing some operations. Also note that n becomes 1 less after the operation.
#
#What is the minimum number of operations needed to make a non-decreasing, i. e. that each element is not less than the previous element?
#
#Input
#Each test contains multiple test cases. The first line contains the number of test cases t (1≤t≤104). The description of the test cases follows.
#
#The first line of each test case contains an integer n (1≤n≤105), the size of array a.
#
#Next line contains n integers a1,a2,…an (ai is 0 or 1), elements of array a.
#
#It's guaranteed that sum of n over all test cases doesn't exceed 2⋅105.
#
#Output
#
#For each test case print a single integer, minimum number of operations needed to make a non-decreasing.



for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr[:arr.count(0)].count(1))
# 1 0 0 1 0 0 1 1 0 0 -> 0 0 1 0 0 1 1 1 0  -> 0 0 0 0 1 1 1 1

# 4
# 0 0 1 0 -> 0 0 0 1
# 1 

# 4
# 1 1 0 0 -> 0 1 1 0 -> 0 0 1 1 


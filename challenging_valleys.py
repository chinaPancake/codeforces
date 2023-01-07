def state_f(arr):
    ans = 'dol'
    for l,n in zip(arr,arr[1:]):
        if ans == 'dol':
            if l<n:
                ans = 'gora'

        elif ans =='gora':
            if l>n:
                ans = 'dol'
                return 'NO'
        
    return 'YES'


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print(state_f(arr=arr))   
       


# T -> F -> bład
# .   .
#  . .
#   . 
#
#[3,2,1,2,3,] 
#
# T-> F -> BŁAD
# [1,2,3,4,3,2,1]
#           .
#       .       .
#   .               .
#.                      .
#
# [3,2,1 ,2,3 ,2,3,4 ]
# T-> F->T->F - Bład
#                           .
#.              .       .
#   .       .       .
#       .               
#
#
# T-> Good
#                           .
#                       .
#               .   .   
#           .   
#.  .   .

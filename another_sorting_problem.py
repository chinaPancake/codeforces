from functools import cmp_to_key

def compare(item1, item2):
    str1 = item1[1]
    str2 = item2[1]
    for i in range(1,len(str1)+1): 
        c1 = str1[i-1]
        c2 = str2[i-1]
        if c1 == c2:
            continue
        if i % 2 == 1:
            if c1 > c2:
                return 1
            return -1

        if i % 2 == 0:
            if c1 > c2:
                return -1
            return 1
    return 0

n,m = map(int, input().split())
left_ = []
right_ = []
string_list = []
for x in range(1,n+1):
    string_ = input()
    string_list.append((x,string_))

result = sorted(string_list, key=cmp_to_key(compare))

for x in result:
    print(x[0], end=' ')



#time limit exceeded on test 7

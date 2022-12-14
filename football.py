first_ = input()
before = first_[0]
count_p = 0

for x in first_:
    if before == x:
        count_p += 1 
        before = x 
    elif before !=x:
        count_p = 1
        before = x
    
    if count_p >= 7:
        print('YES')
        break
    
if count_p < 7:
    print('NO')

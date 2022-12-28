

for t in range(int(input())):
    s = str(input())
    zeros,ones = s.count('0'), s.count('1')
    if min(zeros, ones) % 2 == 1:
        print('DA')
    else:
        print('NET')

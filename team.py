
anwser=0
for t in range(int(input())):
    team = input().split()
    if team.count("1") >= 2:
       anwser +=1 

print(anwser)

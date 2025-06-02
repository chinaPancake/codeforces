players, place_to_comapre = map(int, input().split())
player_list = list(map(int, input().split()))  

score = 0
advance = 0 



for i in range(place_to_comapre):
    score = player_list[i]


for i in range(len(player_list)):
    if player_list[i] >= score and player_list[i]>0:
        advance+=1
    else:
        break

print(advance)

for i in range(int(input())):
    number_of_doors, button = map(int, input().split())
    doors = str(input())
    door_split = doors.split()
    door_list = list(door_split)
    #print(door_list)
    first_door = int(0)
    last_door = int(0)
    for first in door_list:
#        print('pierwsze drzwi: ', first)
#        print("tak wyglada lista: ", door_list)
        if door_list[0] == "0":
            first_door += 1
            door_list.pop(0)

        elif first == "1":
            break
 #   print("po pierwszej petli", door_list)

    for last in reversed(door_list):
  #      print("osttanie drzwi: ", last)
        if door_list[-1] == "0":
            last_door += 1
            door_list.pop()

        elif last == "1":
            break

   # print("po drugiej", door_list)
    #print('od poczatku: ', first_door, 'od konca: ', last_door, 'ile miedzy nimi: ', len(door_list), 'ile sekund: ', button)
    if len(door_list) > button:
        print("NO")
    else:
        print("YES")



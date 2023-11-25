# Вариант №5
 
thing = {"r": 3,"p": 2,"a": 2,"m": 2,"i": 1,"k": 1,"x": 3,"t": 1,"f": 1,"d": 1,"s": 2,"c": 2}
point = {"r": 25,"p": 15,"a": 15,"m": 20,"i": 5,"k": 15,"x": 20,"t": 25,"f": 15,"d": 10,"s": 20,"c": 20}
array = []


for i in "rpamikxtfdsc":      # отношение количества очков к количеству места, которое он занимает
    array_i = thing[i]//point[i]
    array.append([array_i, i])

array.sort(reverse=True)
backpack = []
backpack.append("i")            # по варианту №5 Том астматик и ему нужен ингалятор
survive_points = 20

for i in range(12):
    if (len(backpack) + thing[array[i][1]])<=8:
        for j in range(thing[array[i][1]]):
            backpack.append(array[i][1])

for i in "rpamikxtfdsc":
    if i in backpack:
        survive_points += point[i]
    else:
        survive_points -= point[i]

print(backpack[0:4])
print(backpack[4:8])
print("Итоговые очки выживания для рюкзака размером 8: ", survive_points)
import math

def calculate_borsch_ingredients(portions):

    list = ['яловичина', 700/8, 'буряк', 500/8, 'картопля', 
    500/8, 'морква', 200/8, 'цибуля', 200/8, 'помідори', 300/8, 'капуста', 300/8]
    cortege_list = []
    for i in range(7):
        portion = math.ceil((list[2 * i + 1] * portions)/100) * 100
        cortege_list.append((list[2 * i], portion))
    return cortege_list


print(calculate_borsch_ingredients(0))




def calc(working_hours, rate, bonus = 20):
    lst  = []
    for index, elem in enumerate(working_hours):
        wage = elem * rate + bonus[index]
        lst.append(wage) 
    return lst

def calc_bonus(w_hours):
    lst  = []
    for i in w_hours:
        i = i * rate
        lst.append(i) 
    return lst

if __name__ == "__main__":
    working_hours = [40, 45]
    rate = 1.2
    bonuses = calc_bonus(working_hours)
    wage_1 = calc(working_hours, rate, bonuses)
    print(wage_1)


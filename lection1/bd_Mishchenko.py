# Student Birthday Match Check
import random
# ЦЕ просто щоб точно час заміряти не звертай уваги
import time
start_time = time.time()

att = 100000
chance = 0
stud = 23 #int(input('Введіть кількість студентів: '))

if 1<stud<400:
    for i in range(att):
        data = []
        for j in range(stud):
            bd = random.randint(1,365)
            data.append(bd)
        if len(data) > len(set(data)):
            chance+=1
    prob = round(chance/att*100, 8)
    print(str(prob) + '%')
else:
    print('Число студентів має бути від 2 до 399, почніть програму спочатку.')

print("--- %s seconds ---" % (time.time() - start_time))
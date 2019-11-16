# Student Birthday Match Check
import random
# ЦЕ просто щоб точно час заміряти не звертай уваги
import time
start_time = time.time()


num_of_trials = 100000
counter = 0
stud = 23

my_set = set()


if 1 < stud < 400:
    for i in range(num_of_trials):
        
        for j in range(stud):
            ran = random.randint(1, 365)

            if ran in my_set:
                counter+=1
                my_set.clear()
                break

            my_set.add(ran)
        my_set.clear()
    print(100*counter/num_of_trials)
else:
    print('Число студентів має бути від 2 до 399, почніть програму спочатку.')

print("--- %s seconds ---" % (time.time() - start_time))            
               
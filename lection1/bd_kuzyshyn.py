import random
# Setting how much times will we convey our experiment
num_of_trials = 1000000
# Receiving number of students from user
num_of_students =  23 
#int(input("num of students: "))
counter = 0

# ЦЕ просто щоб точно час заміряти не звертай уваги
import time
start_time = time.time()

# Creating a loop that will repeat 11111 times
for j in range(num_of_trials):
    #Filling array with zeros 
    arr = []
    for i in range(365):
        arr.append(0)

    for j in range(num_of_students):
        #Generating a randim integer
        ran = random.randint(0 , 364)
        #Adding one to an element of "ARR" with index "ran"
        arr[ran] += 1
        #Checking, if there are 2 birthdays in this day
        if (arr[ran] == 2):    
            counter += 1
            break

            
        
    #if there is at least 2 birthdays in one day: 
    #if double_birthday:
        

print(counter)

#rounding to 6 digits after "."
probability = round( 100 *counter / num_of_trials , 8)
print(str(probability) + "%")    

print("--- %s seconds ---" % (time.time() - start_time))
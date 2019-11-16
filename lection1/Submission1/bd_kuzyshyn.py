import random
# Setting how much times will we convey our experiment
num_of_trials = 11111
# Receiving number of students from user
num_of_students =int(input("num of students: "))
counter = 0

# Creating a loop that will repeat 11111 times
for j in range(num_of_trials):
    double_birthday = False
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
            double_birthday = True 
        
    #if there is at least 2 birthdays in one day: 
    if double_birthday:10
        counter += 1
print(counter)

#rounding to 6 digits after "."
probability = round( 100 *counter / num_of_trials , 8)
print(str(probability) + "%")    

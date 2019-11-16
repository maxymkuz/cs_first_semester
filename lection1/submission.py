import random

num_of_trials = 11111
num_of_students =int(input("num of students: "))
counter = 0

for j in range(num_of_trials):
    double_birthday = False
    #Filling array with zeros 
    arr = []
    for i in range(365):
        arr.append(0)

    for j in range(num_of_students):
        #Generating a randim integer
        ran = random.randint(0 , 364)
        arr[ran] += 1

        if (arr[ran] == 2):    
            double_birthday = True
            
        
        
    #if there is at least 2 birthdays in one day: 
    if double_birthday:
        counter += 1
print(counter)

#rounding to 6 digits after
probability = round( 100 *counter / num_of_trials , 8)
print(str(probability) + "%")    

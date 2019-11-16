import random

num_of_trials = 11111
num_of_students = 25

counter = 0

double_birthday = False

studs =[]
for x in range(23):
    studs.append(0)
print(studs)

for i in range(23):
    ran = random.randint(1,365)

    if (ran in studs):
        print(ran)
        double_birthday = True

    studs[i] = ran
    

#for j in range(num_of_trials):

print(studs)


probability = round( 100 *counter / num_of_trials , 6)
print(probability)    

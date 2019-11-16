from random import randint
birthday=[0 for i in range(365)]
counter=0
for i in range(22222):
    a=[]
    for j in range(23):
        s=randint(1,365)
        if birthday[s-1]:
            counter+=1
            birthday[s-1]=0
            for x in a:
                birthday[x-1]=0
            break
        else:
            birthday[s-1]=1
            a.append(s)
    for x in a:
        birthday[x-1]=0

            
        #1
    
print(100*counter/222222)

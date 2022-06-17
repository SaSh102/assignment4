number= int(input ("please enter a number: "))
fact=1
i=1
list=[] 

if number<=0:
    print("No 😐")

else: 
    while fact<=number:
        for i in range(1, number):   
            fact=fact*i
            i+=1
            list.append(fact)

    if number in list:
        print("Yes")
    else:
        print("No")


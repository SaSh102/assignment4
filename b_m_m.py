while True:

    a=int(input("Please enter number A:"))
    b=int(input("Please enter number B:"))

    if a<1 or b<1:
        print("No")
        break
    if a<b:
        temp=a
        a=b
        b=temp
    while (b!=0):
        c=a%b
        a=b
        b=c
    print(a)
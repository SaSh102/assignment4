a= input("Please enter a sentence: ")

c=0
space=False
for i in a:
    if i==" ":
        if space==False:
            c=c+1
            space=True
    else:
        space=False

print("Number of words: ",c+1)



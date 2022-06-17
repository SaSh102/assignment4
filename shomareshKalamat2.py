out=0
IN=1

def shmaresh_kalamat(sentence): 
    state=out 
    count=0
      
    for i in range(len(sentence)): 
        if (sentence[i] == ' '): 
            state=out 
      
        elif state==out: 
            state=IN 
            count+=1
     
    return count 
  
sentence=input("Please enter a sentence:")
print("Number of words: "+str(shmaresh_kalamat(sentence))) 
  
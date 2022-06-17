def safhe_shatranji(n, m):
    i=1
    while(i<=m):
        if (i%2) ==0:
            a = n//2
            b = n%2
            if b == 0:
                print(a*"*#")
            else:
              print(a*"*#"+"*")
            
        else:    
            a = n//2
            b = n%2
            if b == 0:
                print(a*"#*")
            else:
                print(a*"#*"+"#")
        i+=1
        
safhe_shatranji(15, 3)


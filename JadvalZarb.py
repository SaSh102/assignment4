from itertools import count


def safhe_shatranji(n, m):
    i=1
    j=1

    while(i<=m):
        j=1
        while(j<=n):
            print(format(i*j,'2d') , end='   ')
            j+=1

        i+=1
        print()

safhe_shatranji(10, 10)

import cmath

def moadele_dareje_Doo(a,b,c):
    delta=(b*b)-(4*a*c)
    d=cmath.sqrt(delta)
    if delta<<0:
        print('No answer')
    if delta==0:
        x=(-b)+d
        print(x)
    else:
        x1=((-b)+d)/(2*a)
        x2=((-b)-d)/(2*a)
        print(x1 , x2)


moadele_dareje_Doo(1,5,6)

from sys import stdin


def conversion(exp):
    reales=0
    complejo=0
    signo=1
    for i in range(len(exp)):
        if exp[i]== "-":
            signo=-1
        elif exp[i] == "+" :
            signo=1
        elif exp[i].isnumeric():
            reales+=int(exp[i])*signo
        else:
            if (exp[i][0] == "+"):
                complejo+=int(exp[i][1])
            elif (exp[i][0] == "-"):
                complejo-=int(exp[i][1])
            elif exp[i][0] == "i":
                complejo+=1
            else:
                complejo+=int(exp[i][0])*signo
    return (reales,complejo)


def producto (exp1,exp2):
        
    resultado=(exp1[0]*exp2[0]-exp1[1]*exp2[1],exp1[0]*exp2[1]+exp1[1]*exp2[0])
    return resultado


def suma (exp1,exp2):
    resultado=(exp1[0]+exp2[0],exp1[1]+exp2[1])
    return resultado

def resta (exp1,exp2):
    exp2=(exp2[0]*-1,exp2[1]*-1)
    suma (exp1,exp2)

def conjugado (exp):
    resultado =(exp[0],exp[1]*-1)
    return resultado
    
def division (exp1,exp2):
    conj=conjugado(exp2)
    numerador=producto(exp1,conj)
    denominador= (exp2[0]**2)+(exp2[1]**2)
    resultado = (numerador[0]/denominador,numerador[1],denominador)
    return resultado
    
def main():

    exp1= stdin.readline().strip().split()
    exp2= stdin.readline().strip().split()
    long=min(len(exp1),len(exp2))
    exp1=conversion(exp1)
    exp2=conversion(exp2)
    sumaC=suma(exp1,exp2)
    product=producto(exp1,exp2)
    subs=resta(exp1,exp2)
    div=division(exp1,exp2)
    print ('resultado: {0:.2f} + {1}i'.format(div[0],div[1]))
    
    
    
main()
        

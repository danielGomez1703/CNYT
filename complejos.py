from sys import stdin
import math

def Conversion(exp):
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


def Producto (exp1,exp2):
        
    resultado=(exp1[0]*exp2[0]-exp1[1]*exp2[1],exp1[0]*exp2[1]+exp1[1]*exp2[0])
    return resultado


def Suma (exp1,exp2):
    resultado=(exp1[0]+exp2[0],exp1[1]+exp2[1])
    return resultado

def Resta (exp1,exp2):
    exp2=(exp2[0]*-1,exp2[1]*-1)
    respuesta=Suma(exp1,exp2)
    return respuesta

def Conjugado (exp):
    resultado =(exp[0],exp[1]*-1)
    return resultado

    
def Division (exp1,exp2):
    conj=Conjugado(exp2)
    numerador=Producto(exp1,conj)
    denominador= (exp2[0]**2)+(exp2[1]**2)
    resultado = (numerador[0]/denominador,numerador[1]/denominador)
    return resultado

def Modulo(real,imaginario):
    modulo= (real**2 + imaginario**2)**(0.5)
    return modulo

def polarCartesiano(n,grado):
    ladoX=n*math.cos(math.radians(grado))
    ladoY=n*math.sin(math.radians(grado))
    cordenada=(ladoX,ladoY)
    return cordenada
def cartesianoPolar(real,imaginario):
    
    n=Modulo(real,imaginario)
    grado= math.degrees(math.atan2(imaginario,real))
    respuesta=(n,grado)
    return respuesta

def Fase(real,imaginario):

    fase = math.atan2(imaginario,real)
    return fase
    

        

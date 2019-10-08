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
def invertir (c):
    return (-c[0],-c[1])


#------------------------------------------------------------------------------------#

def restaVectores(vec1,vec2):
    res = []
    for i in range(len(vec1)):
        res.append(Resta(vec1[i], vec2[i]))
    return res

def sumaVectores(vec1,vec2):
    res = []
    for i in range(len(vec1)):
        res.append(Suma(vec1[i],vec2[i]))
    return res

def inversoVector(vec):
    res = []
    for i in range(len(vec1)):
        res.append(invertir(vec1[i],vec2[i]))
    return res

def productoScalarV(escalar,vector):
    res = []
    for i in vector:
        res.append(Producto((escalar,0),i))
    return res

def multMatrices (matA,matB):
    filas = len(matA)
    columnas = len(matB[0])
    matriz = [[(0, 0) for x in range(columnas)]  for x in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            for k in range(len(matB)):
                matriz[i][j] = Suma(Producto(matA[i][k], matB[k][j]),matriz[i][j])
    return matriz
    
def productoInterno(matA,matB):
    real = 0
    complejo = 0
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            real += (matA[i][j][0]*matB[i][j][0])
            complejo += (matA[i][j][1]*matB[i][j][1])
    return (real,complejo)

def sumaMatriz(matA,matB):
    resultado =[[0 for i in range (len(matA[0]))] for j in range(len(matA))]
    for i in range(len(matA)):
        for j in range(len(matA[0])):
            resultado[i][j]= Suma(matA[i][j], matB[i][j])
    return resultado
            
def productoEscalarMatriz(escalar,matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]= Producto((escalar,0),matriz[i][j])
    return matriz

def matInversa(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]= invertir(matriz[i][j])
    return matriz

def maTranspuesta (matriz):
    
    resultado =[[(0,0) for i in range (len(matriz))] for j in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            resultado[j][i]= matriz[i][j]
    return resultado

def matConjugada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j]= Conjugado(matriz[i][j])
    return matriz

def matAdjunta(matriz):
    
    return matConjugada(maTranspuesta(matriz))

def Accion(matA,vec):
    vectorResp=[]
    for j in range(len(matA)):
        fila=(0,0)
        for k in range(len(matA[0])):
            fila=Suma(fila,Producto(matA[j][k],vec[j]))
        vectorResp.append(fila)
    return vectorResp
   #return multMatrices(matA,(maTranspuesta([vec])))

def matNorma(Mat):
    return (productoInterno(Mat,Mat)[0],productoInterno(Mat,Mat)[1])
def distanciaMatrices(mat1,mat2):
    matriz = sumaMatriz(mat1,matInversa(mat2))
    distancia = matNorma(matriz)
    return distancia

def identidad(n):
    identidad = [[0 for x in range(n)]for y in range(n)]
    for i in range(n):
        identidad[i][i]=(1,1)
    return identidad


def unitaria(matriz):
    if len(matriz)!=len(matriz[0]):
        return False
    fin = multMatrices(matriz ,matAdjunta(matriz))
    for i in range(len(fin)):
        for j in range(len(fin[0])):
            if ((i==j and fin[i][j][0]!=1 and fin[i][j][0]!=1) or (i!=j and fin[i][j][0]!=0 and fin[i][j][0]!=0)):
                return False
    return True

def hermitian(mat):
    return (matAdjunta(mat) == mat)

#-----------------------------------------------------------------------------------
def canicas(inicio,vec,clicks):
    for i in range(clicks):
        estado = multMatrices(inicio,inicio)
    return estado

def rendijas(n,inicio,vec,clicks):
    inicio = multMatrices (inicio,inicio)
    for i in range(clicks):
        estate = multMatrices(inicial,estado)
    return estate

def rendijasComplejos(n,inicio,vec):
    for i in range(n):
        inicial = multMatrices(inicio,inicio)
    resultado = multMatrices(inicial,[vec])
    return resultado



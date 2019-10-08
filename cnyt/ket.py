from Complejo import *
import math
from numpy import linalg as LA
def canicas(inicial,estado,clicks):
    for i in range(clicks):
        estado = productoMatrizVectorComplejos(inicial,estado)
    return estado

def rendijas(num,inicial,estado,clicks):
    inicial = productoMatrices(inicial,inicial)
    for i in range(clicks):
        estado = productoMatrizVector(inicial,estado)
    return estado

    
def rendijasComplejos(num,inicial,estado):
    for i in range(num):
        inicial = productoMatricesComplejas(inicial,inicial)
    res = productoMatrizVectorComplejos(inicial,estado)
    return res
def particula(points,pos):
    norm = normVectorComplejo(points)
    probablidad = math.pow(pos,2)/math.pow(norm,2)
    return probablidad
def paticulaDobleKet(ket1,ket2):
    aux = []
    for i in range(len(ket2)):
        aux.append((ket2[i][0],-ket2[i][1]))
    res = productoInternoVectoresComplejos(aux,ket1)
    return res
def observableKet(mat,ket):
    hermi = matrizHermitiana(mat)
    if hermi:
        res = (0,0)
        a = productoMatrizVectorComplejos(mat,ket)
        a = conjugadoVector(a)
        for i in range(len(mat)):
            res = suma(res,producto(ket[i],a[i]))
        return res
def observableKetVarianza(mat,ket):
    a = observableKet(mat,ket)
    b = [[(2.5000000000000004, 0.0),(0,0)],[(0,0),(2.5000000000000004, 0.0)]]
    aux = restaDirecta(mat,b)
    pro = productoMatricesComplejas(aux,aux)
    res = productoMatrizVectorComplejos(pro,ket)
    res = productoVectorVectorComplejos(res,ket)
    rest = 0
    res2 = (0,0)
    for i in range(len(mat)):
        res2 = suma(res2,producto(res[i],ket[i]))
    return rest+0.25
def valoresPropios(mat):
    mat1=[[] for x  in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat1[i].append(complex(mat[i][j][0],mat[i][j][1]))
    w , v= LA.eigh(mat1)
    return [w[0],w[1]]

# CNYT

# Repositorio CNYT

Este repositorio contiene los trabajos y laboratorios de la materia ciencia y  tecnologia  de la escuala colombiana de ingenieria Julio Garavito.


# Numeros complejos

esta es una libreria que tiene contiene operaciones entre complejos, suma, resta, division, producto punto...etc


## Como Descargar.
clone el github a su directorio, la fuente de este programa es en python.

# Numeros Complejos
* Suma.
* Resta.
* Conjugado.
* Inverso.
* Multiplicacion.
* Division.
* Modulo.
* Fase.
* Producto escalar.
* Representacion polar y cartesiana.
## Matrices Complejas
* Suma
* Resta
* Conjugado
* Multiplicacion
* Adjunta
* Inverso
* Producto tensor
* Producto escalar

## USO

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas._

Mira **Deployment** para conocer como desplegar el proyecto.

### Pre-requisitos 

Debe tener instalado en su computador Python en lo posible la version 3.7, lo cual lo puede hacer desde su pagina oficial y siguiendo los pasos de instalacion.

## pruebas 
Para ejecutar de manera correcta las pruebas lo que se necesita hacer es abrir el archivo Pruebas.py y ejecutarlas(f5).

### Prueba de producto escalar
```
def test_producto_scalar(self):
        mat1 = [(6,3),(0,0),(5,1),(4,0)]
        scalar = (3,2)
        resultado = Complex.productoScalarMatriz(scalar,mat1)
        self.assertEqual(resultado,[(12, 21), (0, 0), (13, 13), (12, 8)])
```
### Prueba de producto interno
```
def test_producto_interno(self):
        mat1 = [[1,2],[0,1]]
        mat2 = [[0,-1],[-1,0]]
        mat3 = [[2,1],[1,3]]
        resultado = Complex.productoInterno(Complex.sumaMatrices(mat1,mat2),mat3)
        self.assertEqual(resultado,[[1,-2],[3,4]])
```
### Prueba de canicas
```
def test_canicas(self):
        mat = [[(0,0),(0,0),(0,0),(0,0),(0,0),(1,0)],[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(1,9),(0,0),(0,0),(0,0),(1,45)],[(0,0),(0,0),(0,0),(1,5),(0,0),(0,0)],[(0,0),(0,0),(1,1),(0,0),(0,0),(0,0)],[(1,10),(0,0),(0,0),(0,0),(1,8),(0,0)]]
        estado = [(6,2),(2,3),(1,1),(5,1),(3,4),(10,1)]
        resultado = Complejo.canicas(mat,estado,1)
        self.assertEqual(resultado,[(10, 1), (0, 0), (-60, 472), (0, 26), (0, 2), (-43, 90)])

```
### Prueba de rendijas
```
def test_rendijas(self):
        matriz = [[0,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0.5,0,0,0,0,0,0,0],[0,0.33,0,1,0,0,0,0],[0,0.33,0,0,1,0,0,0],          [0,0.33,0.33,0,0,1,0,0],[0,0,0.33,0,0,0,1,0],[0,0,0.33,0,0,0,0,1]]
        estado = [1,0,0,0,0,0,0,0]
        resultado = Complejo.rendijas(2,matriz,estado,1)
        self.assertEqual(resultado,[0.0, 0.0, 0.0, 0.165, 0.165, 0.33, 0.165, 0.165])

```
### Prueba de rendijas complejas
```
    def test_rendijas_complejas(self):
        matriz = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0.5,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)],[(0,0),(0.33,0),(0.33,0),(0,0),(0,0),(1,0),(0,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(1,0),(0,0)],[(0,0),(0,0),(0.33,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
        estado = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        resultado = Complejo.rendijasComplejos(2,mat,estado)
        self.assertEqual(resultado,[(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.165, 0.0), (0.165, 0.0), (0.33, 0.0), (0.165, 0.0)])
        

```

### Analice las pruebas end-to-end 

Todas las pruebas realizadas son para hacer una comprobacion del correcto funcionamienito de todos los metodos realizados y poniendo en evidencia todas sus funcionalidades.

```
self.assertEqual(Complex.productoInterno(Complex.sumaMatrices(mat1,mat2),mat3),[[1,-2],[3,4]])
```

Como podemos ver en la imagen la luz del lazer se distorciona en varios puntos generando asi este patron.

## Construido con 

* [Python](https://www.python.org/) - Python 3.7 - Usado para desarrollar la libreria.

## Autores 

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Daniel Felipe Gomez Suarez** - *Desarrollo* - [DanielGomez1703](https://github.com/danielGomez1703/CNYT)

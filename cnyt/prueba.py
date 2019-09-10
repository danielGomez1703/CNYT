import Complejo;
import unittest;

class TestComplejo(unittest.TestCase):
    def testSuma(self):
        c1=(1,5)
        c2=(2,-3)
        r=Complejo.Suma(c1,c2)
        res=(3,2)
        self.assertEqual(r,res)
    def testProducto(self):
        c1=(1,4)
        c2=(5,1)
        r=Complejo.Producto(c1,c2)
        res=(1,21)
        self.assertEqual(r,res)
    def testResta(self):
        c1=(1,5)
        c2=(2,-3)
        r=Complejo.Resta(c1,c2)
        res=(-1,8)
        self.assertEqual(r,res)
    def testDivision(self):
        c1=(3,2)
        c2=(-1,2)
        r=Complejo.Division(c1,c2)
        res=(1/5,-8/5)
        self.assertEqual(r,res)
        
    def testModulo(self):
        c1=(1,-3)
        r=Complejo.Modulo(c1[0],c1[1])
        res=(c1[0]**2+c1[1]**2)**(1/2)
        self.assertEqual(r,res)
    def testConjugado(self):
        c1=(4,2)
        r=Complejo.Conjugado(c1)
        res=(4,-2)
        self.assertEqual(r,res)
    def testPolarCart(self):
        r=Complejo.polarCartesiano(13.0, 22.619864948040426)
        res=(12,5)
        self.assertEqual(r,res)
    def testCartPolar(self):
        r=Complejo.cartesianoPolar(12,5)
        res=(13.0, 22.619864948040426)
        self.assertEqual(r,res)
    def testFase(self):
        r=Complejo.Fase(1,-1)
        res=-0.7853981633974483
        self.assertEqual(r,res)

    def test_sumaVectores(self):
        self.assertEqual(Complejo.sumaVectores([(1,2)],[(2,3)]),[(3,5)])
        
    def test_restaVectores(self):
        self.assertEqual(Complejo.restaVectores([(1,2)],[(2,3)]),[(-1,-1)])
        
    def test_MatSuma(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        m2=[[(1,5),(2,3)],[(0,1),(4,8)]]
        r=[[(2,10),(12,5)],[(-3,6),(8,16)]]
        res=Complejo.sumaMatriz(m1,m2)
        self.assertEqual(r,res)
    def test_MatInv(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        r=[[(-1,-5),(-10,-2)],[(3,-5),(-4,-8)]]
        res=Complejo.matInversa(m1)
        self.assertEqual(r,res)
    def test_MatMulEsc(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        n=10
        r=[[(10,50),(100,20)],[(-30,50),(40,80)]]
        res= Complejo.productoEscalarMatriz(n,m1)
        self.assertEqual(r,res)
    def test_MatTras(self):
        m1=[[(1,5),(10,2)],[(-3,5),(4,8)]]
        r=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        res=Complejo.maTranspuesta(m1)
        self.assertEqual(r,res)
    def test_MatCon(self):
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[[(1,-5),(-3,-5)],[(10,-2),(4,-8)]]
        res= Complejo.matConjugada(m)
        self.assertEqual(r,res)
    def test_MatAdj(self):
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[[(1,-5),(10,-2)],[(-3,-5),(4,-8)]]
        res= Complejo.matAdjunta(m)
        self.assertEqual(r,res)
    def test_Accion(self):
        v=[(0,9),(3,2),(1,5)]
        m=[[(1,5),(-3,5)],[(10,2),(4,8)]]
        r=[(-90, -18), (22, 58)]
        res=Complejo.Accion(m,v)
        self.assertEqual(r,res)
    def test_NormaMat(self):
        m=[[(3,0),(5,0)],[(2,0),(3,0)]]
        r= 47**(1/2)
        res=Complejo.matNorma(m)
        self.assertEqual(r,res)
    def test_DistMat(self):
        m1=[[(3,0),(5,0)],[(2,0),(3,0)]]
        m2 = [[(0,0),(1,0)],[(-1,0),(0,0)]]
        r=6.557438524302
        res=Complejo.distanciaMatrices(m1,m2)
        self.assertEqual(r,res)
    def test_Unitaria(self):
        #m = [[(1,-2),(3,0)],[(0,2),(4,2)]]
        m = [[(0,0),(1,0)],[(-1,0),(0,0)]]
        res=Complejo.unitaria(m)
        self.assertTrue(res)
    def test_Hermitian(self):
        m = [[(7,0),(6,5)],[(6,-5),(-3,0)]]
        her=Complejo.hermitian(m)
        self.assertTrue(her)
        

if __name__ == "__main__":
    unittest.main()

import unittest

from AreaFiguras import AreaFiguras

class AreaTest(unittest.TestCase):

    def setUp(self):
        self.area = AreaFiguras()

    def test_area_de_triangulo_base_10_altura_8(self):
        self.assertEquals(self.area.obtenAreaTriangulo(10, 8), 40)

    def test_area_de_cuadrado_lado_20(self):
        self.assertEquals(self.area.obtenAreaCuadrado(20), 400)

    def test_area_rectangulo_altura_5_base_7(self):
        self.assertEquals(self.area.obtenAreaRectangulo(5, 7), 35)

    def test_area_circulo_radio_7(self):
        self.assertEquals(self.area.obtenAreaCirculo(7), 153.9384)

    def test_area_trapecio_base_mayor_10_base_menor_8_altura_6(self):
        self.assertEquals(self.area.obtenAreaTrapecio(10, 8, 6), 54)
"""
    def test_seleccion_triangulo(self):
        self.assertEquals(self.area.seleccion(3), "seleccionaste triangulo")

    def test_seleccion_rectangulo(self):
        self.assertEquals(self.area.seleccion(4), "seleccionaste rectangulo")

    def test_seleccion_cuadrado(self):
        self.assertEquals(self.area.seleccion(1), "seleccionaste cuadrado")

    def test_seleccion_circulo(self):
        self.assertEquals(self.area.seleccion(2), "seleccionaste circulo")

    def test_seleccion_trapecio(self):
        self.assertEquals(self.area.seleccion(5), "seleccionaste trapecio")

    def test_seleccion_invalida(self):
        self.assertEquals(self.area.seleccion(20), "no es una opcion valida")
"""


if __name__== '__main__': # pragma: no cover
    unittest.main()
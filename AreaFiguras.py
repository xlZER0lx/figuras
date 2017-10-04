class AreaFiguras():

    def seleccion(self, figura):
        """
        print("1.- Cuadrado")
        print("2.- Circulo")
        print("3._ Triangulo")
        print("4.- Rectangulo")
        print("5.- Trapecio")

        fig = input("De cual figura desea sacar el area? ")
        """

        if(int(figura) == 1):
            lado = input("cuanto mide el lado?")

            self.obtenAreaCuadrado(lado)

            return "seleccionaste cuadrado"
        elif(int(figura) == 2):
            radio = input("cuanto mide el radio?")

            self.obtenAreaCirculo(radio)

            return "seleccionaste circulo"
        elif(int(figura) == 3):
            alturaTri = input("cuanto mide la altura?")
            baseTri = input("cuanto mide la base?")

            self.obtenAreaTriangulo(baseTri, alturaTri)

            return "seleccionaste triangulo"
        elif(int(figura) == 4):
            baseRec = input("cuanto mide la base?")
            alturaRec = input("cuanto mide la altura")

            self.obtenAreaRectangulo(alturaRec, baseRec)

            return "seleccionaste rectangulo"
        elif(int(figura) == 5):
            baseMayor = input("cuanto mide la base mayor?")
            baseMenor = input("cuanto mide la base menor?")
            alturaTrap = input("cuanto mide la altura?")

            self.obtenAreaTrapecio(baseMayor, baseMenor, alturaTrap)

            return "seleccionaste trapecio"
        else:
            return "no es una opcion valida"



    def obtenAreaCirculo(self, r):
        return 3.1416*r*r

    def obtenAreaCuadrado(self, l):
        return l*l

    def obtenAreaRectangulo(self, h, b):
        return h*b

    def obtenAreaTrapecio(self, bMa, bMe, h):
        return ((bMa + bMe)/2)*h

    def obtenAreaTriangulo(self, b, h):
        return (b*h)/2

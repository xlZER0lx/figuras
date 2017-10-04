Feature: Area de un trapecio
	como usuario del archivo areas
	deseo ingresar una base mayor, base menor y una altura
	para obtener el area de un trapecio

	Scenario: Area de un trapecio con base mayor 6, base menor 4 y altura 4
		Dado que tengo la base mayor "6", base menor "4" y altura "4"
		cuando calculo el area
		entonces obtengo el area de trapecio "20"
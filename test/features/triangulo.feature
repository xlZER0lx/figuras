Feature: Area de un triangulo
	como usuario del archivo areas
	deseo ingresar una base y una altura
	para obtener el area de un triangulo

	Scenario: Area de un triangulo con base 3 y altura 6 
		Dado que tengo la base "3" y altura "6"
		cuando calculo el area
		entonces obtengo el area de triangulo "9"

	Scenario: Area de un triangulo con base 5 y altura 4
		Dado que tengo la base "5" y altura "4"
		cuando calculo el area
		entonces obtengo el area de triangulo "10"

	Scenario: Area de un triangulo con base 2 y altura 2
		Dado que tengo la base "2" y altura "2"
		cuando calculo el area
		entonces obtengo el area de triangulo "2"
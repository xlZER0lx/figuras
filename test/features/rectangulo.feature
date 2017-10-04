Feature: Area de un rectangulo
	como usuario del archivo areas
	deseo ingresar una base y una altura
	para obtener el area de un rectangulo

	Scenario: Area de un rectangulo con altura 3 y base 7 
		Dado que tengo la altura "3" y base "7"
		cuando calculo el area
		entonces obtengo el area de rectangulo "21"

	Scenario: Area de un rectangulo con altura 5 y base 6 
		Dado que tengo la altura "5" y base "6"
		cuando calculo el area
		entonces obtengo el area de rectangulo "30"

	Scenario: Area de un rectangulo con altura 2 y base 4
		Dado que tengo la altura "2" y base "4"
		cuando calculo el area
		entonces obtengo el area de rectangulo "8"
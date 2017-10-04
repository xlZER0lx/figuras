Feature: Area de un cuadrado
	como usuario del archivo areas
	deseo ingresar un lado
	para obtener el area de un cuadrado

	Scenario: Area de un cuadrado con lado 7
		Dado que tengo el lado "7"
		cuando calculo el area
		entonces obtengo el area de cuadrado "49"

	Scenario: Area de un cuadrado con lado 2
		Dado que tengo el lado "2"
		cuando calculo el area
		entonces obtengo el area de cuadrado "4"

	Scenario: Area de un cuadrado con lado 10
		Dado que tengo el lado "10"
		cuando calculo el area
		entonces obtengo el area de cuadrado "100"
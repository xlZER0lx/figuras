# -*- coding: utf-8 -*-
from lettuce import step, world
from AreaFiguras import AreaFiguras

@step(u'cuando calculo el area')
def cuando_calculo_el_area(step):
    pass
@step(u'Dado que tengo el radio "([^"]*)"')
def dado_que_tengo_el_radio_group1(step, radio):
    world.area = AreaFiguras()
    world.areacir = world.area.obtenAreaCirculo(int(radio))
@step(u'entonces obtengo el area de circulo "([^"]*)"')
def entonces_obtengo_el_area_de_circulo_group1(step, esperado):
    assert float(esperado) == world.areacir,'El resultado esperado de '\
    +esperado+" y el obtenido es "+str(world.areacir)
@step(u'Dado que tengo el lado "([^"]*)"')
def dado_que_tengo_el_lado_group1(step, lado):
    world.area = AreaFiguras()
    world.areacuad = world.area.obtenAreaCuadrado(int(lado))
@step(u'entonces obtengo el area de cuadrado "([^"]*)"')
def entonces_obtengo_el_area_de_cuadrado_group1(step, esperado):
    assert int(esperado) == world.areacuad,'El resultado esperado de '\
    +esperado+" y el obtenido es "+str(world.areacuad)
@step(u'Dado que tengo la altura "([^"]*)" y base "([^"]*)"')
def dado_que_tengo_la_altura_group1_y_base_group2(step, altura, base):
    world.area = AreaFiguras()
    world.arearec = world.area.obtenAreaRectangulo(int(altura), int(base))
@step(u'entonces obtengo el area de rectangulo "([^"]*)"')
def entonces_obtengo_el_area_de_rectangulo_group1(step, esperado):
    assert int(esperado) == world.arearec,'El resultado esperado de '\
    +esperado+" y el obtenido es "+str(world.arearec)
@step(u'Dado que tengo la base mayor "([^"]*)", base menor "([^"]*)" y altura "([^"]*)"')
def dado_que_tengo_la_base_mayor_group1_base_menor_group2_y_altura_group2(\
    step, basemay, basemen, altura):
    world.area = AreaFiguras()
    world.areatrap = world.area.obtenAreaTrapecio(\
        int(basemay), int(basemen), int(altura))
@step(u'entonces obtengo el area de trapecio "([^"]*)"')
def entonces_obtengo_el_area_de_trapecio_group1(step, esperado):
    assert int(esperado) == world.areatrap,'El resultado esperado de '\
    +esperado+" y el obtenido es "+str(world.areatrap)
@step(u'Dado que tengo la base "([^"]*)" y altura "([^"]*)"')
def dado_que_tengo_la_base_group1_y_altura_group2(step, base, altura):
    world.area = AreaFiguras()
    world.areatri = world.area.obtenAreaTriangulo(int(base), int(altura))
@step(u'entonces obtengo el area de triangulo "([^"]*)"')
def entonces_obtengo_el_area_de_triangulo_group1(step, esperado):
    assert int(esperado) == world.areatri,'El resultado esperado de '\
    +esperado+" y el obtenido es "+str(world.areatri)
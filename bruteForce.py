''' 
----------------------------------------
  Universidad del Valle de Guatemala
  Logica Matematica, seccion 20
  
    - Carol Arevale - 20461
    - Stefano Aragoni - 20261
    - Luis Santos - 20226
    - Jose Gonzales - 20335
    - Diego Perdomo - 20204
    - Diego Cordova - 20212

  bruteForce.py
  - Implementacion del algoritmo
    de fuerza bruta para SAT
  
  Last modified (yy-mm-dd): 2022-08-06
----------------------------------------
'''

import itertools as it

def opt(literales, n):
  ''' 
  producto cartesiano de las literales y asigna valores a las opciones.
  
  AQUI EL FUNCIONAMIENTO DE FUERZA BRUTA: Todas las posibles opciones se declaran aquí. 
  '''

  return [{variable: posibility[literales.index(variable)]
    for variable in literales
  } for posibility in (it.product([True, False], repeat=n))]


def bruteForce(clause):
  '''Implementacion de Algoritmo SAT'''
  literales = []

  for clause_elements in clause:
    for literal in clause_elements:

      #busca cada elemento que está negado, luego lo vuelve positivo.
      if "!" in literal: 
        if(literal[0] == "!"):
            literal = literal[1]
        elif(literal[1] == "!"):
            literal = literal[0]

      #almacena cada literal distinta (siempre positiva) en un array
      if not literal in literales: 
        literales.append(literal)

  #ccuenta cuantos literales distintos hay
  n = len(literales)

  #calcula todas las opciones
  options = opt(literales, n)

  #verifica cada opción posible en la clausula indicada
  for option in options:
    verify = True
    check = True

    for disjuncion in clause:
      disjuncion_Value = False

      for variable in disjuncion:
        if variable[0] == "!":
          check = True 
        else: 
          check = False

        if check: 
          variable = variable[1]
          
        value = option[variable] ^ check
        disjuncion_Value = disjuncion_Value or value
        
      #si sí es válido el disjunction_value, entonces se retorna true junto con las opciones que permitieron el funcionamiento correcto.
      verify = verify and disjuncion_Value
      
    if verify:
      return [True, option]
      
  #si no es válido, no retorna nada y se indica en el menu principal.
  return [False, None]


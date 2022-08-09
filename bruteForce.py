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

def bruteForce(items):
    variables = []

    for item in items:
        for var in item:
            if var[0] == "!": 
                var = var[1]
            if not var in variables: 
                variables.append(var)

    values = [True, False]
    allPosible = it.product(values, repeat=len(variables))
    allPosible = [{
        variable: posibility[variables.index(variable)]
        for variable in variables
    } for posibility in allPosible]

    for i in range(len(allPosible)):
        posibility = allPosible[i]
        satisfied = True

        for item in items:
            check = False
            for variable in item:
                inverse = False
                
                if variable[0] == "!":
                    inverse = True
                
                if inverse: 
                    variable = variable[1]
                
                value = posibility[variable] ^ inverse
                check = check or value
            satisfied = satisfied and check
        
    return [satisfied, posibility]

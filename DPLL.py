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

  DPLL.py
  - Implementacion del algoritmo DPLL
  
  Last modified (yy-mm-dd): 2022-08-06
----------------------------------------
'''

from random import randint
from copy import deepcopy

def logical_not(L):
  '''Devuelve la negacion de la literal L'''
  return L[1:] if L[0] == '!' else '!' + L

def check_disjunction(B):
  ''' 
  Devuelve True si hay una clausula 
  vacia en B y False de lo contrario
  '''
  for clause in B:
    if len(clause) == 0:
      return True

  return False
  
def getLiterals(B):
  '''
  Devuelve una lista con las literales
  de las clausulas dentro de B
  '''
  literals = []

  for clause in B:
    for L in clause:
      temp_L = L[1:] if L[0] == '!' else L

      if temp_L not in literals:
        literals.append(temp_L)

  return literals

def simplify(B, L, I):
  '''
  Remueve las clausulas de B donde aparece L y 
  remueve las instancias de !L de las clausulas
  donde aparece.
  
  Devuelve:
    - B con los cambios realizados
    - I con con el valor de L
  '''
  c_to_remove = []
  
  if len(L) == 1:
    I[L] = True
  else:
    I[L[1]] = False

  for clausula in B:
    if L in clausula:
      c_to_remove.append(clausula)

  for n in c_to_remove:
    B.remove(n)

  L = logical_not(L)

  for clausula in B:
    if L in clausula:
      clausula.remove(L)

  return B, I

def DPLL(B, I:dict = {}) -> tuple:
  '''Implementacion de Algoritno DPLL'''
  
  if len(B) == 0: 
    return True, I
    
  if check_disjunction(B): 
    return False, []

  if isinstance(B[0], set):
    for i in range(len(B)):
      B[i] = list(B[i])
  
  exp = getLiterals(B)
  L = exp[randint(0, len(exp) - 1)]

  result, I1 = DPLL(*simplify(deepcopy(B), L, deepcopy(I)))
  if result: 
    return True, I1

  result, I2 = DPLL(*simplify(deepcopy(B), logical_not(L), deepcopy(I)))
  if result: return True, I2
  
  return False, []

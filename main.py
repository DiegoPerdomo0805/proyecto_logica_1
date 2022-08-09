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

  main.py
  - Implementacion de SAT para
    ecuaciones booleanas
  
  Last modified (yy-mm-dd): 2022-08-06
----------------------------------------
'''

if __name__ == '__main__':
  from DPLL import DPLL
  from bruteForce import bruteForce
  from read import openFile
  
  clauses = openFile()#Clausulas a analizar en algortimo importadas del archivo de texto

  #Resultados
  print("RESULTADOS DE SIMULACIÓN E IMPLEMENTACIÓN:")
  
  def programa1():
    print('\n------- Fuerza Bruta -------\n')
    contador = 1

    for clause in clauses:
      result = bruteForce(clause)

      args = f'Exito con combinación: {result[1]}' if result[0] else 'Es insatisfacible'
      print(f'[Clausula {contador}] {args}')
      contador = contador + 1
  
  def programa2():
    print('\n------- DPLL -------\n')
    contador = 1

    for clause in clauses:
      result = DPLL(clause)

      args = f'Exito con combinación: {result[1]}' if result[0] else 'Es insatisfacible'
      print(f'[Clausula {contador}] {args}')
      contador = contador + 1
  
  #Menu
  while True:
    print()
    opcion = int(
      input("\nMenu:\n   1- Fuerza Bruta \n   2- Algoritmo DPLL  \n   3- Salir \n")
    )

    if opcion == 1:
      programa1()

    elif opcion == 2:
      programa2()

    elif opcion == 3:
      print("\nHasta luego.")
      break
    
    else:
      print("Por favor ingrese un numero correcto\n")

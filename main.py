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
  #Cláusulas a analizar en algortimo
  
  clauses = openFile()#Clausulas a analizar en algortimo importadas del archivo de texto
  #Resultados
  
  print("RESULTADOS DE SIMULACIÓN E IMPLEMENTACIÓN:")
  
  def programa1():
    print('\n------- Por fuerza bruta -------\n')
    for i in range(len(clauses)):
      result, literals = bruteForce(clauses[i])
      args = f'Exito con combinación: {literals}' if result else 'Es insatisfacible'
      print(f'Clausula {i + 1} {args}')
  
  def programa2():
    print('\n------- Utilizando DPLL -------\n')
    for i in range(len(clauses)):
      result, literals = DPLL(clauses[i])
      args = f'Exito con combinación: {literals}' if result else 'Es insatisfacible'
      print(f'Clausula {i + 1} {args}')
  
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

#import os
#cwd = os.getcwd()
#files = os.listdir(cwd)
#print("Files in %r: %s" % (cwd, files))

def openFile():
    f = open('clausulas.txt', 'r')

    clausulas = []

    for i in f.readlines():
        linea = []
        clausula = []
        expression = False
        complejo = False
        com = ''
        for j in i:
            if j == '{':
                expression = True
            elif j == '}':
                expression = False
                linea.append(clausula)
                clausula = []
            elif j == ']':
                clausulas.append(linea)
                linea = []
            elif complejo == True:
                com += j
                complejo = False
                clausula.append(com)
                com = ''
            elif j != ',' and j != ' ' and j != '{' and j != '}' and expression:
                if j == '!':
                    complejo = True
                    com += j
                else:
                    clausula.append(j)
    return clausulas

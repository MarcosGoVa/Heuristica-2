import constraint
from constraint import *
import input_reader
#PE:(1,1)(1,2)(2,1)(4,1)(5,1)(5,2)
problem = Problem()
ambulance_list = []
#Es la lista de ambulancias que tiene elementos tipo 'TSU-X', 'TSU-C', 'TNU-X', 'TSU-C'
PE = []
#Lista con los valores de dominio que tengan electricidad

Dominio, PE, ambulance_list = input_reader.main()

problem.addVariables(ambulance_list, Dominio)

def notEqual (*posicion) :
    for i in range (len(posicion)) :
        for j in range (i+1,len(posicion) ) :
            if i != j and posicion[i] == posicion[j] :
                return False
    return True

def congelador(*lista):
    for i in range (len(lista)) :
        if 'C' in ambulance_list[i]:
            if lista[i] not in PE:
                return False
                #Hay que poner false dentro de las iteraciones del bucle ya que si ponemos true, puede no haber visto 
                #el resto de ambulancias con C y asignarles un valor cualquiera
    return True


def adelantado(*lista):
    for i in range(len(lista)):
         if 'TSU' in ambulance_list[i]:
            for j in range(len(lista)):
                 if (i!=j) and (lista[i][0] == lista[j][0]) and (lista[j][1] > lista[i][1]) and ('TSU' not in ambulance_list[j]) :
                      return False
                 
    return True

def sandwich(*lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i!=j:
                #Caso primera fila
                if (lista[i][0] == 1 and lista[j][0] == lista[i][0] + 1 and lista[i][1] == lista[j][1]):
                    return False
                #Caso última fila
                if (lista[i][0] == Dominio[-1][0] and lista[j][0] == Dominio[-1][0] - 1 and lista[i][1] == lista[j][1]):
                    return False
                #caso sandwich
                if ((lista[i][0]-1,lista[i][1]) in lista and (lista[i][0]+1,lista[i][1]) in lista):
                    return False
    return True

"""def sandwich(*lista):
    for i in range(len(lista)):
        #Caso primera fila
        if(lista[i][0] == 1 and (lista[i][0]+1,lista[i][1]) in lista):
            return False
        #Caso última fila
        if(lista[i][0] == Dominio[-1][0] and (lista[i][0]-1,lista[i][1]) in lista):
            return False
        if ((lista[i][0]-1,lista[i][1]) in lista and (lista[i][0]+1,lista[i][1]) in lista):
                return False
    return True"""
              

problem.addConstraint(constraint.AllDifferentConstraint())
problem.addConstraint(congelador,ambulance_list)
problem.addConstraint(adelantado,ambulance_list)
problem.addConstraint(sandwich,ambulance_list)

solutions = problem.getSolution()
print("Solution: ", solutions)
numsolutions = len(solutions)
print("\nNúmero total de soluciones: ",numsolutions)
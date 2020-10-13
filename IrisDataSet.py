#importar librerias que se necesitaran
import random
import numpy as np

#Declaracion del DataSet Iris-Plant con 150 elemento
iris_DataSet = ([
[5.1,3.5,1.4,0.2,"Iris-setosa"],
[4.9,3.0,1.4,0.2,"Iris-setosa"],
[4.7,3.2,1.3,0.2,"Iris-setosa"],
[4.6,3.1,1.5,0.2,"Iris-setosa"],
[5.0,3.6,1.4,0.2,"Iris-setosa"],
[5.4,3.9,1.7,0.4,"Iris-setosa"],
[4.6,3.4,1.4,0.3,"Iris-setosa"],
[5.0,3.4,1.5,0.2,"Iris-setosa"],
[4.4,2.9,1.4,0.2,"Iris-setosa"],
[4.9,3.1,1.5,0.1,"Iris-setosa"],
[5.4,3.7,1.5,0.2,"Iris-setosa"],
[4.8,3.4,1.6,0.2,"Iris-setosa"],
[4.8,3.0,1.4,0.1,"Iris-setosa"],
[4.3,3.0,1.1,0.1,"Iris-setosa"],
[5.8,4.0,1.2,0.2,"Iris-setosa"],
[5.7,4.4,1.5,0.4,"Iris-setosa"],
[5.4,3.9,1.3,0.4,"Iris-setosa"],
[5.1,3.5,1.4,0.3,"Iris-setosa"],
[5.7,3.8,1.7,0.3,"Iris-setosa"],
[5.1,3.8,1.5,0.3,"Iris-setosa"],
[5.4,3.4,1.7,0.2,"Iris-setosa"],
[5.1,3.7,1.5,0.4,"Iris-setosa"],
[4.6,3.6,1.0,0.2,"Iris-setosa"],
[5.1,3.3,1.7,0.5,"Iris-setosa"],
[4.8,3.4,1.9,0.2,"Iris-setosa"],
[5.0,3.0,1.6,0.2,"Iris-setosa"],
[5.0,3.4,1.6,0.4,"Iris-setosa"],
[5.2,3.5,1.5,0.2,"Iris-setosa"],
[5.2,3.4,1.4,0.2,"Iris-setosa"],
[4.7,3.2,1.6,0.2,"Iris-setosa"],
[4.8,3.1,1.6,0.2,"Iris-setosa"],
[5.4,3.4,1.5,0.4,"Iris-setosa"],
[5.2,4.1,1.5,0.1,"Iris-setosa"],
[5.5,4.2,1.4,0.2,"Iris-setosa"],
[4.9,3.1,1.5,0.1,"Iris-setosa"],
[5.0,3.2,1.2,0.2,"Iris-setosa"],
[5.5,3.5,1.3,0.2,"Iris-setosa"],
[4.9,3.1,1.5,0.1,"Iris-setosa"],
[4.4,3.0,1.3,0.2,"Iris-setosa"],
[5.1,3.4,1.5,0.2,"Iris-setosa"],
[5.0,3.5,1.3,0.3,"Iris-setosa"],
[4.5,2.3,1.3,0.3,"Iris-setosa"],
[4.4,3.2,1.3,0.2,"Iris-setosa"],
[5.0,3.5,1.6,0.6,"Iris-setosa"],
[5.1,3.8,1.9,0.4,"Iris-setosa"],
[4.8,3.0,1.4,0.3,"Iris-setosa"],
[5.1,3.8,1.6,0.2,"Iris-setosa"],
[4.6,3.2,1.4,0.2,"Iris-setosa"],
[5.3,3.7,1.5,0.2,"Iris-setosa"],
[5.0,3.3,1.4,0.2,"Iris-setosa"],
[7.0,3.2,4.7,1.4,"Iris-versicolor"],
[6.4,3.2,4.5,1.5,"Iris-versicolor"],
[6.9,3.1,4.9,1.5,"Iris-versicolor"],
[5.5,2.3,4.0,1.3,"Iris-versicolor"],
[6.5,2.8,4.6,1.5,"Iris-versicolor"],
[5.7,2.8,4.5,1.3,"Iris-versicolor"],
[6.3,3.3,4.7,1.6,"Iris-versicolor"],
[4.9,2.4,3.3,1.0,"Iris-versicolor"],
[6.6,2.9,4.6,1.3,"Iris-versicolor"],
[5.2,2.7,3.9,1.4,"Iris-versicolor"],
[5.0,2.0,3.5,1.0,"Iris-versicolor"],
[5.9,3.0,4.2,1.5,"Iris-versicolor"],
[6.0,2.2,4.0,1.0,"Iris-versicolor"],
[6.1,2.9,4.7,1.4,"Iris-versicolor"],
[5.6,2.9,3.6,1.3,"Iris-versicolor"],
[6.7,3.1,4.4,1.4,"Iris-versicolor"],
[5.6,3.0,4.5,1.5,"Iris-versicolor"],
[5.8,2.7,4.1,1.0,"Iris-versicolor"],
[6.2,2.2,4.5,1.5,"Iris-versicolor"],
[5.6,2.5,3.9,1.1,"Iris-versicolor"],
[5.9,3.2,4.8,1.8,"Iris-versicolor"],
[6.1,2.8,4.0,1.3,"Iris-versicolor"],
[6.3,2.5,4.9,1.5,"Iris-versicolor"],
[6.1,2.8,4.7,1.2,"Iris-versicolor"],
[6.4,2.9,4.3,1.3,"Iris-versicolor"],
[6.6,3.0,4.4,1.4,"Iris-versicolor"],
[6.8,2.8,4.8,1.4,"Iris-versicolor"],
[6.7,3.0,5.0,1.7,"Iris-versicolor"],
[6.0,2.9,4.5,1.5,"Iris-versicolor"],
[5.7,2.6,3.5,1.0,"Iris-versicolor"],
[5.5,2.4,3.8,1.1,"Iris-versicolor"],
[5.5,2.4,3.7,1.0,"Iris-versicolor"],
[5.8,2.7,3.9,1.2,"Iris-versicolor"],
[6.0,2.7,5.1,1.6,"Iris-versicolor"],
[5.4,3.0,4.5,1.5,"Iris-versicolor"],
[6.0,3.4,4.5,1.6,"Iris-versicolor"],
[6.7,3.1,4.7,1.5,"Iris-versicolor"],
[6.3,2.3,4.4,1.3,"Iris-versicolor"],
[5.6,3.0,4.1,1.3,"Iris-versicolor"],
[5.5,2.5,4.0,1.3,"Iris-versicolor"],
[5.5,2.6,4.4,1.2,"Iris-versicolor"],
[6.1,3.0,4.6,1.4,"Iris-versicolor"],
[5.8,2.6,4.0,1.2,"Iris-versicolor"],
[5.0,2.3,3.3,1.0,"Iris-versicolor"],
[5.6,2.7,4.2,1.3,"Iris-versicolor"],
[5.7,3.0,4.2,1.2,"Iris-versicolor"],
[5.7,2.9,4.2,1.3,"Iris-versicolor"],
[6.2,2.9,4.3,1.3,"Iris-versicolor"],
[5.1,2.5,3.0,1.1,"Iris-versicolor"],
[5.7,2.8,4.1,1.3,"Iris-versicolor"],
[6.3,3.3,6.0,2.5,"Iris-virginica"],
[5.8,2.7,5.1,1.9,"Iris-virginica"],
[7.1,3.0,5.9,2.1,"Iris-virginica"],
[6.3,2.9,5.6,1.8,"Iris-virginica"],
[6.5,3.0,5.8,2.2,"Iris-virginica"],
[7.6,3.0,6.6,2.1,"Iris-virginica"],
[4.9,2.5,4.5,1.7,"Iris-virginica"],
[7.3,2.9,6.3,1.8,"Iris-virginica"],
[6.7,2.5,5.8,1.8,"Iris-virginica"],
[7.2,3.6,6.1,2.5,"Iris-virginica"],
[6.5,3.2,5.1,2.0,"Iris-virginica"],
[6.4,2.7,5.3,1.9,"Iris-virginica"],
[6.8,3.0,5.5,2.1,"Iris-virginica"],
[5.7,2.5,5.0,2.0,"Iris-virginica"],
[5.8,2.8,5.1,2.4,"Iris-virginica"],
[6.4,3.2,5.3,2.3,"Iris-virginica"],
[6.5,3.0,5.5,1.8,"Iris-virginica"],
[7.7,3.8,6.7,2.2,"Iris-virginica"],
[7.7,2.6,6.9,2.3,"Iris-virginica"],
[6.0,2.2,5.0,1.5,"Iris-virginica"],
[6.9,3.2,5.7,2.3,"Iris-virginica"],
[5.6,2.8,4.9,2.0,"Iris-virginica"],
[7.7,2.8,6.7,2.0,"Iris-virginica"],
[6.3,2.7,4.9,1.8,"Iris-virginica"],
[6.7,3.3,5.7,2.1,"Iris-virginica"],
[7.2,3.2,6.0,1.8,"Iris-virginica"],
[6.2,2.8,4.8,1.8,"Iris-virginica"],
[6.1,3.0,4.9,1.8,"Iris-virginica"],
[6.4,2.8,5.6,2.1,"Iris-virginica"],
[7.2,3.0,5.8,1.6,"Iris-virginica"],
[7.4,2.8,6.1,1.9,"Iris-virginica"],
[7.9,3.8,6.4,2.0,"Iris-virginica"],
[6.4,2.8,5.6,2.2,"Iris-virginica"],
[6.3,2.8,5.1,1.5,"Iris-virginica"],
[6.1,2.6,5.6,1.4,"Iris-virginica"],
[7.7,3.0,6.1,2.3,"Iris-virginica"],
[6.3,3.4,5.6,2.4,"Iris-virginica"],
[6.4,3.1,5.5,1.8,"Iris-virginica"],
[6.0,3.0,4.8,1.8,"Iris-virginica"],
[6.9,3.1,5.4,2.1,"Iris-virginica"],
[6.7,3.1,5.6,2.4,"Iris-virginica"],
[6.9,3.1,5.1,2.3,"Iris-virginica"],
[5.8,2.7,5.1,1.9,"Iris-virginica"],
[6.8,3.2,5.9,2.3,"Iris-virginica"],
[6.7,3.3,5.7,2.5,"Iris-virginica"],
[6.7,3.0,5.2,2.3,"Iris-virginica"],
[6.3,2.5,5.0,1.9,"Iris-virginica"],
[6.5,3.0,5.2,2.0,"Iris-virginica"],
[6.2,3.4,5.4,2.3,"Iris-virginica"],
[5.9,3.0,5.1,1.8,"Iris-virginica"],
])
#Declaracion de matriz de entrenamiento
train_Set = []
#Declaracion de matriz de prueba
test_Set = []
#Lista para guardar las clases del DataSet
list_Clases = []

#Metodo para sacar las clases
def separar_Clases():
    #Recorrer el DataSet
    for c in iris_DataSet:
        #Si la clase encontrada ya existe en la Lista de Clases
        if c[4] in list_Clases:
            #Pasar a la siguiente iteracion
            continue
        #Si no existe
        else:
            #Agregarla a la lista
            list_Clases.append(c[4])

#Metodo para contar los elementos por clase
def contar_Clase(i):
    #Contador de elementos por clase se inicializa en 0
    cont = 0
    #Recorrer el DataSet
    for n in iris_DataSet:
        #Si la clase del elemento del DataSet es igual a la clase de lista de clase
        if n[4] == list_Clases[i]:
            #Se incrementa el contador
            cont += 1
    #Se retorna el contador
    return cont

#Metodo para generar la matriz Train y Test
def generar_Train_Test(portc):
    #LLamar metodo para separar las clases
    separar_Clases()
    #Iterar por cada clase de la lista de clases
    for x in range(0, len(list_Clases)):
        #Se inicializa el contador en 0
        i = 0
        #Sacar el porcentaje de la clase total de elementos por clase * porcentaje / 100
        porcentaje = (contar_Clase(x)*portc)/100
        #Mientras el contador sea menor al porcentaje
        while i < porcentaje:
            #Generar numero random entre el numero 0 y la longitud del DataSet - 1
            num = random.randint(0, len(iris_DataSet)-1)
            #Sacar elemento del DataSet con el numero Random
            iris = iris_DataSet[num]
            #Si la clase del elemento iris es igual a la clase iterada
            if iris[4] == list_Clases[x]:
                #Sacar un elemento del DataSet e incertarlo en el Train
                train_Set.append(iris_DataSet.pop(num))
                #Se incrementa el contador
                i += 1

#Metodo para sacar la distancia entre dos puntos
def distance(P, Q):
    #Retorna el valor de la raiz cuadrada de la suma del cuadrado de la resta entre dos puntos
    return np.sqrt(np.sum((P - Q)**2))

#Metodo para comparar una lista de puntos con 1
def distanciaPunto(ptrain, puntoTest):
    #Matriz D se inicializa vacia
    D = []
    #Se recorre la matriz mandada a traves del parametro
    for puntoTrain in ptrain:
        #Se inserta en la matriz D la distancia generada por dos puntos
        D.append(distance(puntoTest, puntoTrain))
        #Se guarda ese valor de distancia para imprimirlo
        di = distance(puntoTest, puntoTrain)
        print("Punto Test:", puntoTest, "Punto Train:", puntoTrain, "Distancia:", di)
    #Se imprime la distancia minima
    print("Distancia minima:", min(D))

#Metodo para generar la minima distancia
def minima_Distancia():
    #Se crean dos variables auxiliares
    pTrain = []
    pTest = []
    #Recorrer la matriz de entrenamiento
    for train in train_Set:
        #Eliminar la etiqueta(clase) del elemento
        train.pop(-1)
        #Añadir ese elemento a la matriz auxiliar
        pTrain.append(train)
    #Convertir la matriz a numpy
    pTrain = np.array(pTrain)
    # Recorrer la matriz de entrenamiento
    for test in test_Set:
        # Eliminar la etiqueta(clase) del elemento
        test.pop(-1)
        # Añadir ese elemento a la matriz auxiliar
        pTest.append(test)
    # Convertir la matriz a numpy
    pTest = np.array(pTest)
    #Recorrer la matriz Test numpy
    for puntoTest in pTest:
        #Llamada del metodo para generar la distancia
        distanciaPunto(pTrain, puntoTest)



#Llama de metodos e impresion de resultados
generar_Train_Test(10)
test_Set = iris_DataSet
print(train_Set)
print(len(train_Set))
print(test_Set)
print(len(test_Set))
minima_Distancia()

# importar librerias que se necesitaran
import random
import numpy as np

iris_DataSet = ([
    [5.1, 3.5, 1.4, 0.2, "Iris-setosa"],
    [4.9, 3.0, 1.4, 0.2, "Iris-setosa"],
    [4.7, 3.2, 1.3, 0.2, "Iris-setosa"],
    [4.6, 3.1, 1.5, 0.2, "Iris-setosa"],
    [5.0, 3.6, 1.4, 0.2, "Iris-setosa"],
    [5.4, 3.9, 1.7, 0.4, "Iris-setosa"],
    [4.6, 3.4, 1.4, 0.3, "Iris-setosa"],
    [5.0, 3.4, 1.5, 0.2, "Iris-setosa"],
    [4.4, 2.9, 1.4, 0.2, "Iris-setosa"],
    [4.9, 3.1, 1.5, 0.1, "Iris-setosa"],
    [5.4, 3.7, 1.5, 0.2, "Iris-setosa"],
    [4.8, 3.4, 1.6, 0.2, "Iris-setosa"],
    [4.8, 3.0, 1.4, 0.1, "Iris-setosa"],
    [4.3, 3.0, 1.1, 0.1, "Iris-setosa"],
    [5.8, 4.0, 1.2, 0.2, "Iris-setosa"],
    [5.7, 4.4, 1.5, 0.4, "Iris-setosa"],
    [5.4, 3.9, 1.3, 0.4, "Iris-setosa"],
    [5.1, 3.5, 1.4, 0.3, "Iris-setosa"],
    [5.7, 3.8, 1.7, 0.3, "Iris-setosa"],
    [5.1, 3.8, 1.5, 0.3, "Iris-setosa"],
    [5.4, 3.4, 1.7, 0.2, "Iris-setosa"],
    [5.1, 3.7, 1.5, 0.4, "Iris-setosa"],
    [4.6, 3.6, 1.0, 0.2, "Iris-setosa"],
    [5.1, 3.3, 1.7, 0.5, "Iris-setosa"],
    [4.8, 3.4, 1.9, 0.2, "Iris-setosa"],
    [5.0, 3.0, 1.6, 0.2, "Iris-setosa"],
    [5.0, 3.4, 1.6, 0.4, "Iris-setosa"],
    [5.2, 3.5, 1.5, 0.2, "Iris-setosa"],
    [5.2, 3.4, 1.4, 0.2, "Iris-setosa"],
    [4.7, 3.2, 1.6, 0.2, "Iris-setosa"],
    [4.8, 3.1, 1.6, 0.2, "Iris-setosa"],
    [5.4, 3.4, 1.5, 0.4, "Iris-setosa"],
    [5.2, 4.1, 1.5, 0.1, "Iris-setosa"],
    [5.5, 4.2, 1.4, 0.2, "Iris-setosa"],
    [4.9, 3.1, 1.5, 0.1, "Iris-setosa"],
    [5.0, 3.2, 1.2, 0.2, "Iris-setosa"],
    [5.5, 3.5, 1.3, 0.2, "Iris-setosa"],
    [4.9, 3.1, 1.5, 0.1, "Iris-setosa"],
    [4.4, 3.0, 1.3, 0.2, "Iris-setosa"],
    [5.1, 3.4, 1.5, 0.2, "Iris-setosa"],
    [5.0, 3.5, 1.3, 0.3, "Iris-setosa"],
    [4.5, 2.3, 1.3, 0.3, "Iris-setosa"],
    [4.4, 3.2, 1.3, 0.2, "Iris-setosa"],
    [5.0, 3.5, 1.6, 0.6, "Iris-setosa"],
    [5.1, 3.8, 1.9, 0.4, "Iris-setosa"],
    [4.8, 3.0, 1.4, 0.3, "Iris-setosa"],
    [5.1, 3.8, 1.6, 0.2, "Iris-setosa"],
    [4.6, 3.2, 1.4, 0.2, "Iris-setosa"],
    [5.3, 3.7, 1.5, 0.2, "Iris-setosa"],
    [5.0, 3.3, 1.4, 0.2, "Iris-setosa"],
    [7.0, 3.2, 4.7, 1.4, "Iris-versicolor"],
    [6.4, 3.2, 4.5, 1.5, "Iris-versicolor"],
    [6.9, 3.1, 4.9, 1.5, "Iris-versicolor"],
    [5.5, 2.3, 4.0, 1.3, "Iris-versicolor"],
    [6.5, 2.8, 4.6, 1.5, "Iris-versicolor"],
    [5.7, 2.8, 4.5, 1.3, "Iris-versicolor"],
    [6.3, 3.3, 4.7, 1.6, "Iris-versicolor"],
    [4.9, 2.4, 3.3, 1.0, "Iris-versicolor"],
    [6.6, 2.9, 4.6, 1.3, "Iris-versicolor"],
    [5.2, 2.7, 3.9, 1.4, "Iris-versicolor"],
    [5.0, 2.0, 3.5, 1.0, "Iris-versicolor"],
    [5.9, 3.0, 4.2, 1.5, "Iris-versicolor"],
    [6.0, 2.2, 4.0, 1.0, "Iris-versicolor"],
    [6.1, 2.9, 4.7, 1.4, "Iris-versicolor"],
    [5.6, 2.9, 3.6, 1.3, "Iris-versicolor"],
    [6.7, 3.1, 4.4, 1.4, "Iris-versicolor"],
    [5.6, 3.0, 4.5, 1.5, "Iris-versicolor"],
    [5.8, 2.7, 4.1, 1.0, "Iris-versicolor"],
    [6.2, 2.2, 4.5, 1.5, "Iris-versicolor"],
    [5.6, 2.5, 3.9, 1.1, "Iris-versicolor"],
    [5.9, 3.2, 4.8, 1.8, "Iris-versicolor"],
    [6.1, 2.8, 4.0, 1.3, "Iris-versicolor"],
    [6.3, 2.5, 4.9, 1.5, "Iris-versicolor"],
    [6.1, 2.8, 4.7, 1.2, "Iris-versicolor"],
    [6.4, 2.9, 4.3, 1.3, "Iris-versicolor"],
    [6.6, 3.0, 4.4, 1.4, "Iris-versicolor"],
    [6.8, 2.8, 4.8, 1.4, "Iris-versicolor"],
    [6.7, 3.0, 5.0, 1.7, "Iris-versicolor"],
    [6.0, 2.9, 4.5, 1.5, "Iris-versicolor"],
    [5.7, 2.6, 3.5, 1.0, "Iris-versicolor"],
    [5.5, 2.4, 3.8, 1.1, "Iris-versicolor"],
    [5.5, 2.4, 3.7, 1.0, "Iris-versicolor"],
    [5.8, 2.7, 3.9, 1.2, "Iris-versicolor"],
    [6.0, 2.7, 5.1, 1.6, "Iris-versicolor"],
    [5.4, 3.0, 4.5, 1.5, "Iris-versicolor"],
    [6.0, 3.4, 4.5, 1.6, "Iris-versicolor"],
    [6.7, 3.1, 4.7, 1.5, "Iris-versicolor"],
    [6.3, 2.3, 4.4, 1.3, "Iris-versicolor"],
    [5.6, 3.0, 4.1, 1.3, "Iris-versicolor"],
    [5.5, 2.5, 4.0, 1.3, "Iris-versicolor"],
    [5.5, 2.6, 4.4, 1.2, "Iris-versicolor"],
    [6.1, 3.0, 4.6, 1.4, "Iris-versicolor"],
    [5.8, 2.6, 4.0, 1.2, "Iris-versicolor"],
    [5.0, 2.3, 3.3, 1.0, "Iris-versicolor"],
    [5.6, 2.7, 4.2, 1.3, "Iris-versicolor"],
    [5.7, 3.0, 4.2, 1.2, "Iris-versicolor"],
    [5.7, 2.9, 4.2, 1.3, "Iris-versicolor"],
    [6.2, 2.9, 4.3, 1.3, "Iris-versicolor"],
    [5.1, 2.5, 3.0, 1.1, "Iris-versicolor"],
    [5.7, 2.8, 4.1, 1.3, "Iris-versicolor"],
    [6.3, 3.3, 6.0, 2.5, "Iris-virginica"],
    [5.8, 2.7, 5.1, 1.9, "Iris-virginica"],
    [7.1, 3.0, 5.9, 2.1, "Iris-virginica"],
    [6.3, 2.9, 5.6, 1.8, "Iris-virginica"],
    [6.5, 3.0, 5.8, 2.2, "Iris-virginica"],
    [7.6, 3.0, 6.6, 2.1, "Iris-virginica"],
    [4.9, 2.5, 4.5, 1.7, "Iris-virginica"],
    [7.3, 2.9, 6.3, 1.8, "Iris-virginica"],
    [6.7, 2.5, 5.8, 1.8, "Iris-virginica"],
    [7.2, 3.6, 6.1, 2.5, "Iris-virginica"],
    [6.5, 3.2, 5.1, 2.0, "Iris-virginica"],
    [6.4, 2.7, 5.3, 1.9, "Iris-virginica"],
    [6.8, 3.0, 5.5, 2.1, "Iris-virginica"],
    [5.7, 2.5, 5.0, 2.0, "Iris-virginica"],
    [5.8, 2.8, 5.1, 2.4, "Iris-virginica"],
    [6.4, 3.2, 5.3, 2.3, "Iris-virginica"],
    [6.5, 3.0, 5.5, 1.8, "Iris-virginica"],
    [7.7, 3.8, 6.7, 2.2, "Iris-virginica"],
    [7.7, 2.6, 6.9, 2.3, "Iris-virginica"],
    [6.0, 2.2, 5.0, 1.5, "Iris-virginica"],
    [6.9, 3.2, 5.7, 2.3, "Iris-virginica"],
    [5.6, 2.8, 4.9, 2.0, "Iris-virginica"],
    [7.7, 2.8, 6.7, 2.0, "Iris-virginica"],
    [6.3, 2.7, 4.9, 1.8, "Iris-virginica"],
    [6.7, 3.3, 5.7, 2.1, "Iris-virginica"],
    [7.2, 3.2, 6.0, 1.8, "Iris-virginica"],
    [6.2, 2.8, 4.8, 1.8, "Iris-virginica"],
    [6.1, 3.0, 4.9, 1.8, "Iris-virginica"],
    [6.4, 2.8, 5.6, 2.1, "Iris-virginica"],
    [7.2, 3.0, 5.8, 1.6, "Iris-virginica"],
    [7.4, 2.8, 6.1, 1.9, "Iris-virginica"],
    [7.9, 3.8, 6.4, 2.0, "Iris-virginica"],
    [6.4, 2.8, 5.6, 2.2, "Iris-virginica"],
    [6.3, 2.8, 5.1, 1.5, "Iris-virginica"],
    [6.1, 2.6, 5.6, 1.4, "Iris-virginica"],
    [7.7, 3.0, 6.1, 2.3, "Iris-virginica"],
    [6.3, 3.4, 5.6, 2.4, "Iris-virginica"],
    [6.4, 3.1, 5.5, 1.8, "Iris-virginica"],
    [6.0, 3.0, 4.8, 1.8, "Iris-virginica"],
    [6.9, 3.1, 5.4, 2.1, "Iris-virginica"],
    [6.7, 3.1, 5.6, 2.4, "Iris-virginica"],
    [6.9, 3.1, 5.1, 2.3, "Iris-virginica"],
    [5.8, 2.7, 5.1, 1.9, "Iris-virginica"],
    [6.8, 3.2, 5.9, 2.3, "Iris-virginica"],
    [6.7, 3.3, 5.7, 2.5, "Iris-virginica"],
    [6.7, 3.0, 5.2, 2.3, "Iris-virginica"],
    [6.3, 2.5, 5.0, 1.9, "Iris-virginica"],
    [6.5, 3.0, 5.2, 2.0, "Iris-virginica"],
    [6.2, 3.4, 5.4, 2.3, "Iris-virginica"],
    [5.9, 3.0, 5.1, 1.8, "Iris-virginica"],
])
train_Set = []
test_Set = []
aux_train = []
aux_test = []
list_Clases = []
matC = []



def separar_Clases():
    """Metodo para separar las clases
    Se recorre el array iris_DataSet con un foreach:
        Se compara si la clase del elemento existe en la lista de clases (list_Clases):
            Se avanza a la siguiente iteracion
        Si no existe:
            Se agrega la clase del elemnto a la lista de clases (list_Clases)
    """
    for c in iris_DataSet:
        if c[-1] in list_Clases:
            continue
        else:
            list_Clases.append(c[-1])


def contar_Clase(i):
    """Metodo para contar los elementos de clase con un parametro que sera la posicion i
    Se declara un contador en 0 (cont)
    Se recorre el array iris_DataSet con un foreach:
        Se comparar si la clase del elemento es igual a la clase de la lista de clases en la posicion que se paso como parametro:
            Se incrementa el contador cont
    Se retorna el contador
    """
    cont = 0
    for n in iris_DataSet:
        if n[-1] == list_Clases[i]:
            cont += 1
    return cont


def generar_Train_Test(portc):
    """Metodo para generar el Train y Test con un parametro que sacara el porcentaje (portc) de los elementos
        Se manda llamar el metodo para separar clases
        Se manda llamar el metodo para llenar la matriz matC
        Se recorre el array list_Clases del 0 a su longitud, para obtener los index (x) de elementos del array:
            Se declara la variable i en 0
            Se declara una variable percentage que sera igual a los (elementos de clase con ayuda del metodo contar_Clases(x) por el paremetro (portc)) entre 100
            Un ciclo while mientras i sea menor a percentage:
                Se declara un numero random entre el 0 y la longitud de iris_Dataset -1 (num)
                Se declara un elemento iris que es igual al elemento sacado random iris_DataSet[num]
                Se compara si la clase del elemento iris (iris[-1]) es igual a la clase de la lista de clases (list_Clases[x]):
                    Se agrega el elemento a train_Set que se elimino con pop de iris_DataSet en la posicion num
                    Se incrementa el contador i
    """
    separar_Clases()
    llenadoMatriz()
    for x in range(0, len(list_Clases)):
        i = 0
        percentage = (contar_Clase(x) * portc) / 100
        while i < percentage:
            num = random.randint(0, len(iris_DataSet) - 1)
            iris = iris_DataSet[num]
            if iris[-1] == list_Clases[x]:
                train_Set.append(iris_DataSet.pop(num))
                i += 1


def distance(P, Q):
    """Metodo para sacar la distancia entre dos puntos con dos parametros P y Q
    Se retorna la raiz cuadrada de la sumatoria del cuadrado de la resta entre P y Q
    """
    return np.sqrt(np.sum((P - Q) ** 2))


def llenadoMatriz():
    """Metodo para llenar la matriz de 0 (Numero de clases) X (Numero de clases)
    Se recorre un for del 0 hasta la longitud de la lista de clases (3):
        se crea una lista vacia
        Se vuelve a recorre un for del 0 hasta la longitud de la lista de clases (3):
            Se le agregan 0 a la lista
        Se agrega la lista con tres ceros a la matriz de confusion (matC)
    """
    for i in range(0, len(list_Clases)):
        list = []
        for j in range(0, len(list_Clases)):
            list.append(0)
        matC.append(list)


def matrizConfusion(clases):
    """Metodo para contar los elementos por clase con un parametro una lista con 2 clases
    Se recorre un for del 0 hasta la longitud de la lista de clases (3):
        se compara si la primer clase de la lista que se paso de parametro es igual a la clase de la lista de clases en la posicion de i:
            Se vuelve a recorre un for del 0 hasta la longitud de la lista de clases (3):
                se vuelve a comparar si la segunda clase de la lista que se paso de parametro es igual a la clase de la lista de clases en la posicion de j:
                    se declara un contador (c) que sera igual al valor de el elemento en la matriz de confucion en la posicion ij (matC[i][j])
                    se asina al elemento matC[i][j] el valor del contador (c) mas 1
    """
    for i in range(0, len(list_Clases)):
        if clases[0] == list_Clases[i]:
            for j in range(0, len(list_Clases)):
                if clases[1] == list_Clases[j]:
                    c = matC[i][j]
                    matC[i][j] = c+1


def distanciaPunto(ptrain, puntoTest, claseTest):
    """Metodo para comparar un elementos con un array de elementos con 3 pararmetros, (array, elemento, clase del elemento)
    Se crea una lista para las distancias (D)
    Se crea una lista auxiliar (C) para guardar los clases de los 2 puntos
    Se recorre el array pTrain del 0 a su longitud, para obtener los index de elementos del array:
        Se agrega a D la distancia entre el puntoTest y el punto ptrain con ayuda del metodo distance que rquiere dos parametros el punto P y Q
        Se declara un elemento que sera igual a la distancia entre los mismos puntos
        Se agrega a C la clase del punto test y la clase del punto train
        Se imprime el puntoTest, el puntoTrain y su distancia
    Se imprime la distancia minima dentro de D
    Se declara un index que sera igual a la posicion de la minima distancia dentro de D
    Se manda a llamar el metodo matrizconfusion que necesita de parametro una lista con dos clases, se le manda el elemento de C[index]
    Se imprimen separadores
    """
    D = []
    C = []
    for puntTrain in range(0, len(ptrain)):
        D.append(distance(puntoTest, ptrain[puntTrain]))
        di = distance(puntoTest, ptrain[puntTrain])
        C.append([claseTest, aux_train[puntTrain]])
        print("Punto Test:", puntoTest, "Punto Train:", ptrain[puntTrain], "Distancia:", di)
    index = D.index(min(D))
    matrizConfusion(C[index])
    print(min(D))
    print("Clase Test:", C[index][0], "/ Clase Train:", C[index][1])
    print("-" * 91)
    print("-" * 91)


def minima_Distancia():
    """Metodo para eliminar la etiqueta al test y train y asi poder sacar la minima distancia
    se crea una lista pTest
    se crea una lista pTrain
    Con un forech se recorre la lista train.Set:
        se agrega a la lista auxiliar la etiqueta del elemento train que se le removio con el pop
        se agrega a pTrain el elemento train ya sin etiqueta
    Se convierte la lista pTrain a un array numpy
    Mismo procedimiento pero ahora con el test_Set
    Se recorre el array pTest del 0 a su longitud, para obtener los index de elementos del array:
        Se llama el metodo distancia punto que requiere un array(train), un elemento de pTest, y la etiqueta del elemento pTest
    """
    pTrain = []
    pTest = []
    for train in train_Set:
        aux_train.append(train.pop(-1))
        pTrain.append(train)
    pTrain = np.array(pTrain)
    for test in test_Set:
        aux_test.append(test.pop(-1))
        pTest.append(test)
    pTest = np.array(pTest)
    for puntTest in range(0, len(pTest)):
        distanciaPunto(pTrain, pTest[puntTest], aux_test[puntTest])


def exactitudMatriz():
    """Metodo para sacar la exactitud de la clasificacion de las clases
    se declara el contador en 0
    Se recorre el array matC del 0 a su longitud, para obtener los index (i) de elementos del array:
        Se vuelve a recorrer el array matC del 0 a su longitud, para obtener los index(j) de elementos del array:
            Se compara si los index i y j son iguales:
                sumatoria sera igual a la sumatoria mas el elemento matC[i][j]
    Se declara la exactitud que sera igual a la (sumatoria por 100) entre la longitud de elementos del tes_Set
    Se retorna la exactitud
    """
    sumatoria = 0
    for i in range(0, len(matC)):
        for j in range(0, len(matC)):
            if i == j:
                sumatoria += matC[i][j]
    exactitud = (sumatoria * 100 / len(test_Set))
    return exactitud


#Se llama el metodo para generar el train y tes y se le pasa el porcentaje que queremos en el train
generar_Train_Test(70)
#Se asigna que test_Set sera igual a los elementos de restaron de iris_DataSet
test_Set = iris_DataSet
#Se imprimen las listas y matrices
print(train_Set)
print(len(train_Set))
print(test_Set)
print(len(test_Set))
#Se llama al metodo para sacar la minima distancia
minima_Distancia()
#Se imprime la matriz de confusion y la exactitud
print("Matriz de confusion:", matC)
print("Exactitud de clasificacion:", exactitudMatriz())





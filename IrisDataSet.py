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
    for c in iris_DataSet:
        if c[4] in list_Clases:
            continue
        else:
            list_Clases.append(c[4])


def contar_Clase(i):
    cont = 0
    for n in iris_DataSet:
        if n[4] == list_Clases[i]:
            cont += 1
    return cont


def generar_Train_Test(portc):
    separar_Clases()
    llenadoMatriz()
    for x in range(0, len(list_Clases)):
        i = 0
        percentage = (contar_Clase(x) * portc) / 100
        while i < percentage:
            num = random.randint(0, len(iris_DataSet) - 1)
            iris = iris_DataSet[num]
            if iris[4] == list_Clases[x]:
                train_Set.append(iris_DataSet.pop(num))
                i += 1


def distance(P, Q):
    return np.sqrt(np.sum((P - Q) ** 2))


def llenadoMatriz():
    for i in range(0, len(list_Clases)):
        list = []
        for j in range(0, len(list_Clases)):
            list.append(0)
        matC.append(list)


def matrizConfusion(clases):
    for i in range(0, len(list_Clases)):
        if clases[0] == list_Clases[i]:
            for j in range(0, len(list_Clases)):
                if clases[1] == list_Clases[j]:
                    c = matC[i][j]
                    matC[i][j] = c+1


def distanciaPunto(ptrain, puntoTest, claseTest):
    D = []
    C = []
    for puntTrain in range(0, len(ptrain)):
        D.append(distance(puntoTest, ptrain[puntTrain]))
        di = distance(puntoTest, ptrain[puntTrain])
        C.append([claseTest, aux_train[puntTrain]])
        print("Punto Test:", puntoTest, "Punto Train:", ptrain[puntTrain], "Distancia:", di)
    print(min(D))
    n = D.index(min(D))
    matrizConfusion(C[n])
    print("-" * 91)
    print("-" * 91)


def minima_Distancia():
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
    sumatoria = 0
    for i in range(0, len(matC)):
        for j in range(0, len(matC)):
            if i == j:
                sumatoria += matC[i][j]
    exactitud = (sumatoria * 100 / len(test_Set))
    return exactitud

generar_Train_Test(70)
test_Set = iris_DataSet
print(train_Set)
print(len(train_Set))
print(test_Set)
print(len(test_Set))
minima_Distancia()
print("Matriz de confusion:", matC)
print("Exactitud de clasificacion:", exactitudMatriz())





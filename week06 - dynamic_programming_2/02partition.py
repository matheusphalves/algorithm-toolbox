from functools import reduce

numberItens = int(input(""))
values2 = input("").split() #values of each item (size n)
itensList = [int(x) for x in values2]

#===============SOLUTION
def partition(itens):
    sum = reduce(lambda x,y: x+y, itens)
    if(sum%3==0):
        fraction = int(sum / 3)
        eachPerson = knapsack2(fraction, itens)[-1][-1]
        if(sum - 3*eachPerson==0):
            return 1
        else:
            return 0
    else:
        return 0

#version without repetitions
def knapsack2(weight, itens):
    #cada coluna é um valor de peso
    #cada linha significa quantidade de itens salvos na mochila
    matrixValue = [[0 for i in range(0, weight+1)] for j in range(0, len(itens))]   
    for i in range(0, len(itens)):
        for w in range(1, weight+1): #nada a adicionar em mochila com peso 0
            matrixValue[i][w] = matrixValue[i-1][w]
            if(itens[i]<=w): #wi <= w
                #val = valor(pesoAtual - pesodoItem) + valorItem
                val = matrixValue[i-1][w-itens[i]] + itens[i] #algoritmo modificado para ter a soma dos pesos ao invés de valores
                if(val > matrixValue[i][w]):
                    matrixValue[i][w] = val
    return matrixValue

#===============END OF SOLUTION


print(partition(itensList))
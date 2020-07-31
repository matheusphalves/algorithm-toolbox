values = input("").split() #weight and number of golden bars
values2 = input("").split() #weight of each bar (size n)
goldList = [int(x) for x in values2]

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

if __name__ == '__main__':
    #print(knapsack(10, itens))
    goldList.insert(0, 0)
    matrixValue = knapsack2(int(values[0]), goldList)
    print(matrixValue[-1][-1])




#With repetitions
#weights - peso da mochila
#itens - tupla com o par (valor, peso) da tupla
def knapsack(weight, itens):
    values = [0]*(weight+1) #lista com todos os valores otimizados para pesos anteriores
    values[0] = 0
    for w in range(1, weight+1): #mochila com peso 0 não pode adicionar item algum!
        values[w] = 0
        for i in range(0, len(itens)):
            if(itens[i][0]<=w):
                #val = valor(pesoAtual - pesodoItem) + valorItem
                print(i)
                val = values[w-itens[i][0]] + itens[i][1]
                if(val > values[w]):
                    values[w] = val
    return values

#version without repetitions


def knapsack2(weight, itens):
    #cada coluna é um valor de peso
    #cada linha significa quantidade de itens salvos na mochila
    matrixValue = [[0 for i in range(0, weight+1)] for j in range(0, len(itens)+1)]   
    for i in range(1, len(itens)):
        for w in range(1, weight+1): #nada a adicionar em mochila com peso 0
            matrixValue[i][w] = matrixValue[i-1][w]
            if(itens[i][0]<=w): #wi <= w
                #val = valor(pesoAtual - pesodoItem) + valorItem
                val = matrixValue[i-1][w-itens[i][0]] + itens[i][1]
                if(val > matrixValue[i][w]):
                    matrixValue[i][w] = val
    return matrixValue


weight = 10
itens = ((6, 30), (3, 14), (4, 16), (2, 9))

if __name__ == '__main__':
    #print(knapsack(10, itens))
    print(knapsack2(10, itens))



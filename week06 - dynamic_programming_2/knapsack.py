
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


weight = 10
itens = ((6, 30), (3, 14), (4, 16), (2, 9))

if __name__ == '__main__':
    print(knapsack(10, itens))



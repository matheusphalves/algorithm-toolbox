value = int(input(''))

def calculator(number):
    listNumbers = [0]*(number+1)
    listNumbers[1] = 1

    for i in range(1, number+1):
        listNumbers[i] = listNumbers[i-1] + 1
        if(i%2==0):
            #escolha da menor quantidade de operações
            listNumbers[i] = min(1 + listNumbers[i//2], listNumbers[i])
        if(i%3==0):
            listNumbers[i] = min(1 + listNumbers[i//3], listNumbers[i])

    #lista com valores a cada iteração
    operations = []
    while(number > 1):
        operations.append(number)
        if(listNumbers[number-1] == listNumbers[number] - 1):
            number -= 1 #subtração de 1
        #número é divisível por 2 e resultado é igual ao atual-1
        elif (number%2==0 and (listNumbers[number//2] == listNumbers[number] -1)):
            number //=2
        #número é divisível por 3 e resultado é igual ao atual-1
        elif (number%3==0 and (listNumbers[number//3] == listNumbers[number] -1)):
            number //=3
    operations.append(1)
    operations.reverse()
    return operations
listFinal = calculator(value)
print(len(listFinal)-1)
for x in listFinal:
        print(x, end=' ')

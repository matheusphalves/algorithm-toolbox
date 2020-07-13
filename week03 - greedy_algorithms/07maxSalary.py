n = int(input(""))
values = input("").split()

def greaterOrEqual(a, b): #método verifica qual dos dois números é maior
    #a combinação é verdadeira se a junção a+b der um numero maior que b + a
    return a+b>=b+a

def maxSalary(list): #metódo verifica o máximo valor possível
    result = ""
    while(len(list)!=0):#enquanto a lista não for vazia, devemos procurar os maiores digitos possíveis
        max = list[0]
        for actual in list: #sempre ignoramos o primeiro item
            if(greaterOrEqual(actual, max)):#verifico se o numero atual pode ser maior quando combinado com o maximo. Se sim, ele é o máximo
                max = actual
        list.remove(max)
        result += max
    return result

print(maxSalary(values))
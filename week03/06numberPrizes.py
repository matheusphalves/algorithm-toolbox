

def maxPrizeSequence(number):
    list = [1]
    sum = 0;
    step = 1;
    while(sum<number):
        actualValue = list[-1] + step
        actualSum = sum + actualValue
        
        if(actualSum <number):#proximo elemento
            nextValue =  actualValue + 1 # next
            if(actualSum + actualValue + nextValue>number):
                step = number - actualValue
                list.append(list[-1] + step)
                break #último valor adicionado
         
            list.append(actualValue)
            sum += list[-1]
            step = 1
            print("sum ", sum)
        else:
            list.append(actualValue)#último valor adicionado na lista!
            
    return list


number = input("")
print(maxPrizeSequence(int(number)))

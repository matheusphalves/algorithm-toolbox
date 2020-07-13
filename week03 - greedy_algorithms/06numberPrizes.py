

def maxPrizeSequence(number):
    list = [0]
    sum = 0;
    while(sum<=number):
        step = 1
        actualValue = list[-1] + step
        actualSum = sum + actualValue
        if(actualSum<=number):
            list.append(actualValue)
            sum += list[-1]
            if(sum==number):
                break
            if (actualSum + (actualValue + 1) > number):
                step = 0
                while(actualSum + step <number):
                    step +=1
                list[-1] = (actualValue + step)
                sum += list[-1]
    list.remove(0)
    return list


number = input("")
list = maxPrizeSequence(int(number))
print(len(list))
string = ""
for x in list:
    string += str(x) + " "
print(string)

from functools import reduce

listFib = [0,1]; #list with fib results

def fib(n):
    sizeList = len(listFib)
    if n<sizeList:
        return listFib[n]
    else:
        for i in range(n -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append((listFib[-1] + listFib[-2])%10) #actual term is sum of previous two terms in the sequence
    return listFib[-1] #last index of list


def sumFibRange(n, m):
    sum = 0

    if n%60<m%60:
        shorter = n%60;
        big = m%60
        fib(m % 60)
    else:
        shorter = m%60;
        big = n%60
        fib(n%60)
    for i in range(shorter, big+1):
        sum += listFib[i]

    return sum%10 #last digit of sum


#5618252 6583591534156

number = input("").split()
print(sumFibRange(int(number[0]), int(number[1])))
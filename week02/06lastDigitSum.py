from functools import reduce
listFib = [0,1]; #list with fib results

def fib(n):
    sizeList = len(listFib) #
    if n<sizeList:
        return listFib[n]
    else:
        #(sizeList-1) the last index value
        # n is the index than i need to know
        #the, i must calculate result = n - sizeList-1
        for i in range(n -(sizeList-1)): #I don't calculate all 'n' terms. I need to know how many terms (index) must be increased.
            listFib.append((listFib[-1] + listFib[-2])%10) #actual term is sum of previous two terms in the sequence
    return listFib[-1] #last index of list

def sumFib(n):
    if(n==0 or n==1):
        return n
    fib(n%60) #the last digits of fib sequences are periodic. For pi(10) = 60 length. Then, after 60th, the last digits will be repeat!
    sum =0
    for i in range(0, (n%60)+1):
        sum += listFib[i]
    filterList = list(filter(lambda x: listFib.index(x) <= n % 60, listFib))
    sum = reduce((lambda x, y: x + y), filterList)
    return sum%10 #last digit of sum

number = int(input(""))
print(sumFib(number))


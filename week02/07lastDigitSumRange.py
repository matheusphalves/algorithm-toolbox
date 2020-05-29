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
    if n%60>m%60:#the last digits of fib sequences are periodic. For pi(10) = 60 length. Then, after 60th, the last digits will be repeat!
        big = n%60
        short = m%60
        fib(n%60)
    else:
        big = m%60
        short = n%60 + 1
        fib(m%60)
    sum =0
    print(short, big)
    for i in range(short, big +1):
        sum += listFib[i]
    return sum%10 #last digit of sum


number = input("").split()
print(sumFibRange(int(number[0]), int(number[1])))
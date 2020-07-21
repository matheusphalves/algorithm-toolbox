value = int(input(""))

coinsList = [1, 3,4]

def moneyChange(valueMoney, minCoins):
    for cents in range(valueMoney+1):
        coinCount = cents
        #laço seleciona moedas necessárias para compor valor
        for actualCoin in [c for c in coinsList if c<=cents]:
            if(minCoins[cents-actualCoin]+ 1 < coinCount):
                coinCount = minCoins[cents-actualCoin] +1
        minCoins[cents] = coinCount
    return minCoins[valueMoney]
print(moneyChange(value, [0]*(value+1)))


n = int(input("")) #size of list
valuesN = input("").split() #input values
valuesN = [int(item) for item in valuesN] #list of integers
valuesN.sort() #sorted list
dictionary = {i:0 for i in set(valuesN)} #dictionary with terms

def majoritaryElement(array, dictionary):
    for i in range(0, len(array)):
        dictionary[array[i]] +=1
    result = list(filter(lambda x: x>n//2, list(dictionary.values())))
    return len(result)

print(majoritaryElement(valuesN, dictionary))


#busca melhorada, são evitadas comparações que já foram feitas.
# uma melhor forma de buscar seria encontrar os 2 maiores valores da sequência e então multiplicá-los.

words = input().split()

list = []

for x in words:
	list.append(int(x))

bigger = 0;

for i in range(len(list)):
	for j in range(i+1, len(list)):
		mux = list[i]*list[j];
		if(mux>bigger):
			bigger=mux;


print(bigger)

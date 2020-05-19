number = input()
words = input().split()

list = []

for x in words:
	list.append(int(x))

list.sort();

print(list[len(list)-2]*list[len(list)-1])

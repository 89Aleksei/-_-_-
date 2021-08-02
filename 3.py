s = input()
for i in s:
	if i in range(10):
		i = chr(i)
	else:
		i = ord(i)
        print(i)
def checkMatch(first, second):
	if first == '(' and second == ')':
		return True
	if first == '[' and second == ']':
		return True
	if first == '{' and second == '}':
		return True
	return False

input1 = input()
inputLength = len(input1)

stack = []

if inputLength % 2 != 0:
	print("BAD")
	exit()

for i in input1:
	if not stack:
		stack.append(i)
		continue
	else:
		elem = stack.pop()
		if checkMatch(elem, i):
			continue
		else:
			stack.append(elem)
			stack.append(i)

if not stack:
	print("GOOD")
else:
	print("BAD")








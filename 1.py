#Answer 1

tup=()
pos,neg,odd,even,zero=0,0,0,0,0
for i in range(20):
	i=int(input("Enter an element"))
	tup.append(i)
for element in tup:
	if element>0:
		pos=pos+1;
	else:
		neg=neg+1
	if element%2==0:
		even=even+1
	else:
		odd=odd+1
	if element==0:
		zero=zero+1
print("Positive Numbers:%d"%pos)
print("Negative Numbers:%d"%neg)
print("Even Numbers:%d"%even)
print("Odd Numbers:%d"%odd)
print("Number of zeros:%d"%zero)
	
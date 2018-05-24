#Answer 4
set1=set()
set2=set()
size1=int(input("Enter size of first set"))
size2=int(input("Enter size of set 2"))
for i in range(size1):
	item=int(input("Enter " +str(i+1)+" value"))
	set1.add(item)
for i in range(size2):
	itm=int(input("Enter " +str(i+1)+" value"))
	set2.add(itm)
print("Difference=",(set1-set2))
print("Comparison=",(set1^set2))
print("Intersection=",(set1&set2))

	
	
#Answer 5
pair={}
n=int(input("Enter size"))
for i in range(0,n):
        word = input().split()
        key = word[0]
        value = word[1]
        pair[key]=value

print(pair)

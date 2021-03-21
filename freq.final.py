string=input("please enter word:")
char=input("please enter the letter for which you want the count")
count=0
for i in range(len(string)):
	if(string[i]==char):
		count=count+1
print("number of times the letter has repeated is",count)





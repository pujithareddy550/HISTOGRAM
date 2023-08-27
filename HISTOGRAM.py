def Histogram(l):
    l=sorted(l)
    CountOfEachNumber=[l.count(i) for i in l]
    D=dict(list(zip(l,CountOfEachNumber)))
    ConvertDictToList=list(D.items())
    p=sorted(ConvertDictToList,key=lambda x:x[1])
    return p
while(1):
	print("ENTER THE LIST OF NUMBERS")
	lst=list(map(int,input().split(",")))#taking input list of numbers
	print(Histogram(lst))#calling historgram
	
	print("IF YOU WANT TO STOP PRESS [Y/y] OTHERWISE [N/n]")
	choice=input()
	if choice=="y"or choice=="Y":
	    break
liste1=[1,2,3,4]
liste2=[1,2]
func=list(map(lambda x,y:(x+y,x-y),liste1,liste2))
print(func)
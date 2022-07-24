from collections import deque
liste=deque([2,8,9])
liste2=deque([7,8,9])
func=list(map(lambda x,y:x+y,liste,liste2))
print(func)
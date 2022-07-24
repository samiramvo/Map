liste1=[2,3,4,4]
liste2=[3,8,0,9]
liste3=[1,2]

func=list(map(lambda liste1,liste2,liste3:liste1+liste2+liste3,liste1,liste2,liste3))

print(func)
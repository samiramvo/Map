dictionnaire={"Livres":[1,6,8],"Bananes":[2,8,9],"Cerise":[3,8]}

func=map(dict,zip(*[[(key,i) for i in values]for key,values in dictionnaire.items()]))

print(dict(func))

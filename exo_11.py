liste=[1,2,3,4,5]
def somme(liste0):
    som=0
    for i in liste0:
        som+=i
    return som
liste2=list(map(int,liste))

print(somme(liste2))
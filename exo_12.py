from array import array

table=array("i",[-3,8,-3,-4,1,3,9,0,4])
pos=[i for i in table if i>0]
neg=[i for i in table if i<0]
nul=[i for i in table if i==0]

print("Positif:",pos)
print("Négatif:",neg)
print("Nul",nul)
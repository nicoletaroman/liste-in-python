a=[]
b=[]
with open("input.txt","r") as f:
    x=list(f.readlines())
    prenume=(list(x))
with open("inputvarsta.txt","r") as f:
    y=list(f.readlines())
    varsta=(list(y))
for i in range(0,len(varsta)):
    varsta[i]=int(varsta[i])

for j in range(0,len(prenume)):
    print(prenume[j],"are varsta de",varsta[j])

prenume.append("Andreea")
prenume.append("Ioan")
varsta.append("34")
varsta.append("23")
print(prenume)
print(varsta)
prenume.pop(2)
varsta.pop(2)
print(prenume)
print(varsta)
print(prenume[0:3])
print(prenume[::-1])
print("elementele cu indicile 2 sunt",prenume[2],"si",varsta[2])
print("elementele cu indicile 4 sunt",prenume[4],"si",varsta[4])
j=prenume[0:5]
h=varsta[0:5]
print("elementele de la 0 la 5 sunt",j,h)

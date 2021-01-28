a=[]
with open("input.txt","r") as f:
    x=list(f.readlines())
    prenume=(list(x))
with open("inputvarsta.txt","r") as f:
    y=list(f.readlines())
    varsta=(list(y))
for i in range(0,len(varsta)):
    varsta[i]=int(varsta[i])

for j in range(0,len(prenume)):
for n in range(0,len(varsta)):
    print(a[j]),"are varsta de",a[n]


#sa se afle suma cifrelor unui nr citit 
#de la tastatura
x=int(input("dati un nr"))
y=list(str(x))
print(y)
for i in range(0,len(y)):
    y[i]=int(y[i])
suma=sum(y)
print(suma)


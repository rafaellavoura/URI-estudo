import math
catetooposto = int(input('Valor do cateto oposto: '))
catetoadjacente = int(input('Valor do cateto adjacente: '))
pitagoras = (pow(catetooposto, 2) + pow(catetoadjacente, 2))
hipotenusa = math.sqrt(pitagoras)
print(f"{hipotenusa:.2f}")
distancia = int(input('Qual foi a quantidade de KM percorrido? '))
tempoalugado = int(input('Por quantos dias ele foi alugado? '))
preçodocarro = 60
kmrodados = 0.15
preçototal = (preçodocarro * tempoalugado) + (kmrodados * distancia)
print('O total a pagar é:', f"{preçototal:.2f}")




'''
deltaT = int(input())
velocidade = int(input())
deltaS = deltaT * velocidade
consumoCarro = 11
consumoTotal = deltaS/consumoCarro
print('%.3f' % consumoTotal)
'''
gasolina = 4.69
etanol = 3.50
consumoGasolina = 11
consumoEtanol = 8
percurso = 500
litrosGastosGasolina = percurso/consumoGasolina
litrosGastosEtanol = percurso/consumoEtanol
valorGasolina = litrosGastosGasolina * gasolina
valorEtanol = litrosGastosEtanol * etanol
print(valorGasolina)
print(valorEtanol)
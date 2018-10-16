nome = input()
salarioFixo = float(input())
vendasDoMes = float(input())
bonus = vendasDoMes * 0.15
total = bonus + salarioFixo
print('TOTAL = R$ %.2f' % total)
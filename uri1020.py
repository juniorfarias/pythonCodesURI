idadeEmDias = int(input())
anos = idadeEmDias//365
restoAnos = idadeEmDias%365
meses = restoAnos//30
restoMeses = restoAnos%30
dias = restoMeses//1
print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
tempo = int(input())
horas = tempo // 3600
restoHoras = tempo % 3600
minutos = restoHoras//60
restoMinuto = restoHoras % 60
segundos = restoMinuto % 60
print('{}:{}:{}'.format(horas,minutos,segundos))
N = int(input())
if 0 < N < 1000000:
    cedulas100 = N//100
    resto100 = N % 100
    cedulas50 = resto100//50
    resto50 = resto100 % 50
    cedulas20 = resto50//20
    resto20 = resto50 % 20
    cedulas10 = resto20//10
    resto10 = resto20 % 10
    cedulas5 = resto10//5
    resto5 = resto10 % 5
    cedulas2 = resto5//2
    resto2 = resto5 % 2
    cedulas1 = resto2//1
    print('%d' % N)
    print('%d nota(s) de R$ 100,00' % cedulas100)
    print('%d nota(s) de R$ 50,00' % cedulas50)
    print('%d nota(s) de R$ 20,00' % cedulas20)
    print('%d nota(s) de R$ 10,00' % cedulas10)
    print('%d nota(s) de R$ 5,00' % cedulas5)
    print('%d nota(s) de R$ 2,00' % cedulas2)
    print('%d nota(s) de R$ 1,00' % cedulas1)
a,b,c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
maior = c
if a > maior:
    maior = a
    if b > maior:
        maior = b
elif b > maior:
    maior = b
    if a > maior:
        maior = a
print(maior)


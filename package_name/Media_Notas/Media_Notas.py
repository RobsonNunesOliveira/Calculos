a = float(input('Primeiro bimestre:  '))
if a > 10:
    a= float(input('Você digitou errado. Primeiro bimestre:  '))
b = float(input('Segundo bimestre:  '))
if b > 10:
    b= float(input('Você digitou errado. Segundo bimestre:  '))
c = float(input('Terceiro bimestre:  '))
if c > 10:
    c= float(input('Você digitou errado. Terceiro bimestre:  '))
d = float(input('Quarto  bimestre:  '))
if d > 10:
    d= float(input('Você digitou errado. Quarto bimestre:  '))

media = (a + b + c + d) / 4
print('media: {}'.format(media))


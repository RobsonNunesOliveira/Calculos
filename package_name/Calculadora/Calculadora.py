a= float(input('Entre com o primeiro valor:  '))
b= float(input('Entre com o segundo valor:  '))

soma= a + b
subtraçao= a - b
multiplicaçao= a * b
divisao= a / b
resto = a % b
porcentagem = (a+b)/100


resultado = ('soma:  {soma}, \nsubtraçao: {subtraçao}'
      '\nmultiplicaçao:  {multiplicaçao}'
      '\ndivisao: {divisao}'
      '\nporcentagem: {porcentagem}'
      '\nresto: {resto}'.format(soma=soma,
                                subtraçao=subtraçao,
                                resto=resto,
                                multiplicaçao=multiplicaçao,
                                divisao=divisao,
                                porcentagem=porcentagem))
print(resultado)
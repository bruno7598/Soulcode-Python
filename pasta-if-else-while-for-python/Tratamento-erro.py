#isso é um comentario, escreva informações para si mesmo
#o usuario não visualiza estes comentarios
#TODO: usualmente usado para marcar as coisas a serem corrigidas ou adicionadas
"""Isto é um comentario para proposito de documentação. Veremos com mais detalhes na parte de funções
"""
try:
 primeiro = 5
 segundo = 0
 resultado = primeiro + segundo
 print('CALCULADORA_V0.01')
except Exception as erro:
     print('ERRO: ', str(erro))

try:
 print('o resultado da divisão é: ', primeiro/segundo)
except Exception as erro:
     print('ERRO: ', str(erro))
try:  
 print('o resultado da soma é: ', resultado)
except Exception as erro:
     print('ERRO: ', str(erro))
try:
 print('o resultado da subtração é: ', primeiro-segundo)
except Exception as erro:
     print('ERRO: ', str(erro))
try:
 print('o resultado da multiplicação é: ', primeiro*segundo)
except Exception as erro:
     print('ERRO: ', str(erro))

finally:
 print("O codigo não para!")

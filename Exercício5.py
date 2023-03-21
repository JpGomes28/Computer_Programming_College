import os
os.system('cls' or 'clear')
import math

#EX Aula4 Ex 5

num = float(input('Digite um número qualquer: '))

if num > 0:
    raiz = math.sqrt(num)
    print(f'A raiz quadrada de {num} é {raiz:.2f}')
else:
    print('Não há raiz quadrada de um número negativo em R!')
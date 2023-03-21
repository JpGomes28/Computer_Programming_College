import os
os.system('cls' or 'clear')

#EX Aula4 Ex 3

num1 = int(input('Digite o número A: '))
num2 = int(input('Digite o número B: '))
num3 = int(input('Digite o número C: '))

if num2 < num1 and num2 < num3:
    print(f'O número B é o menor!')
else:
    print(f'O número B não é o menor!')
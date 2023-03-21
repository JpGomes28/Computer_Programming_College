import os
os.system('cls' or 'clear')

#EX Aula4 Ex 4

nota1 = int(input('Digite a sua nota no primeiro semestre: '))
nota2 = int(input('Digite a sua nota no segundo semestre: '))

media = (nota1 + nota2) / 2

if media >= 6:
    print(f'Você está aprovado com média {media}!')
else:
    print(f'Você está reprovado com a média {media}!')

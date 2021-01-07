def imc(peso, altura):
    return peso / (altura * altura)

nome = input('Digite o seu nome: ')
idade = int(input('Idade: '))
peso = int(input('Peso: '))
altura = float(input('Altura: '))

meu_imc = imc(peso, altura)

print(f'{nome} tem {idade} anos de idade e seu imc é {meu_imc:.2f}')
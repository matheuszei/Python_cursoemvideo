#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('Digite um valor: '))
print('=' * 35)
print('TABUADA')
print('=' * 35)
for c in range(0, 11):
    r = 0
    print('{} x {} = {}'.format(n, c, n*c))

cigarro = int(input('Cigarros por dia: '))
ano = int(input('Anos fumando: '))
total = cigarro * ano * 365
d = total/144
print(f'{d:.2f} dias de vida foram perdidos.')

import random
números = random.sample(range(100), 20)
pares = []
ímpares = []
for n in números:
    if n % 2 == 0:
        pares.append(n)
    else:
        ímpares.append(n)
print(f'Números sorteados: {números}')
print(f'Números pares: {pares}')
print(f'Números ímpares: {ímpares}')


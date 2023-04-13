import random
números = random.sample(range(100), 10)
maior = menor = números[0]
for n in números[1:]:
    if n > maior: maior = n
    if n < menor: menor = n
print(f'Números sorteados: {números}')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')




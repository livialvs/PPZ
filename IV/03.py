import random
vetor1 = random.sample(range(100), 10)
vetor2 = random.sample(range(100), 10)
vetor3 = []
for n in range(10):
    vetor3.append(vetor1[n])
    vetor3.append(vetor2[n])
print(f'Primeiro vetor: {vetor1}')
print(f'Segundo vetor: {vetor2}')
print(f'Terceiro vetor: {vetor3}')

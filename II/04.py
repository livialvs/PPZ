a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
if b <= a >= c:
    print(f'O maior número é {a:.2f}')
elif a < b > c:
    print(f'O maior número é {b:.2f}')
else:
    print(f'O maior número é {c:.2f}')

p = float(input('preço: '))
d = float(input('% de desconto: '))
desconto = p * d/100
preço = p - desconto
print(f'desconto: R$ {desconto:.2f}')
print(f'novo preço: R$ {preço:.2f}')


km = float(input('Km percorridos: '))
d = float(input('Dias com o carro: '))
preço = km * 0.15 + d * 60
print(f'Preço a pagar: R${preço:.2f}')

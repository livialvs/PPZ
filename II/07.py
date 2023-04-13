m = float(input('Área a ser pintada em m²: '))
if m % 54 == 0:
    latas = m/54
    print(f'Latas: {latas}')
    print(f'Valor: R${latas * 80:.2f}')
else:
    latas = int(m/54 + 1)
    print(f'Latas: {latas}')
    print(f'Valor: R${latas * 80:.2f}') 

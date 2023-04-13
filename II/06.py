valor = float(input('Valor por hora: '))
horas = int(input('Horas trabalhadas por mês: '))
salário = valor * horas
ir = salário * 11/100
inss = salário * 8/100
sindicato = salário * 5/100
salário2 = salário - ir - inss - sindicato
print(f'+Salário Bruto: R${salário:.2f}')
print(f'-IR: R${ir:.2f}')
print(f'-INSS: R${inss:.2f}')
print(f'-Sindicato: R${sindicato:.2f}')
print(f'=Salário Líquido: R${salário2:.2f}')

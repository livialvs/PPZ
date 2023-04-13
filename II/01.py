a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triângulo')
elif a == b == c:
    print('É um triângulo equilátero')
elif a == b or b == c or a == c:
    print('É um triângulo isóceles')
else:
    print('É um triângulo escaleno')




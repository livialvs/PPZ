cont = 0
for n in range(18644, 33088):
    if '2' in str(n) and '7' not in str(n):
        cont = cont + 1
print(cont)

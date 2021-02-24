# A estrutura for é mais interessante quando existe uma quantidade determinar de repetições
for i in range(1, 11): # 1 até 10
    print('i = {}'.format(i))

for j in range(10): # 0 até 9
    print(f'f = {j}')

# estrutura for aninhado
for x in range(1, 11):
    for y in range(1, 11):
        print(f'{x} * {y} = {x * y}')
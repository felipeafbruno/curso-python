print('Tabela verdade do AND (binario)')
# Tabela verdade do AND
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('')
print('Tabela verdade do OR (binario)')
# Tabela verdade do OR
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('')
print('Tabela verdade do XOR (binario)')
# Tabela verdade do XOR
print(True != True)
print(True != False)
print(False != True)
print(False != False)

print('')
print('Operador de Negaçao Logica (unario)')
# Operação de Negação Lógica
print(not True)
print(not False)

# Operadores bitwise
print('')
print('Operadores Bit-a-Bit (binario)')
print(True & False)
print(False | True)
print(True ^ False)

# Exemplo misturando operadores
saldo = 1000
salario = 4000
despesas = 2900

saldo_positivo = saldo > 0
despesas_controladas = salario - despesas >= 0.2 * salario
meta = saldo_positivo and despesas_controladas
print(meta)
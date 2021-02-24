from decimal import Decimal, getcontext
print(Decimal(1) / Decimal(7))

getcontext().prec = 4 # getcontext().prec -> Define uma precisão para o calculo utilizando o Decimal
print(Decimal(1) / Decimal(7))
print(Decimal.max(Decimal(1), Decimal(7))) # Decimal.max(Decimal(1), Decimal(7)) -> retorna o maior entre os valores passados

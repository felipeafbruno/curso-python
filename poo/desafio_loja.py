from datetime import datetime

from loja.cliente import Cliente
from loja.vendedor import Vendedor
from loja.compra import Compra


cliente = Cliente('Felipe', 26)
vendedor = Vendedor('Bernardo', 45, 2500)

compra1 = Compra(vendedor, datetime.now(), 65.48)
compra2 = Compra(vendedor, datetime.now(), 125.58)
compra3 = Compra(vendedor, datetime.now(), 1500.81)

cliente.registrar_compra(compra1)
cliente.registrar_compra(compra2)
cliente.registrar_compra(compra3)

data_ultima_compra = cliente.get_data_ultima_compra()
print('Data da ultima compra:', data_ultima_compra)

valor_total_compra = cliente.total_compras()
print('Valor total das compras: R$',valor_total_compra)
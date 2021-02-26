from pacote1 import module1
# resolvendo um conflito com nome de módulos com um alias/apelido 
# tanto para o módulo quanto para uma função dentro do módulo
from pacote2 import module1 as module_sub 

print('Soma', module1.somar(5, 5))
print('Subtracao', module_sub.subtracao(3,2))

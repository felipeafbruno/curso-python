trabalho_Terca = True
trabalho_Quinta = False

'''
- Confirmando os 2: TV 50' + sorvete
- Confirmando os 1: TV 32' + sorvete
- Confirmando os nenhum: Fica em casa
'''

tv_50 = trabalho_Terca and trabalho_Quinta
sorvete = trabalho_Terca or trabalho_Quinta
tv_32 = trabalho_Terca != trabalho_Quinta
mais_saudavel = not sorvete

print("TV50={} TV32={} sorvete={} Saudavel={}". format(tv_50, tv_32, sorvete, mais_saudavel))
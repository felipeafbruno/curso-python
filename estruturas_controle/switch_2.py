def get_dias_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sabado',
    }
    return dias.get(dia)


for dia in range(1, 8):
    dia_retornado = get_dias_semana(dia)
    if dia_retornado == 'Domingo' or dia_retornado == 'Sabado':
        print(f'{dia_retornado} é final de semana!')
    elif dia_retornado == 'Segunda' or dia_retornado == 'Terça' or dia_retornado == 'Quarta' or dia_retornado == 'Quinta' or dia_retornado == 'Sexta':
        print(f'{dia_retornado} é dia de semana!')

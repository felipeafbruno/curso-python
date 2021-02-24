from math import pi

if __name__ == '__main__':
    raio = input('Informe o raio: ')
    area_circunferencia = pi * (float(raio) ** 2)
    print(f'Resultado é = {area_circunferencia}')

print('Nome do módulo ', __name__)
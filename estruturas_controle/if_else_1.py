def verificarNota(nota):
    if nota >= 9.1 and nota <= 10.0 :
        print('A')
    elif nota >= 8.1 and nota <= 9.0:
        print('Nota A-')
    elif nota >= 7.1 and nota <= 8.0:
        print('Nota B')
    elif nota >= 6.1 and nota <= 7.0:
        print('Nota B-')
    elif nota >= 5.1 and nota <= 6.0:
        print('Nota C')
    elif nota >= 4.1 and nota <= 5.0:
        print('Nota C-')
    elif nota >= 4.0 and nota <= 3.1:
        print('Nota D')
    elif nota >= 2.1 and nota <= 3.0:
        print('Nota D-')
    elif nota >= 2.0 and nota <= 1.1:
        print('Nota E')
    elif nota >= 1.0 and nota <= 0.0:
        print('Nota E-')
    else:
        print('Nota informe precisa ser um valor numérico')

if __name__ == '__main__':
    print('Modulo: ' + __name__)
    nota = float(input('Informe a nota: '))
    verificarNota(nota)
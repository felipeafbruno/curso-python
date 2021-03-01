def fatorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n 
    else:
        return n * fatorial(n - 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')

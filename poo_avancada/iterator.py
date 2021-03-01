class RGB:
    def __init__(self):
        self.cores = ['red', 'green', 'blue'][::-1]

    def __iter__(self):
        return self

    # __next__() -> defini a classe como um Iterator
    def __next__(self):
        try:
            return self.cores.pop()
        except IndexError:
            raise StopIteration()

    
if __name__ == '__main__':
    cores = RGB()
    print(next(cores))
    print(next(cores))
    print(next(cores))

    for cor in RGB():
        print(cor)
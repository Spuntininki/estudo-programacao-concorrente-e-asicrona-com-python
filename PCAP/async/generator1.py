from typing import Generator

def fibo() -> Generator[int, None, None]:
    valor: int = 0
    proximoValor: int = 1

    while True:
        valor, proximoValor = proximoValor, valor + proximoValor
        yield valor

def counter():
    valor = 0

    while True:
        valor += 1
        yield valor



a = fibo()
b = counter()
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')
print(f'{b.__next__()}: {a.__next__()}')



print('\nPronto!')
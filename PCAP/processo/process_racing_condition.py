import multiprocessing

def deposita(valor):
    for _ in range(10_000):
        valor.value += 1

def saca(valor):
    for _ in range(10_000):
        valor.value -= 1

def transaciona(valor):
    print(f'valor inicial: {valor.value}')

    p1 = multiprocessing.Process(target=deposita, args=(valor, ))
    p2 = multiprocessing.Process(target=saca, args=(valor, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'valor final: {valor.value}')


if __name__ == '__main__':
    valor = multiprocessing.Value('i', 100)
    

    transaciona(valor)


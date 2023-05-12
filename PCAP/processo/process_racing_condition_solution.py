import multiprocessing

def deposita(valor, lock):
    for _ in range(10_000):
        with lock:
            valor.value += 1

def saca(valor, lock):
    for _ in range(10_000):
        with lock:
            valor.value -= 1

def transaciona(valor, lock):
    print(f'valor inicial: {valor.value}')

    p1 = multiprocessing.Process(target=deposita, args=(valor, lock))
    p2 = multiprocessing.Process(target=saca, args=(valor, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f'valor final: {valor.value}')


if __name__ == '__main__':
    valor = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()

    transaciona(valor, lock)


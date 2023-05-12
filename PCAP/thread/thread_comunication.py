from threading import Thread
from queue import Queue
import colorama
import time


def gera_dados(queue):
    for i in range(1, 11):
        queue.put(i)
        print(colorama.Fore.GREEN + f'Inserindo dados. valor: {i}')
        time.sleep(2)

def consome_dados(queue):
    while queue.qsize() > 0:
        valor = queue.get()
        print(colorama.Fore.RED + f'Processando dados. valor: {valor * 2}')
        time.sleep(1)
    queue.task_done()


if __name__ == '__main__':
    print('Inicio do processo')
    queue = Queue()
    th1 = Thread(target=gera_dados, args=(queue, ))
    th2 = Thread(target=consome_dados, args=(queue, ))
    colorama.init()
    th1.start()
    th1.join()

    th2.start()
    th2.join()
    colorama.deinit()
import threading
import time
from random import randint




def main():
    th1 = threading.Thread(target=contar, args=('elefante rosa', 10, randint(0, 3)))
    th2 = threading.Thread(target=contar, args=('Dragão vermelho', 5))
    
    th1.start()
    th2.start()
    print('Teste')
    th1.join()

def contar_segudos(tempo):
    for c in range(1, tempo + 1):
        print(f'{c} segundo(s)')
        time.sleep(1)

def contar(coisa, quantidade, sleep_time =1):
    for c in range(1, quantidade + 1):
        time.sleep(sleep_time)
        contar_segudos(sleep_time)
        print(f'{c} {coisa}(s)\n')
        

if __name__ == '__main__':
    main()
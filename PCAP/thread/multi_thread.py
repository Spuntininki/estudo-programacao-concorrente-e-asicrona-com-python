import threading
import time
def main():
    threads = [
        threading.Thread(target=contar, args=('Ovelha', 10)),
        threading.Thread(target=contar, args=('Jumento', 20)),
        threading.Thread(target=contar, args=('Cavalo', 10)),
    ]

    [th.start() for th in threads]

    [th.join() for th in threads]
    print('testando...')
    print('random input')

def contar(o_que, quantidade):
    for i in range(1, quantidade + 1):
        print(f'{i} {o_que}(s)...'+ '\n')
        time.sleep(1)


if __name__ == '__main__':
    main()
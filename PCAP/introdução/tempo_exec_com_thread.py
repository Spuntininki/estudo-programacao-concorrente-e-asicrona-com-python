import datetime, math
import threading, multiprocessing

def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core')

    inicio = datetime.datetime.now()
    threads = []
    for n in range(1, qtd_cores + 1):
        ini  = 50_000_000 * (n - 1) / qtd_cores
        fim = 50_000_000 * n / qtd_cores
        print(f'Core {n} processando de {ini} até {fim}')

        threads.append(
            threading.Thread(
            target=computa,
            kwargs={
                'inicio': ini, 
                'termino':fim}
            )
        )
    
    [th.start() for th in threads]
    [th.join() for th in threads]


    tempo = datetime.datetime.now() - inicio
    print(tempo.total_seconds())

def computa(termino, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < termino: 
        math.sqrt((pos - fator) * (pos - fator))
        pos += 1


main()


'''
Tempo levado X.X
'''
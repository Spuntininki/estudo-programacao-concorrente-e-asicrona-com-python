import datetime, math
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor


def main():
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core')

    inicio = datetime.datetime.now()
    with ProcessPoolExecutor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini  = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n} processando de {ini} até {fim}')
            executor.submit(computa, args=(ini, fim))


    tempo = datetime.datetime.now() - inicio
    print(tempo.total_seconds())

def computa(fim, inicio=1):
    pos = inicio
    fator = 1000 * 1000
    while pos < fim: 
        math.sqrt((pos - fator) * (pos - fator))
        pos += 1



if __name__ == '__main__':
    main()


'''
Tempo levado 0.316296
'''
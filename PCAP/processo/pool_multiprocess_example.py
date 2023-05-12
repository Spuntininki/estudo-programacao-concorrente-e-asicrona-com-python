import multiprocessing

def processamento(dado):
    return dado ** 2

def initialized_function():
    print(f'Nome do processo atual: {multiprocessing.current_process().name}')

def main():
    tasks = multiprocessing.cpu_count() * 2
    
    pool = multiprocessing.Pool(processes=tasks, initializer=initialized_function)


    entradas = range(17)
    saidas = pool.map(processamento, entradas)

    print(f'Saidas: {saidas}')

    pool.close()
    pool.join()
    

if __name__ == '__main__':
    main()
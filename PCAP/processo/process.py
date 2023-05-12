import multiprocessing

print(f'Iniciando processo: {multiprocessing.current_process().name}')

def do_something(text):
    print(f'Faz algo com {text}')

def main():
    pc = multiprocessing.Process(target=do_something, args=('Testando', ), name='Processo teste')

    #print(f'Iniciando processo {pc.name}')
    pc.start()
    pc.join()

if __name__ == '__main__':
    main()

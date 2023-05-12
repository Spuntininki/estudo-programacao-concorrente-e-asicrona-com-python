import multiprocessing
import ctypes



def funcao_1(val, status):
    if status.value:
        val.value += 10
        status.value = False
    else:
        val.value += 20
        status.value = True
    print(f'Valor: {val.value}')

def funcao_2(val, status):
    if status.value:
        val.value += 20
        status.value = False
    else:
        val.value += 30
        status.value = True
    print(f'Valor: {val.value}')

def main():
    valor = multiprocessing.Value('i', 100)
    status = multiprocessing.Value(ctypes.c_bool, True)

    funcao_1(valor, status)
    funcao_2(valor, status)

if __name__ == '__main__':
    main()
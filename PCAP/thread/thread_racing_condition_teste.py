from threading import Thread
import random
import time

class Conta:
    def __init__(self, saldo) -> None:
        self.saldo = saldo


def main():
    lista_de_contas = cria_varias_contas()
    total = sum(conta.saldo for conta in lista_de_contas)
    print('Iniciando processo de transferência...')

    tarefas = [
        Thread(target=servicos, args=(lista_de_contas, total)),
        Thread(target=servicos, args=(lista_de_contas, total)),
        Thread(target=servicos, args=(lista_de_contas, total)),
        Thread(target=servicos, args=(lista_de_contas, total)),
    ]
    
    [thread.start() for thread in  tarefas]
    [thread.join() for thread in tarefas]

    print('processo finalizado!')
    valida_banco(lista_de_contas, total)

def servicos(contas, total):
    for _ in range(1, 1000):
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(50, 100)
        transfere(c1, c2, valor)
        valida_banco(contas, total)

def pega_duas_contas(lista_de_contas) -> list:
    c1 = random.choice(lista_de_contas)
    c2 = random.choice(lista_de_contas)

    while c2 == c1:
        c2 = random.choice(lista_de_contas)
    return [c1, c2]

def cria_varias_contas() -> list:
    return [
        Conta(random.randint(5000, 10_000)),
        Conta(random.randint(5000, 10_000)),
        Conta(random.randint(5000, 10_000)),
        
    ]

def transfere(conta_origem:Conta , conta_destino:Conta, valor:int):
    if conta_origem.saldo < valor:
        return
    
    conta_origem.saldo -= valor
    time.sleep(0.001)
    conta_destino.saldo += valor

def valida_banco(contas, total):
    total_atual = sum(conta.saldo for conta in contas)

    if total_atual == total:
        print(f'SUCESSO: balanço bancário consistente. total atual: {total_atual} total anterior: {total}', flush=True)
    else:
        print(f'INSUCESSO: balanço bancário inconsistente. total atual: {total_atual} total anterior: {total}', flush=True)


if __name__ == '__main__':
    main()
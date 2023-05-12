import datetime, math
def main():
    inicio = datetime.datetime.now()

    computa(termino=50_000_000)
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
Tempo levado 11.247037
'''
'''
Discente: Daniel
Docente: Heyde
'''

import threading
import time 
import random 

'''
====================================================================================================

Essas bibliotecas não exigem instalações adicionais:

threading: Cria e gerencia várias tarefas ao mesmo tempo.
time: Controla pausas no programa, como o tempo de "pensar" e "comer".
random: Gera tempos aleatórios para ações, tornando o comportamento dos filósofos variável.

====================================================================================================

No código abaixo foi utilizado Programação Orientada à Objetos. Onde temos:

Classes: Hashi (hashis como objetos) e Filosofo (filósofos como threads).
Objetos: Instâncias de Hashi e Filosofo organizam o código.
Encapsulamento: Ações específicas estão isoladas nas classes, evitando repetição.
Herança: Filosofo herda de threading.Thread para funcionar como thread.
Métodos: Comportamentos encapsulados garantem responsabilidade única.

====================================================================================================
'''

# Classe que representa um Hashi
class Hashi:
    def __init__(self):
        self.semaforo = threading.Semaphore(1)

    def pegar(self):
        self.semaforo.acquire()

    def soltar(self):
        self.semaforo.release()

# Classe que representa um Filósofo
class Filosofo(threading.Thread):
    def __init__(self, id_filosofo, hashi_esquerda, hashi_direita):
        threading.Thread.__init__(self)
        self.id_filosofo = id_filosofo
        self.hashi_esquerda = hashi_esquerda
        self.hashi_direita = hashi_direita

    def pensar(self):
        print(f"Filósofo {self.id_filosofo} está pensando.")
        time.sleep(random.uniform(1, 3))

    def comer(self):
        print(f"Filósofo {self.id_filosofo} está com fome.")
        
        # Pegar os hashis (esquerda e direita)
        self.hashi_esquerda.pegar()
        self.hashi_direita.pegar()

        print(f"Filósofo {self.id_filosofo} está comendo.")
        time.sleep(random.uniform(1, 3))

        # Soltar os hashis
        self.hashi_esquerda.soltar()
        self.hashi_direita.soltar()
        
        print(f"Filósofo {self.id_filosofo} terminou de comer.")

    def run(self):
        while True:
            self.pensar()
            self.comer()

# Função principal
def jantar_filosofos():
    num_filosofos = 5
    hashis = [Hashi() for _ in range(num_filosofos)]
    filosofos = []

    # Criar e iniciar cada filósofo
    for i in range(num_filosofos):
        hashi_esquerda = hashis[i]
        hashi_direita = hashis[(i + 1) % num_filosofos]
        filosofo = Filosofo(i, hashi_esquerda, hashi_direita)
        filosofos.append(filosofo)
        filosofo.start()

    # Garantir que as threads rodem indefinidamente
    for filosofo in filosofos:
        filosofo.join()

if __name__ == "__main__":
    jantar_filosofos()

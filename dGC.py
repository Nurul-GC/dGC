from schedule import *
import sqlite3
from time import sleep


class DespertadorGC:
    """DespertadorGC"""
    def __init__(self):
        self.nome = input("Digite o seu Nome:\n> ")
        # self.tempo = input("Digite a hora por definir:\n (hh:mm) > ")

        self.despertador()

    def despertador(self):
        every(5).seconds.do(self.funcao)

        while True:
            try:
                run_pending()
                # sleep(0.5)
            except Exception:
                exit('Algum erro ocorreu.. Terminando o programa!')

    def funcao(self):
        print(f"Ola Mundo.. Eu sou o {self.nome}!")


if __name__ == '__main__':
    DespertadorGC()

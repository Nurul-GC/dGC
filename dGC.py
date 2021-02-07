# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul-GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e Medicina.                                        *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from reprodutorWAV import reprodutor
from schedule import *
from time import sleep


class DespertadorGC:
    """DespertadorGC"""
    def __init__(self):
        print("""
    **********************
    *        dGC         *
    **********************
""")
        self.nome = input("[i] - Digite o seu Nome:\n> ")
        self.titulo = input("[i] - Digite um título para o Alarme:\n> ")
        while True:
            r = input(f"\n[i] - Deseja marcar um despertador (dia)rio ou (sem)anal {self.nome}?\n> ")
            if r == 'dia' or 'd':
                self.diario()
            elif r == 'sem' or 's':
                self.semanal()
            else:
                print(f"[x] - Lamento {self.nome}.. Você precisa digitar [dia ou sem] para iniciar o seu despertador!")

    def diario(self):
        print("""
-----------------------------------------
[i] USE OS NÚMEROS PARA DEFINIR O DIA [i]
-----------------------------------------
[1] = DOMINGO       [2] = SEGUNDA-FEIRA
[3] = TERÇA-FEIRA   [4] = QUARTA-FEIRA
[5] = QUINTA-FEIRA  [6] = SEXTA-FEIRA
[7] = SABADO
""")
        dia = input("[i] - Escolha o dia por definir:\n> ")
        tempo = input("[i] - Digite a hora por definir:\nEx: (hh:mm) > ")

        print(f"""
-----------------------------------------------
[!!] - O alarme {self.titulo} foi bem definido!
        Aguardando o periodo para a execução...
-----------------------------------------------
""")

        # definindo as tarefas de acordo ao dia definido
        if dia == '1':
            every().sunday.at(tempo).do(self.funcao)
        elif dia == '2':
            every().monday.at(tempo).do(self.funcao)
        elif dia == '3':
            every().tuesday.at(tempo).do(self.funcao)
        elif dia == '4':
            every().wednesday.at(tempo).do(self.funcao)
        elif dia == '5':
            every().thursday.at(tempo).do(self.funcao)
        elif dia == '6':
            every().friday.at(tempo).do(self.funcao)
        elif dia == '7':
            every().saturday.at(tempo).do(self.funcao)
        else:
            pass

        # criando o loop para autenticação das tarefas pendentes
        while True:
            run_pending()

    def semanal(self):
        tempo = input("[i] - Digite a hora por definir:\nEx: (hh:mm) > ")
        print(f"""
-----------------------------------------------
[!!] - O alarme {self.titulo} foi bem definido!
        Aguardando o periodo para a execução...
-----------------------------------------------
""")
        every().weeks.at(tempo).do(self.funcao)

        while True:
            run_pending()

    def funcao(self):
        """função responsavel pelos detalhes da execução"""
        print(f"[!!] - Executando Alarme {self.titulo} definido por {self.nome}...")
        reprodutor()


if __name__ == '__main__':
    DespertadorGC()

# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul-GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e Medicina.                                        *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from datetime import datetime
from PyQt5.Qt import *
from rWav.reprodutorWAV import reprodutor
from desktop_notifier import DesktopNotifier, NotificationLevel
from sys import argv


class DespertadorGC:
    def __init__(self):
        self.gc = QApplication(argv)
        self.ferramentas = QWidget()
        self.ferramentas.setPalette(QPalette(QColor(250, 117, 94)))
        self.ferramentas.setWindowIcon(QIcon("../img/favicon_io/favicon-32x32.png"))

        self.hora = None
        self.labelHoraDiario = None
        self.labelHoraSemanal = None
        self.titulo = None
        self.descricao = None

        self.leftlist = QListWidget(self.ferramentas)
        self.leftlist.setFixedSize(100, 40)
        self.leftlist.insertItem(0, 'Diario')
        self.leftlist.insertItem(1, 'Semanal')

        self.janela1 = QWidget()
        self.diario()
        self.janela2 = QWidget()
        self.semanal()

        self.stack = QStackedWidget(self.ferramentas)
        self.stack.addWidget(self.janela1)
        self.stack.addWidget(self.janela2)

        self.timer = QTimer(self.ferramentas)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.mostraHora)
        self.timer.start()

        hbox = QHBoxLayout(self.ferramentas)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.stack)

        self.ferramentas.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)

    def display(self, i):
        self.stack.setCurrentIndex(i)

    def diario(self):
        barraFerramentas = QToolBar(self.ferramentas)
        instrucoes = barraFerramentas.addAction('Intruções')
        instrucoes.triggered.connect(self.instrucoes)
        barraFerramentas.addSeparator()
        sobre = barraFerramentas.addAction('Sobre')
        sobre.triggered.connect(self.sobre)
        barraFerramentas.addSeparator()
        suspender = barraFerramentas.addAction('Suspender')
        suspender.triggered.connect(self.suspender)

        layout = QVBoxLayout()
        layoutDespertador = QFormLayout()

        # -----------calendario------------
        labelCalendario = QCalendarWidget()
        labelCalendario.showToday()
        layout.addWidget(labelCalendario)

        # ------------hora-----------------
        self.labelHoraDiario = QLabel(self.definirHora())
        self.labelHoraDiario.setAlignment(Qt.AlignRight)
        layout.addWidget(self.labelHoraDiario)

        # ---------definição alarme--------
        labelPeriodo = QLabel('<h2>Definindo o Alarme Diario</h2>')
        labelPeriodo.setAlignment(Qt.AlignCenter)
        layoutDespertador.addWidget(labelPeriodo)

        self.titulo = QLineEdit()
        layoutDespertador.addRow('<b>Defina um titulo: *</b>', self.titulo)

        definirPeriodo = QTimeEdit()
        layoutDespertador.addRow('<b>Defina o horario: *</b>', definirPeriodo)

        self.descricao = QTextEdit()
        layoutDespertador.addRow('<b>Defina uma descrição:</b>', self.descricao)

        botaoAtivar = QPushButton('Ativar')
        botaoAtivar.setDefault(True)
        layoutDespertador.addWidget(botaoAtivar)
        layout.addLayout(layoutDespertador)

        # ----------------------------------
        self.janela1.setLayout(layout)

    def semanal(self):
        barraFerramentas = QToolBar(self.ferramentas)
        instrucoes = barraFerramentas.addAction('Intruções')
        instrucoes.triggered.connect(self.instrucoes)
        barraFerramentas.addSeparator()
        sobre = barraFerramentas.addAction('Sobre')
        sobre.triggered.connect(self.sobre)
        barraFerramentas.addSeparator()
        suspender = barraFerramentas.addAction('Suspender')
        suspender.triggered.connect(self.suspender)

        layout = QVBoxLayout()
        layoutDespertador = QFormLayout()

        # -----------calendario------------
        labelCalendario = QCalendarWidget()
        labelCalendario.showToday()
        layout.addWidget(labelCalendario)

        # ------------hora-----------------
        self.labelHoraSemanal = QLabel(self.definirHora())
        self.labelHoraSemanal.setAlignment(Qt.AlignRight)
        layout.addWidget(self.labelHoraSemanal)

        # ---------definição alarme--------
        labelPeriodo = QLabel('<h2>Definindo o Alarme Semanal</h2>')
        labelPeriodo.setAlignment(Qt.AlignCenter)
        layoutDespertador.addWidget(labelPeriodo)

        self.titulo = QLineEdit()
        layoutDespertador.addRow('<b>Defina um titulo: *</b>', self.titulo)

        definirPeriodo = QTimeEdit()
        layoutDespertador.addRow('<b>Defina o horario: *</b>', definirPeriodo)

        self.descricao = QTextEdit()
        layoutDespertador.addRow('<b>Defina uma descrição:</b>', self.descricao)

        botaoAtivar = QPushButton('Ativar')
        botaoAtivar.setDefault(True)
        layoutDespertador.addWidget(botaoAtivar)
        layout.addLayout(layoutDespertador)

        # ----------------------------------
        self.janela2.setLayout(layout)

    def definirHora(self):
        self.hora = QDateTime()
        return self.hora.currentDateTime().toString("hh:mm:ss (ap)")

    def mostraHora(self):
        self.labelHoraSemanal.setText(self.definirHora())
        self.labelHoraDiario.setText(self.definirHora())

    def sobre(self):
        QMessageBox.information(self.ferramentas, 'Sobre o Programa', """...""")

    def instrucoes(self):
        QMessageBox.information(self.ferramentas, 'Instruções', """...""")

    def suspender(self):
        pergunta = QMessageBox.question(self.ferramentas, 'Suspender Programa',
                                        'O programa será suspenso!\nEle continuará aberto, mas funcionando em segundo plano para cumprir com as definições do alarme!')
        if pergunta == 1638:
            self.gc.instance().deleteLater()
        elif pergunta == 65536:
            pass
        else:
            pass

    def notificacao(self):
        notificacao = DesktopNotifier(app_name='dGC', app_icon='../img/favicon_io/favicon-32x32.png', notification_limit=10)
        notificacao.send(title='Alarme', message='',
                         urgency=NotificationLevel.Normal,
                         icon='../img/favicon_io/favicon-16x16.png',
                         buttons={'Ignorar': self.ignorar()}, sound='../sound/Idrada.wav')

    def ignorar(self):
        pass


if __name__ == '__main__':
    app = DespertadorGC()
    app.ferramentas.show()
    app.gc.exec_()

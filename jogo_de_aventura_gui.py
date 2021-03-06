import PySimpleGUI as sg

#Projeto 7 - Jogo de Aventura
#um jogo de decisoes onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas
#chegar a finais diferentes, de acordo com as respostas que eu passe para o programa
#qual o cenario: estamos em uma guerra entre duas naçoes, onde somente uma saira vencedora, entao temos que tomar a decisao correta pra chegar ate a vitoria 
class JogoDeAventura:
    def __init__(self):
        self.cena1 = "Voce nasceu no norte ou no sul? (n/s)\n" # norte = LadoA, SUL = LadoB
        self.cena2 = "Voce prefere a espada ou escudo? (espada/escudo)\n" #espada = LadoA, escudo = LadoB
        self.cena3 = "Qual sua especialidade?(frente/tatico)\n" #linha de frente = LadoA, tatico = LadoB
        
        self.final1 ="Você será um HEROI na linha de frente!"
        self.final2 ="Você será um HEROI protegendo nossas tropas!"
        self.final3 ="Voce FALHARA nesta batalha\nVocê e fraco lhe falta ODIO!"
        self.final4 ="Você FALHARA nos defendedo!"
        self.final5 ="Voçê e um LIDER nato na linha de frente!"
        self.final6 ="Você E UM ESTRATEGISTA nato!"
        self.final7 ="Voçê FALHARA na LIDERANÇA da linha de frente!"
        self.final8 ="Você FALHARAE na sua Estrategia!"

    def Iniciar(self):
        #Layout
        layout = [
           [sg.Output(size=(60,0))],
           [sg.Input(size=(50,0), key='escolha')],
           [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        #criar janela
        self.janela = sg.Window('jogo de aventura!', layout=layout)
        while True:
            self.LerValores()
            #fazer algo com os dados
            if self.evento == 'Iniciar':
            #ler os dados
                print(self.cena1)
                self.LerValores()
                if self.valores['escolha'] == 'n':
                    print(self.cena2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.final1)
                    if self.valores['escolha'] == 'escudo':
                        print(self.final2)
                    print(self.cena3)
                    self.LerValores()
                    if self.valores['escolha'] == 'frente':
                        print(self.final5)
                    if self.valores['escolha'] == 'tatico':
                        print(self.final6)
                if self.valores['escolha'] == 's':
                    print(self.cena2)
                    self.LerValores()
                    if self.valores['escolha'] == 'espada':
                        print(self.final3)
                    if self.valores['escolha'] == 'escudo':
                        print(self.final2)
                    print(self.cena3)
                    self.LerValores()
                    if self.valores['escolha'] == 'frente':
                        print(self.final7)
                    if self.valores['escolha'] == 'tatico':
                        print(self.final8)

    def LerValores(self):
        self.evento, self.valores = self.janela.Read()
            

jogo = JogoDeAventura()
jogo.Iniciar()

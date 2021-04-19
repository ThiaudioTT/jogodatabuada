import tkinter

class tutorial(object):
    def __init__(self,janela):
        
        self.janela = janela
        self.janela.title('Como jogar?')
        self.janela.geometry('500x300')

        self.T_comojogar = tkinter.Label(self.janela,text ='''Como jogar:\nVocê irá decorar a tabuada
            assim que estiver pronto clique no botão continuar
            você irá tentar acertar os números e se quiser pode avançar pra proxima fase.
            ''')
        self.T_comojogar.pack()
        
        self.B_entendido = tkinter.Button(self.janela,text = 'Entendi!', command = lambda:self.janela.destroy())
        self.B_entendido.pack(side = 'bottom')
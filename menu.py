import tkinter
import tabuada
import comojogar
#coloque apenas um modo de aprendizado! soma, subtraçao divisão e etc.

class menu(object):
    def __init__(self,janela):
        #definições da janela#
        self.janela = janela
        self.janela.title('Tabuada Game: Menu')
        self.janela.geometry('500x450')

        #Frames
        self.frame1 = tkinter.Frame(self.janela)
        self.frame1.pack(side = 'top')
        
        self.framebotoes = tkinter.Frame(self.janela)
        self.framebotoes.pack()
        self.framebotoes.place(x = 65, y = 250)


        self.T_Bemvindo = tkinter.Label(self.frame1, text = 'Bem vindo a tabuada')
        self.T_Bemvindo.pack(side = 'top')

        self.T_tabuada = tkinter.Label(self.frame1, text = 'Modo de aprendizado:')
        self.T_tabuada.pack(side = 'bottom')


        #Aritméticas#
        self.B_normal = tkinter.Button(self.framebotoes, text = 'Soma', command = self.soma, width = 15)
        self.B_normal.pack()


        self.B_comojogar = tkinter.Button(janela, text = 'Como jogar?', command = self.func_comojogar)
        self.B_comojogar.pack(side = 'bottom')
        
    def soma(self):
        tabuada.soma()


    def func_comojogar(self):
        janelacomojogar = tkinter.Tk()
        comojogar.tutorial(janelacomojogar)
        janelacomojogar.mainloop()

janela = tkinter.Tk()
menu(janela)

janela.mainloop()
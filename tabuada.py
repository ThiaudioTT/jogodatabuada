#for tabuada in range(1,11):
#    print("{} x {} = {}".format(2,tabuada,2 * tabuada))
import tkinter

def soma():
        janela = tkinter.Tk()
        janela.title('Modo de aprendizado: soma')
        janela.geometry('400x500')
        T_escolhatabuada = tkinter.Label(janela, text = 'Escolha o número: ')
        T_escolhatabuada.pack()

        #frame#
        framebotoes = tkinter.Frame(janela)
        framebotoes.pack()

        def soma2():
                janela.destroy()
                janela_soma2 = tkinter.Tk()
                janela_soma2.title("Soma: 2")
                janela_soma2.geometry("500x600")
                
                T_decore = tkinter.Label(janela_soma2, text = 'Decore: ')
                T_decore.pack()
                
                for s in range(1,10):
                        s = tkinter.Label(janela_soma2,text = "2 + {} = {}\n".format(s,2+s))
                        s.pack()

                #frame#
                F_voltariniciar = tkinter.Frame(janela_soma2)
                F_voltariniciar.pack(side = 'bottom')

                B_iniciar = tkinter.Button(F_voltariniciar, text = "Iniciar Game/aprendizado", width = 20, command = None)
                B_iniciar.pack(side = "left")

                B_voltar = tkinter.Button(F_voltariniciar, text = "Voltar ao menu.", command = lambda:janela_soma2.destroy(), width = 20)
                B_voltar.pack(side = 'right')

                janela_soma2.mainloop()

        #Numeros para escolher a tabuada#
        B2 = tkinter.Button(framebotoes, text = "2", width = 20, command = soma2)
        B2.pack()
        
        B3 = tkinter.Button(framebotoes,text = "3", width = 20)
        B3.pack()

        B4 = tkinter.Button(framebotoes, text = "4", width = 20)
        B4.pack()

        B5 = tkinter.Button(framebotoes, text = "5", width = 20)
        B5.pack()
        
        B6 = tkinter.Button(framebotoes,text = "6", width = 20)
        B6.pack()

        B7 = tkinter.Button(framebotoes, text = "7", width = 20)
        B7.pack()
        
        B8 = tkinter.Button(framebotoes,text = "8", width = 20)
        B8.pack()

        B9 = tkinter.Button(framebotoes, text = "9", width = 20)
        B9.pack()
        
        B10 = tkinter.Button(framebotoes, text = "10", width = 20)
        B10.pack()

        janela.mainloop()
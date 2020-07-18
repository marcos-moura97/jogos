## Jogo da velha
from tkinter import *
import tkinter.messagebox

jogo = Tk()
jogo.title('Jogo da Velha')
jogo.geometry("400x380") #dimensões

jogador_a = StringVar()
jogador_b = StringVar()
p1 = StringVar()
p2 = StringVar()

## Para pôr o nome dos jogadores
nome_jogador1 = Entry(jogo,textvariable=p1,bd=5)
nome_jogador1.grid(row=1,column=1,columnspan=8)

nome_jogador2 = Entry(jogo,textvariable=p2,bd=5)
nome_jogador2.grid(row=2,column=1,columnspan=8)


bclick = True
flag = 0
flag1=0



## Função que desabilita os botões do programa
## Usada quando alguém ganha
def desabilita_botao():

    botao1.configure(state=DISABLED)
    botao2.configure(state=DISABLED)
    botao3.configure(state=DISABLED)
    botao4.configure(state=DISABLED)
    botao5.configure(state=DISABLED)
    botao6.configure(state=DISABLED)
    botao7.configure(state=DISABLED)
    botao8.configure(state=DISABLED)
    botao9.configure(state=DISABLED)



## Função que marca os botões alternadamente quando clicado
def botao_click(botoes):
    global bclick, flag, nome_jogador1, nome_jogador2, jogador_a, jogador_b, mov_usu,flag1

    if botoes["text"] == " " and bclick == True:
        botoes["text"] = "X"
        bclick = False
        jogador_b = p2.get() + " GANHOOOU!"
        jogador_a = p1.get() + " GANHOOOU!"

        checa_vitoria()

        flag += 1
        flag1 +=1




    elif botoes["text"] == " " and bclick == False:
        botoes["text"] = "O"
        bclick = True

        checa_vitoria()
        flag += 1



## Se todas as posições forem ocupadas, o programa checa se alguém ganhou ou se houve empate
def checa_vitoria():

    if(botao1['text'] == 'X' and botao2['text'] == 'X' and botao3['text'] == 'X' or
       botao4['text'] == 'X' and botao5['text'] == 'X' and botao6['text'] == 'X' or
       botao7['text'] == 'X' and botao8['text'] == 'X' and botao9['text'] == 'X' or
       botao1['text'] == 'X' and botao5['text'] == 'X' and botao9['text'] == 'X' or
       botao3['text'] == 'X' and botao5['text'] == 'X' and botao7['text'] == 'X' or
       botao1['text'] == 'X' and botao4['text'] == 'X' and botao7['text'] == 'X' or
       botao2['text'] == 'X' and botao5['text'] == 'X' and botao8['text'] == 'X' or
       botao7['text'] == 'X' and botao6['text'] == 'X' and botao9['text'] == 'X'):

        desabilita_botao()
        tkinter.messagebox.showinfo("Jogo da Velha",jogador_a)

    elif flag==8:
        tkinter.messagebox.showinfo("Jogo da Velha",'Temos um empate!')

    elif(botao1['text'] == 'O' and botao2['text'] == 'O' and botao3['text'] == 'O' or
         botao4['text'] == 'O' and botao5['text'] == 'O' and botao6['text'] == 'O' or
         botao7['text'] == 'O' and botao8['text'] == 'O' and botao9['text'] == 'O' or
         botao1['text'] == 'O' and botao5['text'] == 'O' and botao9['text'] == 'O' or
         botao3['text'] == 'O' and botao5['text'] == 'O' and botao7['text'] == 'O' or
         botao1['text'] == 'O' and botao4['text'] == 'O' and botao7['text'] == 'O' or
         botao2['text'] == 'O' and botao5['text'] == 'O' and botao8['text'] == 'O' or
         botao7['text'] == 'O' and botao6['text'] == 'O' and botao9['text'] == 'O'):

        desabilita_botao()
        tkinter.messagebox.showinfo("Jogo da Velha",jogador_b)



## Diz onde estão os jogadores

label = Label(jogo,text='Jogador 1:',font='Times 20 bold',bg='white',fg='black',height=1,width=8)
label.grid(row=1,column=0)

label = Label(jogo,text='Jogador 2:',font='Times 20 bold',bg='white',fg='black',height=1,width=8)
label.grid(row=2,column=0)


## A matriz de botões

botao1 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao1))
botao1.grid(row=3,column=0)

botao2 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao2))
botao2.grid(row=3,column=1)

botao3 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao3))
botao3.grid(row=3,column=2)

botao4 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao4))
botao4.grid(row=4,column=0)

botao5 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao5))
botao5.grid(row=4,column=1)

botao6 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao6))
botao6.grid(row=4,column=2)

botao7 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao7))
botao7.grid(row=5,column=0)

botao8 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao8))
botao8.grid(row=5,column=1)

botao9 = Button(jogo,text=' ',font='Times 20 bold',bg='gray',fg='white',height=4,width=8,command=lambda: botao_click(botao9))
botao9.grid(row=5,column=2)



jogo.mainloop()

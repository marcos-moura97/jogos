## Imports
# Import a funcao choice para escolher a nossa palavra
from random import choice
# Imports do tkinter
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk



##################################################
## Algumas funções

def sair():
    # Quando apertar no botão sair o programa encerrará
    exit()

def sobre():
    # Quando apertar no botão 'sobre'no Menu esta mensagem aparecerá
    tkinter.messagebox.showinfo('Bem vindo ao jogo da Forca!',
                                'Aperte em "Iniciar Jogo" para renderizar uma nova palavra. Após isso escreva um caractere e aperte "checar". Você têm 6 chances, use-as com sabedoria! ')


def creditos():
    # Meus créditos né hahaha
    tkinter.messagebox.showinfo('Creditos!',
                                'Jogo feito usando a biblioteca Tkinter do Python! Feito por Marcos Moura! Divirta-se :)')

def reseta():
    # Quando o jogo acaba, as variáveis são resetadas
    global chances, chutes
    chances = 6             # Número de chances que a pessoa tem

    chutes = ''             # Esta variável guarda todos os chutes até agora

def atualiza_img(janela,link):
    # Põe a imagem na forca
    image = Image.open(link)
    image = image.resize((200, 200), Image.ANTIALIAS)
    foto = ImageTk.PhotoImage(image)

    lab_img = Label(janela,image=foto)
    lab_img.image = foto
    lab_img.place(x=200,y=150)

def escolhe_palavra():
    # Escolha da palavra

    # Começo abrindo e lendo o arquivo de palavras
    arquivo = open('palavras.txt', 'r')
    palavras = []

    # Cada linha representa um animal. Faço esta varredura para pegar todos os animais
    for linha in arquivo:
        palavras += [linha.split('\n')[0]]

    arquivo.close()

    # Agora retorno uma palavra aleatória da lista
    return choice(palavras)

def novo_jogo():
    # Começo escolhendo uma palavra para jogar
    global palavra
    #palavra = choice(palavras)
    palavra = escolhe_palavra()

    # Agora coloco um Label com os caracteres escondidos
    underlines = ''
    for i in range(0,len(palavra)):
        underlines = underlines + '_ '
    label_ = Label(window,text=underlines,width=50,font=("arial",19,"bold")) # texto livre
    label_.place(x=0,y=400)



def checa():
    global palavra, chances, chutes, imagens
    # Função usada quando você quer checar um caractere
    car = chute.get()

    # começa checando se realmente foi apenas 1 caractere pressionado e se nenhum número.
    # qualquer coisa além disso o programa retorna um errinho.
    if car == '':
        tkinter.messagebox.showerror('Nada digitado!', 'Coé padrinho, digita um caractere aí!')
        return

    elif len(car)!=1 and car.isdigit()==0:
        tkinter.messagebox.showerror('Mais de um caractere encontrado!', 'Coé padrinho, é apenas um caractere!')
        return

    elif car.isdigit():
        tkinter.messagebox.showerror('Sem números!', 'Coé padrinho, nessa palavra não tem número!')
        return

    # Agora que sabemos que apenas um caracter reina, acontece a checagem junto a palavra.
    # Antes de tudom faço a checagem se a letra já tinha sido digitada anteriormente
    # Se já, retorna uma mensagem e sai da função
    if car in chutes:
        tkinter.messagebox.showinfo('Repetido!', 'Esta letra já foi, tente uma diferente!')
        return

    chutes += car # Sem repetições, adiciono o meu chute a variável que guarda todos os chutes

    # Se este caractere não está na palavra, o número de chances é decrementado
    # E a imagem é atualizada
    if car not in palavra:
        chances = chances-1

    # Se ficou sem chances, o jogo acaba logo aqui
    if chances == 0:
        mensagem = 'Perdeeeeeeeu, ficou sem chances! A palavra era ' + palavra
        tkinter.messagebox.showinfo('GAME OVER!', mensagem)
        reseta()
        return

    # Agora faço a varredura dos caracteres na palavra e atualizo o Label que me diz as letras
    chutes_atualizados = ''
    vitoria = True
    for c in palavra:
        if c in chutes:

            chutes_atualizados += c

        else:
            chutes_atualizados += ' _ '
            vitoria = False

    # Se ganhou, reseta geral
    if vitoria:
        tkinter.messagebox.showinfo('VITÓRIA!', 'Parabeeeeeeeens, você ganhou!')
        reseta()
        return

    label_ = Label(window,text=chutes_atualizados,width=50,font=("arial",19,"bold")) # texto livre
    label_.place(x=0,y=400)

    ## Agora atualiza-se a imagem da forca
    atualiza_img(window,imagens.get(chances))

    ## Por fim, mostra as letras usadas
    label_chutes = Label(window,text=chutes,font=("arial",15,"bold")) # texto livre
    label_chutes.place(x=200,y=100)

    chute.set('')



##################################################
## Janela
window = Tk() #cria uma janela
window.geometry("500x600") #dimensões
window.title('Jogo da Forca')

## Carrega a imagem da forca no tk
atualiza_img(window,'imagens/forca.png')

##################################################
## Menu
menu = Menu(window)
window.config(menu=menu)

#submenu 'Arquivo'
subm1 = Menu(menu)
menu.add_cascade(label="Arquivos",menu=subm1)
subm1.add_command(label="Sair",command=sair)

#submenu 'Opcoes'
subm2 = Menu(menu)
menu.add_cascade(label="Opcoes",menu=subm2)
subm2.add_command(label="Sobre",command=sobre)
subm2.add_command(label="Creditos",command=creditos)


##################################################
## Variáveis globais
palavra = ''

chances = 6             # Número de chances que a pessoa tem

chute = StringVar()     # Esta é a variável que guarda o chute atual
chutes = ''             # Esta variável guarda todos os chutes até agora

imagens = {             # Este dicionário relaciona o número de chances com a imagem referente a forca
    6: 'imagens/forca.png',
    5: 'imagens/forca2.png',
    4: 'imagens/forca3.png',
    3: 'imagens/forca4.png',
    2: 'imagens/forca5.png',
    1: 'imagens/forca6.png',
    0: 'imagens/forca7.png',
}

##################################################
## Labels e outras coisas
label1 = Label(window,text='Adivinhe a palavra:',relief='solid',width=20,font=("arial",19,"bold")) # texto livre
label1.place(x=130,y=25)

label1 = Label(window,text='Letras já usadas:',width=20,font=("arial",15,"bold")) # texto livre
label1.place(x=50,y=100)


##################################################
## Botões
b_comeca=Button(window,text='Novo Jogo',width=12,fg='brown',bg='red',command=novo_jogo)
b_comeca.place(x=150,y=550)           # GROOVE, RIDGE, SUNKEN e RAISED

b_sair=Button(window,text='Sair',width=12,fg='brown',bg='red',command=sair)
b_sair.place(x=280,y=550)

b_checa=Button(window,text='Checar',width=12,fg='brown',bg='red',command=checa)
b_checa.place(x=250,y=70)
b_checa.config(width=7)


##################################################
## Entradas
caractere = Label(window,text='Entre com um caractere:',width=20,font=("arial",10,"bold")) # texto livre
caractere.place(x=80,y=70)

car_ent = Entry(window,textvar=chute)
car_ent.place(x=205,y=65)
car_ent.config(width=2)
window.mainloop()

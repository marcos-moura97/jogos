# Importando a biblioteca
import pygame
import sys

# Definindo o objeto bola
class Bola():
    # parâmetros iniciais
    def __init__(self):
        # parametros da bola
        self.raio = 25
        self.cor = RED

        # parametros de posicao
        self.x_pos = 200
        self.y_pos = 200

        self.velx=5
        self.vely=5

        self.desenha_bola(tela,self.x_pos,self.y_pos)

    # método que desenha a bola
    def desenha_bola(self,tela,x,y):
        self.x_pos=x
        self.y_pos=y
        pygame.draw.ellipse(tela, self.cor, [x, y, self.raio, self.raio])

    def atualiza_pos(self,x):
        if self.y_pos<=0 or self.y_pos>=500:  #Topo e fundo
            self.vely = -self.vely

        # Evitar que saia pela direita ou pela esquerda
        elif self.x_pos >= 700 or self.x_pos <= 0:
            self.velx = -self.velx

        # Se pisar no retangulo, também muda de direção
        if self.y_pos==430 and (self.x_pos in range(x,x+200)):
            jump_sound.play()
            self.vely = -self.vely

        # Atualiza a posição

        self.x_pos = self.x_pos+self.velx
        self.y_pos = self.y_pos+self.vely

        return [self.x_pos,self.y_pos]


# Definindo o Objeto da nossa base
class Base():
    def __init__(self):
        self.comprimento = 200
        self.largura = 20
        self.y = 450
        self.cor = GREEN
        self.desenha_base(tela,300)

    def desenha_base(self,tela,x):
        rect = pygame.Rect(x,self.y,self.comprimento,self.largura)
        pygame.draw.rect(tela, self.cor, rect)

# classe que cria um tijolo
class Tijolo(pygame.sprite.Sprite):
    def __init__(self, tela, posicao):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Sprites/tijolo.png')
        tela.blit(self.image, posicao)
        self.rect = self.image.get_rect()
        self.rect.topleft = posicao


# classe que cria o muro
class Muro(pygame.sprite.Group):
    def __init__(self, tela,n_tijolos):
        pygame.sprite.Group.__init__(self)

        pos_x = 0
        pos_y = 20

        self.tijolos = {}

        for i in range(n_tijolos):
            tijolo = Tijolo(tela,(pos_x, pos_y))
            self.add(tijolo)
            self.tijolos[i] = (pos_x,pos_y)
            self.comprimento = tijolo.rect.width
            self.largura = tijolo.rect.height
            pos_x += tijolo.rect.width
            if pos_x >= 700:
                pos_x = 0
                pos_y += tijolo.rect.height


    def atualiza_muro(self,bola,muro,pontos):
        lista_apaga = []
        for i in (self.tijolos):

            cx = bola.x_pos
            cy = bola.y_pos

            pos_tijolo = self.tijolos[i]
            pos_x =  pos_tijolo[0]
            pos_y =  pos_tijolo[1]

            if (cx in range(pos_x,pos_x+self.comprimento)):
                if(cy in range(pos_y,pos_y+self.largura)):
                    bola.vely=-bola.vely
                    lista_apaga.append(i)

        for i in lista_apaga:
            muro.remove(self.tijolos[i])
            del self.tijolos[i]
            punch_sound.play()
            pontos += 10

        for j in self.tijolos:
            tijolo = Tijolo(tela,self.tijolos[j])
            self.add(tijolo)

        return pontos


class Displays():
    def __init__(self):
        self.vidas = 3          #numero de vidas
        self.pontos = 0
        self.gameover = False

    def mostra_pontos(self, tela):
        fonte = pygame.font.SysFont('Consolas', 20)
        texto = fonte.render(str(self.pontos).zfill(5), True, BLACK)
        texto_rect = texto.get_rect()
        texto_rect.topleft = [0, 0]
        tela.blit(texto, texto_rect)

    def mostra_vidas(self, tela):
        fonte = pygame.font.SysFont('Consolas', 20)
        cadena = "Vidas: " + str(self.vidas).zfill(2)
        texto = fonte.render(cadena, True, BLACK)
        texto_rect = texto.get_rect()
        texto_rect.topright = [700, 0]
        tela.blit(texto, texto_rect)

    def game_over(self,x,y):
        global done
        #se não há mais vidas
        if self.vidas==0 and y==500:
            self.gameover = True
            fonte = pygame.font.SysFont('Arial', 72)
            texto = fonte.render('GAME OVER :(', True, RED)
            texto_rect = texto.get_rect()
            texto_rect.center = [350, 250]
            tela.blit(texto, texto_rect)
            return [x,y]

        #Se tocou o solo desconta uma vida e retorna do centro
        elif y==500:
            self.vidas -= 1
            return [350,200]

        # senão volta de onte esteve
        else:
            return [x,y]

# Definindo algumas cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
tamanho = (700, 500)
tela = pygame.display.set_mode(tamanho)

pygame.display.set_caption("Meu Jogo")

# Usado para configurar o quão rápido a tela atualiza
clock = pygame.time.Clock()


# Criando os objetos
bola = Bola()
base = Base()

n_tijolos = 50
muro = Muro(tela,n_tijolos)

display = Displays()

## Carregando sons
jump_sound = pygame.mixer.Sound('Sons/jump.wav')
punch_sound = pygame.mixer.Sound('Sons/punch.wav')

## Variáveis
done = False


# -------- Loop principal -----------
while not done:
    # --- loop do evento principal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    if display.gameover == False:
        # --- Código de desenho deve vir aqui
        tela.fill(WHITE)


        ## Base do Pong

        # Pega posicao
        pos = pygame.mouse.get_pos()

        # Atualiza posicao da bola
        x,y = bola.atualiza_pos(pos[0])

        # Checa se morreu
        x,y = display.game_over(x,y)
        # Desenha bola
        bola.desenha_bola(tela,x,y)

        # Desenha base
        base.desenha_base(tela,pos[0])

        # Atualiza o Muro
        display.pontos = muro.atualiza_muro(bola,muro,display.pontos)


        # Desenha pontos e vidas
        display.mostra_pontos(tela)
        display.mostra_vidas(tela)

        # Desenha um tijolo
        #tijolo = Tijolo(tela,(100, 100))




        # --- Atualiza a tela e o que precisar ser desenhado será
        pygame.display.flip()

        # --- Limite de 60 frames por segundo
        clock.tick(60)

# Fecha a janela e sai do programa
pygame.quit()

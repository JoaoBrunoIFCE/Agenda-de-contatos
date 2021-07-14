import pygame
import PySimpleGUI as sg
import sys
# Implementação do botão
from botao import Button
# Trabalhar com temporizadores
import time
# Para leitura do teclado
import keyboard

# Classe para criar e manipular a inteface com o usuário
class interfaceGrafica ():    
    def telas (self):
        pygame.init()

        # Dimensões da Tela
        size = width, height = 800, 600

        tela = pygame.display.set_mode(size)
        pygame.display.set_caption("Agenda de contatos")
        imagem_fundo = pygame.image.load('./Telas/1 Tela de Login.png')

        janela_aberta = True
        font = pygame.font.Font('freesansbold.ttf', 14)

        # Cor do Botão
        cor_btn = r, g, b = 0, 255, 255
        # Button(cor, x, y, width, height, text)
        btn_W = Button(cor_btn, 123, 342, 65, 65, 'W')
        btn_S = Button(cor_btn, 123, 524, 65, 65, 'S')
        btn_A = Button(cor_btn, 33, 433, 65, 65, 'A')
        btn_D = Button(cor_btn, 215, 433, 65, 65, 'D')


        btn_ESC = Button(cor_btn, 628, 428, 65, 65, 'ESC') #ESC-Sair

        while janela_aberta:

            pygame.time.delay(50) #milissegundos            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    janela_aberta = False
                    
                comandos_clique_unico = pygame.key.get_pressed()

                mouse_pos = pygame.mouse.get_pos()

                #Fecha a janela
                if comandos_clique_unico[pygame.K_ESCAPE] or (btn_ESC.isOver(mouse_pos) and event.type == pygame.MOUSEBUTTONUP):
                    janela_aberta = False
                    print("Clicou em ESC")

            #Lê a tecla pressionada pelo usuário e executa a ação enquanto a tecla estiver pressionada
            #Teclado
            comandos = pygame.key.get_pressed()
            
            #Mouse
            mouse_position = pygame.mouse.get_pos()
            btn_esq_mouse_press, btn_meio_mouse_press, btn_dir_mouse_press = pygame.mouse.get_pressed()

                
            #Teste de teclas para mudar view
            if comandos[pygame.K_w]:
                print("clicou w")
                imagem_fundo = pygame.image.load('./Telas/2 Tela de criação de conta.png')
            
            #Teste de teclas para mudar view
            if comandos[pygame.K_s]:
                print("clicou s")
                imagem_fundo = pygame.image.load('./Telas/3 Tela de Menu principal.png')

            #Teste de teclas para mudar view
            if comandos[pygame.K_a]:
                print("clicou a")
                imagem_fundo = pygame.image.load('./Telas/4 Tela de Inserir contato.png')
                
            #Teste de teclas para mudar view
            if comandos[pygame.K_d]:
                print("clicou d")
                imagem_fundo = pygame.image.load('./Telas/5 Tela de Apagar contato.png')


            #Carrega imagem da variável imagem_fundo na tela
            tela.blit(imagem_fundo,(0,0))

            #Desenha os botões na tela por cima da imagem carregada (implementar teste)
	
            pygame.display.update()

            #mouse = pygame.mouse.get_pos()
            #print (str(mouse[0]) + " , " + str(mouse[1]))
            
        pygame.quit()

GUI = interfaceGrafica()
GUI.telas()

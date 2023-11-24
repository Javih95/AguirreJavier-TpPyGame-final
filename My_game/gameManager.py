import pygame
import sys
from player import Player
from enemy import Enemigo
from ground import Terreno
from plataforma import *
from vidas import *
from enemyGenerator import EnemyGenerator
from trap import Trap
from auxiliar import *
from explosion import *
from menu import *
from ranking import *
class Game:
    def __init__(self):
        #Player
        self.player = Player(300, 300)
        self.players = pygame.sprite.Group()
        self.players.add(self.player)
        #Balas
        self.balas = pygame.sprite.Group()
        self.balas_1 = pygame.sprite.Group()
        self.bombas = pygame.sprite.Group()
        #Enemigo
        self.enemyGenerator = EnemyGenerator()
        #Vidas
        self.vidas = pygame.sprite.Group()
        vida = Vida(50,500,15,15)
        self.vidas.add(vida)
        #Frutas
        self.frutas =pygame.sprite.Group()
        fruta = Frutas (150,500,20,20)
        self.frutas.add(fruta)
        # Crear terrenos y plataformas de ejemplo
        self.terrenos = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.plataforma_movil = pygame.sprite.Group()
        terreno = Terreno(0, 550, 600, 50)
        plataforma = Plataforma(200, 380, 200, 20)
        plataforma_1= Plataforma(200, 500, 200, 20)
        plataforma_movil = Plataforma_movil(50,450,200,20,4)
        self.terrenos.add(terreno)
        self.plataformas.add(plataforma)
        self.plataformas.add(plataforma_1)
        self.plataforma_movil.add(plataforma_movil)
        #Trampas
        self.trap = pygame.sprite.Group()
        trampa = Trap(200,540,60,20)
        self.trap.add(trampa)
        self.colision_jugador_enemigo_procesada = False
        self.collision_clock =0
        #cronometro
        self.cronometro = Cronometro(90)
        self.puntos = self.player.puntos
        self.cantidad_vidas = self.player.vidas
        self.font = pygame.font.Font(None, 36)
        self.en_juego= False
        #Pausa
        self.en_pausa= False
        self.menu_pausa = Menu_pausa(300,300)
        self.ranking = Ranking(100,100)
        self.ranking_menu = False
        self.game_over = False
        self.datos= Manejo_de_datos("lista_jugadores.json")
        print(self.datos.lista_jugadores)
    def run(self,teclas,screen):
        if self.en_juego and not self.game_over:
                if self.en_pausa:
                    self.menu_pausa.dibujar(screen)
                    if self.ranking_menu:
                        self.ranking.dibujar(screen)
                if not self.en_pausa:
                    self.ranking_menu = False
                    self.collision_clock += 1
                    self.puntos = self.player.puntos
                    self.cantidad_vidas = self.player.vidas
                    self.player.update(self.balas,self.bombas,teclas,self.terrenos, self.plataformas,self.plataforma_movil)
                    self.balas.update()
                    self.balas_1.update()
                    self.bombas.update()
                    self.plataforma_movil.update()
                    self.enemyGenerator.update()
                    self.cronometro.update()
                    self.enemyGenerator.enemies.update(self.terrenos, self.plataformas,self.balas_1,self.player,self.plataforma_movil)  # Actualizar enemigos
                    #screen.fill((30, 30, 30))
                self.terrenos.draw(screen)
                self.plataformas.draw(screen)
                self.plataforma_movil.draw(screen)
                self.trap.draw(screen)
                self.frutas.draw(screen)
                self.vidas.draw(screen)
                self.balas.draw(screen)
                self.balas_1.draw(screen)
                self.bombas.draw(screen)
                self.cronometro.dibujar(screen)
                self.enemyGenerator.enemies.draw(screen)
                self.dañar_jugador()
                self.dañar_enmigo()
                self.sumar_vidas()
                self.sumar_puntos()
                self.daño_trampa()
                self.puntos_texto = self.font.render(f"Puntos: {self.puntos}", True, (255, 255, 255))
                self.vidas_texto = self.font.render(f"Vidas: {self.cantidad_vidas}", True, (255, 255, 255))
                screen.blit(self.vidas_texto, (10,50))
                screen.blit(self.puntos_texto, (10,30))
                screen.blit(self.player.image, self.player.rect)
                self.game_over_fun(screen)
        if self.game_over:
            #self.datos.lista_jugadores.append(self.player.nombre)
            #self.datos.guardar_datos("lista_jugadores1")
            self.ranking.dibujar(screen)
            #self.en_pausa = True
    def dañar_enmigo(self):
            #colisiones = pygame.sprite.groupcollide(self.enemyGenerator.enemies,pygame.sprite.Group(self.balas,self.bombas), True, True)
            
        colisiones_balas = pygame.sprite.groupcollide(self.enemyGenerator.enemies, self.balas, True, True)
        colisiones_bombas = pygame.sprite.groupcollide(self.enemyGenerator.enemies, self.bombas, True, False)
            # Combinar las colisiones de balas y bombas
        colisiones = {**colisiones_balas,**colisiones_bombas}
        for enemigo_dañado in colisiones.keys():
            print("le diste")
            self.player.puntos +=1
            print(self.player.puntos)
    def dañar_jugador(self):
            if not self.colision_jugador_enemigo_procesada:
                colisiones_jugador_enemigos = pygame.sprite.spritecollide(self.player, self.enemyGenerator.enemies, False)
                for colision in colisiones_jugador_enemigos:
                    print ("te dieron")
                    self.player.vidas -=1
                    print(self.player.vidas)
                    self.colision_jugador_enemigo_procesada = True
                    self.collision_clock=0
            if self.collision_clock >= 300:
                self.colision_jugador_enemigo_procesada = False
                colisiones_balas = pygame.sprite.spritecollide(self.player,self.balas_1,False)
                for colision in  colisiones_balas:
                    print ("te dieron")
                    self.player.vidas -=1
                    print(self.player.vidas)
                    self.colision_jugador_enemigo_procesada = True
                    self.collision_clock=0
            if self.collision_clock >= 300:
                self.colision_jugador_enemigo_procesada = False
    def sumar_vidas(self):
        colisiones_vidas = pygame.sprite.spritecollide(self.player, self.vidas, True)
        for colision in colisiones_vidas:
            print ("sumaste vida")
            self.player.vidas +=1
            print(self.player.vidas)
    def sumar_puntos(self):
        colisiones_frutas = pygame.sprite.spritecollide(self.player, self.frutas,True)
        for colision in colisiones_frutas:
            print ("sumaste puntos")
            self.player.puntos +=100
            print(self.player.puntos)
    def daño_trampa(self):
        if not self.colision_jugador_enemigo_procesada:
            colision_trampa= pygame.sprite.spritecollide(self.player, self.trap, False)
            for colision in colision_trampa:
                print ("pisaste una trampa")
                self.player.vidas -=1
                print(self.player.vidas)
                self.colision_jugador_enemigo_procesada = True
                self.collision_clock=0
        if self.collision_clock >= 600:
            self.colision_jugador_enemigo_procesada = False
    def game_over_fun(self,screen):
        if self.player.vidas == 0:
            print(self.datos.lista_jugadores)
            self.datos.lista_jugadores.append(self.player.nombre)
            self.datos.guardar_datos("lista_jugadores")
            print(self.datos.lista_jugadores)
            self.ranking.dibujar(screen)
            self.game_over = True 
            


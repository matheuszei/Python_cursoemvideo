#Faça um programa em Python que abre e reproduza o áudio de um arquivo .mp3

import pygame
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()
pygame.event.wait()
'''(021) Faça um programa em Python que abra e reproduza um áudio de um arquivo MP3. '''
import pygame
pygame.mixer.init()
pygame.mixer.music.load('routinemp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
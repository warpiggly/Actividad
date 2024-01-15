#tengo que tener la libreria 
import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla (no se utilizará, pero es necesaria para inicializar el mixer de pygame)
pygame.display.set_mode((800, 800))

# Cargar el sonido (puedes reemplazar "ejemplo.wav" con la ruta de tu propio archivo de sonido)
sonido = pygame.mixer.Sound("ejemplo.wav")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Reproducir el sonido cuando se presiona la tecla espaciadora
                sonido.play()

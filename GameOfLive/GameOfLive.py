# https://www.youtube.com/watch?v=qPtKv9fSHZY
#

import pygame
import time
import numpy

pygame.init()

# Tamaño de la pantalla
width, height = 640, 640
screen = pygame.display.set_mode( (width,height) )

# Color de la rejilla
bg = 8,8,8
screen.fill( bg )

# Numero de celdas
nxC, nyC = 64, 64

# Dimension de la celda
dimCW = int( width/nxC  ) 
dimCH = int( height/nyC )

# Estado de las celdas: Vivas=1 Muertas=0
gameState = numpy.zeros( (nxC,nyC) )        

# Automata que se mueve
gameState[ 5,3 ] = 1
gameState[ 5,4 ] = 1
gameState[ 5,5 ] = 1
gameState[ 6,5 ] = 1
gameState[ 7,4 ] = 1

# Control de la pausa
pauseExect = False


# TODO: afegir noves funcionalitats
# ERROR: 
while True:

    newGameState = numpy.copy( gameState )

    # Limpiamos la pantalla
    screen.fill( bg )
    time.sleep( 0.1 )

    # Capturamos eventos de teclado
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        mouseClick = pygame.mouse.get_pressed()
        
        if sum(mouseClick)>0 :
            posX, posY = pygame.mouse.get_pos()
            print( posX, posY )
            celX, celY = int (numpy.floor( posX / dimCW ) ), int( numpy.floor( posY / dimCH ) )
            # print( celX, celY )
            newGameState[ celX, celY ] = not newGameState[ celX, celY ]


    for y in range  (0,nxC):
        for x in range (0,nyC):
            
            if ( not pauseExect ):

                # Calculamos en numero de vecinos
                n_neigh = gameState[ (x-1) % nxC, (y-1) % nyC ] + \
                          gameState[ (x  ) % nxC, (y-1) % nyC ] + \
                          gameState[ (x+1) % nxC, (y-1) % nyC ] + \
                          gameState[ (x-1) % nxC, (y  ) % nyC ] + \
                          gameState[ (x+1) % nxC, (y  ) % nyC ] + \
                            gameState[ (x-1) % nxC, (y+1) % nyC ] + \
                          gameState[ (x  ) % nxC, (y+1) % nyC ] + \
                          gameState[ (x+1) % nxC, (y+1) % nyC ]

                # Aplicamos reglas del jueg
                # Regla 1
                if gameState[ x, y ] == 0 and n_neigh == 3:
                    newGameState[ x, y ] = 1 
                # Regla 2
                elif gameState[ x, y ] == 1 and ( n_neigh<2 or n_neigh>3 ):
                    newGameState[ x, y ] = 0


            # Dibujo de la rejilla y automatas
            poly = [( (x  ) * dimCW, (y  ) * dimCH ),
                    ( (x+1) * dimCW, (y  ) * dimCH ),
                    ( (x+1) * dimCW, (y+1) * dimCH ) ,
                    ( (x  ) * dimCW, (y+1) * dimCH ) ]

            if( newGameState[x,y] == 0 ):
                pygame.draw.polygon( screen, ( 32, 32, 32), poly, 1 )
            else:
                pygame.draw.polygon( screen, (230,230,230), poly, 0 )

    # Actualizamos el estado
    gameState = numpy.copy( newGameState )

    pygame.display.flip()
            

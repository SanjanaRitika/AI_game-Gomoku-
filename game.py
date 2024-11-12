
import pygame
from pygame.locals import *
from sys import exit
from boardstate import *
from gomoku import Gomoku
from render import GameRender
from gomoku_ai import *

#run in terminal
if __name__ == '__main__': 
    gomoku = Gomoku()
    render = GameRender(gomoku)

    #change the AI here, bigger the depth stronger the AI
    ai = gomokuAI(gomoku, BoardState.BLACK, 2)
    ai2 = gomokuAI(gomoku, BoardState.WHITE, 1)

    result = BoardState.EMPTY

    #enable ai here
    enable_ai = True
    enable_ai2 = False

    #edit if ai plays first
    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()

    while True:
        #ai vs ai section
        if enable_ai2:
            ai2.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print (result, "wins")
                break
            if enable_ai:

                ai.one_step()
                result = gomoku.get_chess_result()

                if result != BoardState.EMPTY:
                    print (result, "wins")
                    break
            else:
                render.change_state()

        

        #pygame event, player vs. ai section
        for event in pygame.event.get():
            #exit

            if event.type == QUIT:
                exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                #play a step
                if render.one_step():
                    result = gomoku.get_chess_result()
                else:
                    continue
                if result != BoardState.EMPTY:
                    break
                if enable_ai:

                    ai.one_step()
                    result = gomoku.get_chess_result()
                else:
                    render.change_state()
        
        #draw
        render.draw_chess()
        render.draw_mouse()

        if result != BoardState.EMPTY:
            render.draw_result(result)

        #update
        pygame.display.update()

        

        

#run this for AI vs AI 
"""""
import pygame
from pygame.locals import *
from sys import exit
import time
from boardstate import *
from gomoku import Gomoku
from render import GameRender
from gomoku_ai import *

if __name__ == '__main__': 
    gomoku = Gomoku()
    render = GameRender(gomoku)

    ai = gomokuAI(gomoku, BoardState.BLACK, 2)
    ai2 = gomokuAI(gomoku, BoardState.WHITE, 1)

    result = BoardState.EMPTY
    enable_ai = True
    enable_ai2 = True

    ai.first_step()
    result = gomoku.get_chess_result()
    render.change_state()

    while result == BoardState.EMPTY:
        pygame.event.pump()  # Process internal pygame events

        # AI-vs-AI loop
        if enable_ai2:
            ai2.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print(result, "wins!")
                break

        if enable_ai:
            ai.one_step()
            result = gomoku.get_chess_result()
            if result != BoardState.EMPTY:
                print(result, "wins!")
                break

        # Draw the board and update display
        render.draw_chess()
        render.draw_mouse()

        if result != BoardState.EMPTY:
            render.draw_result(result)

        pygame.display.update()

        # Optional delay to slow down AI moves
        time.sleep(0.5)

    # Minimal event handler to quit
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
"""
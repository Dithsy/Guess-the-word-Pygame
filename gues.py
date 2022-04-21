import pygame
import random


from pygame.constants import MOUSEBUTTONDOWN

pygame.init()
display = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Guess the word game ")
pygame.display.update()



violet = (148, 0, 211)
ghost_white = (248, 248, 255)
magenta = (255, 0, 255)
limegreen = (50, 205, 50)
orange =(255, 69, 0)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0,0,0)
font = pygame.font.SysFont(None, 30)
message = font.render("welcome to guess the word game where you`ll be entering letters to form a word", True, violet)
display.fill(ghost_white)
display.blit(message,[50, 50])
pygame.display.update()
            

wordbank = ["while", "yatch", "boats", "birds"]
computer = random.choice(wordbank)
correct_letters=["-"]*len(computer)
blanks= "".join(correct_letters)
font = pygame.font.SysFont(None, 100)
message = font.render(blanks, True, magenta)
display.blit(message,[200, 100])
pygame.display.update()

font = pygame.font.SysFont(None, 30)
message = font.render("Here is a hint, the word is 5 letters long", True, violet)
display.blit(message,[50, 150])
pygame.display.update()

player = pygame.font.SysFont(None, 30)
message = player.render("guess a letter: ", True, orange)
display.blit(message,[70, 180])
pygame.display.update()

input_rect = pygame.Rect(240, 180, 40, 30)
text = ''
colour_active = pygame.Color(red)
colour_passive = pygame.Color(black)
color = colour_passive

pygame.draw.rect(display,black,input_rect)
text_surface = font.render(text, True,green)
display.blit(text_surface,input_rect)
pygame.display.update()
               
def position(x,y):
    display.blit(message,[x, y])
    y += 50

quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        
            
    passes = 8
    while passes > 0:
        passes -= 1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                quit = True
            else:
                quit = False

        if event.type == pygame.KEYDOWN:
            event.key == pygame.K_letter
            text = ''

        if quit:
            color= colour_active
        else:
           color = colour_passive  
    
        # if text in computer:
        #     for i in range(len(computer)):
        #         if computer[i] == text:
        #             correct_letters[i] = text
        #             blanks= "".join(correct_letters)
        #             game = pygame.font.SysFont(None, 30)
        #             message = game.render(blanks, True, limegreen)
        #             display.blit(message,[200, 250])
        #             pygame.display.update()
        #     correct_guess = pygame.font.SysFont(None, 30)
        #     message = correct_guess.render("Your guess was correct", True, red)
        #     display.blit(message,[50, 300])
        #     pygame.display.update()
        #     passes += 1
        # else:
        #     guess = pygame.font.SysFont(None, 30)
        #     message = guess.render("Your guess was incorrect!", True, red)
        #     display.blit(message,[50, 300])
        #     pygame.display.update()
            

        #     left = print("The passes you are left with are:", passes)
        #     font = pygame.font.SysFont(None, 30)
        #     message = font.render(left,True, red)
        #     display.blit(message,[50, 350])

        
        # if blanks == computer:
        #     win = pygame.font.SysFont(None, 70)
        #     message = win.render("YOU WIN!!", True, green)
        #     display.blit(message,[200, 500])
        #     pygame.display.update()
        #     break
        # elif passes == 0:
        #     quit = True    
        #     loss = pygame.font.SysFont(None, 70)
        #     message = loss.render("YOU LOST, GAME OVER!!", True, green)
        #     display.blit(message,[200, 500])
        #     pygame.display.update()

quit = True
pygame.quit()
    

import pygame
import time
import random

#Initialize the imported pygame modules.
pygame.init()

#Color Setup
white = (255,255,255) #background
yellow = (255,255,102)
black =(0,0,0) 
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#Display Values
dis_width = 600
dis_height =  400

#Display Setup
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

#Game Clock
clock = pygame.time.Clock()

#Snake Size & Speed
snake_block = 10
snake_speed = 15

#Font Style
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Game Score
def Your_score(score): 
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

#Snake Setup
def our_snake(snake_block, snake_list): 
    for x in snake_list: 
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#End Game Message
def message (msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

#Running the game
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True: #GAME OVER MESSAGE 
            dis.fill(blue)
            message ("You Lost! Press Q - Quit or C - Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            
            for event in pygame.event.get(): #GAME OVER OPTIONS 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): 
            if event.type==pygame.QUIT: #QUITTING THE GAME
                game_over=True
            
            if event.type == pygame.KEYDOWN: #SNAKE MOVEMENTS
                if event.key == pygame.K_LEFT: 
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: 
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: 
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: 
                    y1_change = snake_block
                    x1_change = 0
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #IF SNAKE GOES OUT OF BOUNDS
            game_close = True #GAME OVER

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        pygame.draw.rect(dis,green, [foodx, foody, snake_block, snake_block])
        
        #Our snake is just a list that keeps adding more elements to it. 
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        #Controlling the length of the list. 
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #IF the snake eats itself, game over. 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #Snake setup & Score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()
        
        if x1 == foodx and y1 == foody: #SNAKE EATS FOOD & ADDS 1 LENGTH
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    #Quit method to end the program
    pygame.quit()
    quit()

gameLoop()

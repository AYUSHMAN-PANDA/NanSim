'''
In this code, we are using Pygame library to visualize the grid with hiders, seekers, obstacles, and strategic points. 
The game loop consists of constantly checking for events, updating the display, and updating the game state. 
The game will run until the player closes the window or the program is exited. 
In each iteration of the game loop, we check for events using pygame.event.get() method. 
If the event is a QUIT event, we exit the game loop and the program terminates. 
If not, we update the display by calling update_display() method and update the game state by calling update_game_state() method. 
The update_display() method is responsible for drawing all the game objects such as hiders, seekers, obstacles, and 
strategic points on the screen. The update_game_state() method is responsible for updating the positions of hiders, seekers, 
obstacles, and strategic points based on the game logic.
'''
import pygame
import random

# import logistics function
from strategy_sweep import *
from obstacle_movement import *
from hider_movement import *

# Strategy : 
# 2 for 2way sweep
# 4 for 4way sweep
Strategy = 2
# Strategy = 4


Obstacle_movement = 1
# 1- random, 2- seeker friendly, 3- seeker friendly

# initialize pygame and related modules
pygame.init()
pygame.font.init()

# screen width and height
screen_width = 1300
screen_height = 800

# Status Bar Height
top_status_bar_height = 30 
bottom_status_bar_height = 30 

# screen width and height
grid_width = 100
grid_height = 100
grid_margin = 50


# create screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hide-N-Seek')
Icon = pygame.image.load('logo.png')
pygame.display.set_icon(Icon)

# color definitions
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
lemon = (217, 245, 39)
pink = (240, 24, 182)

# hider dot size
hider_dot_size = 5
hider_color = blue

# seeker size and color
seeker_size = 5
seeker_color = green

# obstacle size and color
obstacle_size = 20
obstacle_color = red

# strategic point size and color
strategic_point_size = 4
strategic_point_color = lemon

# number of obstacles and seekers
num_obstacles = 500
num_seekers = 100
num_hiders = 300

# initialize hider dots
hider_dots = []
for i in range(num_hiders):
    hider_dots.append((random.randint(0+grid_margin, grid_width+grid_margin), random.randint(0+grid_margin, grid_height+grid_margin)))

# initialize seekers
seekers = []
for i in range(num_seekers):
    seekers.append((random.randint(0+grid_margin, grid_width+grid_margin), random.randint(0+grid_margin, grid_height+grid_margin)))

# initialize obstacles
obstacles = []
for i in range(num_obstacles):
    new_obstacle = (random.randint(0+grid_margin, grid_width+grid_margin), random.randint(0+grid_margin, grid_height+grid_margin))
    obstacles.append(new_obstacle)

# initialize strategic points
strategic_points = []
for i in range(num_obstacles):
    strategic_points.append((obstacles[i][0]+obstacle_size//2, obstacles[i][1]))
    strategic_points.append((obstacles[i][0], obstacles[i][1]-obstacle_size//2))
    strategic_points.append((obstacles[i][0], obstacles[i][1]+obstacle_size//2))
    strategic_points.append((obstacles[i][0]-obstacle_size//2, obstacles[i][1]))

# Create a font object for the status bar texts
font = pygame.font.SysFont('arial', 18)

# Create a surface for the top status bar
status_bar_top = pygame.Surface((screen_width, top_status_bar_height))
status_bar_top.fill((113, 131, 201))

# Render the text for the stats
top_text = font.render("Simulation for Sweep Strategy in the Hide and Seek Game", True, (255, 255, 255))
bottom_text_1 = font.render("Hiders", True, (255, 255, 255))
bottom_text_2 = font.render("Seekers", True, (255, 255, 255))
bottom_text_3 = font.render("Obstacles", True, (255, 255, 255))
bottom_text_4 = font.render("Strategic Point", True, (255, 255, 255))
right_text_1 = font.render("Seeker Strategy: " + str(Strategy) + " way Sweep Strategy", True, (255, 255, 255))
# bottom_text_3 = font.render("CPs" + str(), True, (255, 255, 255))

# Create a surface for the bottom status bar
status_bar_bottom = pygame.Surface((screen_width, bottom_status_bar_height))
status_bar_bottom.fill((74, 124, 181))

# Create a surface for the right status bar
right_status_bar_margin = 10
status_bar_right = pygame.Surface((screen_width - (grid_width + grid_margin ), screen_height-bottom_status_bar_height-top_status_bar_height-right_status_bar_margin))
status_bar_right.fill((126, 172, 224))


# temp: delete this todo
all_seekers_pos_1, all_seekers_pos_2, all_seekers_pos_3, all_seekers_pos_4 = get_diagonal_elements(grid_width, grid_height, grid_margin)
# all_seekers_pos_1.reverse()
all_seekers_pos_2.reverse()
total_steps = len(all_seekers_pos_1)
game_step = 0
seekers=all_seekers_pos_1[0] + all_seekers_pos_2[0]
# obstacles = [(0,0)]
print(len(all_seekers_pos_1))
# print(all_seekers_pos_2)
print(len(all_seekers_pos_2))
print(len(all_seekers_pos_3))
print(len(all_seekers_pos_4))
# print(all_seekers_pos_4)


# game loop
running = True
pause = 0
step = 0
game_no = 0
display = 0
while running:
    if(len(hider_dots) == 0):
        display = 1
        
    
    if(game_no == 50):
        pause = 0
    elif(display == 1):
        display = 0
        print("Round no : "+ str( game_no + 1) + " Seekers req : "+ str(step))
        game_no += 1
        step = 0
        hider_dots = []
        for i in range(num_hiders):
            hider_dots.append((random.randint(0+grid_margin, grid_width+grid_margin), random.randint(0+grid_margin, grid_height+grid_margin)))


    if(pause != 0):
        step += 1
        # seekers = all_seekers_pos_2[game_step] + all_seekers_pos_4[game_step]
        # seekers = []
        
        seekers = all_seekers_pos_3[game_step] + all_seekers_pos_4[game_step]
        if(Strategy == 4):
            seekers += all_seekers_pos_1[game_step] + all_seekers_pos_2[game_step]
            
        game_step = (game_step + 1) % total_steps
        # num_seekers = len(seekers)
        # print("No of seekers : ", num_seekers)
        
        # update obstacle positions 
        obstacles = move_obstacle(obstacles, grid_width, grid_height, grid_margin)
        
        # update corresposnding SP posn
        strategic_points = []
        for i in range(num_obstacles):
            strategic_points.append((obstacles[i][0]+obstacle_size//2, obstacles[i][1]))
            strategic_points.append((obstacles[i][0], obstacles[i][1]-obstacle_size//2))
            strategic_points.append((obstacles[i][0], obstacles[i][1]+obstacle_size//2))
            strategic_points.append((obstacles[i][0]-obstacle_size//2, obstacles[i][1]))
        
        # update hiders posn
        hider_dots = hider_movement(hider_dots, strategic_points, grid_width, grid_height, grid_margin)  
        # print(len(hider_dots))

   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_SPACE:
                pause = (pause - 1) * -1
            if event.key == pygame.K_RIGHT:
                # update seekers position
                seekers = all_seekers_pos_1[game_step] + all_seekers_pos_2[game_step] + all_seekers_pos_3[game_step] + all_seekers_pos_4[game_step]
                game_step = (game_step + 10) % total_steps
                # num_seekers = len(seekers)
                # print("No of seekers : ", num_seekers)
                
                # update obstacle positions 
                obstacles = move_obstacle(obstacles, grid_width, grid_height)
                
                # update corresposnding SP posn
                strategic_points = []
                for i in range(num_obstacles):
                    strategic_points.append((obstacles[i][0]+obstacle_size//2, obstacles[i][1]))
                    strategic_points.append((obstacles[i][0], obstacles[i][1]-obstacle_size//2))
                    strategic_points.append((obstacles[i][0], obstacles[i][1]+obstacle_size//2))
                    strategic_points.append((obstacles[i][0]-obstacle_size//2, obstacles[i][1]))
                
                # update hiders posn
                hider_dots = hider_movement(hider_dots, strategic_points, grid_width, grid_height, grid_margin)  

                

            if event.key == pygame.K_LEFT:
                seekers = all_seekers_pos_1[game_step] + all_seekers_pos_2[game_step] + all_seekers_pos_3[game_step] + all_seekers_pos_4[game_step]
                game_step = (game_step - 10) % total_steps
                num_seekers = len(seekers)
                # print("No of seekers : ", num_seekers)
                # if(len(obstacles_positions) == 0):
                #     continue
                # obstacles_moving = True
                # compute()
                # eliminate_hiders_2(seeker_ratio)
    
    screen.fill(white)

    # for drawing grids
    # block_size = 10
    # for x in range(grid_width+grid_margin):
    #     for y in range(grid_height+grid_margin):
    #         rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
    #         pygame.draw.rect(screen, white, rect,1)
    
    # seeker catches hider
    # seeker_set = set(seekers)
    # hider_set = set(hider_dots)
    # caught_hiders = seeker_set.intersection(hider_set)
    # for hider in hider_set:
    #     hider_dots.remove(hider)
    #     print("removed")

    
        
    # draw seekers
    for seeker in seekers:
        pygame.draw.circle(screen, seeker_color, seeker, seeker_size)
        
    # draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, (obstacle[0] - obstacle_size // 2, obstacle[1] - obstacle_size // 2, obstacle_size, obstacle_size))
        
    # draw strategic points
    for point in strategic_points:
        pygame.draw.rect(screen, strategic_point_color, (point[0] - strategic_point_size // 2, point[1] - strategic_point_size // 2, strategic_point_size, strategic_point_size))
    
    # draw hider dots   

    for hider in hider_dots:
        if hider in seekers:
            hider_dots.remove(hider)
        else:
            pygame.draw.circle(screen, hider_color, hider, hider_dot_size)
    
    # draw seekers
    for seeker in seekers:
        pygame.draw.circle(screen, seeker_color, seeker, seeker_size)
    
    # Draw the status bars on the screen
    sb_bottom_x = 0
    sb_bottom_y = screen_height - bottom_status_bar_height
    screen.blit(status_bar_top, (0, 0))
    screen.blit(status_bar_bottom, (sb_bottom_x, sb_bottom_y))
    
    # Blit the text on the botton status bar
    # Hider
    pygame.draw.circle(status_bar_bottom, hider_color, (10,20), hider_dot_size*1.8)
    screen.blit(bottom_text_1, (sb_bottom_x+ 20,  sb_bottom_y+10)) 

    # Seeker
    pygame.draw.circle(status_bar_bottom, seeker_color, (380, 20), seeker_size)
    screen.blit(bottom_text_2, (sb_bottom_x+ 400, sb_bottom_y+ 10)) 

    # Obstacle
    pygame.draw.rect(status_bar_bottom, obstacle_color, (750, 12,  obstacle_size*0.8, obstacle_size*0.8))
    screen.blit(bottom_text_3, (sb_bottom_x+ 780, sb_bottom_y+ 10)) 


    # SP
    pygame.draw.rect(status_bar_bottom, strategic_point_color, (1100, 15,  obstacle_size*0.5, obstacle_size*0.5))
    screen.blit(bottom_text_4, (sb_bottom_x+ 1130, sb_bottom_y+ 10))

    # Blit the text on the right status bar
    sb_right_x = grid_width*1.5
    sb_right_y = top_status_bar_height+right_status_bar_margin//2
    screen.blit(status_bar_right, (sb_right_x, sb_right_y))

    



    t1 = font.render(":::::: Game Stats :::::: ", True, (255, 255, 255))
    t2 = font.render("Grid Size : " + str(grid_height) + " x " + str(grid_width), True, (255, 255, 255))
    t3 = font.render("Number of Hiders : " +str(num_hiders), True, (255, 255, 255))
    t4 = font.render("Number of Obstacles : "+str(num_obstacles), True, (255, 255, 255))
    t5 = font.render("Number of Strategic Points : " + str(num_obstacles*4), True, (255, 255, 255))

    right_text_2 = font.render("Active Seekers: " + str(len(seekers) - 4), True, (255, 255, 255))#small offset for extra seekers. ignored for now
    right_text_3 = font.render("Active Hiders: " + str(len(hider_dots)), True, (255, 255, 255)) 
    right_text_4 = font.render("Game Step: " + str(step), True, (255, 255, 255))

  

    screen.blit(t1, (sb_right_x + 170, sb_right_y + 30))
    screen.blit(t2, (sb_right_x + 20, sb_right_y + 50))
    screen.blit(t3, (sb_right_x + 20, sb_right_y + 70))
    screen.blit(t4, (sb_right_x + 20, sb_right_y + 90))
    screen.blit(t5, (sb_right_x + 20, sb_right_y + 110))
    screen.blit(right_text_1, (sb_right_x + 20, sb_right_y + 130))

    screen.blit(right_text_2, (sb_right_x + 20, sb_right_y + 200))
    screen.blit(right_text_3, (sb_right_x + 20, sb_right_y + 220))
    screen.blit(right_text_4, (sb_right_x + 20, sb_right_y + 240))

    

    # Blit the text on the top status bar
    screen.blit(top_text, (400,3))

    pygame.display.update()
    pygame.time.delay(10)

# quit pygame
pygame.quit()


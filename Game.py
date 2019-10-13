
import pygame
from pygame import image as img
import os
import time

state = "Title"
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("GE:START")
clock = pygame.time.Clock()
Title_selected = None
Options_selected = None
Play_selected = None
Load_game_disabled = True
player_state = "normal"
object_list = ["img/Objects/rock_1.png"]
player_width = 100
player_hight = 100

x,y = 0,0


background = img.load("img/background.png").convert()
background.set_alpha(None)
Title = img.load("img/Title.png").convert_alpha()
options = img.load("img/options.png").convert_alpha()
play = img.load("img/play.png").convert_alpha()
options_isselected = img.load("img/options_isselected.png").convert_alpha()
play_isselected = img.load("img/play_isselected.png").convert_alpha()

coming_soon = img.load("img/coming_soon.png").convert_alpha()
go_back = img.load("img/go_back.png").convert_alpha()
go_back_isselected = img.load("img/go_back_isselected.png").convert_alpha()

New_game = img.load("img/New_game.png").convert_alpha()
New_game_isselected = img.load("img/New_game_isselected.png").convert_alpha()
Load_game = img.load("img/Load_game.png").convert_alpha()
Load_game_isselected = img.load("img/Load_game_isselected.png").convert_alpha()
Load_game_isdisabled = img.load("img/Load_game_isdisabled.png").convert_alpha()

player = img.load("img/player_normal.png").convert_alpha()


objects_group = pygame.sprite.Group()


class Level():
    #                              should be number
    def get_background(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = False
        for line in f.readlines():
            if found == True:
                return line
            elif "# slice {}".format(slice_) in line:
                found = True


    def get_levelsize(self, name):
        f = open("levels/{}.txt".format(name), "r")
        found = False
        i = 0
        for line in f.readlines():
            if i == 0:
                line = eval(line)
                return line
            i += 1

    
    def get_startslice(self, name):
        f = open("levels/{}.txt".format(name), "r")
        found = False
        i = 0
        for line in f.readlines():
            if i == 1:
                line = int(line)
                return line
            i += 1
    

    def get_startpos(self, name):
        f = open("levels/{}.txt".format(name), "r")
        found = False
        i = 0
        for line in f.readlines():
            if i == 2:
                return line
            i += 1

    
    def get_objects(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = 0
        for line in f.readlines():
            if found == 2:
                return line
            if found == 1:
                found = 2
            elif "# slice {}".format(slice_) in line:
                found = 1

lvl_1 = Level()

class Player():

    def __init__(self):
        pass



class object__(pygame.sprite.Sprite):
    def __init__(self, type, location):
        pass
        # pygame.sprite.Sprite.__init__(self)
        # self.size = self.get_rect().size
        # print(self.size)


def re_draw():
    global state
    global player_state
    global background
    global level
    global leveln
    global slice_
    global ex_x
    global ex_y
    global level_size
    global ex_background

    if state == "Title":
        win.blit(background, (0,0))
        win.blit(Title, (0,0))
        if Title_selected == None:
            win.blit(play, (0,400))
            win.blit(options, (0,600))
        elif Title_selected == "play":
            win.blit(play_isselected, (0,400))
            win.blit(options, (0,600))
        elif Title_selected == "options":
            win.blit(play, (0,400))
            win.blit(options_isselected, (0,600))

    
    elif state == "Options":
        win.blit(background, (0,0))
        win.blit(coming_soon, (0,0))
        if Options_selected == None:
            win.blit(go_back, (0,880))
        elif Options_selected == "go_back":
            win.blit(go_back_isselected, (0,880))

    
    elif state == "Play":
        win.blit(background, (0,0))
        if Play_selected == None:
            win.blit(go_back, (0,880))
            win.blit(New_game, (0,300))
        elif Play_selected == "go_back":
            win.blit(go_back_isselected, (0,880))
            win.blit(New_game, (0,300))
        elif Play_selected == "New_game":
            win.blit(go_back, (0,880))
            win.blit(New_game_isselected, (0,300))

        if Load_game_disabled == False:
            if Play_selected == "Load_game":
                win.blit(Load_game_isselected, (0,500))
                win.blit(go_back, (0,880))
                win.blit(New_game, (0,300))
            else:
                win.blit(Load_game, (0,500))
        else:
            if Play_selected == "Load_game":
                win.blit(Load_game_isdisabled, (0,500))
                win.blit(go_back, (0,880))
                win.blit(New_game, (0,300))
            else:
                win.blit(Load_game_isdisabled, (0,500))
        
    
    elif state == "Load_new":
        pass


    elif state == "Explore":
        global Objects
        global Objects_empty
        global ex_background
        if player_state == "normal":
            win.blit(ex_background, (0,0))
            win.blit(player, (ex_x,ex_y))
            if Objects_empty == False:
                for i in Objects:
                    z = 0
                    for e in i:
                        if z == 0:
                            nr = e+1
                        elif z == 1:
                            x = e
                        elif z == 2:
                            y = e
                            exec("win.blit(object_{}, ({}, {}))".format(nr, x, y))
                        z += 1
                



    elif state == "Explore_update":
        Objects = level.get_objects(leveln, slice_)
        Objects_empty = False
        if Objects == "\n":
            Objects_empty = True
        if Objects_empty == False:
            Objects = eval(Objects)
        ex_background = (level.get_background(leveln, slice_)).replace('"', '')
        ex_background = (ex_background).replace("\n", "")
        ex_background = img.load(ex_background).convert()
        ex_background.set_alpha(None)
        if Objects_empty == False:
            x = 1
            for i in object_list:
                exec('object_{} = img.load("{}").convert_alpha()'.format(x, i), globals())
                for i in Objects:
                    z = 0
                    for e in i:
                        if z == 0:
                            nr = e+1
                        elif z == 1:
                            x = e
                        elif z == 2:
                            y = e
                            exec("object_{} = object__(0, ({}, {}))".format(nr, x, y))
                        z += 1
                
                x += 1
            

        state = "Explore"



        
def updates():
    global Title_selected
    global Options_selected
    global Play_selected
    global state
    global player_state
    global ex_x
    global ex_y
    global slice_
    global level_size
    global level
    global leveln
    x, y = pygame.mouse.get_pos()


    if state == "Title":

        # Check which text is hovered over
        if x > 500 and x < 1200:
            if y > 400 and y < 600:
                Title_selected = "play"
            elif y > 600 and y < 800:
                Title_selected = "options"
            else:
                Title_selected = None
        else:
            Title_selected = None

        # Test for clicks on text
        mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
        if mouse_1:
            if Title_selected == "play":
                state = "Play"
                Title_selected = None
                time.sleep(0.1)
            elif Title_selected == "options":
                state = "Options"
                Title_selected = None
                

    elif state == "Options":
        # Check which text is hovered over
        if x > 500 and x < 1200:
            if y > 880:
                Options_selected = "go_back"
            else:
                Options_selected = None
        else:
            Options_selected = None

        # Test for clicks on text
        mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
        if mouse_1:
            if Options_selected == "go_back":
                state = "Title"
                Options_selected = None


    elif state == "Play":
        # Check which text is hovered over
        if x > 500 and x < 1200:
            if y > 880:
                Play_selected = "go_back"
            elif y > 300 and y < 500:
                Play_selected = "New_game"
            elif y > 500 and y < 800:
                Play_selected = "Load_game"
            else:
                Play_selected = None
        else:
            Play_selected = None

        # Test for clicks on text
        mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
        if mouse_1:
            if Play_selected == "go_back":
                state = "Title"
                Play_selected = None
            if Play_selected == "New_game":
                state = "Load_new"
                Play_selected = None


    elif state == "Load_new":
        level = lvl_1
        leveln = "lvl_1"
        slice_ = level.get_startslice(leveln)
        pos = eval(level.get_startpos(leveln))
        ex_x = pos[0]
        ex_y = pos[1]
        level_size = level.get_levelsize(leveln)

        state = "Explore_update"


    elif state == "Explore":
        if player_state == "normal":
            vel = 5
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                ex_y -= vel
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                ex_x -= vel
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                ex_y += vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                ex_x += vel
            if ex_x < 1820 and ex_y < 980 and ex_x > 0 and ex_y > 0:
                pass
            else:
                # You are off the screen
                if ex_x > 1820:
                    if level_size == [1, 1]:
                        ex_x -= vel
                    else:
                        if slice_ % level_size[1] != 0:
                            slice_ += 1
                            ex_x = 0
                            state = "Explore_update"
                        else:
                            ex_x -= vel
                elif ex_x < 0:
                    if level_size == [1, 1]:
                        ex_x += vel
                    else:
                        if slice_ == 1:
                            ex_x += vel
                        elif (slice_-1) % level_size[1] != 0:
                            slice_ -= 1
                            ex_x = 1820
                            state = "Explore_update"
                        else:
                            ex_x += vel
                if ex_y > 980:
                    if level_size == [1, 1]:
                        ex_y -= vel
                    else:
                        if slice_ < (level_size[1]**2)-level_size[1]:
                            slice_ += level_size[1]
                            ex_y = 0
                            state = "Explore_update"
                        else:
                            ex_y -= vel
                elif ex_y < 0:
                    if level_size == [1, 1]:
                        ex_y += vel
                    else:
                        if slice_ > level_size[1]:
                            slice_ -= level_size[1]
                            ex_y = 980
                            state = "Explore_update"
                        else:
                            ex_y += vel

            # Collision
            if True:
                pass


run = True
while run:
    clock.tick(60)
    x, y = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Temporary
    if keys[pygame.K_LCTRL] and keys[pygame.K_SPACE]:
        run = False


    updates()
    re_draw()
    pygame.display.update()


pygame.quit()

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
object_list = ["img/obj/rock_1.png", "img/obj/rock_2.png", "img/obj/house_1.png"]
player_width = 100
player_hight = 100
prev_failed_key = None

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
                line = eval(line)
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
        self.image = img.load("img/player_normal.png").convert_alpha()
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        if True:
            temp = lvl_1.get_startpos("lvl_1")
            self.rect.x = temp[0]
            self.rect.y = temp[1]

    def Collide(self, group1):
        global ex_x
        global ex_y
        global vel
        if pygame.sprite.spritecollideany(self, group1, pygame.sprite.collide_mask) != None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player_.rect.move_ip(0, vel)
                #ex_y += vel
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_.rect.move_ip(vel, 0)
                #ex_x += vel
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_.rect.move_ip(0, vel*-1)
                #ex_y -= vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_.rect.move_ip(vel*-1, 0)
                #ex_x -= vel

player_ = Player()



class Object__(pygame.sprite.Sprite):
    def __init__(self, type, location):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        if type == 0:
            Rock_1.__init__(self)
        elif type == 1:
            Rock_2.__init__(self)
        elif type == 2:
            House_1.__init__(self)

    def setup(self):
        self.size = self.image.get_rect().size
        self.mask = pygame.mask.from_surface(self.image)

class Rock_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[0])
        self.setup()
        self.rect = self.image.get_rect()

class Rock_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[1])
        self.setup()
        self.rect = self.image.get_rect()

class House_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[2])
        self.setup()
        self.rect = self.image.get_rect()

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
    global objects_group
    global came_from
    global level_size
    global prev_failed_key

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
            win.blit(player, player_.rect)
            if Objects_empty == False:
                b = 0
                for i in Objects:
                    z = 0
                    for e in i:
                        if z == 0:
                            nr = b+1
                        elif z == 1:
                            x = e
                        elif z == 2:
                            y = e
                            exec("win.blit(object_{}.image, ({}, {}))".format(nr, x, y))
                        z += 1
                    b += 1
                
                



    elif state == "Explore_update":
        objects_group = pygame.sprite.Group()
        Objects = level.get_objects(leveln, slice_)
        Objects_empty = False
        if Objects == "\n" or Objects == None:
            Objects_empty = True
        if Objects_empty == False:
            Objects = eval(Objects)
        ex_background = (level.get_background(leveln, slice_)).replace('"', '')
        ex_background = (ex_background).replace("\n", "")
        ex_background = img.load(ex_background).convert()
        ex_background.set_alpha(None)
        if Objects_empty == False:
            x_ = 1
            for i in object_list:
                a = 0
                for i in Objects:
                    z = 0
                    for e in i:
                        if z == 0:
                            nr = a+1
                            type_ = e
                        elif z == 1:
                            x = e
                        elif z == 2:
                            y = e
                            exec("object_{} = Object__({}, ({}, {}))".format(nr, type_, x, y), globals())
                            exec("objects_group.add(object_{})".format(nr), globals())
                            exec("object_{}.rect.x = {}".format(nr, x))
                            exec("object_{}.rect.y = {}".format(nr, y))
                        z += 1
                    a += 1
                
                x_ += 1


        # Checks if any object is overlapping player, not perfect but almost works
        for i in objects_group:
            if i.rect.colliderect(player_):
                if came_from == "-x":
                    slice_ -= 1
                    prev_failed_key = "right"
                    state = "Explore_update_again"
                elif came_from == "x":
                    slice_ += 1
                    prev_failed_key = "left"
                    state = "Explore_update_again"
                elif came_from == "-y":
                    slice_ -= level_size[0]
                    prev_failed_key = "down"
                    state = "Explore_update_again"
                elif came_from == "y":
                    slice_ += level_size[0]
                    prev_failed_key = "up"
                    state = "Explore_update_again"
            break
            
        if state != "Explore_update_again":
            state = "Explore"
        elif state == "Explore_update_again":
            state = "Explore_update"



        
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
    global came_from
    global prev_failed_key
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
        came_from = None
        level = lvl_1
        leveln = "lvl_1"
        slice_ = level.get_startslice(leveln)
        pos = level.get_startpos(leveln)
        ex_x = pos[0]
        ex_y = pos[1]
        level_size = level.get_levelsize(leveln)

        state = "Explore_update"


    elif state == "Explore":
        if player_state == "normal":
            global vel
            vel = 5
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player_.rect.move_ip(0, vel*-1)
                ex_y -= vel
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_.rect.move_ip(vel*-1, 0)
                ex_x -= vel
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_.rect.move_ip(0, vel)
                ex_y += vel
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_.rect.move_ip(vel, 0)
                ex_x += vel
            if player_.rect.x < 1820 and player_.rect.y < 980 and player_.rect.x > 0 and player_.rect.y > 0:
                pass
            else:
                # You are off the screen
                if player_.rect.x > 1820:
                    if level_size == [1, 1]:
                        player_.rect.x -= vel
                    else:
                        if slice_ % level_size[1] != 0 and prev_failed_key != "right":
                            slice_ += 1
                            player_.rect.x = 0
                            came_from = "-x"
                            state = "Explore_update"
                        else:
                            player_.rect.x -= vel
                elif player_.rect.x < 0:
                    if level_size == [1, 1]:
                        player_.rect.x += vel
                    else:
                        if slice_ == 1:
                            player_.rect.x += vel
                        elif (slice_-1) % level_size[1] != 0 and prev_failed_key != "left":
                            came_from = "x"
                            slice_ -= 1
                            player_.rect.x = 1820
                            state = "Explore_update"
                        else:
                            player_.rect.x += vel
                if player_.rect.y > 980:
                    if level_size == [1, 1]:
                        player_.rect.y -= vel
                    else:
                        if slice_ < (level_size[1]**2)-level_size[1] and prev_failed_key != "down":
                            came_from = "-y"
                            slice_ += level_size[1]
                            player_.rect.y = 0
                            state = "Explore_update"
                        else:
                            player_.rect.y -= vel
                elif player_.rect.y < 0:
                    if level_size == [1, 1]:
                        player_.rect.y += vel
                    else:
                        if slice_ > level_size[1] and prev_failed_key != "up":
                            came_from = "y"
                            slice_ -= level_size[1]
                            player_.rect.y = 980
                            state = "Explore_update"
                        else:
                            player_.rect.y += vel

            # Collision
            player_.Collide(objects_group)


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
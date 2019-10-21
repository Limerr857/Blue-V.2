
import pygame
from pygame import image as img
import time
import math

pygame.init()

state = "Title"
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("GE:START")
clock = pygame.time.Clock()
Title_selected = None
Options_selected = None
Play_selected = None
Load_game_disabled = True
player_state = "normal"
object_list = ["img/obj/rock_1.png", "img/obj/rock_2.png", "img/obj/house_1.png", "img/NPC/tophat_happy.png", 
               "img/NPC/blacksmith_happy.png", "img/obj/forge_1.png", "img/obj/wall_1.png", "img/obj/wall_2.png", 
               "img/obj/wall_3.png", "img/obj/wall_4.png"]
player_width = 100
player_hight = 100
prev_failed_key = None
tophat_state = "Save"
blacksmith_state = "New"
shop_state = "New"
level_current = 1
item_list = ["img/item/sword_1.png", "img/item/shield_1.png"]

shop_i_cost = "n/a"
shop_i_health = "n/a"
shop_i_attack = "n/a"
shop_i_special = "n/a"
shop_i_selected = "None"
shop_i_bought = []

x,y = 0,0


background = img.load("img/background.png").convert()
background.set_alpha(None)
Title = img.load("img/menu/Title.png").convert_alpha()
options = img.load("img/menu/options.png").convert_alpha()
play = img.load("img/menu/play.png").convert_alpha()
exit_ = img.load("img/menu/exit.png").convert_alpha()
options_isselected = img.load("img/menu/options_isselected.png").convert_alpha()
play_isselected = img.load("img/menu/play_isselected.png").convert_alpha()
exit_isselected = img.load("img/menu/exit_isselected.png").convert_alpha()

go_back = img.load("img/menu/go_back.png").convert_alpha()
go_back_isselected = img.load("img/menu/go_back_isselected.png").convert_alpha()
toggle_music = img.load("img/menu/toggle_music.png").convert_alpha()
toggle_music_isselected = img.load("img/menu/toggle_music_isselected.png").convert_alpha()

New_game = img.load("img/menu/New_game.png").convert_alpha()
New_game_isselected = img.load("img/menu/New_game_isselected.png").convert_alpha()
Load_game = img.load("img/menu/Load_game.png").convert_alpha()
Load_game_isselected = img.load("img/menu/Load_game_isselected.png").convert_alpha()
Load_game_isdisabled = img.load("img/menu/Load_game_isdisabled.png").convert_alpha()

player = img.load("img/player_normal.png").convert_alpha()

shop_background = img.load("img/shop_1.png").convert()
shop_background.set_alpha(None)

roboto_15 = pygame.font.Font("font/Roboto-Bold.ttf", 15)
roboto_30 = pygame.font.Font("font/Roboto-Bold.ttf", 30)
roboto_60 = pygame.font.Font("font/Roboto-Bold.ttf", 60)
roboto_120 = pygame.font.Font("font/Roboto-Bold.ttf", 120)

txt = roboto_15.render("", False, (0, 0, 0))
txt_pos_x = 0
txt_pos_y = 0

music_track_2 = pygame.mixer.music.load("sound/music/menu.mp3")
music_on = True
music_played = False

objects_group = pygame.sprite.Group()
NPC_group = pygame.sprite.Group()
items_group = pygame.sprite.Group()

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

    
    def get_text(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = 0
        x = 0
        for line in f.readlines():
            if found == 3:
                txt = line.split("/n")
                txt = "".join(txt)
                try:
                    return eval(txt)
                except:
                    # Prevents a bug from happening, if you get error ""string index out of range" then lenghten this list.
                    return ["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
            elif "# slice {}".format(slice_) in line:
                found = 1
            elif found > 0:
                found += 1
            x +=1
    

    def get_shopinv(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = 0
        x = 0
        for line in f.readlines():
            if found == 4:
                return eval(line)
            elif "# slice {}".format(slice_) in line:
                found = 1
            elif found > 0:
                found += 1
            x +=1

lvl_1 = Level()


class Player():
    global tophat_state
    global slice_

    def __init__(self):
        self.image = img.load("img/player_normal.png").convert_alpha()
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.inventory = []
        # Temporary
        self.money = "9999"
        # Not temporary
        self.attack = 0
        self.hp = 100
        if True:
            temp = lvl_1.get_startpos("lvl_1")
            self.rect.x = temp[0]
            self.rect.y = temp[1]

    def Collide(self, group1):
        global ex_x
        global ex_y
        global vel
        global txt
        global txt_pos_x
        global txt_pos_y
        global state

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

        dist = 200
        for obj in NPC_group.sprites():
            center1 = obj.rect.center
            center2 = player_.rect.center

            diff_x = abs(center1[0] - center2[0])
            diff_y = abs(center1[1] - center2[1])

            # Pythagorean theorem
            if diff_x**2 + diff_y**2 <= dist**2:
                if obj.type == 3:
                    # Tophat
                    if tophat_state == "Save":
                        global txt
                        txt = lvl_1.get_text("lvl_1", slice_)
                        txt = txt[0]
                        txt = roboto_15.render(txt, True, (0, 0, 0))
                        txt_pos_x = obj.rect.topleft[0]-63
                        txt_pos_y = obj.rect.topleft[1]-100
                elif obj.type == 4:
                    # Blacksmith
                    if blacksmith_state == "New":
                        txt = lvl_1.get_text("lvl_1", slice_)
                        txt = txt[1]
                        txt = roboto_15.render(txt, True, (0, 0, 0))
                        txt_pos_x = obj.rect.topleft[0]-63
                        txt_pos_y = obj.rect.topleft[1]-110

                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_r]:
                            # Player wants to enter the store.
                            state = "Shop_update"
                break
            else:
                txt = roboto_15.render("", False, (0, 0, 0))
                txt_pos_x = 0
                txt_pos_y = 0

                
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
        elif type == 3:
            NPC_tophat_1.__init__(self)
        elif type == 4:
            NPC_blacksmith_1.__init__(self)
        elif type == 5:
            Forge_1.__init__(self)
        elif type == 6:
            Wall_1.__init__(self)
        elif type == 7:
            Wall_2.__init__(self)
        elif type == 8:
            Wall_3.__init__(self)
        elif type == 9:
            Wall_4.__init__(self)

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

class NPC_tophat_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[3])
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class NPC_blacksmith_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[4])
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Forge_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[5])
        self.setup()
        self.rect = self.image.get_rect()

class Wall_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[6])
        self.setup()
        self.rect = self.image.get_rect()

class Wall_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[7])
        self.setup()
        self.rect = self.image.get_rect()

class Wall_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[8])
        self.setup()
        self.rect = self.image.get_rect()

class Wall_4(Object__):
    def __init__(self):
        self.image = img.load(object_list[9])
        self.setup()
        self.rect = self.image.get_rect()


class Item(pygame.sprite.Sprite):
    
    def __init__(self, type_, nr):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.type_ = type_
        
        if type_ == 1:
            Sword_1.__init__(self)
        elif type_ == 2:
            Shield_1.__init__(self)

class Sword_1(Item):
    def __init__(self):
        self.image = img.load(item_list[0])
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_1"

class Shield_1(Item):
    def __init__(self):
        self.image = img.load(item_list[1])
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_1"


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
    global txt
    global txt_pos_x
    global txt_pos_y
    global shop_state
    global level_current
    global shop_i_attack
    global shop_i_health
    global shop_i_cost
    global shop_i_special
    global shop_i_bought

    if state == "Title":
        win.blit(background, (0,0))
        win.blit(Title, (0,0))
        if Title_selected == None:
            win.blit(play, (0,400))
            win.blit(options, (0,600))
            win.blit(exit_, (0,800))
        elif Title_selected == "play":
            win.blit(play_isselected, (0,400))
            win.blit(options, (0,600))
            win.blit(exit_, (0,800))
        elif Title_selected == "options":
            win.blit(play, (0,400))
            win.blit(options_isselected, (0,600))
            win.blit(exit_, (0,800))
        elif Title_selected == "exit":
            win.blit(play, (0,400))
            win.blit(options, (0,600))
            win.blit(exit_isselected, (0,800))

    
    elif state == "Options":
        win.blit(background, (0,0))
        if Options_selected == None:
            win.blit(go_back, (0,880))
            win.blit(toggle_music, (0,600))
        elif Options_selected == "go_back":
            win.blit(go_back_isselected, (0,880))
            win.blit(toggle_music, (0,600))
        elif Options_selected == "toggle_music":
            win.blit(go_back, (0,880))
            win.blit(toggle_music_isselected, (0,600))

    
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
        global txt
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
            win.blit(txt, (txt_pos_x, txt_pos_y))
                

    elif state == "Explore_update":
        objects_group = pygame.sprite.Group()
        Objects = level.get_objects(leveln, slice_)
        Objects_empty = False
        items_group.empty()
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


    elif state == "Shop_update":
        global inv
        global Items_empty
        if shop_state == "New":
            if level_current == 1:
                inv = lvl_1.get_shopinv("lvl_1", slice_)
                Items_empty = False
                if inv == "\n" or inv == None:
                    Items_empty = True
                if Items_empty == False:
                    a = 1
                    for i in inv:
                        nr = a
                        type_ = i
                        exec("item_{} = Item({}, {})".format(nr, type_, nr), globals())
                        exec("items_group.add(item_{})".format(nr), globals())
                        exec("item_{}.rect.x = {}".format(nr, (-57 + 114 * nr)))
                        exec("item_{}.rect.y = {}".format(nr, 114))
                        a += 1
                        
        state = "Shop"
    

    elif state == "Shop":
        if shop_state == "New":
            if level_current == 1:
                win.blit(shop_background, (0, 0))
                if Items_empty == False:
                    x_ = 1
                    for i in inv:
                        ex = """if item_{}.name not in shop_i_bought:
                                    exec("win.blit(item_{}.image, item_{}.rect)", globals())""".format(x_, x_, x_)
                        exec(ex, globals())
                        x_+=1
            txt1 = roboto_30.render(shop_i_attack, True, (255, 255, 255))
            txt2 = roboto_30.render(shop_i_health, True, (255, 255, 255))
            txt3 = roboto_30.render(shop_i_cost, True, (255, 255, 255))
            txt4 = roboto_30.render(shop_i_special, True, (255, 255, 255))
            txt5 = roboto_30.render(player_.money, True, (255, 255, 255))
            win.blit(txt1, (1570, 246))
            win.blit(txt2, (1570, 378))
            win.blit(txt3, (1570, 114))
            win.blit(txt4, (1570, 510))
            win.blit(txt5, (1570, 779))




        
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
    global run
    global inv
    global shop_i_attack
    global shop_i_health
    global shop_i_cost
    global shop_i_special
    global shop_i_selected
    global items_group
    global music_track_1
    global music_on
    global music_played
    global shop_i_bought
    x, y = pygame.mouse.get_pos()

    if state == "Title":
        if music_played == False:
            if music_on:
                pygame.mixer.music.play(-1)
                music_played = True
        else:
            if music_on == False:
                pygame.mixer.music.stop()
                music_played = False


        # Check which text is hovered over
        if x > 500 and x < 1200:
            if y > 400 and y < 600:
                Title_selected = "play"
            elif y > 600 and y < 800:
                Title_selected = "options"
            elif y > 800 and y < 1000:
                Title_selected = "exit"
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
                time.sleep(0.2)
            elif Title_selected == "options":
                state = "Options"
                Title_selected = None
                time.sleep(0.2)
            elif Title_selected == "exit":
                run = False
                

    elif state == "Options":
        # Check which text is hovered over
        if x > 500 and x < 1200:
            if y > 600 and y < 800:
                Options_selected = "toggle_music"
            elif y > 880:
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
                time.sleep(0.1)
            elif Options_selected == "toggle_music":
                if music_on == True:
                    music_on = False
                    pygame.mixer.music.stop()
                    time.sleep(0.1)
                else:
                    music_on = True
                    pygame.mixer.music.play(-1)
                    time.sleep(0.1)


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
                time.sleep(0.1)
            if Play_selected == "New_game":
                state = "Load_new"
                Play_selected = None


    elif state == "Load_new":
        global music_track_1
        music_track_1 = pygame.mixer.music.load("sound/music/ambience.mp3")
        came_from = None
        level = lvl_1
        leveln = "lvl_1"
        slice_ = level.get_startslice(leveln)
        pos = level.get_startpos(leveln)
        ex_x = pos[0]
        ex_y = pos[1]
        level_size = level.get_levelsize(leveln)
        if music_on:
            pygame.mixer.music.play(-1)

        state = "Explore_update"


    elif state == "Explore":
        if player_state == "normal":
            global vel
            vel = 10
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
                        if slice_ <= (level_size[1]**2)-level_size[1] and prev_failed_key != "down":
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


    elif state == "Shop":
        mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()

        # Mouse over exit
        if x >= 1022 and y <= 58:
            if mouse_1:
                state = "Explore_update"
        
        # Mouse over BUY
        if x >= 1582 and x < 1895 and y >= 950 and y < 1065:
            if mouse_1 and shop_i_cost != "n/a":
                if int(player_.money) - int(shop_i_cost) >= 0:
                    if shop_i_selected != "None":
                        shop_i_bought.append(shop_i_selected)
                        try:
                            player_.hp += int(shop_i_health)
                        except:
                            pass
                        try:
                            player_.attack += int(shop_i_attack)
                        except:
                            pass
                        shop_i_health = "n/a"
                        shop_i_attack = "n/a"
                        shop_i_special = "n/a"
                        shop_i_selected = "None"
                        player_.money = int(player_.money)
                        player_.money -= int(shop_i_cost)
                        player_.money = str(player_.money)
                        shop_i_cost = "n/a"


        for item in items_group:
            # Mouse over 
            if x > item.rect.x and x < item.rect.x + 95 and y > item.rect.y and y < item.rect.y + 95:
                if mouse_1:
                    item.clicked = True
                else:
                    item.clicked = False
            else:
                item.clicked = False
        
        x_ = 1
        for item in items_group:
            if item.clicked == True:
                if item.name not in shop_i_bought:
                    exec("item_{}.image = img.load('img/item/{}_selected.png')".format(x_, item.name), globals())
                    if item.type_ == 1:
                        # sword_1
                        shop_i_attack = "3"
                        shop_i_health = "n/a"
                        shop_i_cost = "10"
                        shop_i_special = "None"
                        shop_i_selected = "sword_1"
                    if item.type_ == 2:
                        # shield_1
                        shop_i_attack = "n/a"
                        shop_i_health = "50"
                        shop_i_cost = "5"
                        shop_i_special = "None"
                        shop_i_selected = "shield_1"
                else:
                    exec("item_{}.image = img.load('img/item/{}.png')".format(x_, item.name), globals())
            else:
                exec("item_{}.image = img.load('img/item/{}.png')".format(x_, item.name), globals())
            x_ += 1



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
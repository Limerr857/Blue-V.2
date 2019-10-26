
import pygame
from pygame import image as img
import time
import math
import random

pygame.init()


state = "Title"
win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
pygame.display.set_caption("Blue V.2")
clock = pygame.time.Clock()
Title_selected = None
Options_selected = None
Play_selected = None
Load_game_disabled = True
player_state = "normal"
object_list = [
    
               "img/obj/rock_1.png", "img/obj/rock_2.png", "img/obj/house_1.png", "img/NPC/tophat_happy.png", 
               "img/NPC/blacksmith_happy.png", "img/obj/forge_1.png", "img/obj/wall_1.png", "img/obj/wall_2.png", 
               "img/obj/wall_3.png", "img/obj/wall_4.png", "img/enemy_normal.png", "img/battle/zombie_1.png", 
               "img/obj/tree_1.png", "img/obj/tree_2.png", "img/obj/door_1.png", "img/NPC/sleepy_happy.png"
               
               ]
player_width = 100
player_height = 100
prev_failed_key = None
tophat_state = "Save"
blacksmith_state = "New"
sleepy_state = "Normal"
shop_state = "New"
level_current = 1
item_list = ["img/item/sword_1.png", "img/item/shield_1.png", "img/item/bow_1.png"]
battle_list = ["img/battle/enemy_battle.png", "img/battle/zombie_1.png", "img/battle/battle_door_1.png"]
battle_state = "normal"
battle_animation = "none"
battle_anim_time = 0
battle_menu = 1
battle_queue = []
battle_time = 0
battle_enemy_hp = 100
battle_bosses_killed = []
battle_prevx = 0
battle_prevy = 0

battle_unlocked_shot = False
battle_unlocked_fire = False
battle_unlocked_ice = False
battle_unlocked_heal = False
battle_unlocked_brave = False

shop_i_cost = "n/a"
shop_i_health = "n/a"
shop_i_attack = "n/a"
shop_i_special = "n/a"
shop_i_selected = "None"
shop_i_bought = []
shop_i_name = "n/a"

x,y = 0,0

pause_selected = None
pause_state = "normal"

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

battle_background_1 = img.load("img/battle_1.png").convert()
battle_background_1.set_alpha(None)
battle_menu_1 = img.load("img/battle/battle_menu_1.png").convert_alpha()
battle_menu_2 = img.load("img/battle/battle_menu_2.png").convert_alpha()
battle_menu_3 = img.load("img/battle/battle_menu_3.png").convert_alpha()
battle_bar_hp = img.load("img/battle/bar_hp.png").convert()
battle_bar_attacktime = img.load("img/battle/bar_attacktime.png").convert()
battle_won = img.load("img/battle/won_1.png").convert()
battle_lost = img.load("img/battle/lost_1.png").convert()
battle_lock = img.load("img/battle/locked_1.png").convert_alpha()
battle_retreated = img.load("img/battle/retreated_1.png").convert()
battle_start_1 = img.load("img/battle/start_1.png").convert()
battle_start_2 = img.load("img/battle/start_2.png").convert()
battle_start_3 = img.load("img/battle/start_3.png").convert()

pause_background = img.load("img/pause/pause_1.png").convert()
pause_paused = img.load("img/pause/paused.png").convert_alpha()
pause_main_menu = img.load("img/pause/main_menu.png").convert_alpha()
pause_exit_game = img.load("img/pause/exit_game.png").convert_alpha()
pause_return = img.load("img/pause/return.png").convert_alpha()
pause_save = img.load("img/pause/save.png").convert_alpha()
pause_main_menu_isselected = img.load("img/pause/main_menu_isselected.png").convert_alpha()
pause_exit_game_isselected = img.load("img/pause/exit_game_isselected.png").convert_alpha()
pause_return_isselected = img.load("img/pause/return_isselected.png").convert_alpha()
pause_save_isselected = img.load("img/pause/save_isselected.png").convert_alpha()
pause_sure = img.load("img/pause/sure.png")
pause_all_unsaved = img.load("img/pause/all_unsaved.png")
pause_go_back = img.load("img/pause/go_back.png")
pause_go_back_isselected = img.load("img/pause/go_back_isselected.png")
pause_continue_isselected = img.load("img/pause/continue_isselected.png")
pause_continue = img.load("img/pause/continue.png")

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
enemies_group = pygame.sprite.Group()


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


    def get_enemies(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = 0
        x = 0
        for line in f.readlines():
            if found == 5:
                return eval(line)
            elif "# slice {}".format(slice_) in line:
                found = 1
            elif found > 0:
                found += 1
            x +=1
    

    def get_spawns(self, name, slice_):
        f = open("levels/{}.txt".format(name), "r")
        found = 0
        x = 0
        for line in f.readlines():
            if found == 1:
                return eval(line)
            elif "# slice {} spawns".format(slice_) in line:
                found = 1
            x +=1
            
lvl_1 = Level()


class Player():
    global tophat_state
    global slice_
    global sleepy_state

    def __init__(self):
        self.image = img.load("img/player_normal.png").convert_alpha()
        self.image_battle = img.load("img/battle/player_battle.png").convert_alpha()
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.inventory = []
        # Temporary
        self.money = 15
        self.attack = 50
        # Not temporary
        self.hp = 100
        self.maxhp = 100
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
        global slice_
        global battle_enemy
        global battle_bosses_killed

        if pygame.sprite.spritecollideany(self, group1, pygame.sprite.collide_mask) != None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player_.rect.move_ip(0, vel)
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player_.rect.move_ip(vel, 0)
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player_.rect.move_ip(0, vel*-1)
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player_.rect.move_ip(vel*-1, 0)

        dist = 200
        for obj in NPC_group.sprites():
            center1 = obj.rect.center
            center2 = player_.rect.center

            diff_x = abs(center1[0] - center2[0])
            diff_y = abs(center1[1] - center2[1])

            # Pythagorean theorem
            if diff_x**2 + diff_y**2 <= dist**2:
                if obj.slice_ == slice_:
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
                            if keys[pygame.K_SPACE]:
                                # Player wants to enter the store.
                                state = "Shop_update"
                    elif obj.type == 15:
                        # Sleepy
                        if sleepy_state == "Normal":
                            txt = lvl_1.get_text("lvl_1", slice_)
                            txt = txt[0]
                            txt = roboto_15.render(txt, True, (0, 0, 0))
                            txt_pos_x = obj.rect.topleft[0]-63
                            txt_pos_y = obj.rect.topleft[1]-20
                    break
            else:
                txt = roboto_15.render("", False, (0, 0, 0))
                txt_pos_x = 0
                txt_pos_y = 0

        
        dist = 150
        for obj in enemies_group.sprites():
            if obj.type not in battle_bosses_killed:
                center1 = obj.rect.center
                center2 = player_.rect.center

                diff_x = abs(center1[0] - center2[0])
                diff_y = abs(center1[1] - center2[1])

                # Pythagorean theorem
                if diff_x**2 + diff_y**2 <= dist**2:
                    # Check so that the enemy is in the same frame
                    if obj.slice_ == slice_:
                        battle_enemy = obj.name
                        state = "Battle_update"

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
        elif type == 10:
            Boss_1.__init__(self)
        elif type == 11:
            Zombie_1.__init__(self)
        elif type == 12:
            Tree_1.__init__(self)
        elif type == 13:
            Tree_2.__init__(self)
        elif type == 14:
            Door_1.__init__(self)
        elif type == 15:
            NPC_sleepy_1.__init__(self)

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

class Boss_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[10])
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Boss_1"
        enemies_group.add(self)

class Zombie_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[11])
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_1"
        enemies_group.add(self)

class Tree_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[12])
        self.setup()
        self.rect = self.image.get_rect()

class Tree_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[13])
        self.setup()
        self.rect = self.image.get_rect()

class Door_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[14])
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Door_1"
        enemies_group.add(self)

class NPC_sleepy_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[15])
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)


class Item(pygame.sprite.Sprite):
    
    def __init__(self, type_, nr):
        pygame.sprite.Sprite.__init__(self)
        self.clicked = False
        self.type_ = type_
        
        if type_ == 1:
            Sword_1.__init__(self)
        elif type_ == 2:
            Shield_1.__init__(self)
        elif type_ == 3:
            Bow_1.__init__(self)
        elif type_ == 4:
            Sword_2.__init__(self)
        elif type_ == 5:
            Shield_2.__init__(self)

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

class Bow_1(Item):
    def __init__(self):
        self.image = img.load(item_list[2])
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "bow_1"
    
class Sword_2(Item):
    def __init__(self):
        self.image = img.load(item_list[0])
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_2"

class Shield_2(Item):
    def __init__(self):
        self.image = img.load(item_list[1])
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_2"


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
    global battle_state
    global music_played
    global battle_enemy
    global battle_enemy_img
    global battle_enemy_x
    global battle_enemy_y
    global battle_animation
    global battle_anim_time
    global battle_time
    global battle_menu
    global battle_enemy_hp
    global battle_enemy_maxhp
    global battle_enemy_attack
    global battle_enemy_gold
    global battle_gold_random
    global battle_bosses_killed
    global battle_prevx
    global battle_prevy
    global battle_prevgold
    global txt1
    global txt2
    global battle_unlocked_shot
    global battle_unlocked_fire
    global battle_unlocked_ice
    global battle_unlocked_heal
    global battle_unlocked_brave
    global battle_start_time
    global pause_selected
    global pause_state
    global Title_selected
    global run

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
                            string = """if object_{}.type not in battle_bosses_killed: win.blit(object_{}.image, ({}, {}))""".format(nr, nr, x, y)
                            exec(string)
                        z += 1
                    b += 1
            win.blit(txt, (txt_pos_x, txt_pos_y))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                state = "Pause"
                

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
                            if type_ not in battle_bosses_killed:
                                exec("object_{} = Object__({}, ({}, {}))".format(nr, type_, x, y), globals())
                                exec("objects_group.add(object_{})".format(nr), globals())
                                exec("object_{}.rect.x = {}".format(nr, x))
                                exec("object_{}.rect.y = {}".format(nr, y))
                                exec("object_{}.slice_ = {}".format(nr, slice_))
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
            txt5 = roboto_30.render(str(player_.money), True, (255, 255, 255))
            txt6 = roboto_30.render(shop_i_name, True, (255, 255, 255))
            win.blit(txt1, (1570, 246))
            win.blit(txt2, (1570, 378))
            win.blit(txt3, (1570, 114))
            win.blit(txt4, (1570, 510))
            win.blit(txt5, (1570, 779))
            win.blit(txt6, (1570, 642))


    elif state == "Battle":
        b_x, b_y = pygame.mouse.get_pos()
        if battle_state == "normal":
            battle_gold_random = 0
            if level_current == 1:
                win.blit(battle_background_1, [0, 0])
            if music_played == True:
                pygame.mixer.music.stop()
                music_played = False

            if battle_enemy_hp <= 0:
                battle_state = "Won"
            elif player_.hp <= 0:
                battle_state = "Lost"
            
            win.blit(player_.image_battle, player_.rect)
            win.blit(battle_enemy_img, (battle_enemy_x, battle_enemy_y))
            win.blit(battle_bar_attacktime, (581, 90))
            win.blit(battle_bar_hp, (581, 17))
            win.blit(battle_bar_hp, (996, 17))

            if battle_menu == 1:
                win.blit(battle_menu_1, (0, 0))
                win.blit(battle_menu_2, (1344, 0))
                # TODO LATER: Make stuff "select" when mouse is over like the menu
                
                # If button is locked
                if battle_unlocked_shot == False:
                    win.blit(battle_lock, (257, 137))
                if battle_unlocked_fire == False:
                    win.blit(battle_lock, (257, 246))
                if battle_unlocked_ice == False:
                    win.blit(battle_lock, (257, 355))
                if battle_unlocked_heal == False:
                    win.blit(battle_lock, (1601, 28))
                if battle_unlocked_brave == False:
                    win.blit(battle_lock, (1601, 137))
                #if battle_unlocked_placeholder == False:
                    #win.blit(battle_lock, (1601, 28))

                mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
                if mouse_1:
                    if b_x >= 13 and b_x <= 563:
                        # Mouse is probably over one of the buttons on the right.
                        if b_y >= 17 and b_y <= 117:
                            # Clicked on the Slash button
                            battle_queue.append("p_slash")
                        elif b_y >= 126 and b_y <= 226:
                            # Clicked on the Shot 
                            if battle_unlocked_shot:
                                battle_queue.append("p_shot")
                        elif b_y >= 235 and b_y <= 335:
                            # Clicked on the Fire button
                            if battle_unlocked_fire:
                                battle_queue.append("p_fire")
                        elif b_y >= 334 and b_y <= 444:
                            # Clicked on the ice button
                            if battle_unlocked_ice:
                                battle_queue.append("p_ice")
                    elif b_x >= 1344 and b_x <= 1920: 
                        # Mouse is probably over one of the buttons on the left.
                        if b_y >= 17 and b_y <= 117:
                            # Clicked on the Heal button
                            if battle_unlocked_heal:
                                battle_queue.append("p_heal")
                        elif b_y >= 126 and b_y <= 226:
                            # Clicked on the Brave button
                            if battle_unlocked_brave:
                                battle_queue.append("p_brave")
                        elif b_y >= 235 and b_y <= 335:
                            # Clicked on the PLACEHOLDER button
                            pass
                        elif b_y >= 334 and b_y <= 444:
                            # Clicked on the Retreat button
                            battle_menu = 2

            elif battle_menu == 2:
                # Retreat menu is up
                win.blit(battle_menu_1, (0, 0))
                win.blit(battle_menu_3, (1344, 0))
                mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()

                # If button is locked
                if battle_unlocked_shot == False:
                    win.blit(battle_lock, (257, 137))
                if battle_unlocked_fire == False:
                    win.blit(battle_lock, (257, 246))
                if battle_unlocked_ice == False:
                    win.blit(battle_lock, (257, 355))
                if battle_unlocked_heal == False:
                    win.blit(battle_lock, (1601, 28))
                if battle_unlocked_brave == False:
                    win.blit(battle_lock, (1601, 137))
                #if battle_unlocked_placeholder == False:
                    #win.blit(battle_lock, (1601, 28))

                if mouse_1:
                    if b_x >= 13 and b_x <= 563:
                        # Mouse is probably over one of the buttons on the right.
                        if b_y >= 17 and b_y <= 117:
                            # Clicked on the Slash button
                            battle_queue.append("p_slash")
                        elif b_y >= 126 and b_y <= 226:
                            # Clicked on the Shot button
                            if battle_unlocked_shot:
                                battle_queue.append("p_shot")
                        elif b_y >= 235 and b_y <= 335:
                            # Clicked on the Fire button
                            if battle_unlocked_fire:
                                battle_queue.append("p_fire")
                        elif b_y >= 334 and b_y <= 444:
                            # Clicked on the ice button
                            if battle_unlocked_ice:
                                battle_queue.append("p_ice")
                    elif b_x >= 1344 and b_x <= 1920: 
                        # Mouse is probably over one of the buttons on the left.
                        if b_y >= 126 and b_y <= 226:
                            # Clicked on the Yes, retreat button
                            battle_state = "Retreated"
                        elif b_y >= 235 and b_y <= 335:
                            # Clicked on the No button
                            battle_menu = 1

            # Main animation queue
            battle_speed = eval("{}.speed".format(battle_enemy))
            if battle_time > battle_speed:
                battle_time = 0
                if battle_enemy == "Boss_1":
                    battle_queue.append("e_slash")
                if battle_enemy == "Zombie_1":
                    battle_queue.append("e_slash")
                if battle_enemy == "Door_1":
                    temp = random.randint(1, 3)
                    if temp == 1 or temp == 2:
                        battle_queue.append("e_slash")
                    elif temp == 3:
                        battle_queue.append("e_shot")
            elif battle_time <= battle_speed:
                battle_time += 1
            else:
                print("Error")
            if battle_queue != []:
                battle_state = "anim"
                battle_animation = battle_queue[0]
                battle_queue.pop(0)

            # Attack time bar
            pygame.draw.rect(win, (200, 200, 200), (586, 95, round(battle_time/battle_speed*748-3), 10))

            # Player and Enemy HP (respectively)
            try:
                pygame.draw.rect(win, (abs(player_.hp/player_.maxhp*255-255), player_.hp/player_.maxhp*255, 0), (586, 22, round(player_.hp/player_.maxhp*333), 54))
                pygame.draw.rect(win, (abs(battle_enemy_hp/battle_enemy_maxhp*255-255), battle_enemy_hp/battle_enemy_maxhp*255, 0), (1001, 22, round(battle_enemy_hp/battle_enemy_maxhp*333), 54))
            except:
                pass


            if battle_enemy_hp <= 0:
                battle_state = "Won"
            elif player_.hp <= 0:
                battle_state = "Lost"


        if battle_state == "anim":

            if battle_animation == "e_slash":
                if battle_anim_time < 100:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(battle_enemy_attack/5*-1, battle_enemy_attack/5)
                    player_.hp -= battle_enemy_attack + temp
            elif battle_animation == "p_slash":
                if battle_anim_time < 100:
                    player_.rect.x += 2
                    battle_anim_time += 2
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    player_.rect.x -= 2
                    battle_anim_time += 2
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(player_.attack/5*-1, player_.attack/5)
                    battle_enemy_hp -= player_.attack + temp
            
            elif battle_animation == "e_shot":
                if battle_anim_time < 100:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(battle_enemy_attack/5*-1, battle_enemy_attack/5)
                    player_.hp -= battle_enemy_attack + temp
            elif battle_animation == "p_shot":
                if battle_anim_time < 100:
                    player_.rect.x += 2
                    battle_anim_time += 2
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    player_.rect.x -= 2
                    battle_anim_time += 2
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(player_.attack/5*-1, player_.attack/5)
                    battle_enemy_hp -= player_.attack + temp

            else:
                print('"{}" is not recognized as a battle_animation.'.format(battle_animation))


            
            if level_current == 1:
                win.blit(battle_background_1, [0, 0])
            if music_played == True:
                pygame.mixer.music.stop()
                music_played = False
            win.blit(player_.image_battle, player_.rect)
            win.blit(battle_enemy_img, (battle_enemy_x, battle_enemy_y))
            win.blit(battle_bar_attacktime, (581, 90))
            win.blit(battle_bar_hp, (581, 17))
            win.blit(battle_bar_hp, (996, 17))
    

            # Main animation queue
            battle_speed = eval("{}.speed".format(battle_enemy))
            if battle_time > battle_speed:
                battle_time = 0
                if battle_enemy == "Boss_1":
                    battle_queue.append("e_slash")
                if battle_enemy == "Zombie_1":
                    battle_queue.append("e_slash")
                if battle_enemy == "Door_1":
                    temp = random.randint(1, 3)
                    if temp == 1 or temp == 2:
                        battle_queue.append("e_slash")
                    elif temp == 3:
                        battle_queue.append("e_shot")
            elif battle_time <= battle_speed:
                battle_time += 1
            else:
                print("Error")

            # Attack time bar
            pygame.draw.rect(win, (200, 200, 200), (586, 95, round(battle_time/battle_speed*748-3), 10))

            # Player and Enemy HP (respectively)
            try:
                pygame.draw.rect(win, (abs(player_.hp/player_.maxhp*255-255), player_.hp/player_.maxhp*255, 0), 
                (586, 22, round(player_.hp/player_.maxhp*333), 54))
                pygame.draw.rect(win, (abs(battle_enemy_hp/battle_enemy_maxhp*255-255), battle_enemy_hp/battle_enemy_maxhp*255, 0), 
                (1001, 22, round(battle_enemy_hp/battle_enemy_maxhp*333), 54))
            except:
                pass


        if battle_state == "Won":
            win.blit(battle_won, (0, 0))
            if battle_gold_random == 0:
                battle_gold_random = random.randint(-1, 3)
            if player_.money + battle_enemy_gold + battle_gold_random == battle_prevgold + battle_enemy_gold + battle_gold_random:
                player_.money += battle_enemy_gold + battle_gold_random

                txt1 = roboto_120.render(str(battle_enemy_gold + battle_gold_random), True, (255, 255, 255))
                txt2 = roboto_120.render(str(round(player_.hp/player_.maxhp*100)), True, (255, 255, 255))
            win.blit(txt1, (900, 300))
            win.blit(txt2, (900, 700))
            player_.rect.x = battle_prevx
            player_.rect.y = battle_prevy

            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:
                if b_x >= 1695 and b_y >= 985:
                    # Clicked on Next button
                    dist = 300
                    for obj in enemies_group.sprites():
                        center1 = obj.rect.center
                        center2 = player_.rect.center

                        diff_x = abs(center1[0] - center2[0])
                        diff_y = abs(center1[1] - center2[1])

                        # Pythagorean theorem
                        if diff_x**2 + diff_y**2 <= dist**2:
                            # Check so that the enemy is in the same frame
                            if obj.slice_ == slice_:
                                enemies_group.remove(obj)
                                objects_group.remove(obj)
                                if obj.type not in battle_bosses_killed:
                                    battle_bosses_killed.append(obj.type)
                    state = "Explore_update"
                    battle_state = "normal"


        if battle_state == "Lost":
            win.blit(battle_lost, (0, 0))
            if battle_gold_random == 0:
                battle_gold_random = random.randint(1, 3)
            if player_.money - battle_enemy_gold * battle_gold_random == battle_prevgold - battle_enemy_gold * battle_gold_random:
                if player_.money - battle_enemy_gold * battle_gold_random >= 0:
                    player_.money -= battle_enemy_gold * battle_gold_random

                    txt1 = roboto_120.render(str(battle_enemy_gold * battle_gold_random), True, (255, 255, 255))
                else:
                    txt1 = roboto_120.render("all", True, (255, 255, 255))
                    player_.money = 0
                txt2 = roboto_120.render(str(round(battle_enemy_hp/battle_enemy_maxhp*100)), True, (255, 255, 255))
            win.blit(txt1, (900, 300))
            win.blit(txt2, (900, 700))
            slice_ = level.get_startslice(leveln)
            temp = level.get_startpos(leveln)
            player_.rect.x = temp[0]
            player_.rect.y = temp[1]

            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:
                if b_x >= 1695 and b_y >= 985:
                    # Clicked on Next button
                    state = "Explore_update"
                    battle_state = "normal"


        if battle_state == "Retreated":
            win.blit(battle_retreated, (0, 0))
            if battle_gold_random == 0:
                battle_gold_random = random.randint(1, 3)
            if player_.money - battle_enemy_gold * battle_gold_random == battle_prevgold - battle_enemy_gold * battle_gold_random:
                if player_.money - battle_enemy_gold + battle_gold_random >= 0:
                    player_.money -= battle_enemy_gold + battle_gold_random

                    txt1 = roboto_120.render(str(battle_enemy_gold + battle_gold_random), True, (255, 255, 255))
                else:
                    txt1 = roboto_120.render("all", True, (255, 255, 255))
                    player_.money = 0
                txt2 = roboto_120.render(str(round(battle_enemy_hp/battle_enemy_maxhp*100)), True, (255, 255, 255))
            win.blit(txt1, (900, 300))
            win.blit(txt2, (900, 700))
            slice_ = level.get_startslice(leveln)
            temp = level.get_startpos(leveln)
            player_.rect.x = temp[0]
            player_.rect.y = temp[1]

            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:
                if b_x >= 1695 and b_y >= 985:
                    # Clicked on Next button
                    state = "Explore_update"
                    battle_state = "normal"


        if battle_state == "Start":
            if battle_start_time <= 60:
                win.blit(battle_start_1, (0, 0))
            elif battle_start_time <= 120:
                win.blit(battle_start_2, (0, 0))
            elif battle_start_time <= 180:
                win.blit(battle_start_3, (0, 0))
            elif battle_start_time > 180:
                battle_state = "normal" 
            battle_start_time += 1
        

        if battle_state == "Start_update":
            battle_start_time = 0
            battle_state = "Start"


    elif state == "Battle_update":
        battle_prevx = player_.rect.x
        battle_prevy = player_.rect.y
        player_.rect.x = 50
        player_.rect.y = 650
        player_.hp = player_.maxhp
        battle_time = 0
        battle_prevgold = player_.money
        battle_menu = 1

        if battle_enemy == "Boss_1":
            battle_enemy_img = img.load(battle_list[0]).convert_alpha()
            battle_enemy_x = 1800
            battle_enemy_y = 650
            battle_enemy_hp = 100
            battle_enemy_maxhp = 100
            battle_enemy_attack = 15
            battle_enemy_gold = 100
        elif battle_enemy == "Zombie_1":
            battle_enemy_img = img.load(battle_list[1]).convert_alpha()
            battle_enemy_x = 1800
            battle_enemy_y = 650
            battle_enemy_hp = 100
            battle_enemy_maxhp = 100
            battle_enemy_attack = 15
            battle_enemy_gold = 10
        elif battle_enemy == "Door_1":
            battle_enemy_img = img.load(battle_list[2]).convert()
            battle_enemy_x = 1500
            battle_enemy_y = 600
            battle_enemy_hp = 400
            battle_enemy_maxhp = 400
            battle_enemy_attack = 30
            battle_enemy_gold = 20

        state = "Battle"
        battle_state = "Start_update"


    elif state == "Pause":
        if pause_state == "normal":
            win.blit(pause_background, (0, 0))
            win.blit(pause_paused, (0, 0))

            x, y = pygame.mouse.get_pos()

            if x > 804 and x < 1116 and y > 210 and y < 389:
                # Mouse over return
                pause_selected = "return"
            elif x > 697 and x < 1222 and y > 389 and y < 568:
                # Mouse over main menu
                pause_selected = "main_menu"
            elif x > 852 and x < 1068 and y > 568 and y < 747:
                # Mouse over save
                pause_selected = "save"
            elif x > 728 and x < 1191 and y > 901 and y < 1080:
                # Mouse over exit game
                pause_selected = "exit_game"
            else:
                pause_selected = None


            if pause_selected == None:
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
            elif pause_selected == "return":
                win.blit(pause_return_isselected, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
            elif pause_selected == "main_menu":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu_isselected, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
            elif pause_selected == "save":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save_isselected, (0, 568))
                win.blit(pause_exit_game, (0, 901))
            elif pause_selected == "exit_game":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game_isselected, (0, 901))
            
            # Check for clicks
            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:    
                if pause_selected == "return":
                    state = "Explore_update"
                elif pause_selected == "main_menu":
                    pause_state = "m_sure"
                elif pause_selected == "save":
                    state = "save"
                elif pause_selected == "exit_game":
                    pause_state = "e_sure"

        elif pause_state == "m_sure":
            win.blit(pause_background, (0, 0))
            win.blit(pause_sure, (0, 0))

            x, y = pygame.mouse.get_pos()

            if x > 1255 and x < 1625 and y > 568 and y < 747:
                # Mouse over go back
                pause_selected = "go_back"
            elif x > 269 and x < 691 and y > 568 and y < 747:
                # Mouse over continue
                pause_selected = "continue"
            else:
                pause_selected = None

            if pause_selected == None:
                win.blit(pause_continue, (0, 568))
                win.blit(pause_go_back, (960, 568))
            elif pause_selected == "go_back":
                win.blit(pause_continue, (0, 568))
                win.blit(pause_go_back_isselected, (960, 568))
            elif pause_selected == "continue":
                win.blit(pause_continue_isselected, (0, 568))
                win.blit(pause_go_back, (960, 568))
            
            # Check for clicks
            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:    
                if pause_selected == "go_back":
                    pause_state = "normal"
                    pause_selected = None
                if pause_selected == "continue":
                    state = "Title"
                    Title_selected = None
                    time.sleep(0.1)
            
        elif pause_state == "e_sure":
            win.blit(pause_background, (0, 0))
            win.blit(pause_sure, (0, 0))

            x, y = pygame.mouse.get_pos()

            if x > 1255 and x < 1625 and y > 568 and y < 747:
                # Mouse over go back
                pause_selected = "go_back"
            elif x > 269 and x < 691 and y > 568 and y < 747:
                # Mouse over continue
                pause_selected = "continue"
            else:
                pause_selected = None

            if pause_selected == None:
                win.blit(pause_continue, (0, 568))
                win.blit(pause_go_back, (960, 568))
            elif pause_selected == "go_back":
                win.blit(pause_continue, (0, 568))
                win.blit(pause_go_back_isselected, (960, 568))
            elif pause_selected == "continue":
                win.blit(pause_continue_isselected, (0, 568))
                win.blit(pause_go_back, (960, 568))
            
            # Check for clicks
            mouse_1, mouse_2, mouse_3 = pygame.mouse.get_pressed()
            if mouse_1:
                if pause_selected == "go_back":
                    pause_state = "normal"
                    pause_selected = None
                if pause_selected == "continue":
                    run = False

    elif state == "Pause_update":
        pause_state = "normal"
        state = "Pause"
        pause_selected = None


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
    global battle_enemy
    global shop_i_name
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
            vel = 15
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


            spawns = level.get_spawns(leveln, slice_)
            if spawns != None:
                for spawn in spawns:
                    x = 0
                    for i in spawn:
                        if x == 0:
                            temp1 = i
                        elif x == 1:
                            temp2 = random.randint(0, i) 
                            if temp2 == 1:
                                if temp1 == 11:
                                    battle_enemy = "Zombie_1"
                                    state = "Battle_update"
                        x += 1
                        

                        

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
                if player_.money - int(shop_i_cost) >= 0:
                    if shop_i_selected != "None":
                        shop_i_bought.append(shop_i_selected)
                        try:
                            if plater_.maxhp < int(shop_i_health):
                                player_.maxhp = int(shop_i_health)
                            else:
                                player_.maxhp += int(shop_i_health)/3
                        except:
                            pass
                        try:
                            if player_.attack < int(shop_i_attack):
                                player_.attack = int(shop_i_attack)
                            else:
                                player_.attack += int(shop_i_attack)/3
                        except:
                            pass
                        shop_i_health = "n/a"
                        shop_i_attack = "n/a"
                        shop_i_special = "n/a"
                        shop_i_selected = "None"
                        player_.money -= int(shop_i_cost)
                        shop_i_cost = "n/a"
                        shop_i_name = "n/a"


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
                        shop_i_attack = "30"
                        shop_i_health = "n/a"
                        shop_i_cost = "10"
                        shop_i_special = "None"
                        shop_i_selected = "sword_1"
                        shop_i_name = "Bronze Sword"
                    if item.type_ == 2:
                        # shield_1
                        shop_i_attack = "n/a"
                        shop_i_health = "50"
                        shop_i_cost = "5"
                        shop_i_special = "None"
                        shop_i_selected = "shield_1"
                        shop_i_name = "Bronze Shield"
                    if item.type_ == 3:
                        # bow_1
                        shop_i_attack = "15"
                        shop_i_health = "n/a"
                        shop_i_cost = "25"
                        shop_i_special = "None"
                        shop_i_selected = "bow_1"
                        shop_i_name = "Shortbow"
                    if item.type_ == 4:
                        # sword_2
                        shop_i_attack = "10"
                        shop_i_health = "n/a"
                        shop_i_cost = "50"
                        shop_i_special = "None"
                        shop_i_selected = "sword_2"
                        shop_i_name = "Iron Sword"
                    if item.type_ == 5:
                        # shield_2
                        shop_i_attack = "n/a"
                        shop_i_health = "150"
                        shop_i_cost = "70"
                        shop_i_special = "None"
                        shop_i_selected = "shield_2"
                        shop_i_name = "Iron Shield"
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
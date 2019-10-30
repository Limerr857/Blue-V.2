
import pygame
from pygame import image as img
import time
import math
import random

pygame.mixer.pre_init(44100, 16, 2, 4096)
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
               "img/obj/tree_1.png", "img/obj/tree_2.png", "img/obj/door_1.png", "img/NPC/sleepy_happy.png",
               "img/battle/demon_1.png", "img/battle/knight_1.png", "img/obj/knight_3.png", "img/obj/tower_1.png",
               "img/princess_1.png", "img/obj/level_exit_1.png", "img/obj/dark_wall_1.png", "img/obj/dark_wall_2_1.png",
               "img/obj/dark_wall_3.png", "img/obj/dark_wall_4_1.png", "img/obj/demon_2.png", "img/obj/zombie_2.png",
               "img/obj/dark_wall_2_2.png", "img/obj/dark_wall_4_2.png", "img/obj/tree_3.png", "img/obj/tree_4.png",
               "img/obj/tree_5.png", "img/obj/tree_6.png", "img/obj/forge_2.png", "img/obj/potion_1.png",
               "img/NPC/wizard_1.png", "img/battle/zombiewizard_1.png", "img/battle/zombiewizard_2.png", "img/battle/zombiewizard_3.png",
               "img/obj/fireplace_1.png", "img/princess_2.png", "img/obj/cactus_1.png", "img/obj/cactus_2.png",
               "img/obj/cactus_3.png", "img/obj/cactus_4.png", "img/obj/cactus_5.png", "img/obj/cactus_6.png",
               "img/obj/fireplace_2.png", "img/obj/temple_1_1.png", "img/obj/temple_1_2.png", "img/obj/temple_1_3.png", 
               "img/obj/temple_1_4.png", "img/obj/temple_1_5.png", "img/obj/temple_1_6.png", "img/obj/temple_1_7.png", 
               "img/obj/temple_1_8.png", "img/obj/temple_1_9.png", "img/battle/sandmonster_1.png", "img/battle/sandmonster_2.png", 
               "img/battle/slime_1.png", "img/obj/forge_3.png", "img/obj/potion_2.png", "img/obj/magic_1.png",
               "img/obj/sandwizard_1.png"

               ]
player_width = 100
player_height = 100
prev_failed_key = None
tophat_state = "Save"
blacksmith_state = "New"
sleepy_state = "Normal"
shop_state = "New"
level_current = 1
item_list = [
    
            "img/item/sword_1.png", "img/item/shield_1.png", "img/item/bow_1.png", "img/item/sword_3.png",
            "img/item/shield_3.png", "img/item/sword_4.png", "img/item/shield_4.png", "img/item/heal_1.png",
            "img/item/brave_1.png", "img/item/bow_2.png", "img/item/shield_5.png", "img/item/sword_5.png",
            "img/item/shield_6.png", "img/item/sword_6.png", "img/item/shield_7.png", "img/item/scroll_1.png"
            
            ]
battle_list = [

                "img/battle/enemy_battle.png", "img/battle/zombie_1.png", "img/battle/battle_door_1.png", "img/battle/demon_1.png",
                "img/battle/knight_1.png", "img/battle/knight_3.png", "img/battle/zombie_2.png", "img/battle/demon_2.png",
                "img/battle/zombiewizard_1.png", "img/battle/zombiewizard_2.png", "img/battle/zombiewizard_3.png", "img/battle/sandmonster_1.png", 
                "img/battle/sandmonster_2.png", "img/battle/slime_1.png", "img/battle/slime_2.png", "img/battle/slime_3.png", 
                "img/battle/slime_4.png", "img/battle/slime_5.png", "img/battle/sandwizard_1.png"
              
              ]
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
battle_effect_1 = 10000
battle_effect_2 = 10000
battle_effect_3 = 10000
battle_effect_4 = 10000
battle_effect_5 = 10000
battle_effect_6 = 10000
battle_effect_7 = 10000
battle_effect_8 = 10000
battle_effect_9 = 10000
battle_effect_10 = 10000
battle_effect_11 = 10000
battle_effect_12 = 10000

battle_effect_e1 = 10000
battle_effect_e2 = 10000
battle_effect_e3 = 10000
battle_effect_e4 = 10000
battle_effect_e5 = 10000
battle_effect_e6 = 10000
battle_effect_e7 = 10000
battle_effect_e8 = 10000
battle_effect_e9 = 10000
battle_effect_e10 = 10000
battle_effect_e11 = 10000
battle_effect_e12 = 10000

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
battle_background_2 = img.load("img/battle_2.png").convert()
battle_background_2.set_alpha(None)
battle_background_3 = img.load("img/battle_3.png").convert()
battle_background_3.set_alpha(None)
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
pause_sure = img.load("img/pause/sure.png").convert_alpha()
pause_all_unsaved = img.load("img/pause/all_unsaved.png").convert_alpha()
pause_go_back = img.load("img/pause/go_back.png").convert_alpha()
pause_go_back_isselected = img.load("img/pause/go_back_isselected.png").convert_alpha()
pause_continue_isselected = img.load("img/pause/continue_isselected.png").convert_alpha()
pause_continue = img.load("img/pause/continue.png").convert_alpha()
pause_reset_pos = img.load("img/pause/reset_pos.png").convert_alpha()
pause_reset_pos_isselected = img.load("img/pause/reset_pos_isselected.png").convert_alpha()

effect_fire = img.load("img/effect/effect_fire.png").convert_alpha()
effect_ice = img.load("img/effect/effect_ice.png").convert_alpha()
effect_heal = img.load("img/effect/effect_heal.png").convert_alpha()
effect_brave = img.load("img/effect/effect_brave.png").convert_alpha()

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

sound_fire = pygame.mixer.Sound("sound/effects/fire.wav")
sound_ice = pygame.mixer.Sound("sound/effects/ice.wav")
sound_heal = pygame.mixer.Sound("sound/effects/heal.wav")
sound_slash = pygame.mixer.Sound("sound/effects/slash.wav")
sound_shot = pygame.mixer.Sound("sound/effects/shot.wav")

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
                    # Prevents a bug from happening, if you get the error ""string index out of range" then lenghten this list.
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
lvl_2 = Level()
lvl_3 = Level()


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
        self.money = 99999
        self.attack = 9999
        # Not temporary
        self.potion_power = 100
        self.potion_healinv = 0
        self.potion_braveinv = 0
        self.brave = False
        self.iced = False
        self.ranged_attack = 0
        self.magic_attack = 30
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
        global level_current
        global came_from
        global level_size
        global music_track_1
        global level 
        global leveln 
        global pos


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

        dist = 250
        for obj in NPC_group.sprites():
            global slice_
            center1 = obj.rect.center
            center2 = player_.rect.center

            diff_x = abs(center1[0] - center2[0])
            diff_y = abs(center1[1] - center2[1])

            # Pythagorean theorem
            if diff_x**2 + diff_y**2 <= dist**2:
                if obj.slice_ == slice_:
                    if obj.type == 3:
                        if level_current == 1:
                            # Tophat
                            if tophat_state == "Save":
                                global txt
                                txt = lvl_1.get_text("lvl_1", slice_)
                                txt = txt[0]
                                txt = roboto_15.render(txt, True, (0, 0, 0))
                                txt_pos_x = obj.rect.topleft[0]-63
                                txt_pos_y = obj.rect.topleft[1]-100
                        elif level_current == 3:
                            # Tophat
                            if tophat_state == "Save":
                                txt = lvl_3.get_text("lvl_3", slice_)
                                txt = txt[0]
                                txt = roboto_15.render(txt, True, (0, 0, 0))
                                txt_pos_x = obj.rect.topleft[0]-45
                                txt_pos_y = obj.rect.topleft[1]-95

                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_SPACE]:
                                    # Player wants to enter the store.
                                    state = "Shop_update"
                    elif obj.type == 4:
                        # Blacksmith
                        if blacksmith_state == "New":
                            if level_current == 1:
                                txt = lvl_1.get_text("lvl_1", slice_)
                                txt = txt[1]
                                txt = roboto_15.render(txt, True, (0, 0, 0))
                                txt_pos_x = obj.rect.topleft[0]-63
                                txt_pos_y = obj.rect.topleft[1]-110

                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_SPACE]:
                                    # Player wants to enter the store.
                                    state = "Shop_update"
                            elif level_current == 2:
                                txt = lvl_2.get_text("lvl_2", slice_)
                                txt = txt[0]
                                txt = roboto_15.render(txt, True, (255, 255, 255))
                                txt_pos_x = 652
                                txt_pos_y = 705

                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_SPACE]:
                                    # Player wants to enter the store.
                                    state = "Shop_update"
                            elif level_current == 3:
                                txt = lvl_3.get_text("lvl_3", slice_)
                                txt = txt[0]
                                txt = roboto_15.render(txt, True, (0, 0, 0))
                                txt_pos_x = 215
                                txt_pos_y = 481

                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_SPACE]:
                                    # Player wants to enter the store.
                                    state = "Shop_update"
                    elif obj.type == 15:
                        if level_current == 1:
                            # Sleepy
                            if sleepy_state == "Normal":
                                txt = lvl_1.get_text("lvl_1", slice_)
                                txt = txt[0]
                                txt = roboto_15.render(txt, True, (0, 0, 0))
                                txt_pos_x = obj.rect.topleft[0]-63
                                txt_pos_y = obj.rect.topleft[1]-20
                    elif obj.type == 20:
                        if level_current == 1:
                            # Prinsess fake 1
                            txt = lvl_1.get_text("lvl_1", slice_)
                            txt = txt[0]
                            txt = roboto_15.render(txt, True, (0, 0, 0))
                            txt_pos_x = 570
                            txt_pos_y = 1000
                    elif obj.type == 36:
                        if level_current == 2:
                            # Wizard 1
                            txt = lvl_2.get_text("lvl_2", slice_)
                            txt = txt[0]
                            txt = roboto_15.render(txt, True, (255, 255, 255))
                            txt_pos_x = 820
                            txt_pos_y = 910

                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_SPACE]:
                                # Player wants to enter the store.
                                state = "Shop_update"
                        elif level_current == 3:
                            # Wizard 1
                            txt = lvl_3.get_text("lvl_3", slice_)
                            txt = txt[0]
                            txt = roboto_15.render(txt, True, (0, 0, 0))
                            txt_pos_x = 536
                            txt_pos_y = 374

                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_SPACE]:
                                # Player wants to enter the store.
                                state = "Shop_update"
                    elif obj.type == 45:
                        if level_current == 2:
                            # Fake princess 2
                            txt = lvl_2.get_text("lvl_2", slice_)
                            txt = txt[0]
                            txt = roboto_15.render(txt, True, (255, 255, 255))
                            txt_pos_x = 699
                            txt_pos_y = 844

                            keys = pygame.key.get_pressed()
                    break
            else:
                txt = roboto_15.render("", False, (0, 0, 0))
                txt_pos_x = 0
                txt_pos_y = 0

        
        dist = 200
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


        dist = 150
        for obj in group1.sprites():
            if obj.type == 21:
                center1 = obj.rect.center
                center2 = player_.rect.center

                diff_x = abs(center1[0] - center2[0])
                diff_y = abs(center1[1] - center2[1])
                if diff_x**2 + diff_y**2 <= dist**2:
                    if obj.slice_ == slice_:
                        # Object is exit, close and on the same slice.
                        level_current = 2
                        state = "Explore_update"
                        # HERE WE GO!
                        music_track_1 = pygame.mixer.music.load("sound/music/ambience.mp3")
                        came_from = None
                        level = lvl_2
                        leveln = "lvl_2"
                        slice_ = level.get_startslice(leveln)
                        pos = level.get_startpos(leveln)
                        ex_x = pos[0]
                        ex_y = pos[1]
                        player_.rect.x = pos[0]
                        player_.rect.y = pos[1]
                        level_size = level.get_levelsize(leveln)
                        if music_on:
                            pygame.mixer.music.play(-1)
            elif obj.type == 44:
                center1 = obj.rect.center
                center2 = player_.rect.center

                diff_x = abs(center1[0] - center2[0])
                diff_y = abs(center1[1] - center2[1])
                if diff_x**2 + diff_y**2 <= dist**2:
                    if obj.slice_ == slice_:
                        # Object is exit, player is close and on the same slice.
                        level_current = 3
                        state = "Explore_update"
                        # HERE WE GO!
                        music_track_1 = pygame.mixer.music.load("sound/music/ambience.mp3")
                        came_from = None
                        level = lvl_3
                        leveln = "lvl_3"
                        slice_ = level.get_startslice(leveln)
                        pos = level.get_startpos(leveln)
                        ex_x = pos[0]
                        ex_y = pos[1]
                        player_.rect.x = pos[0]
                        player_.rect.y = pos[1]
                        level_size = level.get_levelsize(leveln)
                        if music_on:
                            pygame.mixer.music.play(-1)
                        



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
        elif type == 16:
            Demon_1.__init__(self)
        elif type == 17:
            Knight_1.__init__(self)
        elif type == 18:
            Knight_3.__init__(self)
        elif type == 19:
            Tower_1.__init__(self)
        elif type == 20:
            NPC_princess_1.__init__(self)
        elif type == 21:
            Level_exit_1.__init__(self)
        elif type == 22:
            Dark_wall_1.__init__(self)
        elif type == 23:
            Dark_wall_2_1.__init__(self)
        elif type == 24:
            Dark_wall_3.__init__(self)
        elif type == 25:
            Dark_wall_4_1.__init__(self)
        elif type == 26:
            Demon_2.__init__(self)
        elif type == 27:
            Zombie_2_1.__init__(self)
        elif type == 28:
            Dark_wall_2_2.__init__(self)
        elif type == 29:
            Dark_wall_4_2.__init__(self)
        elif type == 30:
            Tree_3.__init__(self)
        elif type == 31:
            Tree_4.__init__(self)
        elif type == 32:
            Tree_5.__init__(self)
        elif type == 33:
            Tree_6.__init__(self)
        elif type == 34:
            Forge_2.__init__(self)
        elif type == 35:
            Potion_1.__init__(self)
        elif type == 36:
            NPC_wizard_1.__init__(self)
        elif type == 37:
            Zombiewizard_1.__init__(self)
        elif type == 38:
            Zombiewizard_2.__init__(self)
        elif type == 39:
            Zombiewizard_3.__init__(self)
        elif type == 40:
            Zombie_2_2.__init__(self)
        elif type == 41:
            Zombie_2_3.__init__(self)
        elif type == 42:
            Zombie_2_4.__init__(self)
        elif type == 43:
            Zombie_2_5.__init__(self)
        elif type == 44:
            Fireplace_1.__init__(self)
        elif type == 45:
            NPC_princess_2.__init__(self)
        elif type == 46:
            Cactus_1.__init__(self)
        elif type == 47:
            Cactus_2.__init__(self)
        elif type == 48:
            Cactus_3.__init__(self)
        elif type == 49:
            Cactus_4.__init__(self)
        elif type == 50:
            Cactus_5.__init__(self)
        elif type == 51:
            Cactus_6.__init__(self)
        elif type == 52:
            Fireplace_2.__init__(self)
        elif type == 53:
            Temple_1_1.__init__(self)
        elif type == 54:
            Temple_1_2.__init__(self)
        elif type == 55:
            Temple_1_3.__init__(self)
        elif type == 56:
            Temple_1_4.__init__(self)
        elif type == 57:
            Temple_1_5.__init__(self)
        elif type == 58:
            Temple_1_6.__init__(self)
        elif type == 59:
            Temple_1_7.__init__(self)
        elif type == 60:
            Temple_1_8.__init__(self)
        elif type == 61:
            Temple_1_9.__init__(self)
        elif type == 62:
            Sandmonster_1.__init__(self)
        elif type == 63:
            Sandmonster_2.__init__(self)
        elif type == 64:
            Slime_1.__init__(self)
        elif type == 65:
            Forge_3.__init__(self)
        elif type == 66:
            Potion_2.__init__(self)
        elif type == 67:
            Magic_1.__init__(self)
        elif type == 68:
            Sandwizard_1.__init__(self)

    def setup(self):
        self.size = self.image.get_rect().size
        self.mask = pygame.mask.from_surface(self.image)

class Rock_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[0]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Rock_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[1]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class House_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[2]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class NPC_tophat_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[3]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class NPC_blacksmith_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[4]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Forge_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[5]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Wall_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[6]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Wall_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[7]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Wall_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[8]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Wall_4(Object__):
    def __init__(self):
        self.image = img.load(object_list[9]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Boss_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[10]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Boss_1"
        enemies_group.add(self)

class Zombie_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[11]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_1"
        enemies_group.add(self)

class Tree_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[12]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Tree_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[13]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Door_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[14]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Door_1"
        enemies_group.add(self)

class NPC_sleepy_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[15]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Demon_1(Object__):
    speed = 400 # 6.66 seconds
    def __init__(self):
        self.image = img.load(object_list[16]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Demon_1"
        enemies_group.add(self)

class Knight_1(Object__):
    speed = 350 # 5.83 seconds
    def __init__(self):
        self.image = img.load(object_list[17]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Knight_1"
        enemies_group.add(self)

class Knight_3(Object__):
    speed = 300 # 3.33 seconds
    def __init__(self):
        self.image = img.load(object_list[18]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Knight_3"
        enemies_group.add(self)

class Tower_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[19]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class NPC_princess_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[20]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Level_exit_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[21]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Dark_wall_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[22]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Dark_wall_2_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[23]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Dark_wall_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[24]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Dark_wall_4_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[25]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Demon_2(Object__):
    speed = 200 # 3.33 seconds
    def __init__(self):
        self.image = img.load(object_list[26]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Demon_2"
        enemies_group.add(self)

class Zombie_2_1(Object__):
    speed = 240 # 4 seconds
    def __init__(self):
        self.image = img.load(object_list[27]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_2_1"
        enemies_group.add(self)

class Dark_wall_2_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[28]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Dark_wall_4_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[29]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Tree_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[30]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Tree_4(Object__):
    def __init__(self):
        self.image = img.load(object_list[31]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Tree_5(Object__):
    def __init__(self):
        self.image = img.load(object_list[32]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Tree_6(Object__):
    def __init__(self):
        self.image = img.load(object_list[33]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Forge_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[34]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Potion_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[35]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class NPC_wizard_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[36]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Zombiewizard_1(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[37]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombiewizard_1"
        enemies_group.add(self)

class Zombiewizard_2(Object__):
    speed = 300 # 5 seconds
    def __init__(self):
        self.image = img.load(object_list[38]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombiewizard_2"
        enemies_group.add(self)

class Zombiewizard_3(Object__):
    speed = 280
    def __init__(self):
        self.image = img.load(object_list[39]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombiewizard_3"
        enemies_group.add(self)

class Zombie_2_2(Object__):
    speed = 240 # 4 seconds
    def __init__(self):
        self.image = img.load(object_list[27]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_2_1"
        enemies_group.add(self)

class Zombie_2_3(Object__):
    speed = 240 # 4 seconds
    def __init__(self):
        self.image = img.load(object_list[27]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_2_1"
        enemies_group.add(self)

class Zombie_2_4(Object__):
    speed = 240 # 4 seconds
    def __init__(self):
        self.image = img.load(object_list[27]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_2_1"
        enemies_group.add(self)

class Zombie_2_5(Object__):
    speed = 240 # 4 seconds
    def __init__(self):
        self.image = img.load(object_list[27]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Zombie_2_1"
        enemies_group.add(self)

class Fireplace_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[40]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class NPC_princess_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[41]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        NPC_group.add(self)

class Cactus_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[42]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Cactus_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[43]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Cactus_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[44]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Cactus_4(Object__):
    def __init__(self):
        self.image = img.load(object_list[45]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Cactus_5(Object__):
    def __init__(self):
        self.image = img.load(object_list[46]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Cactus_6(Object__):
    def __init__(self):
        self.image = img.load(object_list[47]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Fireplace_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[48]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[49]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[50]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[51]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_4(Object__):
    def __init__(self):
        self.image = img.load(object_list[52]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_5(Object__):
    def __init__(self):
        self.image = img.load(object_list[53]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_6(Object__):
    def __init__(self):
        self.image = img.load(object_list[54]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_7(Object__):
    def __init__(self):
        self.image = img.load(object_list[55]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_8(Object__):
    def __init__(self):
        self.image = img.load(object_list[56]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Temple_1_9(Object__):
    def __init__(self):
        self.image = img.load(object_list[57]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Sandmonster_1(Object__):
    speed = 300 
    def __init__(self):
        self.image = img.load(object_list[58]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Sandmonster_1"
        enemies_group.add(self)

class Sandmonster_2(Object__):
    speed = 400 
    def __init__(self):
        self.image = img.load(object_list[59]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Sandmonster_2"
        enemies_group.add(self)

class Slime_1(Object__):
    speed = 400 
    def __init__(self):
        self.image = img.load(object_list[60]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Slime_1"
        enemies_group.add(self)

class Forge_3(Object__):
    def __init__(self):
        self.image = img.load(object_list[61]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Potion_2(Object__):
    def __init__(self):
        self.image = img.load(object_list[62]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Magic_1(Object__):
    def __init__(self):
        self.image = img.load(object_list[63]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()

class Sandwizard_1(Object__):
    speed = 300 # 3.33 seconds
    def __init__(self):
        self.image = img.load(object_list[64]).convert_alpha()
        self.setup()
        self.rect = self.image.get_rect()
        self.name = "Sandwizard_1"
        enemies_group.add(self)



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
        elif type_ == 6:
            Sword_3.__init__(self)
        elif type_ == 7:
            Shield_3.__init__(self)
        elif type_ == 8:
            Sword_4.__init__(self)
        elif type_ == 9:
            Shield_4.__init__(self)
        elif type_ == 10:
            Heal_1.__init__(self)
        elif type_ == 11:
            Brave_1.__init__(self)
        elif type_ == 12:
            Bow_2.__init__(self)
        elif type_ == 13:
            Shield_5.__init__(self)
        elif type_ == 14:
            Sword_5.__init__(self)
        elif type_ == 15:
            Shield_6.__init__(self)
        elif type_ == 16:
            Sword_6.__init__(self)
        elif type_ == 17:
            Shield_7.__init__(self)
        elif type_ == 18:
            Scroll_1.__init__(self)
        elif type_ == 19:
            Scroll_2.__init__(self)
        elif type_ == 20:
            Scroll_3.__init__(self)
        elif type_ == 21:
            Scroll_4.__init__(self)
        elif type_ == 22:
            Scroll_5.__init__(self)


class Sword_1(Item):
    def __init__(self):
        self.image = img.load(item_list[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_1"

class Shield_1(Item):
    def __init__(self):
        self.image = img.load(item_list[1]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_1"

class Bow_1(Item):
    def __init__(self):
        self.image = img.load(item_list[2]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "bow_1"
    
class Sword_2(Item):
    def __init__(self):
        self.image = img.load(item_list[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_2"

class Shield_2(Item):
    def __init__(self):
        self.image = img.load(item_list[1]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_2"

class Sword_3(Item):
    def __init__(self):
        self.image = img.load(item_list[3]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_3"

class Shield_3(Item):
    def __init__(self):
        self.image = img.load(item_list[4]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_3"

class Sword_4(Item):
    def __init__(self):
        self.image = img.load(item_list[5]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_4"

class Shield_4(Item):
    def __init__(self):
        self.image = img.load(item_list[6]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_4"

class Heal_1(Item):
    def __init__(self):
        self.image = img.load(item_list[7]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "heal_1"

class Brave_1(Item):
    def __init__(self):
        self.image = img.load(item_list[8]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "brave_1"

class Bow_2(Item):
    def __init__(self):
        self.image = img.load(item_list[9]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "bow_2"

class Shield_5(Item):
    def __init__(self):
        self.image = img.load(item_list[10]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_5"

class Sword_5(Item):
    def __init__(self):
        self.image = img.load(item_list[11]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_5"

class Shield_6(Item):
    def __init__(self):
        self.image = img.load(item_list[12]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_6"

class Sword_6(Item):
    def __init__(self):
        self.image = img.load(item_list[13]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "sword_6"

class Shield_7(Item):
    def __init__(self):
        self.image = img.load(item_list[14]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "shield_7"

class Scroll_1(Item):
    def __init__(self):
        self.image = img.load(item_list[15]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "scroll_1"

class Scroll_2(Item):
    def __init__(self):
        self.image = img.load(item_list[15]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "scroll_2"

class Scroll_3(Item):
    def __init__(self):
        self.image = img.load(item_list[15]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "scroll_3"

class Scroll_4(Item):
    def __init__(self):
        self.image = img.load(item_list[15]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "scroll_4"

class Scroll_5(Item):
    def __init__(self):
        self.image = img.load(item_list[15]).convert_alpha()
        self.rect = self.image.get_rect()
        self.size = self.rect.size
        self.name = "scroll_5"


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
    global battle_effect_1
    global battle_effect_2
    global battle_effect_3
    global battle_effect_4
    global battle_effect_5
    global battle_effect_6
    global battle_effect_7
    global battle_effect_8
    global battle_effect_9
    global battle_effect_10
    global battle_effect_11
    global battle_effect_12
    global battle_potions_healleft
    global battle_effect_e1
    global battle_effect_e2
    global battle_effect_e3
    global battle_effect_e4
    global battle_effect_e5
    global battle_effect_e6
    global battle_effect_e7
    global battle_effect_e8
    global battle_effect_e9
    global battle_effect_e10
    global battle_effect_e11
    global battle_effect_e12
    global battle_enemy_brave
    global battle_enemy_iced
    global battle_queue
    global music_bplayed
    global music_track_5
    global Items_empty

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
                            string = "if object_{}.type not in battle_bosses_killed: win.blit(object_{}.image, ({}, {}))".format(nr, nr, x, y)
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
                            else:
                                exec("object_{} = Object__({}, ({}, {}))".format(nr, type_, x, y), globals())
                                exec("objects_group.add(object_{})".format(nr), globals())
                                exec("object_{}.rect.x = {}".format(nr, 10000))
                                exec("object_{}.rect.y = {}".format(nr, 10000))
                                exec("object_{}.slice_ = {}".format(nr, slice_))
                        z += 1
                    a += 1
                
                x_ += 1


        # Checks if any object is overlapping player, not perfect but almost works

        # Disabled bc it breaks stuff on level 2

        # for i in objects_group:
        #     if i.rect.colliderect(player_):
        #         if came_from == "-x":
        #             slice_ -= 1
        #             prev_failed_key = "right"
        #             state = "Explore_update_again"
        #         elif came_from == "x":
        #             slice_ += 1
        #             prev_failed_key = "left"
        #             state = "Explore_update_again"
        #         elif came_from == "-y":
        #             slice_ -= level_size[0]
        #             prev_failed_key = "down"
        #             state = "Explore_update_again"
        #         elif came_from == "y":
        #             slice_ += level_size[0]
        #             prev_failed_key = "up"
        #             state = "Explore_update_again"
        #     break
            
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
            elif level_current == 2:
                inv = lvl_2.get_shopinv("lvl_2", slice_)
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
            elif level_current == 3:
                inv = lvl_3.get_shopinv("lvl_3", slice_)
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
            if level_current == 1 or level_current == 2 or level_current == 3:
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
                win.blit(battle_background_1, (0, 0))
            elif level_current == 2:
                win.blit(battle_background_2, (0, 0))
            elif level_current == 3:
                win.blit(battle_background_3, (0, 0))
            if battle_enemy_hp <= 0:
                battle_state = "Won"
            elif player_.hp <= 0:
                battle_state = "Lost"
            
            win.blit(player_.image_battle, player_.rect)
            win.blit(battle_enemy_img, (battle_enemy_x, battle_enemy_y))
            win.blit(battle_bar_attacktime, (581, 90))
            win.blit(battle_bar_hp, (581, 17))
            win.blit(battle_bar_hp, (996, 17))

            if player_.potion_healinv <= 0:
                battle_potions_healleft = False
            else:
                battle_potions_healleft = True

            if player_.potion_braveinv <= 0:
                battle_potions_braveleft = False
            else:
                battle_potions_braveleft = True

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
                if battle_potions_healleft == False and battle_unlocked_heal == True:
                    win.blit(battle_lock, (1601, 28))
                if battle_potions_braveleft == False and battle_unlocked_brave == True:
                    win.blit(battle_lock, (1601, 137))

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
                            if battle_unlocked_heal and battle_potions_healleft:
                                battle_queue.append("p_heal")
                        elif b_y >= 126 and b_y <= 226:
                            # Clicked on the Brave button
                            if battle_unlocked_brave and battle_potions_braveleft:
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
            if battle_enemy_iced == True:
                battle_speed /= 2
            if battle_enemy_brave == True:
                battle_speed *= 2
            if battle_time > battle_speed:
                battle_time = 0
                if battle_enemy == "Boss_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Zombie_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Door_1":
                    temp = random.randint(1, 3)
                    if temp == 1 or temp == 2:
                        battle_queue.append("e_slash")
                    elif temp == 3:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Demon_1":
                    temp = random.randint(1, 6)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Knight_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Knight_3":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    elif temp == 6:
                        battle_queue.append("e_ice")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Demon_2":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Zombie_2_1":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    elif temp < 8:
                        battle_queue.append("e_shot")
                    elif temp == 10:
                        battle_queue.append("e_brave")
                    else:
                        battle_queue.append("e_ice")
                elif battle_enemy == "Zombiewizard_1":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_fire")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Zombiewizard_2":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_ice")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Zombiewizard_3":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_shot")
                    else:
                        battle_queue.append("e_brave")
                elif battle_enemy == "Sandmonster_1":
                    temp = random.randint(1, 10)
                    if temp < 7:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Sandmonster_2":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Slime_1":
                    temp = random.randint(1, 10)
                    if temp < 10:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Sandwizard_1":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_fire")
                    elif temp < 8:
                        battle_queue.append("e_ice")
                    elif temp < 10:
                        battle_queue.append("e_heal")
                    else:
                        battle_queue.append("e_brave")    
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
                if battle_anim_time == 0:
                    sound_slash.play()
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time < 100:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(battle_enemy_attack/5*-1), round(battle_enemy_attack/5))
                    player_.hp -= battle_enemy_attack + temp
            elif battle_animation == "p_slash":
                if battle_anim_time == 0:
                    sound_slash.play()
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time < 100:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time >= 100 and battle_anim_time <= 200:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x -= 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x -= 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x -= 1
                        battle_anim_time += 1
                elif battle_anim_time > 200:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(player_.attack/5*-1), round(player_.attack/5))
                    battle_enemy_hp -= player_.attack + temp
            
            elif battle_animation == "e_shot":
                if battle_anim_time == 0:
                    sound_shot.play()
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time < 25:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time >= 25 and battle_anim_time <= 50:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                elif battle_anim_time > 50:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(battle_enemy_attack/5*-1), round(battle_enemy_attack/5))
                    player_.hp -= battle_enemy_attack/4 + temp
            elif battle_animation == "p_shot":
                if battle_anim_time == 0:
                    sound_shot.play()
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time < 25:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time >= 25 and battle_anim_time <= 50:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x -= 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x -= 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x -= 1
                        battle_anim_time += 1
                elif battle_anim_time > 50:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(player_.ranged_attack/5*-1), round(player_.ranged_attack/5))
                    battle_enemy_hp -= player_.ranged_attack + temp
            
            elif battle_animation == "e_fire":
                if battle_anim_time == 0:
                    sound_fire.play()
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time < 50:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                    if battle_anim_time % 10 == 0:
                        battle_effect_e1 = random.randint(-15, 95)
                        battle_effect_e2 = random.randint(-15, 95)
                        battle_effect_e3 = random.randint(-15, 95)
                        battle_effect_e4 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                    # Fire effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_e1 = random.randint(-15, 95)
                        battle_effect_e2 = random.randint(-15, 95)
                        battle_effect_e3 = random.randint(-15, 95)
                        battle_effect_e4 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(battle_enemy_attack/5*-1), round(battle_enemy_attack/5))
                    player_.hp -= battle_enemy_attack + temp
                    battle_effect_e1 = 10000
                    battle_effect_e2 = 10000
                    battle_effect_e3 = 10000
                    battle_effect_e4 = 10000
            elif battle_animation == "p_fire":
                if battle_anim_time == 0:
                    sound_fire.play()
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time < 50:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                    if battle_anim_time % 10 == 0:
                        battle_effect_1 = random.randint(-15, 95)
                        battle_effect_2 = random.randint(-15, 95)
                        battle_effect_3 = random.randint(-15, 95)
                        battle_effect_4 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x -= 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x -= 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x -= 1
                        battle_anim_time += 1
                    # Fire effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_1 = random.randint(-15, 95)
                        battle_effect_2 = random.randint(-15, 95)
                        battle_effect_3 = random.randint(-15, 95)
                        battle_effect_4 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(player_.magic_attack/5*-1), round(player_.magic_attack/5))
                    battle_enemy_hp -= player_.magic_attack + temp
                    battle_effect_1 = 10000
                    battle_effect_2 = 10000
                    battle_effect_3 = 10000
                    battle_effect_4 = 10000

            elif battle_animation == "e_ice":
                if battle_anim_time == 0:
                    sound_ice.play()
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                elif battle_anim_time < 50:
                    battle_enemy_x -= 2
                    battle_anim_time += 2
                    if battle_anim_time % 10 == 0:
                        battle_effect_e5 = random.randint(-15, 95)
                        battle_effect_e6 = random.randint(-15, 95)
                        battle_effect_e7 = random.randint(-15, 95)
                        battle_effect_e8 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    battle_enemy_x += 2
                    battle_anim_time += 2
                    # ice effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_e5 = random.randint(-15, 95)
                        battle_effect_e6 = random.randint(-15, 95)
                        battle_effect_e7 = random.randint(-15, 95)
                        battle_effect_e8 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(battle_enemy_attack/5*-1), round(battle_enemy_attack/5))
                    player_.hp -= battle_enemy_attack + temp / 2
                    battle_effect_e5 = 10000
                    battle_effect_e6 = 10000
                    battle_effect_e7 = 10000
                    battle_effect_e8 = 10000
                    player_.iced = True
            elif battle_animation == "p_ice":
                if battle_anim_time == 0:
                    sound_ice.play()
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                elif battle_anim_time < 50:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x += 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x += 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x += 1
                        battle_anim_time += 1
                    if battle_anim_time % 10 == 0:
                        battle_effect_5 = random.randint(-15, 95)
                        battle_effect_6 = random.randint(-15, 95)
                        battle_effect_7 = random.randint(-15, 95)
                        battle_effect_8 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    if player_.brave == False and player_.iced == False or player_.brave == True and player_.iced == True:
                        player_.rect.x -= 2
                        battle_anim_time += 2
                    elif player_.brave == True:
                        player_.rect.x -= 4
                        battle_anim_time += 4
                    elif player_.iced == True:
                        player_.rect.x -= 1
                        battle_anim_time += 1
                    # Fire effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_5 = random.randint(-15, 95)
                        battle_effect_6 = random.randint(-15, 95)
                        battle_effect_7 = random.randint(-15, 95)
                        battle_effect_8 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(player_.magic_attack/5*-1), round(player_.magic_attack/5))
                    battle_enemy_hp -= player_.magic_attack + temp / 2
                    battle_effect_5 = 10000
                    battle_effect_6 = 10000
                    battle_effect_7 = 10000
                    battle_effect_8 = 10000
                    battle_enemy_iced = True

            elif battle_animation == "e_heal":
                if battle_anim_time == 0:
                    sound_heal.play()
                    battle_anim_time += 2
                elif battle_anim_time < 50:
                    battle_anim_time += 2
                    if battle_anim_time % 10 == 0:
                        battle_effect_e9 = random.randint(-15, 95)
                        battle_effect_e10 = random.randint(-15, 95)
                        battle_effect_e11 = random.randint(-15, 95)
                        battle_effect_e12 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    battle_anim_time += 2
                    # heal effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_e9 = random.randint(-15, 95)
                        battle_effect_e10 = random.randint(-15, 95)
                        battle_effect_e11 = random.randint(-15, 95)
                        battle_effect_e12 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(battle_enemy_attack/5*-1), round(battle_enemy_attack/5))
                    if battle_enemy_hp + battle_enemy_attack + temp <= battle_enemy_maxhp:
                        battle_enemy_hp += battle_enemy_attack + temp
                    else:
                        battle_enemy_hp = battle_enemy_maxhp
                    battle_effect_e9 = 10000
                    battle_effect_e10 = 10000
                    battle_effect_e11 = 10000
                    battle_effect_e12 = 10000
            elif battle_animation == "p_heal":
                if battle_anim_time == 0:
                    sound_heal.play()
                    battle_anim_time += 2
                elif battle_anim_time < 50:
                    battle_anim_time += 2
                    if battle_anim_time % 10 == 0:
                        battle_effect_9 = random.randint(-15, 95)
                        battle_effect_10 = random.randint(-15, 95)
                        battle_effect_11 = random.randint(-15, 95)
                        battle_effect_12 = random.randint(-15, 95)
                elif battle_anim_time >= 50 and battle_anim_time <= 100:
                    battle_anim_time += 2
                    # Heal effect
                    if battle_anim_time % 10 == 0:
                        battle_effect_9 = random.randint(-15, 95)
                        battle_effect_10 = random.randint(-15, 95)
                        battle_effect_11 = random.randint(-15, 95)
                        battle_effect_12 = random.randint(-15, 95)
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    temp = random.randint(round(player_.potion_power/5*-1), round(player_.potion_power/5))
                    if player_.hp + player_.potion_power + temp <= player_.maxhp:
                        player_.hp += player_.potion_power + temp
                    else:
                        player_.hp = player_.maxhp
                    player_.potion_healinv -= 1
                    battle_effect_9 = 10000
                    battle_effect_10 = 10000
                    battle_effect_11 = 10000
                    battle_effect_12 = 10000

            elif battle_animation == "e_brave":
                if battle_anim_time == 0:
                    sound_heal.play()
                    battle_anim_time += 2
                elif battle_anim_time >= 1 and battle_anim_time <= 100:
                    battle_anim_time += 2
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    battle_enemy_brave = True
            elif battle_animation == "p_brave":
                if battle_anim_time == 0:
                    sound_heal.play()
                    battle_anim_time += 2
                elif battle_anim_time >= 1 and battle_anim_time <= 100:
                    battle_anim_time += 2
                elif battle_anim_time > 100:
                    battle_anim_time = 0
                    battle_animation = "none"
                    battle_state = "normal"
                    player_.brave = True
                    player_.potion_braveinv -= 1

            else:
                print('"{}" is not recognized as a battle_animation.'.format(battle_animation))


            
            if level_current == 1:
                win.blit(battle_background_1, [0, 0])
            if level_current == 2:
                win.blit(battle_background_2, [0, 0])
            elif level_current == 3:
                win.blit(battle_background_3, (0, 0))
            
            if battle_animation == "p_brave":
                win.blit(effect_brave, (13, 611))
            elif battle_animation == "e_brave":
                win.blit(effect_brave, (1307, 611))


            win.blit(player_.image_battle, player_.rect)
            win.blit(battle_enemy_img, (battle_enemy_x, battle_enemy_y))
            win.blit(battle_bar_attacktime, (581, 90))
            win.blit(battle_bar_hp, (581, 17))
            win.blit(battle_bar_hp, (996, 17))
            win.blit(effect_fire, (battle_enemy_x + battle_effect_1, battle_enemy_y + battle_effect_2))
            win.blit(effect_fire, (battle_enemy_x + battle_effect_3, battle_enemy_y + battle_effect_4))

            win.blit(effect_ice, (battle_enemy_x + battle_effect_5, battle_enemy_y + battle_effect_6))
            win.blit(effect_ice, (battle_enemy_x + battle_effect_7, battle_enemy_y + battle_effect_8))

            win.blit(effect_heal, (player_.rect.x + battle_effect_9, player_.rect.y + battle_effect_10))
            win.blit(effect_heal, (player_.rect.x + battle_effect_11, player_.rect.y + battle_effect_12))

            win.blit(effect_fire, (player_.rect.x + battle_effect_e1, player_.rect.y + battle_effect_e2))
            win.blit(effect_fire, (player_.rect.x + battle_effect_e3, player_.rect.y + battle_effect_e4))

            win.blit(effect_ice, (player_.rect.x + battle_effect_e5, player_.rect.y + battle_effect_e6))
            win.blit(effect_ice, (player_.rect.x + battle_effect_e7, player_.rect.y + battle_effect_e8))

            win.blit(effect_heal, (battle_enemy_x + battle_effect_e9, battle_enemy_y + battle_effect_e10))
            win.blit(effect_heal, (battle_enemy_x + battle_effect_e11, battle_enemy_y + battle_effect_e12))
    

            # Main animation queue
            battle_speed = eval("{}.speed".format(battle_enemy))
            if battle_time > battle_speed:
                battle_time = 0
                if battle_enemy == "Boss_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Zombie_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Door_1":
                    temp = random.randint(1, 3)
                    if temp == 1 or temp == 2:
                        battle_queue.append("e_slash")
                    elif temp == 3:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Demon_1":
                    temp = random.randint(1, 6)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Knight_1":
                    battle_queue.append("e_slash")
                elif battle_enemy == "Knight_3":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    elif temp == 6:
                        battle_queue.append("e_ice")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Demon_2":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Zombie_2_1":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    elif temp < 8:
                        battle_queue.append("e_shot")
                    elif temp == 10:
                        battle_queue.append("e_brave")
                    else:
                        battle_queue.append("e_ice")
                elif battle_enemy == "Zombiewizard_1":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_fire")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Zombiewizard_2":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_ice")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Zombiewizard_3":
                    temp = random.randint(1, 10)
                    if temp < 9:
                        battle_queue.append("e_shot")
                    else:
                        battle_queue.append("e_brave")
                elif battle_enemy == "Sandmonster_1":
                    temp = random.randint(1, 10)
                    if temp < 7:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Sandmonster_2":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_fire")
                elif battle_enemy == "Slime_1":
                    temp = random.randint(1, 10)
                    if temp < 10:
                        battle_queue.append("e_slash")
                    else:
                        battle_queue.append("e_shot")
                elif battle_enemy == "Sandwizard_1":
                    temp = random.randint(1, 10)
                    if temp < 6:
                        battle_queue.append("e_fire")
                    elif temp < 8:
                        battle_queue.append("e_ice")
                    elif temp < 10:
                        battle_queue.append("e_heal")
                    else:
                        battle_queue.append("e_brave")    
                
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
            if music_on and music_bplayed == False:
                pygame.mixer.music.stop()
                music_track_5 = pygame.mixer.music.load("sound/music/ambience.mp3")
                pygame.mixer.music.play(-1)
                music_bplayed = True
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
            if music_on and music_bplayed == False:
                pygame.mixer.music.stop()
                music_track_5 = pygame.mixer.music.load("sound/music/ambience.mp3")
                pygame.mixer.music.play(-1)
                music_bplayed = True
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
            if music_on and music_bplayed == False:
                pygame.mixer.music.stop()
                music_track_5 = pygame.mixer.music.load("sound/music/ambience.mp3")
                pygame.mixer.music.play(-1)
                music_bplayed = True
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
        player_.rect.x = 250
        player_.rect.y = 750
        player_.hp = player_.maxhp
        battle_time = 0
        battle_prevgold = player_.money
        battle_menu = 1
        battle_enemy_brave = False
        battle_enemy_iced = False
        player_.brave = False
        player_.iced = False
        battle_queue = []
        music_bplayed = False

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
            battle_enemy_y = 750
            battle_enemy_hp = 100
            battle_enemy_maxhp = 100
            battle_enemy_attack = 15
            battle_enemy_gold = 10
        elif battle_enemy == "Door_1":
            battle_enemy_img = img.load(battle_list[2]).convert()
            battle_enemy_x = 1500
            battle_enemy_y = 600
            battle_enemy_hp = 200
            battle_enemy_maxhp = 200
            battle_enemy_attack = 30
            battle_enemy_gold = 20
        elif battle_enemy == "Demon_1":
            battle_enemy_img = img.load(battle_list[3]).convert_alpha()
            battle_enemy_x = 1800
            battle_enemy_y = 750
            battle_enemy_hp = 250
            battle_enemy_maxhp = 250
            battle_enemy_attack = 35
            battle_enemy_gold = 20
        elif battle_enemy == "Knight_1":
            battle_enemy_img = img.load(battle_list[4]).convert_alpha()
            battle_enemy_x = 1800
            battle_enemy_y = 750
            battle_enemy_hp = 350
            battle_enemy_maxhp = 350
            battle_enemy_attack = 30
            battle_enemy_gold = 30
        elif battle_enemy == "Knight_3":
            battle_enemy_img = img.load(battle_list[5]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 420
            battle_enemy_maxhp = 420
            battle_enemy_attack = 40
            battle_enemy_gold = 200
        elif battle_enemy == "Zombie_2_1":
            battle_enemy_img = img.load(battle_list[6]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 800
            battle_enemy_maxhp = 800
            battle_enemy_attack = 120
            battle_enemy_gold = 500
        elif battle_enemy == "Demon_2":
            battle_enemy_img = img.load(battle_list[7]).convert_alpha()
            battle_enemy_x = 1650
            battle_enemy_y = 600
            battle_enemy_hp = 1500
            battle_enemy_maxhp = 1500
            battle_enemy_attack = 200
            battle_enemy_gold = 2000
        elif battle_enemy == "Zombiewizard_1":
            battle_enemy_img = img.load(battle_list[8]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 500
            battle_enemy_maxhp = 500
            battle_enemy_attack = 40
            battle_enemy_gold = 60
        elif battle_enemy == "Zombiewizard_2":
            battle_enemy_img = img.load(battle_list[9]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 500
            battle_enemy_maxhp = 500
            battle_enemy_attack = 40
            battle_enemy_gold = 60
        elif battle_enemy == "Zombiewizard_3":
            battle_enemy_img = img.load(battle_list[10]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 650
            battle_enemy_maxhp = 650
            battle_enemy_attack = 70
            battle_enemy_gold = 80
        elif battle_enemy == "Sandmonster_1":
            battle_enemy_img = img.load(battle_list[11]).convert_alpha()
            battle_enemy_x = 1800
            battle_enemy_y = 750
            battle_enemy_hp = 800
            battle_enemy_maxhp = 800
            battle_enemy_attack = 80
            battle_enemy_gold = 200
        elif battle_enemy == "Sandmonster_2":
            battle_enemy_img = img.load(battle_list[12]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 1000
            battle_enemy_maxhp = 1000
            battle_enemy_attack = 100
            battle_enemy_gold = 300
        elif battle_enemy == "Slime_1":
            # Randomizes the skin used
            temp = random.randint(1, 5)
            battle_enemy_img = img.load(battle_list[12+temp]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 1300
            battle_enemy_maxhp = 1300
            battle_enemy_attack = 150
            battle_enemy_gold = 500
        elif battle_enemy == "Sandwizard_1":
            battle_enemy_img = img.load(battle_list[18]).convert_alpha()
            battle_enemy_x = 1700
            battle_enemy_y = 650
            battle_enemy_hp = 1300
            battle_enemy_maxhp = 1300
            battle_enemy_attack = 150
            battle_enemy_gold = 500


        state = "Battle"
        battle_state = "Start_update"
        music_track_2 = pygame.mixer.music.load("sound/music/battle.mp3")
        if music_on:
            pygame.mixer.music.play(-1)


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
            elif x > 0 and x < 446 and y > 998 and y < 1080:
                # Mouse over reset pos
                pause_selected = "reset_pos"
            else:
                pause_selected = None


            if pause_selected == None:
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
                win.blit(pause_reset_pos, (0, 998))
            elif pause_selected == "return":
                win.blit(pause_return_isselected, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
                win.blit(pause_reset_pos, (0, 998))
            elif pause_selected == "main_menu":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu_isselected, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
                win.blit(pause_reset_pos, (0, 998))
            elif pause_selected == "save":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save_isselected, (0, 568))
                win.blit(pause_exit_game, (0, 901))
                win.blit(pause_reset_pos, (0, 998))
            elif pause_selected == "exit_game":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game_isselected, (0, 901))
                win.blit(pause_reset_pos, (0, 998))
            elif pause_selected == "reset_pos":
                win.blit(pause_return, (0, 210))
                win.blit(pause_main_menu, (0, 389))
                win.blit(pause_save, (0, 568))
                win.blit(pause_exit_game, (0, 901))
                win.blit(pause_reset_pos_isselected, (0, 998))
            
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
                elif pause_selected == "reset_pos":
                    state = "Explore_update"
                    pos = level.get_startpos(leveln)
                    ex_x = pos[0]
                    ex_y = pos[1]
                    player_.rect.x = pos[0]
                    player_.rect.y = pos[1]
                    slice_ = level.get_startslice(leveln)

        elif pause_state == "m_sure":
            music_track_2 = pygame.mixer.music.load("sound/music/menu.mp3")
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
                    music_played = False
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
    global battle_unlocked_shot
    global battle_unlocked_brave
    global battle_unlocked_fire
    global battle_unlocked_heal
    global battle_unlocked_ice
    global level_current
    global leveln
    global level
    global slice_
    global pos
    global ex_x 
    global ex_y
    global level_size
    global x
    global y

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
        # TODO: REMOVE THESE, temporary!!!!
        level = lvl_3
        leveln = "lvl_3"
        level_current = 3
        # not
        slice_ = level.get_startslice(leveln)
        pos = level.get_startpos(leveln)
        ex_x = pos[0]
        ex_y = pos[1]
        player_.rect.x = pos[0]
        player_.rect.y = pos[1]
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
                                elif temp1 == 16:
                                    battle_enemy = "Demon_1"
                                elif temp1 == 17:
                                    battle_enemy = "Knight_1"
                                elif temp1 == 37:
                                    battle_enemy = "Zombiewizard_1"
                                elif temp1 == 38:
                                    battle_enemy = "Zombiewizard_2"
                                elif temp1 == 39:
                                    battle_enemy = "Zombiewizard_3"
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
                        if shop_i_selected != "heal_1" and shop_i_selected != "brave_1":
                            shop_i_bought.append(shop_i_selected)
                        else:
                            if shop_i_selected == "heal_1":
                                battle_unlocked_heal = True
                            elif shop_i_selected == "brave_1":
                                battle_unlocked_brave = True
                        try:
                            if plater_.maxhp < int(shop_i_health):
                                player_.maxhp = int(shop_i_health)
                            else:
                                player_.maxhp += int(shop_i_health)/3
                        except:
                            pass
                        try:
                            if shop_i_selected != "bow_1" and shop_i_selected != "bow_2":
                                if player_.attack < int(shop_i_attack):
                                    player_.attack = int(shop_i_attack)
                                else:
                                    player_.attack += int(shop_i_attack)/3
                            elif shop_i_selected == "bow_1":
                                if player_.ranged_attack < int(shop_i_attack):
                                    player_.ranged_attack = int(shop_i_attack)
                                else:
                                    player_.ranged_attack += int(shop_i_attack)/3
                            elif shop_i_selected == "bow_2":
                                if player_.ranged_attack < int(shop_i_attack):
                                    player_.ranged_attack = int(shop_i_attack)
                                else:
                                    player_.ranged_attack += int(shop_i_attack)/3
                        except:
                            pass
                        if shop_i_selected == "bow_1":
                            battle_unlocked_shot = True
                        if shop_i_selected == "bow_2":
                            battle_unlocked_shot = True
                        elif shop_i_selected == "heal_1":
                            player_.potion_healinv += 1
                        elif shop_i_selected == "brave_1":
                            player_.potion_braveinv += 1

                        elif shop_i_selected == "scroll_1":
                            battle_unlocked_fire = True
                        elif shop_i_selected == "scroll_2":
                            battle_unlocked_ice = True
                        elif shop_i_selected == "scroll_3":
                            player_.magic_attack *= 2
                        elif shop_i_selected == "scroll_4":
                            player_.magic_attack *= 3
                        elif shop_i_selected == "scroll_5":
                            player_.magic_attack *= 4

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
                    elif item.type_ == 2:
                        # shield_1
                        shop_i_attack = "n/a"
                        shop_i_health = "150"
                        shop_i_cost = "5"
                        shop_i_special = "None"
                        shop_i_selected = "shield_1"
                        shop_i_name = "Bronze Shield"
                    elif item.type_ == 3:
                        # bow_1
                        shop_i_attack = "15"
                        shop_i_health = "n/a"
                        shop_i_cost = "30"
                        shop_i_special = "None"
                        shop_i_selected = "bow_1"
                        shop_i_name = "Shortbow"
                    elif item.type_ == 4:
                        # sword_2
                        shop_i_attack = "50"
                        shop_i_health = "n/a"
                        shop_i_cost = "50"
                        shop_i_special = "None"
                        shop_i_selected = "sword_2"
                        shop_i_name = "Iron Sword"
                    elif item.type_ == 5:
                        # shield_2
                        shop_i_attack = "n/a"
                        shop_i_health = "200"
                        shop_i_cost = "70"
                        shop_i_special = "None"
                        shop_i_selected = "shield_2"
                        shop_i_name = "Iron Shield"
                    elif item.type_ == 6:
                        # sword_3
                        shop_i_attack = "90"
                        shop_i_health = "n/a"
                        shop_i_cost = "100"
                        shop_i_special = "None"
                        shop_i_selected = "sword_3"
                        shop_i_name = "Gold Dagger"
                    elif item.type_ == 7:
                        # shield_3
                        shop_i_attack = "n/a"
                        shop_i_health = "350"
                        shop_i_cost = "110"
                        shop_i_special = "None"
                        shop_i_selected = "shield_3"
                        shop_i_name = "Gold Shield"
                    elif item.type_ == 8:
                        # sword_4
                        shop_i_attack = "150"
                        shop_i_health = "n/a"
                        shop_i_cost = "200"
                        shop_i_special = "None"
                        shop_i_selected = "sword_4"
                        shop_i_name = "Magic Sword"
                    elif item.type_ == 9:
                        # shield_4
                        shop_i_attack = "n/a"
                        shop_i_health = "600"
                        shop_i_cost = "200"
                        shop_i_special = "None"
                        shop_i_selected = "shield_4"
                        shop_i_name = "Magic Shield"
                    elif item.type_ == 10:
                        # heal_1
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "200"
                        shop_i_special = "Heals you."
                        shop_i_selected = "heal_1"
                        shop_i_name = "Health Potion"
                    elif item.type_ == 11:
                        # brave_1
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "200"
                        shop_i_special = "Faster attack speed."
                        shop_i_selected = "brave_1"
                        shop_i_name = "Brave Potion"
                    elif item.type_ == 12:
                        # bow_2
                        shop_i_attack = "30"
                        shop_i_health = "n/a"
                        shop_i_cost = "140"
                        shop_i_special = "None"
                        shop_i_selected = "bow_2"
                        shop_i_name = "Recurve Bow"
                    elif item.type_ == 13:
                        # shield_5
                        shop_i_attack = "n/a"
                        shop_i_health = "800"
                        shop_i_cost = "300"
                        shop_i_special = "None"
                        shop_i_selected = "shield_5"
                        shop_i_name = "Ultra Shield"
                    elif item.type_ == 14:
                        # sword_5
                        shop_i_attack = "200"
                        shop_i_health = "n/a"
                        shop_i_cost = "300"
                        shop_i_special = "None"
                        shop_i_selected = "sword_5"
                        shop_i_name = "Ultra Sword"
                    elif item.type_ == 15:
                        # shield_6
                        shop_i_attack = "n/a"
                        shop_i_health = "1000"
                        shop_i_cost = "600"
                        shop_i_special = "None"
                        shop_i_selected = "shield_6"
                        shop_i_name = "Cursed Shield"
                    elif item.type_ == 16:
                        # sword_6
                        shop_i_attack = "400"
                        shop_i_health = "n/a"
                        shop_i_cost = "600"
                        shop_i_special = "None"
                        shop_i_selected = "sword_6"
                        shop_i_name = "Cursed Sword"
                    elif item.type_ == 17:
                        # shield_7
                        shop_i_attack = "n/a"
                        shop_i_health = "2000"
                        shop_i_cost = "1000"
                        shop_i_special = "None"
                        shop_i_selected = "shield_7"
                        shop_i_name = "Force field"
                    elif item.type_ == 18:
                        # scroll_1
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "300"
                        shop_i_special = "Cast fire on your enemies."
                        shop_i_selected = "scroll_1"
                        shop_i_name = "Scroll of fire"
                    elif item.type_ == 19:
                        # scroll_2
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "300"
                        shop_i_special = "Cast ice on your enemies."
                        shop_i_selected = "scroll_2"
                        shop_i_name = "Scroll of ice"
                    elif item.type_ == 20:
                        # scroll_3
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "400"
                        shop_i_special = "Double your magic."
                        shop_i_selected = "scroll_3"
                        shop_i_name = "Scroll of doubling"
                    elif item.type_ == 21:
                        # scroll_4
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "600"
                        shop_i_special = "Triple your magic."
                        shop_i_selected = "scroll_4"
                        shop_i_name = "Scroll of tripling"
                    elif item.type_ == 22:
                        # scroll_5
                        shop_i_attack = "n/a"
                        shop_i_health = "n/a"
                        shop_i_cost = "900"
                        shop_i_special = "Quadruple your magic."
                        shop_i_selected = "scroll_5"
                        shop_i_name = "Scroll of Quadrupling"
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
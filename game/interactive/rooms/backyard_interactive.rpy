init python:
    class LocationBackyard(Location):
        title="backyard"
        def scene(self,elements):
            elements.append("images/sadie_house/backyard/bg_backyard_1{dark}.jpg")
            
            
            if konami_story == 11 and char_at("konamipool","pool") and not is_talking("konamipool"):
                elements.append([(493, 570),"images/sadie_house/backyard/charbutton_konami5_{state}.png", "konami_pool_inter", "*^"])
            
            
            elements.append([(625, 638),"images/sadie_house/backyard/inter_poolchair1{dark}_{state}.png", "$blocked$", None])
            
            
            elements.append([(1094, 404),"images/sadie_house/backyard/inter_backdoor1{dark}_{state}.png", "goto_hallwayf1", "*>"])
            
            
            elements.append([(197, 551),"images/sadie_house/backyard/inter_lawnmower{dark}_{state}.png", "backyard_lawnmower_inter", "*^"])
            
            
            elements.append([(1587, 904),"images/sadie_house/backyard/inter_sidewalk{dark}_{state}.png", "$blocked$", None])
            
            
            elements.append([(0, 732),"images/sadie_house/backyard/inter_steppingstones{dark}_{state}.png", "goto_backyard2", "*>"])
            
            
            if wallpaper_unlocked6 == False:
                elements.append([(166, 419),"images/sadie_house/hidden wallpaper/hidden_wallpaper_6.png", "hidden_wallpaper_6_inter", "*^"])
















default loc_backyard = LocationBackyard()

label goto_backyard:
    call set_location ("loc_backyard") from _call_set_location_1
    show screen main_hud_icon

    return

label hidden_wallpaper_6_inter:
    $ wallpaper_unlocked6 = True
    $ renpy.notify("Wallpaper 6 unlocked")
    return

label backyard_lawnmower_inter:
    if chores_unlocked == False:
        l_mc ". . . ?"
        jump goto_backyard
        return

    if now(["morning"]):
        menu:
            "Work now ?" if True:
                l_mc "Alright, let's get to it !"
                jump lawnmore_start
                return
            "Not yet" if True:


                jump goto_backyard
                return
    l_mc ". . nah don't want to mow the lawn at the moment. Do it during the morning "

    return

label lawnmore_start:
    hide screen main_hud_icon
    show black with dissolve
    scene chores_mowing_01
    hide black
    pause
    play sound "music/lawnmoww.mp3"
    show chores_mowing_02 with dissolve
    pause
    hide chores_mowing_02
    show chores_mowing_02 with dissolve
    stop sound fadeout 1.0
    pause
    hide chores_mowing_02
    $ random_cash_range = renpy.random.randint(3,6)
    $ main_mc.got_cash(random_cash_range)

    show screen money_earn_display with Dissolve(.3)


    $ now.advance()
    show screen main_hud_icon
    jump goto_backyard

label konami_pool_inter:
    if konami_story == 11:
        jump konami_event_2
        return

    ". . . ."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc


































































































init python:
    class LocationBackyard2(Location):
        title="backyard 2"
        def scene(self,elements):
            elements.append("images/sadie_house/backyard 2/bg_backyard_2{dark}.jpg") 
            
            if konami_story == 1 and char_at("konami","treeh") == True:
                elements.append([(1752, 177),"images/sadie_house/backyard 2/charbutton_konami1_{state}.png", "backyard2_konami", "*^"])
            
            
            
            elements.append([(1085, 418),"images/sadie_house/backyard 2/inter_bush{dark}_{state}.png", "konami_backyard_inter", "*>"])
            
            
            elements.append([(1537, 308),"images/sadie_house/backyard 2/inter_ropeladder{dark}_{state}.png", "treehouse_inter", "*>"])
            
            
            elements.append([(1405, 186),"images/sadie_house/backyard 2/inter_pigeon_day.png", "pigeon_inter", "*^"])
            
            
            
            if go_back_btn == True:
                elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_backyard", "*>"])
            
            
            if wallpaper_unlocked7 == False:
                elements.append([(136, 584),"images/sadie_house/hidden wallpaper/hidden_wallpaper_7.png", "hidden_wallpaper_7_inter", "*^"])
            
            
            if wallpaper_unlocked8 == False:
                elements.append([(1653, 95),"images/sadie_house/hidden wallpaper/hidden_wallpaper_8.png", "hidden_wallpaper_8_inter", "*^"])

default loc_backyard2 = LocationBackyard2()

label goto_backyard2:
    call set_location ("loc_backyard2") from _call_set_location_5
    show screen main_hud_icon

    if konami_story == 12:
        jump konami_event_2z
        return
    return


label backyard2_konami:
    hide screen main_hud_icon
    if konami_discovered == False:
        l_mc "(Is that someone up in the treehouse?)"
        l_mc "(Who the heck is that creep ? I don't recongnize that person from here at all)"
        l_mc "(I should handle this as cool as I can. Can't afford to get into more trouble after what happened at school)"
        l_mc "(I'll go up there to see who it is but I have to keep calm)"
        $ konami_discovered = True
        jump goto_backyard2
        return
    elif True:
        l_mc "Let's go up there"
        jump goto_backyard2
        return

    jump goto_backyard2
    return

label pigeon_inter:
    l_mc "A pigeon . . ?"
    l_mc "He has a scarf"
    return

label hidden_wallpaper_7_inter:
    $ wallpaper_unlocked7 = True
    $ renpy.notify("Wallpaper 7 unlocked")
    return

label hidden_wallpaper_8_inter:
    $ wallpaper_unlocked8 = True
    $ renpy.notify("Wallpaper 8 unlocked")
    return

label treehouse_inter:
    if konami_story == 7 and now(["morning", "afternoon"]):
        jump konami_event_1
        return
    if konami_story == 16 and now(["saturday", "sunday"]) and now(["morning"]):
        jump konami_event_4
        return

    jump goto_treehouse
    return

label konami_backyard_inter:
    if konami_entrance_access == True:
        jump goto_konami_backyard
        return
    elif True:
        l_mc "Let me see. . wait"
        l_mc "Is that my neighbor's backyard ?"
        l_mc "Let's not go in there yet."
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

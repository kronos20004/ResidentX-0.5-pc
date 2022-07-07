init python:
    class LocationTreehouse(Location):
        title="Treehouse"
        def scene(self,elements):
            elements.append("images/sadie_house/tree_house/bg_treehouse{dark}.jpg") 
            
            
            if konami_treehouse == True:
                if char_at("konami","treeh") and not is_talking("konami"):
                    if konami_story == 1:
                        elements.append([(953, 388),"images/sadie_house/tree_house/charbutton_konami2{dark}_{state}.png", "konami_intro_ch", "*^"])
                    else:
                        elements.append([(1123, 320),"images/sadie_house/tree_house/charbutton_konami3{dark}.png", "konami_treehouse_inter", "*^"])
            
            
            
            elements.append([(554, 225),"images/sadie_house/tree_house/inter_bbgun{dark}_{state}.png", "$blocked$","@^BB GUN" ])
            
            
            elements.append([(0, 0),"images/sadie_house/tree_house/inter_ropeladder2{dark}_{state}.png", "goto_backyard2", "*>"])
            
            
            if wallpaper_unlocked4 == False:
                elements.append([(447, 907),"images/sadie_house/hidden wallpaper/hidden_wallpaper_4.png", "hidden_wallpaper_4_inter", "*^"])


default loc_treehouse = LocationTreehouse()

label goto_treehouse:
    call set_location ("loc_treehouse") from _call_set_location_3
    show screen main_hud_icon

    if konami_story == 8:
        jump konami_event1z
        return

    if konami_chap1_done == True and konami_story == 4:
        jump backyard2_konami_chap1d
        return

    return

label konami_treehouse_inter:
    if konami_story == 4:
        jump konami_chapter_one
        return
    elif True:
        l_mc ". . . ."
        return
    jump goto_treehouse
    return


label backyard2_konami_chap1d:
    hide charbutton_konami3
    hide screen main_hud_icon

    show lucas normal pose4 default at left with Dissolve(.3)
    show konami normal pose blush default_downt at right with Dissolve(.3)
    l_konami "ok bye! I think I hear my mom calling me so better go!"

    show lucas normal pose4 default_talk at left
    show konami normal pose blush default_down at right
    l_mc "what? I didn’t hear anything"

    show lucas normal pose4 default at left
    show konami normal pose default_talk at right
    l_konami "see ya!"

    $ konami_story += 1
    $ konami_talking = False
    $ now.advance()
    hide konami normal pose default_talk with moveoutright
    show lucas normal pose4 default_talk at left
    l_mc "sure, I’ll catch you lat . . ."

    show lucas normal pose4 what at left
    pause

    show lucas normal pose4 default_talk at left
    l_mc "what the hell was that? She just booked it out of here."
    l_mc "was it something I said?"

    hide lucas normal pose4 default_talk with moveoutright
    jump goto_treehouse
    return

label hidden_wallpaper_4_inter:
    $ wallpaper_unlocked4 = True
    $ renpy.notify("Wallpaper 4 unlocked")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

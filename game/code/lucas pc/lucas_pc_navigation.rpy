















image lucas_pc_wallpaper2 = ConditionSwitch(
    "lucas_pc_wallpaper == 1", "images/customs/PC Lucas/lucas_wallpaper_bg.jpg",
    "lucas_pc_wallpaper == 2", "images/customs/PC Lucas/lucas_pc_wallpaper2.jpg",
    "lucas_pc_wallpaper == 3", "images/customs/PC Lucas/lucas_pc_wallpaper3.png",
    "lucas_pc_wallpaper == 4", "images/customs/PC Lucas/lucas_pc_wallpaper4.png",
    "lucas_pc_wallpaper == 5", "images/customs/PC Lucas/lucas_pc_wallpaper5.png",
    "lucas_pc_wallpaper == 6", "images/customs/PC Lucas/lucas_pc_wallpaper6.png",
    "lucas_pc_wallpaper == 7", "images/customs/PC Lucas/lucas_pc_wallpaper7.png",
    "lucas_pc_wallpaper == 8", "images/customs/PC Lucas/lucas_pc_wallpaper8.png",
    )



































































































screen minigame_start_screen():
    modal True
    zorder 1
    add "module_minigames_homescreen"
    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1712, 4, 207, 76)
        action Hide("minigame_start_screen")




    imagebutton:
        idle Null()
        if eleanor_story == 10 or eleanor_story == 11 or eleanor_story == 17:
            mouse "interaction_m"
        else:
            mouse "deny_m"

        if eleanor_story == 10:
            action Hide("minigame_start_screen"), Call("isJigSawGame")
        elif eleanor_story == 11:
            action Hide("minigame_start_screen"), Call("isJigSawGamee")
        elif eleanor_story == 17:
            action Hide("minigame_start_screen"), Call("isJigSawGameee")
        else:
            action NullAction()
        area (680, 811, 564, 141)


screen lucas_pc_trash():
    modal True
    zorder 1



    drag:
        xysize 835, 833
        add "lucas_pc_trashimg"
        button:
            area 780, 0, 40, 30
            action Hide("lucas_pc_trash", transition=Dissolve(0.2))

screen lucas_pc_window():
    modal True
    zorder 1
    drag:
        xysize 835, 833
        add "lucas_pc_window_ui"
        button:
            area 780, 0, 40, 30
            action Hide("lucas_pc_window", transition=Dissolve(0.2))




screen lucas_explorer_window():
    modal True
    zorder 1

    add "pc_lucas_explorer"

    button:
        area (1702, 94, 105, 106)
        action Hide("lucas_explorer_window", transition=Dissolve(0.2))
        mouse "interaction_m"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        action Show("map_swap_scr2")
        area (720, 347, 480, 618)

    imagebutton:
        idle Null()
        mouse "deny_m"
        action Show("in_progress_box")
        area (183, 352, 459, 602)

    imagebutton:
        idle Null()
        mouse "deny_m"
        action Show("in_progress_box")
        area (1272, 349, 469, 614)

    imagebutton:
        idle Null()
        mouse "interaction_m"
        action OpenURL("https://www.patreon.com/theredpixel")
        area (585, 212, 145, 125)

screen lucas_main_folder():
    modal True
    zorder 2
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("lucas_main_folder")

    hbox:
        xalign 0.27
        yalign 0.32
        spacing 50
        imagebutton:
            idle "pc_lucas_icon_gallery"
            at dial_effect
            mouse "interaction_m"
            action Show("pc_lucas_gallery_screen")

        imagebutton:
            idle "pc_lucas_icon_wallpapers"
            at dial_effect
            mouse "interaction_m"
            action Show("lucas_wallpaper_change")

        imagebutton:
            idle "pc_lucas_icon_music"
            at dial_effect
            mouse "interaction_m"
            action Show("in_progress_box")

screen pc_lucas_gallery_screen():
    modal True
    zorder 3
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("pc_lucas_gallery_screen"), Hide("lucas_main_folder")

    imagebutton:
        idle "pc_lucas_nav_return"

        at dial_effect
        xalign 0.73
        yalign 0.08
        action Hide("pc_lucas_gallery_screen")

    hbox:
        xpos 380
        ypos 280
        spacing 30


        if eleanor_gallery_profile == False:
            imagebutton:
                idle "pc_lucas_gallery_eleanor_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()
        else:
            imagebutton:
                idle "pc_lucas_gallery_eleanor"
                at dial_effect
                mouse "interaction_m"
                action Show("lucas_eleanor_gallery_anim")

        imagebutton:
            idle "pc_lucas_gallery_sadie"
            at dial_effect
            mouse "interaction_m"
            action Show("lucas_sadie_gallery_anim")


        if konami_gallery_profile == False:
            imagebutton:
                idle "pc_lucas_gallery_konami_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()
        else:
            imagebutton:
                idle "pc_lucas_gallery_konami"
                at dial_effect
                mouse "interaction_m"
                action Show("lucas_konami_gallery_anim")

        if jada_gallery_profile == False:
            imagebutton:
                idle "pc_lucas_gallery_jada_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()
        else:
            imagebutton:
                idle "pc_lucas_gallery_jada"
                at dial_effect
                mouse "interaction_m"
                action Show("lucas_jada_gallery_anim")



screen lucas_konami_gallery_anim():
    modal True
    zorder 4
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("lucas_konami_gallery_anim"), Hide("pc_lucas_gallery_screen"), Hide("lucas_main_folder")

    imagebutton:
        idle "pc_lucas_nav_return"

        at dial_effect
        xalign 0.73
        yalign 0.08
        action Hide("lucas_konami_gallery_anim")

    hbox:
        xalign 0.24
        yalign 0.32
        spacing 30

        if konami_gallery_1_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_konami1"
                at dial_effect
                mouse "interaction_m"
                action Return("konami_masturbation_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_konami1_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()



screen lucas_jada_gallery_anim():
    modal True
    zorder 4
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("lucas_jada_gallery_anim"), Hide("pc_lucas_gallery_screen"), Hide("lucas_main_folder")

    imagebutton:
        idle "pc_lucas_nav_return"

        at dial_effect
        xalign 0.73
        yalign 0.08
        action Hide("lucas_jada_gallery_anim")

    hbox:
        xpos 380
        ypos 270
        spacing 30

        if jada_gallery_1_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_jada1"
                at dial_effect
                mouse "interaction_m"
                action Return("jada_frontsex_gallery_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_jada1_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()

        if jada_gallery_2_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_jada2"
                at dial_effect
                mouse "interaction_m"
                action Return("jada_backsex_gallery_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_jada2_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()




screen lucas_eleanor_gallery_anim():
    modal True
    zorder 4
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("lucas_eleanor_gallery_anim"), Hide("pc_lucas_gallery_screen"), Hide("lucas_main_folder")

    imagebutton:
        idle "pc_lucas_nav_return"

        at dial_effect
        xalign 0.73
        yalign 0.08
        action Hide("lucas_eleanor_gallery_anim")

    hbox:
        xalign 0.35
        yalign 0.32
        spacing 30

        if eleanor_gallery_1_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_eleanor1"
                at dial_effect
                mouse "interaction_m"
                action Return("eleanor_shower_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_eleanor1_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()

        if eleanor_gallery_2_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_eleanor2"
                at dial_effect
                mouse "interaction_m"
                action Return("eleanor_sleep_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_eleanor2_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()

screen lucas_sadie_gallery_anim():
    modal True
    zorder 4
    add "pc_lucas_gallery"

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1590, 72, 107, 101)
        action Hide("lucas_sadie_gallery_anim"), Hide("pc_lucas_gallery_screen"), Hide("lucas_main_folder")

    imagebutton:
        idle "pc_lucas_nav_return"

        at dial_effect
        xalign 0.73
        yalign 0.08
        action Hide("lucas_sadie_gallery_anim")

    hbox:
        xalign 0.24
        yalign 0.32
        spacing 30

        if sadie_gallery_1_unlocked == True:
            imagebutton:
                idle "pc_lucas_galleryscene_sadie1"
                at dial_effect
                mouse "interaction_m"
                action Return("sadie_video1_inter")
        else:
            imagebutton:
                idle "pc_lucas_galleryscene_sadie1_alt"
                at dial_effect
                mouse "deny_m"
                action NullAction()


screen lucas_pc_sadiename():
    modal True
    zorder 1

    add "images/customs/input_gui/relationship_inputsadie2.png" alpha 0.9 at truecenter
    input:
        xalign 0.5 yalign 0.54
        default "[sadie_refer_input]"
        value VariableInputValue("sadie_refer_input")
        bold True
        size 40
        color "#FFFF"
        length 9
    button:
        action Hide("lucas_pc_sadiename", transition = Dissolve(0.2))
        background None




screen lucas_wallpaper_change():
    modal True
    zorder 2
    add "transparent_bg_pc"

    button:
        action Hide("lucas_wallpaper_change", transition = Dissolve(0.2))
        background None


    vbox:
        pos (100, 100)
        hbox:
            align (0.5,0.3)
            spacing 5
            imagebutton:
                idle "wallpaper_select2"
                mouse "interaction_m"
                at dial_effect

                action SetVariable("lucas_pc_wallpaper", 1)
            imagebutton:
                idle "wallpaper_select1"
                mouse "interaction_m"
                at dial_effect

                action SetVariable("lucas_pc_wallpaper", 2)

            if wallpaper_unlocked3 == True:
                imagebutton:
                    idle "wallpaper_select3"
                    mouse "interaction_m"
                    at dial_effect

                    action SetVariable("lucas_pc_wallpaper", 3)
            else:
                imagebutton:
                    idle "wallpaper_unkown"
                    mouse "deny_m"
                    at dial_effect
                    action NullAction()

            if wallpaper_unlocked4 == True:
                imagebutton:
                    idle "wallpaper_select4"
                    mouse "interaction_m"
                    at dial_effect

                    action SetVariable("lucas_pc_wallpaper", 4)
            else:
                imagebutton:
                    idle "wallpaper_unkown"
                    mouse "deny_m"
                    at dial_effect
                    action NullAction()
        hbox:


            spacing 5

            if wallpaper_unlocked5 == True:
                imagebutton:
                    idle "wallpaper_select5"
                    mouse "interaction_m"
                    at dial_effect

                    action SetVariable("lucas_pc_wallpaper", 5)
            else:
                imagebutton:
                    idle "wallpaper_unkown"
                    mouse "deny_m"
                    at dial_effect
                    action NullAction()

            if wallpaper_unlocked6 == True:
                imagebutton:
                    idle "wallpaper_select6"
                    mouse "interaction_m"
                    at dial_effect

                    action SetVariable("lucas_pc_wallpaper", 6)
            else:
                imagebutton:
                    idle "wallpaper_unkown"
                    mouse "deny_m"
                    at dial_effect
                    action NullAction()

            if wallpaper_unlocked7 == True:
                imagebutton:
                    idle "wallpaper_select7"
                    mouse "interaction_m"
                    at dial_effect

                    action SetVariable("lucas_pc_wallpaper", 7)
            else:
                imagebutton:
                    idle "wallpaper_unkown"
                    mouse "deny_m"
                    at dial_effect
                    action NullAction()

















init python:
    class LocationLucaspc(Location):
        title="Lucas PC"
        def scene(self,elements):
            
            elements.append("#lucas_pc_wallpaper2")
            
            
            
            
            
            
            elements.append([None, "images/customs/pc Lucas/lucas_pc_layout{dark}_{state}.png"])
            
            
            
            if exit_btn == True:
                elements.append([(1700, 911),"images/customs/computer_exit_{state}.png", "goto_lucasroom", None])
            
            
            elements.append([(1634,116), "images/customs/pc Lucas/lucas_sadiename_{state}.png", [Show("lucas_pc_sadiename")], None])
            
            
            elements.append([(141,140), "images/customs/pc Lucas/lucas_trash_icon_{state}.png", [Show("lucas_pc_trash")], None])
            
            
            elements.append([(300,140), "images/customs/pc Lucas/lucas_pc_icon_{state}.png", [Show("lucas_main_folder")], None])
            
            
            elements.append([(141,370), "images/customs/pc Lucas/lucas_explorer_{state}.png", [Show("lucas_explorer_window")], None])
            
            
            
            elements.append([(300,370), "images/customs/pc Lucas/lucas_pc_picturework_{state}.png", "$blocked$" , None])
            
            
            
            elements.append([(300,600), "images/customs/pc Lucas/lucas_writer_{state}.png", "$blocked$" , None])
            
            
            elements.append([(130,616), "images/customs/pc Lucas/lucas_modules_icon_{state}.png", [Show("minigame_start_screen")], None])


default loc_lucaspc = LocationLucaspc()

label goto_lucaspc:
    call set_location ("loc_lucaspc") from _call_set_location_11
    hide screen main_hud_icon

    return

label eleanor_shower_inter:
    hide screen lucas_main_folder
    hide screen lucas_eleanor_gallery_anim
    hide screen pc_lucas_gallery_screen

    jump eleanor_shower_dialogue1
    return

label konami_masturbation_inter:
    hide screen lucas_main_folder
    hide screen lucas_konami_gallery_anim
    hide screen pc_lucas_gallery_screen   
    jump konami_masturbation_anim3
    return

label eleanor_sleep_inter:
    hide screen lucas_main_folder
    hide screen lucas_eleanor_gallery_anim
    hide screen pc_lucas_gallery_screen

    jump eleanor_thigh_grind_video
    return

label sadie_video1_inter:
    hide screen lucas_main_folder
    hide screen lucas_sadie_gallery_anim
    hide screen pc_lucas_gallery_screen
    jump sadie_video_anim1
    return

label jada_frontsex_gallery_inter:
    hide screen lucas_main_folder
    hide screen lucas_jada_gallery_anim
    hide screen pc_lucas_gallery_screen
    jump jada_frontsex_gall_anim
    return

label jada_backsex_gallery_inter:
    hide screen lucas_main_folder
    hide screen lucas_jada_gallery_anim
    hide screen pc_lucas_gallery_screen
    jump jada_backsex_gallery_anim
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

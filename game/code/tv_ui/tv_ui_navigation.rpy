



label tv_scene_show:
    scene black
    scene chill_opening with dissolve
    pause
    jump tv_navigation

label tv_navigation:
    $ loc = "tv_navigation"
    hide screen main_hud_icon
    hide screen my_invisible_btn




    scene chill_homescreen





    call screen tv_ui_interactive

    $ result = _return




    $ renpy.jump(loc)




screen tv_ui_interactive():






















    imagebutton:
        idle "chill_thumb_ace"
        hover "deny_thumbnail"
        if sadie_story == 7:
            action Jump("sadie_movie_7nightz")
            hover "chill_thumb_ace_h"
            mouse "interaction_m"

        action NullAction()
        mouse "deny_m"
        xpos 55
        ypos 265



    imagebutton:
        idle "chill_thumb_samara"
        if sadie_story == 15:
            action Jump("sadie_movie_8nightz")
            hover "chill_thumb_samara_h"
            mouse "interaction_m"
        else:
            hover "deny_thumbnail"
            mouse "deny_m"

        action NullAction()
        xpos 550
        ypos 265



    imagebutton:
        idle "chill_thumb_singularity"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 1045
        ypos 265


    imagebutton:
        idle "chill_thumb_ourblue"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 1540
        ypos 265


    imagebutton:
        idle "chill_thumb_notpullingout"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 55
        ypos 675


    imagebutton:
        idle "chill_thumb_searcher"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 540
        ypos 675


    imagebutton:
        idle "chill_thumb_kinodertoten"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 1030
        ypos 675



    imagebutton:
        idle "chill_thumb_captjackfap"
        hover "deny_thumbnail"
        mouse "deny_m"
        action NullAction()
        xpos 1540
        ypos 675
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

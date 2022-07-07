


















































































init python:
    class LocationYogaroom(Location):
        title="Yoga Room"
        def scene(self,elements):
            elements.append("images/sadie_house/yoga/bg_yogaroom{dark}.jpg")
            
            
            
            elements.append([(954, 294),"images/sadie_house/yoga/inter_dooryoga1{dark}_{state}.png", "goto_hallwayf2", "*>"])
            
            
            if yoga_sadie_scene == True and sadie_yogabtn == True:
                elements.append([(822, 306),"images/sadie_house/yoga/yoga_room_sadie_figure1{dark}_{state}.png", "yoga_sadie_event1", "*<"])
            
            
            
            if char_at("sadieyoga","yogaz") and not is_talking("sadieyoga"):
                elements.append([(822, 306),"images/sadie_house/yoga/yoga_room_sadie_figure1{dark}_{state}.png", "yoga_sadie_inter", "*<"])










default loc_yogaroom = LocationYogaroom()

label goto_loc_yogaroom:
    call set_location ("loc_yogaroom") from _call_set_location_19
    show screen main_hud_icon

    if now(["saturday","sunday"]) and now(["morning"]) and jada_story == 3:
        jump jada_firstintro
        return
    if now(["saturday","sunday"]) and now(["morning"]) and jada_story == 6:
        jump jada_2ndevent
        return

    if jada_story == 4:
        jump jada_introend
        return



    if yoga_sadie_ended == True:
        hide screen main_hud_icon
        $ sadie_yogabtn = False
        show lucas workoutpose pose7 sure at left with Dissolve(.5)
        show sadie workout pose default at right with Dissolve(.5)
        pause

        show sadie workout pose sad_talk
        l_sadie "I really didn’t mean for any of that to happen. Are you sure you're okay? You don’t want me to have a look to make sure?"
        show sadie workout pose happy
        show lucas workoutpose pose7 default_talk
        l_mc "No, I'm good. I'm feeling better now. It's not your fault, it was just a normal cramp for not stretching"
        show sadie workout pose grump_talk
        show lucas workoutpose pose7 mkay
        l_sadie "and that’s why you always stretch"
        show sadie workout pose grumpy
        show lucas workoutpose pose7 mkay_talk
        l_mc "I just forgot this time"
        show sadie workout pose happy_talk
        show lucas workoutpose pose7 default
        l_sadie "Well I'm still glad you're feeling better now"
        show sadie workout pose happy
        show lucas workoutpose pose7 default_talk
        l_mc "I better go clean myself up . . . I mean stretch myself off to get the blood flowing, you know?"
        show sadie workout pose happy_talk
        show lucas workoutpose pose7 default
        l_sadie "OK, but make sure to stretch next time before we start"
        show sadie workout pose default
        show lucas workoutpose pose7 blank
        l_mc "*Next time?*"
        pause
        show lucas workoutpose pose7 default_talk
        l_mc "Yeah sure thing"

        $ lucas_scope = True
        hide lucas workoutpose pose7 default at left with Dissolve(.5)
        hide sadie workout pose default at right with Dissolve(.5)
        jump goto_lucasroom
        return

    return

label yoga_sadie_inter:
    l_mc "Seems like she is doing her yoga"
    l_mc "Let's not bug her."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

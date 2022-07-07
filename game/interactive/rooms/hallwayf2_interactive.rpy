init python:
    class LocationHallwayf2(Location):
        title="Hallway F2"
        def scene(self,elements):
            
            elements.append("images/sadie_house/hallway_f2/bg_f2hallway{dark}.jpg")
            
            
            
            
            if yoga_sadie_scene == True:
                elements.append([(923, 198),"images/sadie_house/hallway_f2/inter_doorhatch{dark}_{state}.png", "$blocked$",None])
            elif eleanor_story == 2:
                elements.append([(923, 198),"images/sadie_house/hallway_f2/inter_doorhatch{dark}_{state}.png", "$blocked$",None ])
            elif eleanor_story == 23:
                elements.append([(923, 198),"images/sadie_house/hallway_f2/inter_doorhatch{dark}_{state}.png", "$blocked$",None ])
            elif sadie_story < 3:
                elements.append([(923, 198),"images/sadie_house/hallway_f2/inter_doorhatch{dark}_{state}.png", "sadie_story_deny", "*>"])
            else:
                elements.append([(923, 198),"images/sadie_house/hallway_f2/inter_doorhatch{dark}_{state}.png", "goto_attic", "*>"])
            
            
            if eleanor_story == 2:
                elements.append([(689, 174),"images/sadie_house/hallway_f2/inter_doorbathroom1{dark}_{state}.png", "$blocked$", None ])
            elif eleanor_story == 23:
                elements.append([(689, 174),"images/sadie_house/hallway_f2/inter_doorbathroom1{dark}_{state}.png", "eleanor_bathroom_event", "*>"])
            elif sadie_story < 2:
                elements.append([(689, 174),"images/sadie_house/hallway_f2/inter_doorbathroom1{dark}_{state}.png", "sadie_story_deny", "*>"])
            elif sadie_story < 3:
                elements.append([(689, 174),"images/sadie_house/hallway_f2/inter_doorbathroom1{dark}_{state}.png", "sadie_story_deny1", "*>"])
            else:
                elements.append([(689, 174),"images/sadie_house/hallway_f2/inter_doorbathroom1{dark}_{state}.png", "goto_bathroomf2", "*>"])
            
            
            if bailey_map_cross == False:
                elements.append([(1157, 231),"images/sadie_house/hallway_f2/inter_doorbailey2{dark}_{state}.png", "bailey_door_deny", "*>"])
            else:
                elements.append([(1157, 231),"images/sadie_house/hallway_f2/inter_doorbailey2{dark}_{state}.png", "bailey_door_deny1", "*>"])
            
            
            
            if yoga_sadie_scene == True:
                elements.append([(1312, 0),"images/sadie_house/hallway_f2/inter_doorlucas2{dark}_{state}.png", "$blocked$",None ])
            elif eleanor_story == 2:
                elements.append([(1312, 0),"images/sadie_house/hallway_f2/inter_doorlucas2{dark}_{state}.png", "$blocked$",None ])
            elif eleanor_story == 23:
                elements.append([(1312, 0),"images/sadie_house/hallway_f2/inter_doorlucas2{dark}_{state}.png", "$blocked$",None])
            else:
                elements.append([(1312, 0),"images/sadie_house/hallway_f2/inter_doorlucas2{dark}_{state}.png", "goto_lucasroom", "*>"])
            
            
            if eleanor_story == 2:
                elements.append([(121, 0),"images/sadie_house/hallway_f2/inter_doorsadie{dark}_{state}.png", "$blocked$","@^LOCKED" ])
            else:
                elements.append([(121, 0),"images/sadie_house/hallway_f2/inter_doorsadie{dark}_{state}.png", "goto_sadieroom", "*>"])      
            
            
            
            if eleanor_story == 23:
                elements.append([(912, 461),"images/sadie_house/hallway_f2/inter_staircase3{dark}_{state}.png", "$blocked$",None ])
            
            elif yoga_sadie_scene == True:
                elements.append([(912, 461),"images/sadie_house/hallway_f2/inter_staircase3{dark}_{state}.png", "$blocked$",None])
            
            elif sadie_story < 3:
                elements.append([(912, 461),"images/sadie_house/hallway_f2/inter_staircase3{dark}_{state}.png", "sadie_story_deny", "*>"])
            
            else:
                elements.append([(912, 461),"images/sadie_house/hallway_f2/inter_staircase3{dark}_{state}.png", "goto_lobbyf1", "*>"])
            
            
            if eleanor_story == 2:
                elements.append([(807, 261),"images/sadie_house/hallway_f2/inter_dooryoga1{dark}_{state}.png", "$blocked$", None ])
            
            elif sadie_story < 3:
                elements.append([(807, 261),"images/sadie_house/hallway_f2/inter_dooryoga1{dark}_{state}.png", "sadie_story_deny", "*>"])
            
            else:
                elements.append([(807, 261),"images/sadie_house/hallway_f2/inter_dooryoga1{dark}_{state}.png", "goto_loc_yogaroom", "*>"])






















default loc_hallwayf2 = LocationHallwayf2()

label goto_hallwayf2:
    call set_location ("loc_hallwayf2") from _call_set_location_16
    show screen main_hud_icon


    if sadie_story == 0:
        jump sadie_story_int_0

    return

label sadie_story_deny1:



    jump sadie_bathroom_1
    return

label sadie_story_deny:
    "Not yet"
    jump goto_hallwayf2
    return


label bailey_door_deny:
    "I shouldn't go to her room, she isn't here"
    $ bailey_map_cross = True
    show screen map_updated_notify with dissolve
    jump goto_hallwayf2
    return




label eleanor_bathroom_event:
    if item_spareoutfit in inv:
        jump eleanor_third_session_bath2
        return
    elif True:
        l_mc "I should grab her clothe . . ."
        return
    return

label bailey_door_deny1:
    "She isn't home yet"
    jump goto_hallwayf2
    return


label sadie_story_int_0:
    hide screen main_hud_icon

    l_sadie "Lucas !!!"
    show lucas pose4 normal alert at left with moveinleft
    pause
    show lucas pose4 normal alert_talk
    l_mc "What the..."
    show lucas pose4 normal default_talk at left with moveinleft
    l_mc "Yeah [sadie_refer_input] !?!"
    l_mc "Do you need something ?"
    show sadie normal pose4 default_talk at right with moveinright
    show lucas pose4 normal default with Dissolve(0.2)
    l_sadie "Awe thank god, could you do me a favour sweetie ?"
    show lucas pose4 normal alert_talk
    show sadie normal pose4 default
    l_mc "Could you put something on first [sadie_refer_input]?"
    show lucas pose4 normal alert
    show sadie normal pose4 awe_talk

    l_sadie "That’s what I’m asking you about, dear. Can you go get my Shirt and underwear from my room?"
    l_sadie "I left them in my closet"
    show lucas pose4 normal alert_talk
    show sadie normal pose4 awe
    l_mc "What? Your underwear?"
    show lucas pose4 normal alert
    show sadie normal pose4 awe_talk
    l_sadie "Oh, come on."
    l_sadie "It’s just my bra and shirt. I clean your underwear all the time."
    show sadie normal pose4 default_talk
    l_sadie "I’m going to be late for work so hurry."
    show sadie normal pose4 default
    show lucas pose4 normal assured_talk
    l_mc "Fine I’ll go get your outfit. It’s in your closet, right?"
    show sadie normal pose4 happy_talk
    show lucas pose4 normal assured
    l_sadie "Yes, it’s hanging on the wall inside my closet."
    show sadie normal pose4 happy
    show lucas pose4 normal puzzle_talk
    l_mc "mmmkay, I’ll be right back."
    hide sadie normal with moveoutright

    pause
    show lucas pose4 normal puzzle
    hide lucas pose4 with moveoutleft
    $ sadie_story += 1
    jump goto_hallwayf2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

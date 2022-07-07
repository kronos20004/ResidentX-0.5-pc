





init python:
    class LocationSadieroom(Location):
        title="Sadie Room"
        def scene(self,elements):
            elements.append("images/sadie_house/sadie_room/bg_bedroomsadie{dark}.jpg")
            
            
            if sadie_story == 10 or sadie_story == 13:
                elements.append([(1488, 331),"images/sadie_house/sadie_room/inter_doorbalcony2{dark}_{state}.png", "$blocked$", None ])
            else:
                elements.append([(1488, 331),"images/sadie_house/sadie_room/inter_doorbalcony2{dark}_{state}.png", "goto_sadiebalcony", "*>"])
            
            
            
            
            
            
            
            
            if char_at("sadiebed","sadie_b") and not is_talking("sadiebed"):
                elements.append([(972, 485),"images/sadie_house/sadie_room/inter_bedsadie2{dark}_{state}.png", "sadie_bed_interaction", "*<"])   
            else:
                elements.append([(972, 485),"images/sadie_house/sadie_room/inter_bedsadie1{dark}_{state}.png", "sadie_bed_interaction", "*^"]) 
            
            
            if char_at("sadiebedz","sadiebz") and not is_talking("sadiebedz"):
                elements.append([(950, 409),"images/sadie_house/sadie_room/CharButton_Sadie10{dark}_{state}.png", "sadie_bed_interactionz", "*<"])  
            
            
            elements.append([(292, 302),"images/sadie_house/sadie_room/inter_closet2{dark}_{state}.png", "goto_sadiecloset", "*>"])
            
            
            if sadie_story == 10:
                elements.append([(699, 348),"images/sadie_house/sadie_room/inter_doorsadie1{dark}_{state}.png", "$blocked$",None ])
            else:
                elements.append([(699, 348),"images/sadie_house/sadie_room/inter_doorsadie1{dark}_{state}.png", "goto_hallwayf2", "*>"])
            
            
            elements.append([(1407, 400),"images/sadie_house/sadie_room/inter_jewelrybox{dark}_{state}.png", "sadie_chest_interaction", "*>"])












default loc_sadieroom = LocationSadieroom()

label goto_sadieroom:
    call set_location ("loc_sadieroom") from _call_set_location_24
    show screen main_hud_icon

    if sadie_story == 9:
        hide screen main_hud_icon
        show sadie normal pose default at right with moveinright
        show lucas normal pose4 mkay_talk at left with moveinleft
        l_mc "Soooooo . . . are you going to get changed here or…"
        show sadie normal smirk_talk
        show lucas normal mkay
        l_sadie "It is my room, isn’t it? You can change in my closet once you find something just wait in there until I’m done changing. And no peaking.."
        show sadie normal smirk
        show lucas normal mkay_talk
        l_mc "As if."
        show sadie normal default
        show lucas normal puzzle_talk
        l_mc "Can I go take a look in your closet now?"
        show lucas normal puzzle
        show sadie normal default_talk
        l_sadie "Go ahead."
        $ sadie_story += 1
        hide sadie normal default at right with moveoutright
        hide lucas normal default_talk at left with moveoutleft
        jump goto_sadieroom
        return

    return


label sadie_chest_interaction:

    if strangerelic_office == True and sadie_room_chestkey == False:
        hide screen main_hud_icon
        if now(["morning", "afternoon"]):
            scene ui_pendantbox_1_day
        elif now(["evening", "night"]):
            scene ui_pendantbox_1_night
        l_mc "Looks like this pendant was meant to fit in this little crevice"

        if now(["morning", "afternoon"]):
            scene ui_pendantbox_2_day
        elif now(["evening", "night"]):
            scene ui_pendantbox_2_night
        show ui_pendantbox_pendant
        l_mc "There we go"
        l_mc "Another key ? A key for another key, seems like a fair trade"
        pause
        $ inv.append(item_chestkey)
        $ inv.remove(item_strangerelic)
        hide item_chestkey
        $ strangerelic_insert = True
        $ sadie_room_chestkey = True
        show screen item_updated_notify with dissolve
        jump goto_sadieroom
        return

    elif strangerelic_insert == True:
        hide screen main_hud_icon
        if now(["morning", "afternoon"]):
            scene ui_pendantbox_2_day
            show ui_pendantbox_pendant
        elif now(["evening", "night"]):
            scene ui_pendantbox_1_night
            show ui_pendantbox_pendant
        l_mc "I have already acquried the key here"
        jump goto_sadieroom
        return
    elif True:

        hide screen main_hud_icon
        if now(["morning", "afternoon"]):
            scene ui_pendantbox_1_day
        elif now(["evening", "night"]):
            scene ui_pendantbox_1_night
        l_mc "Funny looking jewelry box. Has a little Spherical indentation in the center. Is something supposed to fit there?"
        jump goto_sadieroom
        return

label sadie_bed_interaction:
    hide screen main_hud_icon
    if now(["morning", "afternoon", "evening"]):
        l_mc ". . . ."
    elif now(["night"]):
        if char_at("sadiebed","sadie_b") == True:
            l_mc "She is sleeping, let's not bother her."
        elif True:
            l_mc ". . . ."
    jump goto_sadieroom

    return


label sadie_bed_interactionz:
    jump sadie_bedz_interaction
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

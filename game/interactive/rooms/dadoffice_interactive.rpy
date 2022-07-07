


image medallion_display = "mini/medallion_puzzle_display.jpg"

init python:
    class LocationOfficef1(Location):
        title="Office F1"
        def scene(self,elements):
            elements.append("images/sadie_house/dad_office/bg_f1office{dark}.jpg")
            
            
            
            if medallion_puzzle_dialogue == False and medallion_puzzle_solve == False and bookshelf_close == False:
                elements.append([(1308,61),"images/sadie_house/dad_office/inter_bookshelf1{dark}.png", None])
            
            elif medallion_puzzle_dialogue == True and medallion_puzzle_solve == True and office_strangebattery == False:
                elements.append([(1485,33),"images/sadie_house/dad_office/inter_bookshelf2{dark}.png", None])
                elements.append([(1594,509),"images/sadie_house/dad_office/inter_strangebattery{dark}_{state}.png", "office_battery_inter", "*^"])
            
            elif office_strangebattery == True:
                elements.append([(1485,33),"images/sadie_house/dad_office/inter_bookshelf3{dark}.png", None])
            
            
            
            if leo_laptop_map_icon == False:
                elements.append([(347,548),"images/sadie_house/dad_office/inter_laptop1{dark}_{state}.png", "leo_laptop_office_inter", "*^"])
            elif sadie_night_couch_keypad == False:
                elements.append([(347,548),"images/sadie_house/dad_office/inter_laptop1{dark}_{state}.png", "office_keypad_sadie_inter", "*^"])
            else:
                elements.append([(347,548),"images/sadie_house/dad_office/inter_laptop1{dark}_{state}.png", "leo_laptop_navigation", "*^"])
            
            
            elements.append([(1064,635),"images/sadie_house/dad_office/inter_chest1{dark}_{state}.png", "office_chest_inter", "*^"])   
            
            
            
            if medallion_puzzle_solve == False:
                if medallion_piece == False:
                    elements.append([(1462,483),"images/sadie_house/dad_office/inter_medallions{dark}_{state}.png", "office_medallion_inter", "*^"])  
                elif medallion_piece_used == False:
                    elements.append([(1462,483),"images/sadie_house/dad_office/inter_medallions{dark}_{state}.png", "office_medallion_inter2", "*^"]) 
                else:
                    elements.append([(1462,483),"images/sadie_house/dad_office/inter_medallions{dark}_{state}.png", [Show("medallion_puzzle_screen")], "*^"])
            
            
            
            if strangerelic_office == False:
                elements.append([(640,483),"images/sadie_house/dad_office/inter_strangerelic{dark}_{state}.png", "office_strangerelic_inter", "*^"])
            
            if wallpaper_unlocked5 == False:
                elements.append([(804,88),"images/sadie_house/hidden wallpaper/hidden_wallpaper_5.png", "hidden_wallpaper_5_inter", "*^"])
            
            
            elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_livingf1", "*>"])











default loc_officef1 = LocationOfficef1()

label goto_officef1:
    call set_location ("loc_officef1") from _call_set_location_15
    show screen main_hud_icon

    if medallion_puzzle_solve == True and medallion_puzzle_dialogue == False:
        jump first_office_shelf_move



    return

label hidden_wallpaper_5_inter:
    $ wallpaper_unlocked5 = True
    $ renpy.notify("Wallpaper 5 unlocked")
    jump goto_officef1
    return


label first_office_shelf_move:
    show black with dissolve
    "*Click*"
    l_mc "Ok, so now what ?"
    hide black
    $ inv.remove(item_medallion)
    $ medallion_puzzle_dialogue = True
    $ bookshelf_close = True
    $ medallion_puzzle_dialogue = True
    l_mc "I see, the bookshelf just moved"
    l_mc "So now my dad has a cliche moving book shelf as well. Why am I not surprised at this point ?"
    show screen journal_updated_notify
    jump goto_officef1
    return



label office_medallion_inter:
    if medallion_map_icon == False:
        $ medallion_map_icon = True
        show screen map_updated_notify with dissolve
        jump goto_officef1
        return
    hide screen main_hud_icon
    scene medallion_display with fade
    l_mc "Some weird looking medallions . . "
    l_mc "Never knew what they were for"
    l_mc "He never even let me touch them, always being so stubborn with his personal belongings"
    l_mc "Don't think he'll mind me touching them now"
    l_mc "But. . ."
    l_mc "It's missing a piece"
    jump goto_officef1
    return

label office_medallion_inter2:
    hide screen main_hud_icon
    show lucas normal pose4 default at left with Dissolve(.5)
    pause
    show lucas normal pose4 default_talk
    "Ok, I guess I should put the medallions right beside it"
    $ medallion_piece_used = True

    "Ah, there we go"
    "i can try to mess around these little golden medallions pieces now"
    jump goto_officef1
    return

label office_battery_inter:
    if item_handsaw in inv:
        hide screen main_hud_icon
        show lucas normal pose4 default_talk at left with Dissolve(.5)
        l_mc "The handsaw would definitly cut these off"
        show lucas normal pose10 glad
        $ office_strangebattery = True







        pause
        show lucas normal pose10 happy_talk
        l_mc "There we go, that done it"
        l_mc "Lets pick up this strange looking battery"
        show lucas normal pose7 default
        pause
        $ inv.append(item_stranegbattery)
        hide lucas normal pose7 default at left with Dissolve(.5)
        show screen item_updated_notify with dissolve
        show screen journal_updated_notify with dissolve
        jump goto_officef1
        return
    elif True:

        hide screen main_hud_icon
        l_mc "Hmm, what is that? behind these wooden planks"
        l_mc "What could he be hiding back here? Something strange for sure"
        l_mc "I can't get through it, probably need to find something that can cut through this"
        jump goto_officef1
        return

label office_strangerelic_inter:
    hide screen main_hud_icon
    show lucas normal pose4 puzzle at left with Dissolve(.5)
    pause
    show lucas normal pose11 default_d_talk
    l_mc "What a interesting looking relic"
    l_mc "I'll hold onto it for now"
    show lucas normal pose4 default

    "Strange Relic acquired"
    $ inv.append(item_strangerelic)
    $ strangerelic_office = True
    hide item_relic
    hide lucas normal pose4 default at left
    show screen item_updated_notify with dissolve
    jump goto_officef1
    return

label leo_laptop_office_inter:
    l_mc "[leo_refer_input]'s laptop"
    $ leo_laptop_map_icon = True
    show screen map_updated_notify with dissolve
    jump goto_officef1
    return

label office_keypad_sadie_inter:
    l_mc "I should ask [sadie_refer_input] about the Keypad first"
    jump goto_officef1
    return

label office_chest_inter:

    if chest_map_icon == False:
        $ chest_map_icon = True
        show screen map_updated_notify with dissolve
    hide screen main_hud_icon


    if item_chestkey in inv:
        if now(["morning", "afternoon"]):
            scene ui_chest_closed

        elif now(["evening", "night"]):
            scene ui_chest_closed_alt
        l_mc "I think this unkown key should fit in here"

        if now(["morning", "afternoon"]):
            scene ui_chest_open
            if medallion_piece == False:
                show item_medallion_chest
            if office_leo_note == False:
                show item_leosnote

        elif now(["evening", "night"]):
            scene ui_chest_open_alt
            if medallion_piece == False:
                show item_medallion_chest_alt
            if office_leo_note == False:
                show item_leosnote_alt

        $ inv.remove(item_chestkey)
        l_mc "And abracadabra"
        l_mc "What have we got in here?"
        l_mc "A medallion and some note along with other valuables"
        l_mc "Let's just take that in"
        show item_medallion_thumb at truecenter with Dissolve(.5)
        $ inv.append(item_medallion)
        pause
        hide item_medallion_thumb
        $ medallion_piece = True
        hide item_medallion_chest
        hide item_medallion_chest_alt
        l_mc "What else is there"
        l_mc "Some kind of note left by [leo_refer_input] ?"
        l_mc "Well, I might as well take a look"
        hide item_leosnote
        hide item_leosnote_alt
        $ office_leo_note = True
        show ui_leosnote with Dissolve(.8)
        pause
        l_mc "What the hell ?"
        l_mc "Was he killed ?"
        l_mc "How am I supposed to deal with this? His death was no accident"
        l_mc "Fine then, I’ll keep this to myself but I can’t promise I won’t keep looking into this more. I have to to keep searching"
        l_mc "After everything, you at least owe me this"
        l_mc "just as self-contained as ever, even in death"
        l_mc "I've read enough"
        l_mc "I can't let this bring me down"
        show screen item_updated_notify with dissolve
        jump goto_officef1
        return

    if office_leo_note == True:
        hide screen main_hud_icon
        if now(["morning","afternoon"]):
            scene ui_chest_open
        elif now(["evening","night"]):
            scene ui_chest_open_alt
        l_mc "Nothing to see here"
        jump goto_officef1
        return
    elif True:

        hide screen main_hud_icon
        if now(["morning","afternoon"]):
            scene ui_chest_closed
        elif now(["evening","night"]):

            scene ui_chest_closed_alt
        l_mc "The chest is locked and I'm not about to damage his stuff just to open this"
        l_mc "I'll come back later, with a better solution"
        jump goto_officef1
        return



    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

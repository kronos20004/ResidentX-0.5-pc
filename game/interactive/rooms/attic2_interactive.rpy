

























































































































































































































screen attic_pinboard():
    modal True
    key "mouseup_1" action Hide("attic_pinboard", transition = Dissolve(0.1))

    if boardinfo_map_icon == False:

        timer 0.1 action Show("map_updated_notify"), SetVariable("boardinfo_map_icon", True)



    if now(["evening", "night"]):
        add "pinboard_night"
    elif now(["morning", "afternoon"]):
        add "pinboard"

init python:
    class LocationAttic2(Location):
        title="Attic 2"
        def scene(self,elements):
            elements.append("images/sadie_house/attic2/bg_attichidden{dark}.jpg")
            
            
            
            
            if attic2_strangebattery == True and attic2_computer_solved == False:
                elements.append([(570,388),"images/sadie_house/attic2/inter_alientech2{dark}_{state}.png", [Show("alien_keypad")], "*^"])
            
            elif attic2_strangebattery == True and attic2_computer_solved == True:
                elements.append([(570,388),"images/sadie_house/attic2/inter_alientech2{dark}_{state}.png", "attic2_alienpc_inter", "*^"])
            
            elif attic2_strangebattery == False and attic2_computer_solved == False:
                elements.append([(611,546),"images/sadie_house/attic2/inter_alientech1{dark}_{state}.png", "attic2_alienpc_inter", "*^"])
            
            
            
            if attic_paint == False:
                elements.append([(1743,348),"images/sadie_house/attic2/inter_doorhidden{dark}_{state}.png", "attic_door_deny", "*>"])
            else:
                if attic_hidden_door == False:
                    elements.append([(1743,348),"images/sadie_house/attic2/inter_doorhidden{dark}_{state}.png", "attic2_door_unlock", "*>"])
                else:
                    elements.append([(1743,348),"images/sadie_house/attic2/inter_doorhidden{dark}_{state}.png", "goto_attic", "*>"])
            
            
            
            if closet_dial_open == False:
                elements.append([(919,891),"images/sadie_house/attic2/inter_hatchhidden{dark}_{state}.png", "attic2_hatch_lock", "*>"])
            else:         
                elements.append([(919,891),"images/sadie_house/attic2/inter_hatchhidden{dark}_{state}.png", "goto_sadiecloset", "*>"])
            
            
            
            elements.append([(805,331),"images/sadie_house/attic2/inter_pinboard{dark}_{state}.png", [Show("attic_pinboard")], "*^"])
            
            
            
            
            
            
            if wallpaper_unlocked3 == False:
                elements.append([(1286, 607),"images/sadie_house/hidden wallpaper/hidden_wallpaper_3.png", "hidden_wallpaper_3_inter", "*^"])


default loc_attic2 = LocationAttic2()

label goto_attic2:
    call set_location ("loc_attic2") from _call_set_location_21
    show screen main_hud_icon

    if hidden_attic_discovered == False:
        jump attic2_discovered
        return

    if attic2_computer_solved == True and facility_story == 0:
        hide screen main_hud_icon
        if now(["morning", "afternoon"]):
            scene atticomputer_blank
        elif now(["evening", "night"]):
            scene atticomputer_blank2
        window hide
        centered "{color=7fff00}{size=45}{font=gui/fonts/acumin_regular.otf}PENDING SINGAL \n{/font}{/size}{/color}"
        centered "{color=7fff00}{size=45}{font=gui/fonts/acumin_regular.otf}SENDING COORDINATES \n{/font}{/size}{/color}" with dissolve
        centered "{color=7fff00}{size=45}{font=gui/fonts/acumin_regular.otf}TRANSMITION COMPLETE \n{/font}{/size}{/color}" with dissolve
        centered "{color=7fff00}{size=45}{font=gui/fonts/acumin_regular.otf}POWERING OFF \n{/font}{/size}{/color}"
        if now(["morning", "afternoon"]):
            scene atticcomputer_dayoff
        elif now(["evening", "night"]):
            scene atticcomputer_nightoff
        pause
        l_mc "Ok . . ."
        l_mc "What was that?"
        l_mc "Was that it?.."
        l_mc "Well that was pretty anti-climactic for everything I had to do"
        l_mc "Where am I supposed to go to next ?"
        l_mc "Was that a big waste of time or what ?"
        $ facility_story += 1
        show screen journal_updated_notify with dissolve
        jump goto_attic2
        return

    return



label attic_door_deny:
    l_mc "OK there's another door here"
    l_mc "Well it's still seem to be stuck. Something must be jamming it from the other side"
    jump goto_attic2
    return


label attic2_discovered:
    hide screen main_hud_icon
    l_mc "What the..."
    l_mc "[leo_refer_input] had a secret attic hidden here?"
    l_mc "Since when?... why? how?"
    l_mc "Wait.. what is that weird computer thing over there?"

    l_mc "I better check it out"
    l_mc "... and this place smells pretty bad"
    $ hidden_attic_discovered = True
    jump goto_attic2
    return

label attic2_door_unlock:
    l_mc "*Unlocks the door*"
    l_mc "AH HA, there we go"
    l_mc "Door is unlocked"
    $ attic_hidden_door = True
    jump goto_attic2
    return

label attic2_hatch_lock:
    l_mc "Hm...... it's locked"
    jump goto_attic2
    return

label attic2_scope_interaction:
    l_mc "Looks useful, but there isn't any reason to use the scope at the moment "
    jump goto_attic2
    return

label hidden_wallpaper_3_inter:
    $ wallpaper_unlocked3 = True
    $ renpy.notify("Wallpaper 3 unlocked")
    jump goto_attic2
    return

label attic2_alienpc_inter:
    if atticstrange_map_icon == True:
        $ atticstrange_map_icon = False
        show screen map_updated_notify with dissolve

    if item_stranegbattery in inv:
        hide screen main_hud_icon
        l_mc "Hey wait a minute"
        l_mc "I think I can fit this thing into the slot over the computer"
        l_mc "okay, well let's give it a go"
        $ inv.remove(item_stranegbattery)
        "Strange Battery inserted"






        $ attic2_strangebattery = True
        l_mc "Nice !"
        l_mc "I'm a genius"
        show screen journal_updated_notify with dissolve
        jump goto_attic2
        return

    elif attic2_computer_solved == True:
        l_mc "Don't think I should touch this computer anymore, not any time sooner"
        jump goto_attic2
        return
    elif True:

        hide screen main_hud_icon
        l_mc "that’s some strange looking computer is this? It doesn’t look like any computer I’ve ever"
        l_mc "another one of his strange inventions, I presume"
        l_mc "whatever it is, it doesn’t seem to be turning on"
        l_mc "It has some strange circular crevice on the top"
        l_mc "I better find some way of turning this thing on"
        jump goto_attic2
        return

    jump goto_attic2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:
    class Locationfrontf1(Location):
        title="Front F1"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/front door/bg_frontdoor{dark}.jpg")
            elif now(["night"]):
                elements.append("images/sadie_house/front door/bg_frontdoor_midnight.jpg")
            
            
            
            elements.append([(849,116),"images/sadie_house/front door/inter_doorfront{dark}_{state}.png", "frontdoor_interaction", "*>"])
            
            
            elements.append([(233,953),"images/sadie_house/front door/inter_doorfloor{dark}_{state}.png", "goto_lobbyf1", "*>"])
            
            
            elements.append([(728,556),"images/sadie_house/front door/inter_mailbin{dark}_{state}.png", "frontdoor_mail_interaction", "*^"])



default loc_frontf1 = Locationfrontf1()

label goto_frontf1:
    call set_location ("loc_frontf1") from _call_set_location_4
    show screen main_hud_icon


    if eleanor_story == 21 and now("morning") and now(["tuesday", "thursday"]):
        jump eleanor_third_session
        return
    if eleanor_story == 29 and now("night") and now(["tuesday", "thursday"]):
        jump eleanor_fourth_session
        return

    return

label frontdoor_interaction:
    if eleanor_story == 2 and now(["morning", "afternoon"]):
        jump eleanor_first_event
        return
    if eleanor_story == 6 and now(["evening"]) and now(["tuesday", "thursday"]):
        jump eleanor_second_event
        return
    if eleanor_story == 14 and now("afternoon") and now(["tuesday", "thursday"]):
        jump eleanor_third_event
        return
    elif True:
        l_mc "Can't leave"
        jump goto_frontf1
        return

label frontdoor_mail_interaction:
    if mail_map_icon == False:
        $ mail_map_icon = True
        show screen map_updated_notify with dissolve
        return

    if item_lens_arrival == 2:
        $ item_lens_arrival += 1
        $ inv.append(item_lens)
        show item_lens at truecenter with dissolve
        pause
        hide item_lens at truecenter with dissolve
        show screen item_updated_notify with dissolve
        pause
        hide screen item_updated_notify

        jump goto_frontf1
        return


    if item_manga_arrival == 2:
        $ item_manga_arrival += 1
        $ inv.append(item_manga1)
        show item_manga1 at truecenter with dissolve
        pause
        hide item_manga1 at truecenter with dissolve
        show screen item_updated_notify with dissolve
        pause
        hide screen item_updated_notify
        l_mc "Nice, I better text Konami"
        $ konami_phone_points += 1
        jump goto_frontf1


    if item_christmassanta_arrival == 2 and item_christmastree_arrival == 2:
        $ item_christmassanta_arrival += 1
        $ item_christmastree_arrival += 1
        l_mc "Nice, the Santa outfit & Tree is here !"
        l_mc "Better go place these things in my room for now so she doesn’t see them yet. "
        $ christmas_treedeco_btn = True
        $ christmas_santasuit_btn = True
        return

    if item_christmassanta_arrival == 2:
        $ item_christmassanta_arrival += 1
        "Nice, my santa outfit is here !"
        "I'll put it in my room"
        $ christmas_santasuit_btn = True
        return

    if item_christmastree_arrival == 2:
        $ item_christmastree_arrival += 1
        "Comes in a box instead of the whole physical tree, huh. Technology changed these days"
        "I'll put it in my room"
        $ christmas_treedeco_btn = True
        return

    l_mc "A mailbox"
    l_mc "hmm.. looks empty in here"

    jump goto_frontf1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

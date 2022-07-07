
























































































































































































































































init python:
    class LocationSadiecloset(Location):
        title="Closet"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/sadie_closet/bg_closetsadie{dark}.jpg")
            elif now(["night"]):
                elements.append("images/sadie_house/sadie_closet/bg_closetsadie_midnight.jpg")
            
            
            elements.append([(1025,9),"images/sadie_house/sadie_closet/inter_box1{dark}_{state}.png","$blocked$", None])
            
            
            
            
            if sadie_story == 1:
                elements.append([(1108, 350),"images/sadie_house/sadie_closet/inter_outfitsadie1{dark}_{state}.png", "sadie_businessoutfit_interact", "*^"])
            
            
            
            
            if eleanor_story == 23 and spareitem_eleanor == False:
                elements.append([(965, 545),"images/sadie_house/sadie_closet/inter_wardrobe1{dark}_{state}.png", "eleanor_spare_out_interact", "*^"]) 
            else:
                elements.append([(965, 545),"images/sadie_house/sadie_closet/inter_wardrobe1{dark}_{state}.png", "$blocked$", None])
            
            
            
            if key_pad_unlocked == False:
                elements.append([(1307, 557),"images/sadie_house/sadie_closet/inter_dialpad1{dark}_{state}.png", "sadie_closet_dial_lock", "*^"]) 
            
            elif closet_dial_open == True:
                elements.append([(1307, 557),"images/sadie_house/sadie_closet/inter_dialpad1{dark}_{state}.png", "sadie_closet_dial_finish", "*^"])     
            else:
                elements.append([(1307, 557),"images/sadie_house/sadie_closet/inter_dialpad1{dark}_{state}.png", [Show("closet_keypad")], "*^"])     
            
            
            
            
            
            
            
            if sadie_story == 12:
                elements.append([(312, 193),"images/sadie_house/sadie_closet/inter_doorcloset1{dark}_{state}.png", "closet_sadie_event2alt_inter", "*^"])
            else:
                elements.append([(312, 193),"images/sadie_house/sadie_closet/inter_doorcloset1{dark}_{state}.png", "goto_sadieroom", "*>"])
            
            
            
            if closet_dial_open == True:
                if sadie_story == 10 or sadie_story == 12 or sadie_story == 13:
                    elements.append([(638, 239),"images/sadie_house/sadie_closet/inter_shuttercloset{dark}_{state}.png", "$blocked$", None])
                elif eleanor_story == 23:
                    elements.append([(638, 239),"images/sadie_house/sadie_closet/inter_shuttercloset{dark}_{state}.png", "$blocked$", None])
                else:
                    elements.append([(638, 239),"images/sadie_house/sadie_closet/inter_shuttercloset{dark}_{state}.png", "closet_shutter_inter", "*^" ])
            
            
            
            
            
            
            
            
            if sadie_story == 10:
                elements.append([(834, 874),"images/sadie_house/sadie_closet/inter_outfitlucas1_{state}.png", "closet_sadie_event2", "*^"])






default loc_sadiecloset = LocationSadiecloset()

label goto_sadiecloset:
    call set_location ("loc_sadiecloset") from _call_set_location_18
    show screen main_hud_icon

    if sadie_story == 11:
        hide screen main_hud_icon
        show lucas workoutpose pose1 default at left with Dissolve(.15)
        "(I gained my control back. I better stop here before I commit an act of disgrace upon myself)"
        hide lucas workoutpose pose1 default
        show lucas workoutpose pose1 mkay at left
        "(I need to stop here before I commit an act of disgrace upon myself.)"
        "(Jeez, I haven’t even put my pants on.)"
        show lucas workoutpose pose2 mkay at left with Dissolve(.15)
        pause
        show lucas workoutpose pose4 mkay at left with Dissolve(.15)
        l_mc "(Yeah, these fit good except for the part that’s poking out.)"
        l_mc "(It should calm down by the time I get back to her)"
        $ sadie_story += 1
        hide lucas workoutpose pose3 mkay at left with Dissolve(.15)
        jump goto_sadiecloset
        return


    return


label closet_sadie_event2:
    hide screen main_hud_icon
    show lucas normal pose5 default_talk at left with Dissolve(.15)
    l_mc "Ok this should do just fine"
    hide lucas normal default_talk at left
    show lucas normal pose35 default at left with Dissolve(.15)
    pause
    hide lucas normal pose35 default at left
    show lucas normal pose34 cocky at left with Dissolve(.15)
    pause
    hide lucas normal pose34
    show lucas workoutpose pose1 default with Dissolve(.15)
    pause
    l_sadie "You find anything in there sweety?"
    show lucas workoutpose pose1 default_talk
    l_mc "Yeah. I just put a shirt on now."
    show lucas workoutpose pose1 default
    l_sadie "ok, I’m still not done yet. Just hold on a bit longer."
    show lucas workoutpose pose1 mkay
    l_mc "(Wait a sec… oh no.)"
    l_mc "(This isn't good)"

    jump sadie_event2
    return



label eleanor_spare_out_interact:
    $ spareitem_eleanor = True
    hide screen main_hud_icon
    show item_spareoutfit at truecenter with dissolve
    pause
    $ inv.append(item_spareoutfit)
    hide item_spareoutfit at truecenter with dissolve
    show screen item_updated_notify with dissolve
    hide screen item_updated_notify
    l_mc "Alright, this should be just fine for her"
    l_mc "I'll just go slip this in for her now"
    l_mc "Wait a second. . ."
    jump eleanor_closet_peek1
    return

label sadie_businessoutfit_interact:
    hide screen main_hud_icon





    l_mc "Hmm…? What the heck is this thing back here?"
    l_mc "Probably another one of [sadie_refer_input]’s weird contraptions."
    l_mc "Maybe [sadie_refer_input] knows what this keypad is for."
    l_mc "Looks cool but I shouldn’t mess with it for now. I’ll come back later to check it out or ask [sadie_refer_input] about it."
    l_mc "I’ll just go and hand her the clothes she asked for before she’s late for work and starts blaming it on me."

    $ inv.append(item_sadiebusinessoutfit)
    hide sadies_half_outfit_thumb
    show screen journal_updated_notify with dissolve
    show screen item_updated_notify with dissolve
    $ sadie_story += 1
    jump goto_sadiecloset
    return

label closet_sadie_event2alt_inter:
    hide screen main_hud_icon
    show inter_doorcloset_def_day
    show lucas workoutpose pose3 default at left with Dissolve(.15)
    show sadie workout pose default at right with moveinright
    show lucas workoutpose pose3 default_talk
    l_mc "Hey, you done yet?"
    show sadie workout pose default_talk
    show lucas workoutpose pose3 default
    l_sadie "Yeah, all done here. Going on ahead to the yoga room. I’ll meet you there."
    show sadie workout pose happy
    show lucas workoutpose pose9 blank
    l_mc "(Thank God that’s over with. Who knows what I would’ve done had I seen more.)"
    $ sadie_story += 1
    $ yoga_sadie_scene = True
    hide inter_doorcloset_def_day
    hide lucas workoutpose pose9 default at left with moveoutleft
    hide sadie workout pose default at right with moveoutright
    jump goto_sadiecloset
    return

label sadie_closet_dial_finish:
    l_mc "I already unlocked it"
    jump goto_sadiecloset
    return

label sadie_closet_dial_lock:
    if sadie_story == 1:
        l_mc "Hm . . . "
        jump goto_sadiecloset
        return
    elif secret_keypad_map == False:
        l_mc "I better mark this keypad on my map"
        show screen map_updated_notify with dissolve
        $ secret_keypad_map = True
        jump goto_sadiecloset
        return
    elif key_pad_unlocked == False:
        l_mc "I should probably talk to Sadie first, about this"
        jump goto_sadiecloset
        return
    return


label closet_shutter_inter:
    if sadie_story == 10 or sadie_story == 11 or sadie_story == 12:
        l_mc ". . ."
        return
    if eleanor_story == 23:
        l_mc ". . ."
        return

    jump goto_attic2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

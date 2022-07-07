



init python:
    class LocationLucasRoom(Location):
        title="Lucas Room"
        def scene(self,elements):
            elements.append("images/sadie_house/lucas_room/bg_bedroomlucas{dark}.jpg")
            
            
            elements.append([(851, 298),"images/sadie_house/lucas_room/inter_pclucas{dark}_{state}.png", "goto_lucaspc_inter", "*^"])
            
            
            
            
            if eleanor_story == 7 and now(["evening", "night"]) and eleanor_btn_lucasroom == True:
                elements.append([(665, 321),"images/sadie_house/lucas_room/eleanor_btn1{dark}_{state}.png", "eleanor_teaching_event1", "*^"])
            
            if eleanor_story == 15 and now(["morning", "afternoon"]) and eleanor_btn_lucasroom == True:
                elements.append([(665, 321),"images/sadie_house/lucas_room/eleanor_btn2{dark}_{state}.png", "eleanor_teaching_event2", "*^"])
            
            if eleanor_story == 25 and now(["morning", "afternoon"]) and eleanor_btn_lucasroom == True:
                elements.append([(665, 321),"images/sadie_house/lucas_room/eleanor_btn3{dark}_{state}.png", "eleanor_teaching_event3", "*^"])
            
            
            
            if eleanor_story == 2:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "$blocked$", None ])
            elif eleanor_story == 7:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "$blocked$",None])
            elif eleanor_story == 15:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "$blocked$",None ])
            elif eleanor_story == 25:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "$blocked$",None ])
            elif konami_story == 3:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "$blocked$",None ])
            else:
                elements.append([(1008, 407),"images/sadie_house/lucas_room/inter_bedlucas1{dark}_{state}.png", "lucas_bed_interaction", "*^"])
            
            
            
            if lucas_scope == True and not loc_lucasroom["scope_done"]:
                elements.append([(1792, 403),"images/sadie_house/lucas_room/inter_telescope{dark}_{state}.png", "mcroom_scope_inter", "*^"])
            
            
            if christmas_treedeco_btn == True and christmas_treedeco_used == False:
                elements.append([(316, 743),"images/sadie_house/lucas_room/inter_treebox{dark}_{state}.png", "mcroom_treebox_inter", "*^"])
            
            
            if christmas_santasuit_btn == True and lucas_wearsanta_suit == False:
                elements.append([(1479, 623),"images/sadie_house/lucas_room/inter_outfitsanta{dark}_{state}.png", "mcroom_santasuit_inter", "*^"])
            
            
            if eleanor_story == 7:
                elements.append([(1522, 195),"images/sadie_house/lucas_room/inter_doorlucas1{dark}_{state}.png", "$blocked$","@^LOCKED" ])
            elif eleanor_story == 15:
                elements.append([(1522, 195),"images/sadie_house/lucas_room/inter_doorlucas1{dark}_{state}.png", "$blocked$","@^LOCKED" ])
            elif eleanor_story == 25:
                elements.append([(1522, 195),"images/sadie_house/lucas_room/inter_doorlucas1{dark}_{state}.png", "$blocked$","@^LOCKED" ])
            elif konami_story == 3:
                elements.append([(1522, 195),"images/sadie_house/lucas_room/inter_doorlucas1{dark}_{state}.png", "$blocked$","@^LOCKED" ])
            else:
                elements.append([(1522, 195),"images/sadie_house/lucas_room/inter_doorlucas1{dark}_{state}.png", "goto_hallwayf2", "*>"])
            
            
            elements.append([(1567, 799),"images/sadie_house/lucas_room/inter_doujin{dark}_{state}.png", "lucas_room_magazine_inter", "*^"])        

















default loc_lucasroom = LocationLucasRoom()

label goto_lucasroom:
    call set_location ("loc_lucasroom") from _call_set_location_17
    show screen main_hud_icon

    if chores_sadie_talk == 0 and shop_first_time == True:
        jump lucas_room_chorez
        return

    if konami_story == 17 and now(["night", "evening"]):
        $ konami_phone_points += 1
        $ konami_story += 1
        return

    if now(["night", "evening"]) and konami_story == 21:
        $ konami_phone_points += 1
        $ konami_story += 1
        return

    if christmas_story == 2:
        jump christmas_l_2
        return



    if jada_story == 7:
        jump jada_continue3rd_scene2
        return
    if jada_story == 8:
        jump jada_3rd_end
        return

    if eleanor_story == 5 and now("evening") and now(["tuesday", "thursday"]):
        hide screen main_hud_icon
        play sound "music/doorbell_03.mp3"
        l_mc "That must be Ms. Eleanor, I better get to the front door"
        $ eleanor_story += 1
        jump goto_lucasroom
        return

    if eleanor_story == 1:
        hide screen main_hud_icon
        l_mc "hmm.. what is that?"
        play sound "music/doorbell_03.mp3"
        pause
        l_mc "Someone's at the front door, I wonder who it is"
        l_mc "I better check it out"
        $ eleanor_story += 1
        jump goto_lucasroom
        return

    if eleanor_story == 13 and now("afternoon") and now(["tuesday", "thursday"]):
        hide screen main_hud_icon
        play sound "music/doorbell_03.mp3"
        l_mc "That must be Ms. Eleanor, I better go answer it"
        $ eleanor_story += 1
        jump goto_lucasroom
        return


    if eleanor_story == 26:
        jump eleanor_story_third_end
        return

    if eleanor_story == 24:
        jump eleanor_story_third_sessionz
        return

    if eleanor_story == 16:
        jump eleanor_teaching_event2zz
        return

    if eleanor_story == 18:
        $ eleanor_story += 1
        $ eleanor_phone_points += 1


    if eleanor_story == 20 and now("morning") and now(["tuesday", "thursday"]):
        play sound "music/doorbell_03.mp3"
        l_mc "I think eleanor is by the door"
        l_mc "Should check"
        $ eleanor_story += 1
        jump goto_lucasroom
        return

    if eleanor_story == 28 and now("night") and now(["tuesday", "thursday"]):
        play sound "music/doorbell_03.mp3"
        l_mc "I think eleanor is by the door"
        l_mc "Should check"
        $ eleanor_story += 1
        jump goto_lucasroom
        return

    if eleanor_story == 30 and now("evening"):
        jump eleanor_event_fourth_bed
        return

    if eleanor_story == 31 and now("morning"):
        jump eleanor_event_fourth_end
        return






    if eleanor_story == 8:
        window hide
        hide screen main_hud_icon
        show lucas normal pose4 default at left with Dissolve(.3)
        show eleanor normal pose default at right with Dissolve(.3)
        pause
        show lucas normal pose4 default_talk
        l_mc "We are done for today already ?"
        show lucas normal pose4 default
        show eleanor normal pose default_talk
        l_eleanor "Yeah, I'm sorry but I think your brain has had enough for today"
        show lucas normal pose4 default_talk
        show eleanor normal pose default
        l_mc "When can I call you again?"
        show lucas normal pose4 default
        show eleanor normal pose2 default_talk
        l_eleanor "Actually, there are some student learning modules I want you to take on your computer. I’ve assigned some of these from the school’s internet database"
        show lucas normal pose4 puzzle_talk
        show eleanor normal pose2 default
        l_mc "Student modules? You mean like online classes"
        show lucas normal pose4 mkay
        show eleanor normal pose1 default_talk
        l_eleanor "Well kind of but these will just be more like your homework. I want you to complete the student modules I’ve sent to your student account as soon as you’ve logged in"
        l_eleanor "once you’ve completed your homework, then you can give me another call to come over and help you more like we did today"
        l_eleanor "Does that sound fair?"
        show lucas normal pose4 glad_talk
        show eleanor normal pose default
        l_mc "I guess so. You can expect me to call you pretty soon because I'll be completing those modules in no time"
        show lucas normal pose4 glad
        show eleanor normal pose3 default
        l_eleanor "(This kid really is onto something, what did I do to have him all focused on studying?)"
        show lucas normal pose4 glad
        show eleanor normal pose default_talk
        l_eleanor "Wow... you really want to see me sooner"
        show lucas normal pose4 what
        show eleanor normal pose grumpy_talk
        l_eleanor "This is just our first day Lucas"
        show lucas normal pose4 sad_talk
        show eleanor normal pose grumpy
        l_mc "No . . .I just. ."
        show lucas normal pose4 assured
        show eleanor normal pose default_talk
        l_eleanor "I'll be leaving now, I know where the door is so no need to walk me out"
        l_eleanor "I'll see you soon"
        show lucas normal pose4 glad_talk
        show eleanor normal pose default
        l_mc "Okay, yeah ! see you soon"
        hide eleanor normal pose default with moveoutright
        show lucas normal pose5 puzzle with dissolve
        pause

        $ eleanor_story += 1
        jump goto_lucasroom
        return












    if yoga_sadie_ended == True:
        hide screen main_hud_icon
        show lucas normal pose6 what at left with Dissolve(0.2)
        pause
        l_mc "That was the last thing I needed to happen to confuse me even more about my [sadie_relationship_input]."
        show lucas normal mkay_talk
        l_mc "I really need to stop putting myself in those situations with her. Knowing how dumb she can be, its granted that she wont make it any easier for me."
        l_mc "What a degenerate I am"
        l_mc "But sometimes its hard to say no to her. I do love her and like to spend time with her"
        l_mc "These moments will most likely be unavoidable but I still have to try and make the best of those problems."
        show lucas normal pose4
        l_mc "What a nightmare. I wish she was more aware of what she does. *Sigh*"
        $ sadie_story += 1
        hide lucas normal what at left with Dissolve(0.2)
        $ yoga_sadie_scene = False
        $ yoga_sadie_ended = False
        $ yoga_sadie = True

        $ sadie_yoga_sch += 1
        show screen journal_updated_notify with dissolve
        jump goto_lucasroom
        return





    return


label lucas_room_chorez:
    l_mc "I'm actually broke right now and I stopped getting an allowence after the incident at school. There has to be some way to get money."
    l_mc "I better go ask [sadie_refer_input] if I can do anything to start making some mulla around here."
    $ chores_sadie_talk += 1
    return

label lucas_dressup:
    show lucas normal pose34 default with dissolve
    $ renpy.pause ()
    hide lucas normal pose34 default with dissolve
    show lucas normal pose35 default with dissolve
    l_mc "Alright, lets get started."
    jump goto_lucasroom
    return

label lucas_room_magazine_inter:

    show magazine_girl_nisego
    pause
    l_mc "Man I love this guy. Draws some of the best doujin out there. Hope I can be as good as Nisego some day."
    jump goto_lucasroom
    return


label konami_phoneshort_event5:
    l_mc "That was very short."
    l_mc "Judging by how short that text was, I’m sure she’s already figured out that I caught her masturbating."
    l_mc "What am I going to do now? Dammit!"
    l_mc "I’ll just have to go and see what she has to say while her mom is out of the house."
    l_mc "I should show up early in the afternoon"
    $ konami_story += 1
    jump goto_lucasroom
    return
label konami_phoneshort_event5z:
    hide screen phone_contacts
    l_mc "It looks like our time together will be put on hold for a while this time."
    l_mc "*sigh*"
    $ konami_story += 1
    jump goto_lucasroom
    return


label mcroom_treebox_inter:
    if christmas_santasuit_btn == False:
        l_mc "I got to buy the santa suit first, before I decorate the house !"
        return
    elif True:

        if now(["morning", "evening", "afternoon"]):
            l_mc "I’m going to decorate the house with this stuff but I better wait until it’s midnight so that [sadie_refer_input] is fully asleep. I’d Like to really surprise her and give her some of that Christmas joy."
            return
        if now(["night"]):
            l_mc "Time is of the essence; I need to do this quickly and quietly or I’ll wake her up."
            $ christmas_treedeco_used = True
            $ christmas_story += 1
            jump goto_livingf1
            return
    return

label mcroom_santasuit_inter:
    l_mc "I should probably decorate the Tree first, and this outfit does look nice !"
    return

label mcroom_scope_inter:
    if scope_inter_1 == False:
        hide screen main_hud_icon
        show frame_telescope with dissolve
        l_mc "What is this ? Did my [sadie_relationship_input] place this here ?"
        l_sadie "Found this stashed away in the attic. thought you might like it"
        l_mc "Thanks, [sadie_refer_input], buuuut I think the front lens is broken."
        l_mc "I should take this up to the attic and watch some stars."
        l_mc "But I need to buy a replacement lens for it first. I can buy it online through my computer as long as I have the money"
        l_mc "I’ll leave this here until I receive the new lens. "
        hide frame_telescope with dissolve
        $ jada_gallery_profile = True
        $ renpy.notify("Jada's Gallery Unlocked")
        $ jada_journal = True
        $ scope_inter_1 = True
        $ quest_log_active.add("jada")
        show screen journal_updated_notify with dissolve
        show screen main_hud_icon
        return
    if item_lens in inv:
        $ inv.remove(item_lens)
        l_mc "That should do the trick. Looks good and functional to me now."
        l_mc "I can use this up in the attic window whenever I want now. As long as it’s night time It should be fine."
        l_mc "Won’t be of much use during the day time though."
        $ loc_lucasroom["scope_done"] = True
        $ scope_attic1 = True
        jump goto_lucasroom
        return
    elif True:
        l_mc "I need to buy a new “Lens” for it from my computer first. "

        return


    return

label lucas_bed_interaction:
    label lucas_bed_choice:
        hide screen main_hud_icon
        if konami_story == 3:
            l_mc "I should look at the phone and text konami"
            return

        menu:

            "Text Konami" if now(["night", "evening"]) and konami_story == 2:
                $ konami_story += 1
                $ konami_phone_points += 1
                if now(["evening"]):
                    $ now.advance()
                jump goto_lucasroom
                return

            "Rest" if now(["morning", "afternoon", "evening"]):
                if sadie_night_couch_keypad == False:
                    l_mc "I should explore around before I rest"
                    jump goto_lucasroom
                    return

                jump lucas_rest
            "Sleep" if True:

                if sadie_night_couch_keypad == False:
                    l_mc "I should explore around before I rest"
                    jump goto_lucasroom
                    return
                if now(["morning", "afternoon"]):

                    l_mc "I shouldn't sleep yet.. not even evening or night yet"
                    jump goto_lucasroom
                    return
                elif True:
                    if now(["night"]):
                        jump lucas_sleep
                    elif now(["evening"]):
                        $ now.advance()
                        jump lucas_sleep
            "Leave" if True:

                jump goto_lucasroom
                return


label goto_lucaspc_inter:
    if pc_lucas_map == False:
        $ pc_lucas_map = True
        show screen map_updated_notify with dissolve
        return

    if sadie_night_couch_keypad == False:
        l_mc "I should explore around first"
        return

    jump goto_lucaspc
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

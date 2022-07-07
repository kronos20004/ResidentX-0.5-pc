








image living_room_blur_day:
    "images/sadie_house/living_room/bg_livingroom.jpg"
    alpha 0.4
    blur 13
image living_room_blur_dark:
    "images/sadie_house/living_room/bg_livingroom_dark.jpg"
    alpha 0.4
    blur 13

init python:
    class Locationlivingf1(Location):
        title="Living F1"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/living_room/bg_livingroom{dark}.jpg")
            
            elif now(["night"]):
                elements.append("images/sadie_house/living_room/bg_livingroom_midnight.jpg")
            
            
            if christmas_decoration_enable == True:
                if now(["morning", "afternoon", "evening"]):
                    elements.append("images/sadie_house/living_room/livingroom_christmas{dark}.png")
                elif now(["night"]):
                    elements.append("images/sadie_house/living_room/livingroom_christmas_midnight.png")
            
            
            elements.append([(1400,238),"images/sadie_house/living_room/inter_doorbasement1{dark}_{state}.png", "goto_basement", "*>"])
            
            
            
            
            
            
            
            
            
            
            
            
            if char_at("sadiecouch","sadieliv") and not is_talking("sadiecouch"):
                elements.append([(1124, 413),"images/sadie_house/living_room/charbutton_sadie2{dark}_{state}.png", "sadie_interaction", "*^"])  
            
            
            
            if random_tv_screen == 1 and now("evening"):
                elements.append([(404,230),"images/sadie_house/living_room/inter_tvgirl_{state}.png", "tv_interaction", "*^"])
            elif random_tv_screen == 2 and now("evening"):
                elements.append([(404,230),"images/sadie_house/living_room/inter_tvspider_{state}.png", "tv_interaction", "*^"])
            else:
                elements.append([(404,230),"images/sadie_house/living_room/inter_tv1{dark}_{state}.png", "tv_interaction", "*^"])
            
            
            
            elements.append([(910,269),"images/sadie_house/living_room/inter_dooroffice2{dark}_{state}.png", "goto_officef1", "*>"])
            
            
            elements.append([(621,246),"images/sadie_house/living_room/inter_hallway1{dark}_{state}.png", "goto_hallwayf1", "*>"])
            
            
            if exit_btn == True:
                elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_lobbyf1", "*>"])










default loc_livingf1 = Locationlivingf1()

label goto_livingf1:
    call set_location ("loc_livingf1") from _call_set_location_2
    show screen main_hud_icon
    if christmas_story == 1:
        jump christmas_l_1
        return

    if christmas_story == 3:
        jump christmas_l_3
    return

label tv_interaction:
    if tv_map_icon == False:
        $ tv_map_icon = True
        show screen map_updated_notify with dissolve
        return

    if sadie_story == 4:
        jump sadie_tv_story1
        return
    elif True:

        if char_at("sadiecouch","sadieliv") == True:
            hide screen main_hud_icon
            l_mc "[sadie_refer_input] is watching at the moment"
            jump goto_livingf1
            return

        if now(["morning", "afternoon"]):
            hide screen main_hud_icon
            if now(["morning","afternoon"]):
                show living_room_blur_day
            if now(["night", "evening"]):
                show living_room_blur_dark
            menu:
                "Skip time ?" if True:
                    jump tv_skip_time
                    return
                "Not yet" if True:
                    jump goto_livingf1
                    return

            label tv_skip_time:


                hide screen main_hud_icon
                scene movienight_bg_day
                show lucas tv pose mkay with dissolve
                $ renpy.pause(1, hard=True)
                l_mc "** . . . . . . "


                $ now.advance()
                $ renpy.scene()
                jump goto_livingf1
                return

        elif now(["evening"]):
            l_mc "Don't feel like watching ."
            jump goto_livingf1
            return

        elif now(["night"]):
            hide screen main_hud_icon
            l_mc "it's too late in the night to watch now . ."
            jump goto_livingf1
            return

label sadie_interaction:
    label sadie_couch_interaction:
        hide screen main_hud_icon
        $ sadiecouch_talking = True
        $ exit_btn = False
        if now(["morning","afternoon"]):
            show living_room_blur_day
        if now(["night", "evening"]):
            show living_room_blur_dark
        show sadie normal pose default at right with Dissolve(.15)
        show lucas normal pose4 default at left with Dissolve(.15)
        menu:
            "What are you watching ?" if sadie_story < 6:

                jump sadie_watch_interaction
                return

            "Hey [sadie_refer_input], what you up to ?" if sadie_story == 14:
                jump sadie_movietalk2
                return

            "Let's watch the movie !" if sadie_story == 15:
                jump sadie_movie_8night
                return

            "Ask her about spending time together" if sadie_story > 14 and sadie_convo1_done == False:
                jump sadie_inter_convo2
                return

            "Movie Night" if sadie_story == 7:

                $ sadiecouch_talking = False
                $ exit_btn = True
                jump sadie_movie_7night

            "Ask her about making money" if chores_sadie_talk == 1:
                jump sadie_living_chore_talk
                return

            "Ask her about Christmas (New Update)" if christmas_enable == 0 and chores_sadie_talk == 2:
                jump sadie_christmas_trigger
                return

            "Ask her about the closet keypad" if sadie_night_couch_keypad == False:

                jump sadie_keypad_interaction
                return
            "Leave" if True:


                $ sadiecouch_talking = False
                $ exit_btn = True
                $ renpy.scene()
                jump goto_livingf1

        jump goto_livingf1
        return

label sadie_living_chore_talk:
    show lucas normal default_talk
    l_mc "Hey [sadie_refer_input], im kind of in need of some money right now so is there anything at all that I can do to get some allowence back?"
    show sadie normal assured_talk
    show lucas normal default
    l_sadie "Hmmmmm. . . well maybe I can give you some money if you start doing chores around the house. how's that sound?"
    show sadie normal assured
    show lucas normal happy_talk
    l_mc "Awesome! sounds good to me. so what do you have in mind?"
    show sadie normal default_talk
    show lucas normal happy
    l_sadie "Well for starters, you can mow the lawn every morning. the grass has been getting pretty long."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Consider it done"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "You can also do the dirty laundry every monday."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Monday . Got it !"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "And I supoose you can take care of the dishes every day. In the afternoon"
    show sadie normal default
    show lucas normal happy_talk
    l_mc "Nice. you wont ever have to wash another dish in your life, [sadie_refer_input]. I'll be your glorified dishwasher."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Thanks honey."
    show sadie normal happy
    show lucas normal glad_talk
    l_mc "NO! thank you. "
    show sadie normal happy_talk
    show lucas normal glad
    l_sadie "Have fun, dear"
    $ chores_sadie_talk += 1
    $ chores_unlocked = True




    jump sadie_couch_interaction
    return

label sadie_watch_interaction:
    show sadie normal default_talk with Dissolve(.15)
    l_sadie "Oh, I’m just watching pretty little liars. It’s pretty boring but I’m sure your company will help."
    show lucas normal pose4 default_talk
    show sadie normal pose1 default
    l_mc "Sorry [sadie_refer_input]. Maybe next time, I swear."
    show lucas normal pose5 puzzle
    l_mc "(I don’t think I’m ready for another risky situation to make me doubt my relationship with her.)"
    show sadie normal assured_talk
    show lucas normal pose5 default
    l_sadie "Fine, leave your little old [sadie_relationship_input] all by herself than"
    show sadie normal assured
    show lucas normal pose4 happy_talk
    l_mc "Don’t worry. We’ll watch another movie sometime soon."
    show sadie normal awe_talk
    show lucas normal pose4 default
    l_sadie "Fine. Goodbye honey"
    show sadie normal awe
    show lucas normal pose4 default_talk
    l_mc "Bye."
    jump sadie_couch_interaction
    return

label sadie_keypad_interaction:
    show lucas normal pose4 puzzle_talk with Dissolve(.15)
    l_mc "I was wondering."
    show sadie normal default_talk
    show lucas normal pose5 puzzle
    l_sadie "Hmm? What’s on your mind?"
    show lucas normal pose4 mkay_talk
    show sadie normal default
    l_mc "Have you seen that weird keypad in your closet ?"
    l_mc "I know it's probably one of [leo_refer_input]'s constructions but what is it for anyway?"
    show lucas normal pose4 default
    show sadie normal default_talk
    l_sadie "I have no clue what that thing is for, to be honest"
    show sadie normal sad_talk
    l_sadie "He never really shared anything about it and we didn’t really talk much. You know he was always busy with his own work."
    l_sadie "So, I didn’t really bother to ask."
    show sadie normal sad
    l_sadie ". . ."
    show lucas normal pose4 sad_talk
    l_mc "[sadie_refer_input] . . ."
    l_mc "I miss him too."
    show lucas normal pose4 happy_talk
    l_mc "But don’t worry, I’ll be here for you for as long as you want."
    show sadie normal happy
    pause
    hide sadie normal pose
    hide lucas normal pose4
    show sadie universal_hugz pose1 with dissolve
    pause
    show sadie universal_hugz pose2
    l_sadie "Thank you honey. Now don’t start complaining when I come for more consolation ok."

    show sadie universal_hugz pose3
    l_mc "Yeah, sure thing. We’re here for each other."

    pause
    hide sadie universal_hugz
    show sadie normal pose default_talk at right
    show lucas normal pose5 default at left
    l_sadie "Maybe you can find something about that keypad in his office room. Just don’t make a complete mess in there. I like to keep it clean just as he left it."

    show sadie normal default
    show lucas normal pose5 default_talk
    l_mc "Don't worry. I like to keep it neat too."
    l_mc "Ok I'll see you later."
    show sadie normal default_talk
    show lucas normal pose5 default
    l_sadie "See you later dear."

    $ sadie_night_couch_keypad = True
    $ key_pad_unlocked = True
    show screen journal_updated_notify with dissolve
    jump sadie_couch_interaction
    return

label sadie_christmas_trigger:

    show lucas normal default_talk
    l_mc "So, Christmas Is coming up pretty soon and we still haven’t decorated you know?"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "I’m so sorry dear. It totally slipped my mind; I guess with Bailey away from the house for college, and your [leo_refer_input] not around anymore, it just hasn’t felt the same way anymore."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Yeah, I know [sadie_refer_input]. Don’t worry though, just leave this to me and I’ll make it feel a little better. You still have me around so I’ll do whatever I need to do."
    show sadie normal sad_talk
    show lucas normal default
    l_sadie "Oh dear, I don’t know what I’d do without you. I’m sorry if I’ve been a little bit of a drag to have around with my emotions these days."
    show sadie normal default
    show lucas normal happy_talk
    l_mc "Don’t be dumb, you’re my [sadie_relationship_input], why would you be a drag on me? You’ve always been there for me so it’s time I pay back what’s due to the greatest [sadie_relationship_input] in the world."
    show sadie normal awe_talk
    show lucas normal happy
    l_sadie "Don’t make me cry now please."
    show sadie normal awe
    show lucas normal happy_talk
    l_mc "I got you, just leave this year to me. I better go and start prepping now. See you when everything is ready."
    show sadie normal awe_talk
    show lucas normal happy
    l_sadie "Bye honey."

    $ sadiecouch_talking = False
    $ christmas_enable += 1
    show lucas normal default
    hide sadie normal
    jump christmas_introl
    return

label christmas_introl:
    l_mc "Alright, I better make this a good Christmas year for her. Hate to see her a little depressed when her own daughter won’t show up for Christmas."
    show lucas normal puzzle
    l_mc "I’ll start looking online for some decorations and maybe a present as well. There should be some good stuff to shop for."

    $ exit_btn = True
    $ go_back_btn = True
    jump goto_livingf1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

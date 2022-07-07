init python:
    class LocationSadiebalcony(Location):
        title="Balcony"
        def scene(self,elements):
            elements.append("images/sadie_house/sadie_room/sadie_balcony/bg_balcony{dark}.jpg")
            
            
            elements.append([(1086, 199),"images/sadie_house/sadie_room/sadie_balcony/inter_doorbalcony1{dark}_{state}.png", "goto_sadieroom", "*>"])
            
            
            
            if char_at("sadiebaclony","sadie_d") and not is_talking("sadiebaclony"):
                elements.append([(620, 300),"images/sadie_house/sadie_room/sadie_balcony/CharButton_Sadie1{dark}_{state}.png", "sadie_balcony_interaction", "*<"])   
            
            
            
            
            
            
            
            
            if now(["night"]):
                
                elements.append([(290,373),"images/sadie_house/sadie_room/sadie_balcony/inter_sexytime2_dark.png", None])

default loc_sadiebalcony = LocationSadiebalcony()

label goto_sadiebalcony:
    call set_location ("loc_sadiebalcony") from _call_set_location_20
    show screen main_hud_icon



    return

label sadie_balcony_interaction:
    label sadie_bcl_int_label:
        hide screen main_hud_icon




        $ sadiebaclony_talking = True
        show sadie normal pose default at right with Dissolve(.15)
        show lucas normal pose4 default at left with Dissolve(.15)

        menu:






            "Hey, maybe we can watch another movie tonight, yeah?" if sadie_story == 6:


                jump sadie_watch_tonight
                return


            "How is work going?" if sadie_story < 8:

                jump sadie_work_talk
                return

            "Talk about School." if sadie_story < 8:

                jump sadie_schooltalk_inter
                return


            "You still missing Bailey ?" if konami_story == 0:
                show sadie normal pose default_talk
                l_sadie "Of course, I do. Any mother would miss their children when off to college. Don’t you miss her too?"
                show sadie normal default
                show lucas normal pose4 puzzle_talk
                l_mc "Maybe. It’s nice to have a little breather from her. She was always so protective and clingy with me. "
                show sadie normal default
                show lucas normal default
                l_sadie "She only cares for you. And she’s older than you so it’s natural for her to be protective of you. I bet she’s thinking about you right now."
                show sadie normal grumpy
                show lucas normal sad_talk
                l_mc "I know I know. I don’t completely hate being pampered. It’s just a nice change of pace."
                show sadie normal smirk_talk
                show lucas normal sad
                l_sadie "Does that mean you don’t like getting pampered by me?"
                show sadie normal smirk
                show lucas normal happy_talk
                l_mc "What? No no, I don’t mind at all. Honestly."
                show sadie normal smirk_talk
                show lucas normal happy
                l_sadie "And here I was thinking I’d miss you when you go off to college as well."
                show sadie normal smirk
                show lucas normal glad_talk
                l_mc "Yeah yeah, whatever. "



                $ konami_journal = True
                $ konami_story += 1
                $ konami_treehouse = True
                $ quest_log_active.add("konami")
                show screen journal_updated_notify with dissolve
                hide screen journal_updated_notify with dissolve
                $ sadiebaclony_talking = False
                $ info_log_active.add("konamiz")
                jump sadie_bcl_int_label

            "You ready for yoga?" if sadie_story == 8 and yoga_sadie == False and now(["afternoon"]):
                show sadie normal happy_talk
                show lucas normal happy
                l_sadie "Oh really? Come on then. Let’s go, what are we waiting for. I’m ready"
                show sadie normal happy
                show lucas normal default_talk
                l_mc "Ok, just calm down will you"
                l_mc "I was just going to ask if you have any bottoms I can use. I don’t have any clean pants or shorts."
                show lucas normal puzzle_talk
                l_mc "Bottoms for men of course."
                show sadie normal default_talk
                show lucas normal default
                l_sadie "Yeah, I still have some of Leo’s old clothing in my room’s closet. You two were almost the same height, so I’m sure the clothes will fit you."
                show sadie normal default_talk
                show lucas normal default
                l_sadie "Are we starting now ?"
                show sadie normal default
                menu:
                    "No" if True:
                        show sadie normal default
                        show lucas normal happy_talk
                        "Maybe not right now, give me some time. I’ll let you know when I’m ready"
                        show sadie normal awe_talk
                        show lucas normal happy
                        "Alright but don’t leave me hanging for too long."
                        show sadie normal awe
                        show lucas normal default_talk
                        "I won’t. "
                        jump sadie_balcony_interaction
                        return
                    "Yes" if True:

                        show sadie normal default
                        show lucas normal default_talk
                        "Yeah, I’ll go check your closet for a spare change of clothes and meet up back here. "
                        show sadie normal default_talk
                        show lucas normal default
                        "I have to get changed as well so let’s go get changed together."
                        show sadie normal default
                        show lucas normal alert_talk
                        "Wait what? Together?"
                        show sadie normal default_talk
                        show lucas normal alert
                        "Yeah, what’s the problem?"
                        show sadie normal default
                        show lucas normal happy_talk
                        "No problem at all, I guess. let’s go to your room than."

                        $ sadie_story += 1
                        $ sadiebaclony_talking = False
                        jump sadie_bcl_int_label
                        return
            "Leave" if True:


                $ sadiebaclony_talking = False
                jump goto_sadiebalcony
                return

    jump goto_sadiebalcony
    return



label sadie_watch_tonight:
    show lucas normal default_talk
    l_mc "It was pretty fun. Even if we didn’t end up watching the whole thing"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "Took you long enough. I was hoping you’d ask sooner."

    show sadie normal happy_talk
    l_sadie "I promise not to fall asleep this time, but only if you pick a movie that I’d like this time. *giggle*"
    show sadie normal default
    show lucas normal default_talk
    l_mc "Well, what kind of movie you got in mind?"
    show sadie normal grumpy
    show lucas normal mkay
    l_sadie "Hmmmmm . . ."
    show sadie normal happy_talk
    l_sadie "let’s go with a comedy. How about that?"
    show sadie normal awe
    show lucas normal glad_talk
    l_mc "And a comedy you shall have milady."
    show lucas normal default
    show sadie normal happy_talk
    l_sadie "Ooohh, I can’t wait. Don’t leave me hanging though."
    show lucas normal glad_talk
    show sadie normal happy
    l_mc "I wouldn’t dare to, see you later at night."
    show lucas normal default
    show sadie normal default_talk
    l_sadie "Bye bye."


    $ sadie_story += 1
    $ sadiebaclony_talking = False
    show screen journal_updated_notify with dissolve



    jump goto_sadiebalcony
    return

label sadie_watch_tonightz:
    show lucas normal default_talk
    l_mc "It was pretty fun. Even if we didn’t end up watching the whole thing"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "Took you long enough. I was hoping you’d ask sooner."

    show sadie normal happy_talk
    l_sadie "I promise not to fall asleep this time, but only if you pick a movie that I’d like this time. *giggle*"
    show sadie normal default
    show lucas normal default_talk
    l_mc "Well, what kind of movie you got in mind?"
    show sadie normal grumpy
    show lucas normal mkay
    l_sadie "Hmmmmm . . "
    show sadie normal happy_talk
    l_sadie "let’s go with a comedy. How about that?"
    show sadie normal awe
    show lucas normal glad_talk
    l_mc "And a comedy you shall have milady."
    show lucas normal default
    show sadie normal happy_talk
    l_sadie "Ooohh, I can’t wait. Don’t leave me hanging though."
    show lucas normal glad_talk
    show sadie normal happy
    l_mc "I wouldn’t dare to, see you later at night."
    show lucas normal default
    show sadie normal default_talk
    l_sadie "Bye bye."

    $ sadiekit_talking = False
    $ sadie_story += 1
    show screen journal_updated_notify with dissolve



    jump kitchen_sadie_inter
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

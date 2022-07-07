init python:
    class Locationkitchenf1(Location):
        title="Kitchen F1"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/kitchen/bg_kitchen{dark}.jpg")
            elif now(["night"]):
                elements.append("images/sadie_house/kitchen/bg_kitchen_midnight.jpg")
            
            
            
            elements.append([(807,470),"images/sadie_house/kitchen/kitchen_sink{dark}_{state}.png","kitchen_sink_inter", "*^"])
            
            
            
            if go_back_btn == True:
                elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_lobbyf1", "*^"])
            
            
            if char_at("sadiekit","kitchen") and not is_talking("sadiekit"):
                elements.append([(1157, 425),"images/sadie_house/kitchen/CharButton_Sadie6_{state}.png", "kitchen_sadie_inter", "@*<"])  










default loc_kitchenf1 = Locationkitchenf1()

label goto_kitchenf1:
    call set_location ("loc_kitchenf1") from _call_set_location_22
    show screen main_hud_icon

    if sadie_story == 3:
        jump sadie_chapter_1_kitchen
        return


    return


label kitchen_sadie_inter:
    label sadie_kitchen_int_label:
        hide screen main_hud_icon
        $ sadiekit_talking = True
        $ go_back_btn = False
        show sadie normal pose default at right with Dissolve(.15)
        show lucas normal pose4 default at left with Dissolve(.15)
        menu:
            "Hey, maybe we can watch another movie tonight, yeah ?" if sadie_story == 6:

                jump sadie_watch_tonightz
                return


            "Hey [sadie_refer_input], what you up to ?" if sadie_story == 14:
                jump sadie_movietalk2_kitchen
                return

            "How is work going?" if sadie_story < 8:

                jump sadie_work_talkz
                return

            "Talk about School." if sadie_story < 8:

                jump sadie_schooltalk_interz
                return
            "Ask her about making money" if chores_sadie_talk ==1:
                jump sadie_kitchen_chore_talk
                return

            "You still missing Bailey ?" if konami_story == 0:
                jump sadie_konami_kitchen_talk
                return

            "Ask her about Christmas (New Update)" if christmas_enable == 0 and chores_sadie_talk == 2:
                jump sadie_christmas_trigger
                return
            "Leave" if True:

                $ sadiekit_talking = False
                $ go_back_btn = True
                $ renpy.scene()
                jump goto_kitchenf1
                return


label sadie_kitchen_chore_talk:
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
    $ sadiekit_talking = False
    $ go_back_btn = True
    $ renpy.scene()
    jump goto_kitchenf1
    return

label sadie_konami_kitchen_talk:
    show sadie normal default_talk
    l_sadie "Of course, I do. Any mother would miss their children when off to college. Don’t you miss her too?"
    show sadie normal default
    show lucas normal puzzle_talk
    l_mc "Maybe. It’s nice to have a little breather from her. She was always so protective and clingy with me. "
    show sadie normal default
    show lucas normal grump_talk
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
    $ sadiekit_talking = False
    $ go_back_btn = True
    $ konami_journal = True
    $ konami_story += 1
    $ info_log_active.add("konamiz")
    $ konami_treehouse = True

    show screen journal_updated_notify with dissolve

    jump goto_kitchenf1
    return







































label kitchen_sink_inter:
    if chores_unlocked == False:
        l_mc ". . . ?"
        return
    elif True:
        menu:
            "Work ?" if True:
                if kitchen_sink_work == True:
                    l_mc "Alright, let's get started"
                    jump clean_kitchen_start
                    return
                elif True:

                    l_mc "Already cleaned, try tomorrow."
                    jump goto_kitchenf1
                    return
            "Nah" if True:

                jump goto_kitchenf1
                return

        label clean_kitchen_start:
            hide screen main_hud_icon
            show black with dissolve
            scene chores_dishes_01
            hide black
            pause
            $ kitchen_sink_work = False
            l_mc "Let's grab the dishes !"
            show chores_dishes_02 with Dissolve(.3)
            pause
            show chores_dishes_02 with hpunch
            pause
            hide chores_dishes_02 with Dissolve(.3)
            l_mc "There we go."
            $ random_cash_range = renpy.random.randint(2,3)
            $ main_mc.got_cash(random_cash_range)

            show screen money_earn_display with Dissolve(.3)


            $ renpy.scene()
            $ now.advance()
            show screen main_hud_icon
            jump goto_kitchenf1
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

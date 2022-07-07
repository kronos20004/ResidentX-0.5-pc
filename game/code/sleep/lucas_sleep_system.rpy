



transform lucas_sleep_position:
    xpos -20
    ypos .68


label lucas_rest:
    hide screen main_hud_icon
    if now(["evening", "night"]):
        scene bg_bedlucas_alt
        show bg_bedlucas_doorclosed_alt
        show lucas sleep_night sleep1
        l_mc "errr"
        $ now.advance()
        jump goto_lucasroom
        return

    if now(["morning", "afternoon"]):
        scene bg_bedlucas
        show bg_bedlucas_doorclosed
        show lucas sleep_day pose sleep1
        l_mc "huuuu"
        $ now.advance()
        pause
        jump goto_lucasroom
        return

label lucas_sleep:
    $ random_tv_screen = renpy.random.randint(1,2)
    $ kitchen_sink_work = True



    hide screen main_hud_icon
    scene bg_bedlucas_alt
    show bg_bedlucas_doorclosed_alt
    show lucas sleep_night sleep1
    stop music
    play sound "music/sfx_sleep_01.wav"
    pause

    l_mc "errr"


    pause
    if jada_story == 1:
        $ jada_story += 1

    if jada_story == 5 and now(["monday", "tuesday", "thursday", "friday"]):
        $ jada_story += 1

    if item_christmastree_arrival == 1:
        $ item_christmastree_arrival += 1
        $ quickies_phone_points += 1



    if item_christmassanta_arrival == 1:
        $ item_christmassanta_arrival += 1
        $ quickies_phone_points += 1




    if item_lens_arrival == 1:
        $ item_lens_arrival += 1
        $ quickies_phone_points += 1


    if item_manga_arrival == 1:
        $ item_manga_arrival += 1
        $ quickies_phone_points += 1


    if bookshelf_close == False and office_strangebattery == True:
        $ bookshelf_close = True


    scene lucas_room_day

    $ now.advance()
    stop music
    play sound "music/yawn_01.mp3"
    call set_location ("loc_lucasroom") from _call_set_location_25


    if eleanor_story == 0 and now("thursday"):
        $ eleanor_story += 1

    if konami_story == 5:
        $ konami_story += 1
        $ konami_phone_points += 1

    if konami_story == 9:
        $ konami_story += 1
        $ konami_phone_points += 1

    if konami_story == 14:
        $ konami_story += 1
        $ konami_phone_points += 1

    if now(["tuesday", "thursday"]):
        if eleanor_story == 3:
            $ eleanor_story += 1
            $ eleanor_phone_points += 1

    if eleanor_story == 9 and eleanor_2nd_text == False:
        $ eleanor_2nd_text = True
        $ eleanor_phone_points += 1

    if eleanor_story == 27 and now(["tuesday", "thursday"]):
        $ eleanor_story += 1


    if facility_story == 1 and now(["saturday","sunday"]):
        jump facility_event1

    if sadie_story == 5:
        $ sadie_story += 1



    if facility_story == 2 and now(["saturday","sunday"]):
        scene black
        pause
        scene bg_bedlucas
        show bg_bedlucas_doorclosed
        show lucas sleep_day pose ohshit
        pause
        show lucas sleep_day pose ohshit_t
        stop music
        l_mc ". . ."
        l_mc "Oh god"
        l_mc "I'm all sweaty"
        l_mc "Did I just have a bad dream . ."
        l_mc "Nah, probably some delusion dream, can't remember"
        hide lucas sleep_day pose
        show char_lucas_bedoff_day with dissolve
        l_mc "Time to just get up"
        l_mc "Ow! Something is poking my ass"


        pause



        call set_location ("loc_lucasroom") from _call_set_location_26
        show lucas normal pose33 blank at left with Dissolve(0.01)
        pause
        show lucas normal pose33 assured_talk
        l_mc "The hell is this thing"
        show lucas normal pose33 mkay_talk
        l_mc "I don't remember bringing this here"
        l_mc "Did [sadie_refer_input] bring this in here by accident?"
        show lucas normal pose33 mkay
        pause        
        show lucas normal pose33 default_talk
        l_mc "Seems oddly fimiliar, haven't I seen the shape of this object somewhere in the house before ?"
        l_mc "Hmpf, who knows"
        l_mc "I better dress up anyways"
        hide lucas normal pose33 mkay_talk
        $ inv.append(item_dreamkey)
        show lucas normal pose34 happy with dissolve
        $ renpy.pause ()
        hide lucas normal pose34 default with dissolve
        show lucas normal pose35 default with dissolve

        l_mc "Alright, let's get started"

        play music "music/music4.mp3"
        show screen item_updated_notify with dissolve
        $ facility_story += 1
        $ renpy.scene()
        jump goto_lucasroom
        return



    if eleanor_story == 32 and now(["tuesday", "thursday"]):
        $ eleanor_phone_points += 1
        $ eleanor_story += 1

    if eleanor_story == 12 and now(["tuesday", "thursday"]):
        window hide
        l_mc "*I should call eleanor about the module before I get up*"
        "*Calls*"
        l_mc "Hey, Eleanor"
        l_mc "It's me, Lucas"
        l_eleanor "Oh Lucas, what the sudden call so early ?"
        l_mc "I just wanted you to know I just finished the module"
        l_eleanor "That's great, I should come by during the day time"
        l_mc "Ok"
        $ eleanor_story += 1


    show lucas normal pose34 happy with dissolve
    pause













    $ renpy.pause ()
    hide lucas normal pose34 default with dissolve
    show lucas normal pose35 default with dissolve

    l_mc "Alright, lets get started"

    play music "music/music4.mp3"
    $ renpy.scene()



    jump goto_lucasroom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

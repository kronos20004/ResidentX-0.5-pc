transform lucas_intro_figure:
    xpos 0.2 ypos 0.1
    linear 1.0 xpos 0.1

transform lucas_big_hand:
    ypos -280
    xpos -40
    subpixel True
    zoom 1.05
    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23

    linear 0.05 rotate 20

    linear 0.05 rotate 23




    repeat




label storyline_chapter_1:
    stop music

    scene black
    show transition_card 1 with fade
    hide event_bedtime_sadie_01 4
    show custom_text_card "1 week ago" with dissolve
    pause
    hide custom_text_card
    hide transition_card with Dissolve(0.1)
    show event_intro_01
    l_mc "(I wonder what Ms. Eleanor wanted to see me about?)"
    l_mc "(She said I need to see her after class for dropping my performance in class.)"
    l_mc "(God, I hope she doesn’t bring in my [sadie_relationship_input] to school and have a talk about my grades.) "
    l_unkown "Hey, what are you doing?! "
    l_mc "What? Is someone arguing?"
    hide event_intro_01
    show black with dissolve
    pause
    show event_intro_02 zorder 1

    hide black with dissolve



    l_uglyb "Please Ms. Eleanor, I only want to feel a little bit."
    show event_intro_02_anim zorder 0 at lucas_intro_figure
    l_eleanor "Stop it! Get away from me, I’m your teacher you little twerp. You’ll be reprimanded for this so you better stop it now !"
    l_uglyb "Sorry but I can’t help it anymore. If I’m in trouble, I might as well get my troubles worth."
    l_eleanor "You can’t be serious."
    l_mc "(That big bastard.)"
    hide event_intro_02_anim

    l_mc "Hey! Asshat!"
    l_uglyb "What?"

    show black with dissolve
    hide event_intro_02
    pause
    hide black
    play sound "music/sounds/wind_animepunch.mp3"
    show event_intro_03
    show event_intro_03_anim at lucas_big_hand
    show event_intro_03_overlay
    l_uglyb "Oh. . ."
    $ renpy.pause(2.0)


    show black with dissolve
    hide event_intro_03
    hide event_intro_03_anim
    hide event_intro_03_overlay
    pause
    show event_intro_03_2 with dissolve
    hide black with dissolve
    stop music
    play sound "music/berightback.mp3"
    pause
    pause
    show black with dissolve
    hide event_intro_03_2
    play sound "music/sounds/punch_cartoon.mp3"
    show event_intro_04 with vpunch
    hide black with dissolve
    l_uglyb "Ugh . . ."
    l_eleanor "Lucas!? Wait that’s enough, you two"
    l_mc "If she said no, it means no you dumb fuck."
    hide event_intro_04
    play sound "music/sounds/punch_cartoon.mp3"
    show event_intro_05 with vpunch
    l_eleanor "No, stop it before you make it worse on yourself, Lucas."
    l_mc "You want to kiss something so badly, kiss the floor."
    l_uglyb "AAhh . . ."
    l_eleanor "Oh no!"









    scene white with flash
    scene bg_bedlucas
    show bg_bedlucas_doorclosed
    show lucas sleep_day pose sleep
    pause
    hide lucas sleep_day pose sleep
    show char_lucas_bed3 with Dissolve(0.1)

    play music "music/music4.mp3"
    l_mc "*sigh*"
    l_mc "(I’m such an idiot.)"
    l_mc "(Suspended from school for beating that kid up.)"
    l_mc "(Damn prick, had it coming though and I’d probably do it again if I could.) "
    l_mc "(But look at me now, treated like a common criminal.) "
    l_mc "(Did I perhaps go a little overboard with him?)"
    l_mc "(Graduation is soon and I get suspended for helping a teacher out. Now I’ll be held back and repeat another school year. What a joke.)"
    l_mc "(What’s done, is done I guess.)"
    l_mc "(Best not to fester on it for too long.)"
    l_mc "(Better just get up and find something to do in the meantime.)"


    call set_location ("loc_lucasroom") from _call_set_location_12

    show lucas normal pose34 default with dissolve
    $ renpy.pause ()
    hide lucas normal pose34 default with dissolve
    show lucas normal pose35 default with dissolve
    pause
    show screen main_hud_icon
    l_mc "Alright, lets get started"
    call roaming from _call_roaming
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

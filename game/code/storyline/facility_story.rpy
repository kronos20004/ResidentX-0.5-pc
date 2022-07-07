label facility_event1:
    hide screen main_hud_icon
    scene black with dissolve
    centered "{color=7fff00}{size=45}{font=gui/fonts/acumin_regular.otf} *2:26 AM* \n . . \ . .{/font}{/size}{/color}"
    scene bg_bedlucas_alt
    stop music
    show bg_bedlucas_doorclosed_night
    show lucas sleep_night sleep1
    pause
    hide lucas sleep_night sleep1
    show char_lucas_bedufo_1_night with Dissolve(.1)
    pause
    hide char_lucas_bedufo_1_night
    show char_lucas_bedufo_2_night with Dissolve(.1)
    pause
    hide char_lucas_bedufo_2_night
    show char_lucas_bedufo_3_night with Dissolve(.1)
    pause
    hide char_lucas_bedufo_3_night
    show char_lucas_bedufo_4_night with Dissolve(.1)
    pause
    scene black with dissolve
    pause

    scene event_abduction_1
    show pov_blur_1
    pause
    l_mc "huh . . . what"
    hide pov_blur_1
    show pov_blur_2
    pause
    l_mc "where. . ."
    hide pov_blur_2
    l_mc "What's going on?"
    l_mc "I can't move my arms or legs"
    l_mc "Am I having sleep paralysis now?"
    scene event_abduction_2 with Dissolve(.5)
    l_mc "The fuck are you?"
    scene event_abduction_3
    l_stranger "Mind your language. I can understand your fowl tongue"
    l_stranger "Or would you rather I sleep your orifice?"
    scene event_abduction_2
    l_mc "This is some strange ass dream alright"
    scene event_abduction_3
    l_stranger "This is no such dream of yours"
    scene event_abduction_2
    l_mc "Of course, only I would dream of such a busty babe showing me underboob"
    l_mc "What a treat, even if she does look a little strange"
    scene event_abduction_3
    l_stranger "Does your tongue have no end to vulgarity? For such a young specimen to speak of my physique"
    l_stranger "not even of your species"
    scene event_abduction_2
    l_mc "Whatever, you're just a dream anyways"
    l_mc "Might as well glance at such a magnificent view"
    scene event_abduction_6 with dissolve
    l_mc ". . . ."
    scene event_abduction_7 with Dissolve(.2)
    l_mc "Such a marvelous design sculpted by my brain's imgination"
    l_mc "If only I could get rid of my limbs from these shakles that hold me in place"
    l_mc "So close, yet so far away"
    l_mc "I hope this won't be such a cruel dream from which I wake, right before the good part starts"
    l_stranger "Silence already, most foul-mouthed boy"
    scene event_abduction_2 with dissolve
    pause
    scene event_abduction_4 with Dissolve(.3)
    pause
    scene event_abduction_5 with Dissolve(.3)
    l_stranger "I would not imagine your presence would annoy me such as it did"
    l_stranger "You are only here because I want you to aid me in locating someone"
    scene event_abduction_4
    l_mc "What are you talking about? Just let me go already so we can get this dream started before it ends"
    scene event_abduction_5
    l_stranger "I was planning to give you this to help your search"
    l_stranger "But after your barrage of insults, I think I know juuuuuust the right place to put this"
    scene event_abduction_4
    l_mc "Wait what . . .?"
    l_mc "I don't roll that way, come on"
    l_mc "Stop joking around"
    scene event_abduction_5
    l_stranger "Don't worry, this won't hurt"
    scene event_abduction_4
    l_mc "You're kidding, this is no dream, it's a nightmare !"
    $ facility_story += 1
    hide event_abduction_4
    jump lucas_sleep
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

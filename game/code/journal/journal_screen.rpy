screen journal_screen():
    modal True
    zorder 1
    add "journal_contents" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2














    vbox:
        xpos 256
        ypos 473


        spacing 10

        imagebutton:
            idle "entry_sadie"
            mouse "interaction_m"

            action Hide("journal_screen"), Show("sadie_journal")




        imagebutton:
            idle "entry_enigma"
            mouse "interaction_m"

            action Hide("journal_screen"), Show("leo_journal")




        imagebutton:
            idle "entry_eleanor"
            mouse "interaction_m"

            action Hide("journal_screen"), Show("eleanor_journal")




        if konami_journal == True:
            imagebutton:
                idle "entry_konami"
                mouse "interaction_m"

                action Hide("journal_screen"), Show("konami_journal")


    hbox:
        xalign 0.14
        yalign 0.94
        spacing 8
        imagebutton:
            idle "page_1_idle"
            hover "page_1_hover"
            mouse "interaction_m"
            action Hide("journal_screen_2"), Show("journal_screen")

        imagebutton:
            idle "page_2_idle"
            hover "page_2_hover"
            mouse "interaction_m"
            action Hide("journal_screen"), Show("journal_screen_2")


screen journal_screen_2():
    modal True
    zorder 1
    add "journal_contents" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen_2"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Show("journal_screen_2")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen_2"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen_2"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("journal_screen_2"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    vbox:
        xpos 256
        ypos 473


        spacing 10


        if jada_journal == True:
            imagebutton:
                idle "entry_jada"
                mouse "interaction_m"
                action Hide("journal_screen_2"), Show("jada_journal")


    hbox:
        xalign 0.14
        yalign 0.94
        spacing 8
        imagebutton:
            idle "page_1_idle"
            hover "page_1_hover"
            mouse "interaction_m"
            action Hide("journal_screen_2"), Show("journal_screen")

        imagebutton:
            idle "page_2_idle"
            hover "page_2_hover"
            mouse "interaction_m"
            action Hide("journal_screen"), Show("journal_screen_2")



screen sadie_journal():
    modal True
    zorder 1
    add "journal_open" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("sadie_journal"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("sadie_journal"),Hide("leo_journal"), Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    frame:
        pos (205,235)
        background None

        text "{b}{color=#000000}{font=fonts/Mansalva-Regular.ttf}[sadie_refer_input]'s Quest{/font}{/color}{/b}"
        vbox:
            spacing -10
            yalign 0.072
            if sadie_story == 1:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Find her business cloth\n {/font}{/color}"

            if sadie_story == 2:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Hand her the business cloth\n {/font}{/color}"

            if sadie_story == 3:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- See her at the Kitchen\n {/font}{/color}"

            if sadie_story == 4:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Watch TV, she might come home by then\n {/font}{/color}"

            if sadie_story == 6:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Talk to her at the Balcony during evening. \n Not always \n {/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Or at the Kitchen ! \n {/font}{/color}"

            if sadie_story == 7 and journal_sadie_movienight == False:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Watch with her at living room, when she is there. \n {/font}{/color}"
            elif journal_sadie_movienight == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s}- Movienight checked \n{/s}{/font}{/color}"

            if sadie_story == 8:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Ask Sadie at the Balcony, in the afternoon \n for Yoga (tuesday & friday)\n {/font}{/color}"
            if sadie_story == 14:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Reached the end of her content ! \n{/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Support us on {a=https://patreon.com/TheRedPixel}{color=#e88833} Patreon {/color}{/a} ! \n{/font}{/color}"

            if sadie_night_couch_keypad == False and sadie_story == 2:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Talk to Sadie about the Keypad in her Closet\n {/font}{/color}"
            elif sadie_night_couch_keypad == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s}- keypad checked \n{/s}{/font}{/color}"


            if yoga_sadie_scene == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Do yoga with Sadie\n {/font}{/color}"







screen leo_journal():
    modal True
    zorder 1
    add "journal_open" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("leo_journal"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("leo_journal"), Hide("sadie_journal"), Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    frame:
        pos (205,235)
        background None

        text "{b}{color=#000000}{font=fonts/Mansalva-Regular.ttf}Leo secrets Quest{/font}{/color}{/b}"
        vbox:
            spacing -10
            yalign 0.072
            if key_pad_unlocked == False:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Explore\n {/font}{/color}"

            if closet_dial_open == False and key_pad_unlocked == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Try to unlock the keypad\n {/font}{/color}"
            elif closet_dial_open == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s} Keypad Unlocked \n{/s}{/font}{/color}"

            if office_strangebattery == False and medallion_puzzle_solve == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Should find a tool to cut the wood \n{/font}{/color}"

            if item_stranegbattery in inv:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- What could I use the battery for ? \n{/font}{/color}"
            if attic2_strangebattery == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s} Strange battery implemented \n{/s}{/font}{/color}"
            if attic2_computer_solved == False and attic2_strangebattery == True:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Solve the cryptic computer code \n{/font}{/color}"

            if facility_story == 1:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Maybe should sleep during saturday or sunday \n{/font}{/color}"

            if facility_story == 3 and item_dreamkey in inv:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- I think this dreamkey is used on something. . .\n{/font}{/color}"


screen eleanor_journal():
    modal True
    zorder 1
    add "journal_open" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("eleanor_journal"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("eleanor_journal"), Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    frame:
        pos (205,235)
        background None

        text "{b}{color=#000000}{font=fonts/Mansalva-Regular.ttf}Eleanor Quest{/font}{/color}{/b}"
        vbox:
            spacing -10
            yalign 0.072
            if eleanor_story == 1:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- N/A\n {/font}{/color}"
            if eleanor_story == 2:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check the door\n {/font}{/color}"
            if eleanor_story == 3:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Wait for the text during Tuesday or Thursday\n {/font}{/color}"
            if eleanor_story == 4:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check your phone.\n {/font}{/color}"
            if eleanor_story == 5:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will ring the bell during tuesday or thursday\n {/font}{/color}"
            if eleanor_story == 6:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She is by the door (tuesday, or thursday) evening\n {/font}{/color}"
            if eleanor_story == 9:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will text you about the Module soon\n {/font}{/color}"
            if eleanor_story == 10 or eleanor_story == 11:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Complete the Module\n {/font}{/color}"
            if eleanor_story == 12:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- I will call her during her off \n which is tuesday or thursday\n {/font}{/color}"
            if eleanor_story == 13:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will ring the bell in afternoon\n {/font}{/color}"
            if eleanor_story == 14:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She at the door (afternoon)\n {/font}{/color}"
            if eleanor_story == 17:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Do the Module\n {/font}{/color}"
            if eleanor_story == 18:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Wait for Text from Eleanor \n {/font}{/color}"
            if eleanor_story == 19:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check your text from Eleanor \n {/font}{/color}"


            if eleanor_story == 20:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}-Eleanor will come in the morning \n (tuesday or thursday) \n {/font}{/color}"

            if eleanor_story == 21:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}-She is at the front door (tuesday or thursday) \n {/font}{/color}"

            if eleanor_story == 23:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}-Grab her clothe from [sadie_refer_input]'s Closet' \n {/font}{/color}"

            if eleanor_story == 28:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will ring the door at night (tuesday , thursday)\n {/font}{/color}"

            if eleanor_story == 29:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She is by the front door, night\n {/font}{/color}"

            if eleanor_story == 32:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Eleanor will text you during tuesday/thursday \n {/font}{/color}"

            if eleanor_story == 33:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Look at the text.\n {/font}{/color}"

            if eleanor_story == 34:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Find her Bra at the Laundry\n {/font}{/color}"

            if eleanor_story == 35:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Reached the end of her content ! \n{/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Support us on {a=https://patreon.com/TheRedPixel}{color=#e88833} Patreon {/color}{/a} ! \n{/font}{/color}"





screen konami_journal():
    modal True
    zorder 1
    add "journal_open" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("konami_journal"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("konami_journal"), Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    frame:
        pos (205,235)
        background None

        text "{b}{color=#000000}{font=fonts/Mansalva-Regular.ttf}Konami Quest{/font}{/color}{/b}"
        vbox:
            spacing -10
            yalign 0.072
            if konami_story == 1:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- There is something going on in the tree house\n {/font}{/color}"
            if konami_story == 2:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Text konami at night\n {/font}{/color}"
            if konami_story == 4:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Konami should be at the Tree House during evening\n {/font}{/color}"
            if konami_story == 5:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Wait for a text next day or so.\n {/font}{/color}"
            if konami_story == 6:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check her text.\n {/font}{/color}"
            if konami_story == 7:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Meet her at the Treehouse during the day.\n {/font}{/color}"

            if konami_story == 9:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Wait for a text next day or so.\n {/font}{/color}"

            if konami_story == 10:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check Text. \n {/font}{/color}"

            if konami_story == 11:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Konami should be at the pool during the \n weekends(sat/sun).\n {/font}{/color}"

            if konami_story == 13:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Buy the managa ! and \n then head to her house. \n {/font}{/color}"

            if konami_story == 14:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Wait for a text next day or so.  \n {/font}{/color}"

            if konami_story == 15:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Check text. \n {/font}{/color}"

            if konami_story == 16:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Visit Treehouse during weekends (Morning) \n {/font}{/color}"

            if konami_story == 17:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will text you at night \n {/font}{/color}"

            if konami_story == 20:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Show up at her room during \n the afternoon (weekdays) \n {/font}{/color}"


            if konami_story == 21:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Text Konami at night  \n {/font}{/color}"

            if konami_story == 23:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Reached the end of her content ! \n{/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Support us on {a=https://patreon.com/TheRedPixel}{color=#e88833} Patreon {/color}{/a} ! \n{/font}{/color}"
screen jada_journal():
    modal True
    zorder 1
    add "journal_open" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Hide("journal_screen_2"), Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("jada_journal"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("journal_screen_2"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("journal_screen_2"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("jada_journal"), Hide("journal_screen"), Hide("inventorystuff")]
        xpos 1407 ypos 2

    frame:
        pos (205,235)
        background None

        text "{b}{color=#000000}{font=fonts/Mansalva-Regular.ttf}Jada's Quest{/font}{/color}{/b}"
        vbox:
            spacing -10
            yalign 0.072
            if jada_story == 0:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Buy the lens and then\n {/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Interact with the Scope again\n {/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Afterward, check the Attic and interact with \n the scope\n {/font}{/color}"
            if jada_story == 1:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- I should check the scope whenever !\n {/font}{/color}"
            if jada_story == 2:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- I should check the scope whenever !\n {/font}{/color}"
            if jada_story == 3:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Visit the yoga room during weekends (Morning)\n {/font}{/color}"
            if jada_story == 4:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Visit the yoga room during weekends (Morning)\n {/font}{/color}"
            if jada_story == 5:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Visit the yoga room during weekends (Morning)\n {/font}{/color}"
            if jada_story == 9:
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- You reached the end of her content\n {/font}{/color}"
                text "{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Support us on {a=https://patreon.com/TheRedPixel}{color=#e88833} Patreon {/color}{/a} ! \n{/font}{/color}"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

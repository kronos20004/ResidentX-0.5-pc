init offset = -1













style healthui is text:

    size 34
    color "#dcffaf"

    font "fonts/bahnschrift/BAHNSCHRIFT 1.TTF"

    outlines [ (5, "#00FF00") ]


















style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xpos -1293
    xsize gui.customscrollbarsize
    base_bar Frame("gui/scrollbar/scroll_bar_custom.png")
    thumb Frame("gui/scrollbar/scroll_thumb_custom.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say(who, what):
    style_prefix "say"
    hbox:


        xalign 0.01
        yalign 0.99
        spacing 4




        imagebutton:
            idle "hud_dialogue_hide"
            hover "hud_dialogue_hide_alt"
            action HideInterface()


        imagebutton:
            ypos 25
            idle "hud_dialogue_skip"

            at btn
            action Skip() alternate Skip(fast=True, confirm=True)


        imagebutton:
            ypos 25
            idle "hud_dialogue_auto"
            at btn
            action Preference("auto-forward", "toggle")


        imagebutton:
            ypos 25
            idle "hud_dialogue_quicksave"
            at btn
            action QuickSave()


        imagebutton:
            ypos 25
            idle "hud_dialogue_menu"
            at btn
            action ShowMenu("navigation")

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"




    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0



init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/hud_dialoguebox.png", xalign=0.5, yalign=0.5)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos












screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width










screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action




define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")





































default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

transform cycle_icon_hud_position:
    xalign 0.98 yalign 0


























screen money_earn_display():
    zorder 1
    vbox:
        xalign 0.93
        yalign 0.99
        add "images/bubble/notification_moneyearned.png"
        text "{size=65}[random_cash_range]{/size}" xpos 130 ypos -110
        timer 3.0 action Hide("money_earn_display", transition = Dissolve(0.2))

screen main_hud_icon():



    zorder 1


    imagebutton:
        yalign 0.040
        xalign 0.81
        idle "gui/hud/hud_icon_bed.png"
        at btn


        if sadie_story in (9,10,11,12,13):
            action NullAction()
        if renpy.get_screen("say") or eleanor_story == 2:
            action NullAction()

        action Return("goto_lucasroom")

    imagebutton:
        yalign 0.040
        xalign 0.72
        idle "gui/hud/hud_icon_menu.png"
        hover "gui/hud/hud_icon_menuhover.png"
        action ShowMenu("navigation")
    hbox:
        yalign 0.029
        xalign 0.99
        spacing 10
        if now(["monday"]):
            add "gui/hud/hud_day_monday.png"
        if now(["tuesday"]):
            add "gui/hud/hud_day_tuesday.png"
        if now(["wednesday"]):
            add "gui/hud/hud_day_wednesday.png"
        if now(["thursday"]):
            add "gui/hud/hud_day_thursday.png"
        if now(["friday"]):
            add "gui/hud/hud_day_friday.png"
        if now(["saturday"]):
            add "gui/hud/hud_day_saturday.png"
        if now(["sunday"]):
            add "gui/hud/hud_day_sunday.png"
        vbox:
            ypos -20
            if now("morning"):
                add "gui/hud/hud_time_morning.png"

            elif now(["afternoon"]):
                add "gui/hud/hud_time_noon.png"

            elif now(["evening"]):
                add "gui/hud/hud_time_night.png"

            elif now(["night"]):
                add "gui/hud/hud_time_midnight.png"
    vbox:
        xalign 0.98
        yalign 0.12
        add "hud_icon_money"
        text "[main_mc.cash]" outlines [ (1, "#000000", 0, 0.7) ] ypos -55 xpos 115 size 45















    imagebutton:
        yalign 0.02
        xalign 0.01
        idle "gui/hud/hud_icon_map.png"

        at btn
        action Show("map_swap_scr")


    imagebutton:
        yalign 0.05
        xalign 0.105
        idle "gui/hud/hud_icon_journal.png"

        at btn
        action Show("book_view")

    imagebutton:
        yalign 0.05
        xalign 0.230
        idle "gui/hud/hud_icon_phone.png"
        at btn

        action Show("phone_contacts")




















image menu_thunder_animation:
    "gui/menu/Main Menu/thunder_lvl1.png" with dissolve
    .3
    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .3
    "gui/menu/Main Menu/thunder_lvl3.png" with dissolve
    .1
    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .1
    "gui/menu/Main Menu/thunder_lvl3.png" with dissolve
    .05
    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .05


    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .3
    "gui/menu/Main Menu/thunder_lvl3.png" with dissolve
    .1
    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .1
    "gui/menu/Main Menu/thunder_lvl3.png" with dissolve
    .05
    "gui/menu/Main Menu/thunder_lvl2.png" with dissolve
    .05
    "gui/menu/Main Menu/thunder_lvl1.png" with dissolve
    .01
    pause 1.5


    repeat










screen main_menu():
    tag menu






    add "gui/menu/gui_menuhome_wallpaper.jpg"




    vbox:
        xalign 0.037
        yalign 0.565
        imagebutton auto "gui/menu/Button_NewGame_%s.png" focus_mask True action Start()


        imagebutton auto "gui/menu/Button_LoadGame_%s.png" focus_mask True action ShowMenu('load')

        imagebutton auto "gui/menu/Button_Settings_%s.png" focus_mask True action ShowMenu('preferences')

        imagebutton auto "gui/menu/button_credit_%s.png" focus_mask True action ShowMenu('credit')


        imagebutton auto "gui/menu/button_quit_%s.png" focus_mask True action Quit(confirm=not main_menu)


    imagebutton idle "gui/menu/mainmenu_patreon.png" xpos .81 ypos .89 at dial_effect focus_mask True action OpenURL("https://www.patreon.com/theredpixel")

    vbox:
        xalign 0.98
        yalign 0.02
        text "{size=24}{b}{font=fonts/bahnschrift/BAHNSCHRIFT 6.TTF} Renpy Version : [renpy.version_only] \n \n Build : 0.5 (Non-Patron Build) {/size}{/b}{/font}"






screen navigation():
    tag menu
    add "gui_menupause_main_layout"

    imagebutton:
        idle "gui_pause_return"
        xpos 0.82
        ypos 0.05
        at dial_effect
        action Return()

    vbox xalign 0.36 yalign 0.35:
        spacing 10
        imagebutton:
            idle "gui_menupause_main_save"


            at dial_effect
            action ShowMenu('save')

        imagebutton:
            idle "gui_menupause_main_load"


            at dial_effect
            action ShowMenu('load')

        imagebutton:
            idle "gui_menupause_main_settings"


            at dial_effect
            action ShowMenu('preferences')

        imagebutton:
            idle "gui_menupause_main_menu"


            at dial_effect
            action MainMenu()

        imagebutton:
            idle "gui_menupause_main_exit"


            at dial_effect
            action Quit()
































































































































































































































































style rx_popuptext is text:
    text_align 0.5
    size 35
    color "#f7bc4a"
    font "gui/fonts/acumin_bold.otf"

style credit_font is text:
    text_align 1
    size 25
    color "#e9ddc2"

    outlines [ (4, "#244167", 0, 2) ]

screen credit():





    style_prefix "main_menu" tag menu


    add "ui_credits"


    viewport id "vp":
        mousewheel True


        draggable True

        xalign .5
        yalign 0.85
        xmaximum 870
        ymaximum 700

        has vbox
        text "{=credit_font}{color=#ffff}Creator" outlines [ (2, "#000", 0, 2) ] xalign .5
        text "{=credit_font}{color=#d41e66}PINKER & ILW" outlines [ (2, "#4a031f", 0, 2) ] xalign .5
        text ""
        text "{=credit_font}{color=#ffff}Credit for in-game features" outlines [ (2, "#000", 0, 2) ] xalign .5
        text "{=credit_font}{color=#FFC0CB}Kia & Shawna" outlines [ (2, "#244167", 0, 2) ] xalign .5
        text ""
        text "{=credit_font}{color=#ffff}Our Patron (Golden & Silver)" outlines [ (2, "#000", 0, 2) ] xalign .5
        text ""

        text "{=credit_font}{color=#d4b22a}Golden Tier" outlines [ (2, "#691d10", 0, 2) ] xalign .5
        text "{=credit_font}Gordon L Blackhorse, Kocsta, Gabe statnyk, Luis hernadez, McLeod, Pu$$yB0$$, Randall-jk, Steve Walston, Welfare, Wolle123, Agust Johansson, Alex Gibson, badworker, bulldawg77, Dan Wayne" outlines [ (2, "#244167", 0, 2) ] xalign .5
        text ""
        text "{=credit_font}{color=#ffff}Silver Tier" outlines [ (2, "#4f4e4d", 0, 2) ] xalign .5
        text "{=credit_font}Mugenendo, Osamurai, Pascal Touteau, peepeepoopoo69, Peter Ottes, poplockpop, rush, Trevor Taylor, Xzaust F, Zach Culff, Aaron Cox, Balzarin Ivan, Diego Smith, eddygarre, Eyesovereasy, Heil, jordi pelay lahuerta, Kris, Lukaplesh" outlines [ (2, "#244167", 0, 2) ] xalign .5
    imagebutton:
        idle "ui_credits_goback"
        xpos 0.85
        ypos 0.88
        at dial_effect
        action Return()


screen bonus_key():
    default bonus_code = ""
    add "cheatcode_input_gui"
    hbox:
        xalign .5
        yalign .535

        input default "TYPE IN HERE":
            length 25
            value ScreenVariableInputValue('bonus_code')
    hbox:
        xalign .5
        yalign .75
        spacing 60
        imagebutton:
            idle "cheatcode_enteri"
            action Function(is_valid_bonus_code, bonus_code=bonus_code)
        imagebutton:
            idle "cheatcode_goback"
            action Jump("cheat_direction")















































transform btn:
    on idle:
        alpha 1.0
    on hover:
        alpha 0.8



























screen game_menu(title):
    style_prefix "gm"

    transclude

    button:
        xysize 200,200 foreground None align 0.94,0.05
        hover_background "images/customs/save/gui_pause_return_h.png"
        background "images/customs/save/gui_pause_return.png"
        at btn
        action Return()

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


screen save():
    tag menu
    add "gui_menupause_save_layout"
    use file_slots(_("Save"))

screen load():
    tag menu
    add "gui_menupause_load_layout"
    use file_slots(_("Load"))

screen unsupported_save():
    modal True
    zorder 50
    frame:
        background Frame("gui_menupause_save_slot")
        padding (50,50)
        align (0.5, 0.5)

        has vbox:
            align (0.5, 0.5)
            spacing 15
        label _("Old saves is not compatible with new version ! ! ! ! ! ! !") xalign 0.5 style "dialogue_text1"
        textbutton _("{color=#000}Ok{/color}") xpadding 10 ypadding 10:
            xalign 0.5
            keysym ('K_RETURN', 'K_KP_ENTER', 'K_SELECT', "K_ESCAPE")
            action Hide("unsupported_save")

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    style_prefix "sav"
    use game_menu(title):
        vbox:
            align (.5,.6)


            grid 3 2:
                for slot in range(1, 7):


                    $ is_supported = FileJson(slot, key="_version") in (_version, None)
                    button at btn:

                        xmaximum 650
                        ymaximum 600
                        xysize 400,330
                        background Frame("images/customs/load/gui_menupause_save_slot.png", 10,10) top_margin 20 xmargin 50
                        action (
                            FileAction(slot) if (is_supported or renpy.get_screen("save"))
                            else Show("unsupported_save")
                        )

                        has vbox
                        add FileScreenshot(slot) xysize 395,240
                        text FileTime(slot, format=_("{#file_time}%a, %H:%M - %b %d  %Y, "), empty=_("empty slot")) text_align .5 ypos 20
                        if FileSaveName(slot):
                            text FileSaveName(slot)
                        key "save_delete" action FileDelete(slot)

        hbox:
            align (.48,.5)

            spacing 10



            yalign 0.12



            textbutton _("<") action FilePagePrevious() style "resident_menu_frame" text_size 50 at btn

            if config.has_autosave:



                imagebutton:
                    idle "gui_menupause_save_autosave"
                    at btn
                    action FilePage("auto")

            if config.has_quicksave:
                imagebutton:
                    idle "gui_menupause_save_quicksave"
                    at btn
                    action FilePage("quick")



            for page in range(1, 8):
                textbutton "[page]" action FilePage(page) style "resident_menu_frame" text_size 50 at btn

            textbutton _(">") action FilePageNext() style "resident_menu_frame" text_size 50 at btn




















style resident_menu_frame:
    background Frame("customs/save/gui_menupause_save_page.png")
    padding (30,20)





style alert_load_text:
    color "db4809"
    size 50

style dialogue_text1:
    color "#ffff"
    font "fonts/Mansalva-Regular.ttf"







































































































































































































































screen preferences():
    tag menu
    on "replaced" action Hide('gui_tooltip')
    add "gui_menupause_settings_layout"


    frame xalign 0.706 yalign 0.117:
        style_group "pref"
        has vbox
        bar value Preference("text speed")

    frame xalign 0.706 yalign 0.354:
        style_group "pref"
        has vbox
        bar value Preference("music volume")

    frame xalign 0.706 yalign 0.586:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")














    hbox:

        spacing 14
        xalign 0.5
        yalign 0.85
        imagebutton idle "gui_menupause_settings_window1" hover "gui_menupause_settings_window1_h" action Preference('display', 'window')
        imagebutton idle "gui_menupause_settings_window2" hover "gui_menupause_settings_window2_h" action Preference('display', 'fullscreen')


    imagebutton idle "gui_pause_return" xalign 0.97 yalign 0.05 action Return() at btn





















init -2 python:



    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/menu/setting/menu/setting_bar_full.png"
    style.pref_slider.right_bar = "gui/menu/setting/menu/setting_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 370
    style.pref_slider.ymaximum = 50


screen escape_key():
    key "K_ESCAPE" action ShowMenu("navigation")









































































































































screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0















screen confirm(message, yes_action, no_action):

    modal True

    zorder 200


    if eleanor_story < 6:
        add "wallpaper_eleanor1"
    elif eleanor_story > 20:
        add "wallpaper_eleanor1_alt"
    else:
        add "wallpaper_eleanor1"

    frame:
        align .12,.3
        xsize 1000 background None
        has vbox
        label _(message):
            style "confirm_prompt"
        hbox:
            spacing 100
            imagebutton:

                background None
                idle "images/customs/quit_message/yes_quit_btn_idle.png"
                hover "images/customs/quit_message/yes_quit_btn_hover.png"

                action yes_action
            imagebutton:

                background None
                idle "images/customs/quit_message/no_quit_btn_idle.png"
                hover "images/customs/quit_message/no_quit_btn_hover.png"

                action no_action

    key "game_menu" action no_action















































    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")






































screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 9

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:


    font "DejaVuSans.ttf"









screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")









screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing


        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)



        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            has fixed:
                yfit gui.nvl_height is None

            if d.who is not None:

                text d.who:
                    id d.who_id

            text d.what:
                id d.what_id





































define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")







style pref_vbox:
    variant "medium"
    xsize 675
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

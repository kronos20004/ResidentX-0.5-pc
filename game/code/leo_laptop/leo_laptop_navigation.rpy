
image leolaptop_night_exit_ui = "images/customs/leo_laptop/leolaptop_night_I.png"
image leolaptop_day_exit_ui = "images/customs/leo_laptop/leolaptop_I.png"

label leo_laptop_navigation:
    $ loc = "leo_laptop_navigation"
    hide screen main_hud_icon



    scene leolaptop_wallpaper
    if now(["evening", "night"]):
        show leolaptop_night_exit_ui
    elif True:
        show leolaptop_day_exit_ui




    call screen leo_laptop_interactive

    $ result = _return




    $ renpy.jump(loc)




screen leo_laptop_interactive():














    imagebutton:
        idle "computer_exit_idle"
        hover "computer_exit_hover"
        action Jump("goto_officef1")
        xpos 1700
        ypos 911




    imagebutton:
        idle "trash_btn"
        hover "trash_btn_h"
        action Show("leo_laptop_trash")
        xpos 141
        ypos 140



    imagebutton:
        idle "computer_btn"
        hover "computer_btn_h"
        action NullAction()
        xpos 300
        ypos 140



    imagebutton:
        idle "explorer_btn"
        hover "explorer_btn_h"
        action Show("leo_explorer_window")
        xpos 141
        ypos 370


    imagebutton:
        idle "keypad_btn"
        hover "keypad_btn_h"
        action Show("leo_laptop_keypad")
        xpos 300
        ypos 370


    imagebutton:
        idle "frequency_btn"
        hover "frequency_btn_h"
        action Show("leo_frequency_window")
        xpos 141
        ypos 600


    imagebutton:
        idle "writer_btn"
        hover "writer_btn_h"
        action NullAction()
        xpos 300
        ypos 600

screen leo_laptop_trash():
    modal True
    zorder 1

    drag:
        area 773, 100, 820, 800
        add "laptop_trash_screen" pos -773, -100
        button:
            area 770, 0, 40, 30
            action Hide("leo_laptop_trash", transition=Dissolve(0.2))


screen leo_laptop_keypad():
    modal True
    zorder 1
    drag:
        area 560, 145, 675, 745
        add "leo_textnote" pos -560, -145
        button:
            area 635, 0, 40, 30
            action Hide("leo_laptop_keypad", transition=Dissolve(0.2))













screen leo_keypad_deny():
    modal True
    zorder 1

    add "leo_pass_deny"
    key "mouseup_1" action Hide("leo_keypad_deny", transition = Dissolve(0.2))



screen leo_explorer_window():
    modal True
    zorder 1

    add "explorer_bg"
    key "mouseup_1" action Hide("leo_explorer_window", transition = Dissolve(0.2))



















screen leo_frequency_window():
    modal True
    zorder 1

    button:
        action Hide("leo_frequency_window", transition=Dissolve(0.2))

    drag:
        area 580, 540, 800, 280
        add "leopassword_input" pos -600, -540
        hbox:
            align .55, .80
            input:
                value VariableInputValue("leo_password_input", default=True, returnable=True)
                default "TYPE ME"
                color "#ffff"
                bold True
                size 90
                length 11

    if leo_password_coreect == leo_password_input:
        drag:
            area 540, 80, 810, 800
            add "frequency_window" pos -540, -80
            button:
                area 770, 0, 40, 30

                action Hide("leo_frequency_window", transition=Dissolve(0.2))
            imagebutton:
                focus_mask True
                idle "laptop_leo_frequencycode"
                mouse "interaction_m"
                pos -540, -80
                action Show("leo_frequency_window_code")

    elif len(leo_password_input) < 11:
        timer .1 action Hide("leo_keypad_deny")
    else:
        timer .1 action Show("leo_keypad_deny")


screen leo_frequency_window_code():
    modal True
    zorder 2
    drag:
        area 665, 160, 1115, 760
        add "laptop_leo_frequencycode_2" pos -665, -160
        button:
            area 1075, 0, 40, 30
            action Hide("leo_frequency_window_code", transition=Dissolve(0.2))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

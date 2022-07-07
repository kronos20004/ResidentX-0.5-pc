screen alien_keypad():
    modal True
    zorder 1
    default code = "bfic"
    default inputs = ""
    default chars = "abcdefghi"
    if now(["morning", "afternoon"]):
        add "minigames/computer_pad/atticcomputer_dayon.jpg"
    elif now(["evening", "night"]):
        add "minigames/computer_pad/atticcomputer_nighton.jpg"
    vbox:
        imagebutton:

            idle "roamingbutton_goback"
            action Hide("alien_keypad")
            xpos 250
            ypos 955
            at dial_effect

    vbox:
        frame:
            background None
            xsize 880
            ysize 100
            has hbox:
                xpos 510
                ypos 190
                spacing 100
                xsize 20
                ysize 20
            for i in inputs:
                add "minigames/computer_pad/sym{}.png".format(i)
        frame:
            background None
            xsize 600
            button:
                xpos 1180
                ypos 500
                add "minigames/computer_pad/key enter.png"

                if inputs == code:
                    action Function(renpy.notify, "correct"), SetScreenVariable("inputs", ""), Hide("alien_keypad"), SetVariable("attic2_computer_solved", True), Return("goto_attic2")
                else:
                    action Function(msg.msg, "That didn't work at all, wrong code?"), SetScreenVariable("inputs", "")

            hbox:
                spacing 10 box_wrap True
                xpos 410
                ypos 230
                vpgrid:
                    ysize 1200
                    xsize 1200
                    rows 3
                    cols 5

                    for i in chars:
                        button:
                            add "minigames/computer_pad/keypad{}.png".format(i)
                            action If(len(inputs) < 4, SetScreenVariable("inputs", inputs + i)), Play("sound", "music/mouse_click_02.wav")
                            at dial_effect
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

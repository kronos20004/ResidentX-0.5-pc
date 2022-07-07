transform dial_effect:
    parallel:
        on idle:
            alpha 1.0
        on hover:
            alpha 0.5

default inputs = ""
default code = "1694"
default chars = "123456789"
screen closet_keypad():
    modal True
    zorder 1
    if now(["morning", "afternoon"]):
        add "dialpad_bg"
    elif now(["evening", "night"]):
        add "dialpad_bg_night"
    default inputs = ""
    default code = "1694"
    default chars = "123456789"


    button:
        action Hide("closet_keypad", transition = Dissolve(0.2))
        background None

    frame:
        background None
        xsize 200
        button:
            xpos 650
            ypos 808
            at dial_effect
            if now(["morning", "afternoon"]):
                add "minigames/closet keypad/dial_keyenter.png"
            elif now(["evening", "night"]):
                add "minigames/closet keypad/keyenter_night.png"

            if inputs == code:
                action [Hide("closet_keypad"),Return("goto_sadiecloset"), SetVariable("closet_dial_open", True),Show("journal_updated_notify")], SetScreenVariable("inputs", "")
            elif inputs != code:

                action [Hide("closet_keypad"),Return("goto_sadiecloset"), SetVariable("closet_dial_open", False)], SetScreenVariable("inputs", "")
        hbox:
            spacing 4 box_wrap True
            xpos 650
            ypos 238
            vpgrid:
                spacing 8
                ysize 600
                xsize 1200
                rows 3
                cols 3

                for i in chars:
                    button:
                        if now(["morning", "afternoon"]):
                            add "minigames/closet keypad/dial key{}.png".format(i)
                        elif now(["evening", "night"]):
                            add "minigames/closet keypad/key{}_night.png".format(i)
                        action If(len(inputs) < 4, SetScreenVariable("inputs", inputs + i)), Play("sound", "music/click.mp3")

                        at dial_effect

    hbox:
        align 0.648,.1
        spacing 18
        if len(inputs) < 4:
            add "minigames/closet keypad/dial false_off.png"
            add "minigames/closet keypad/dial true_off.png"
        else:
            if inputs == code:

                timer 0.1 action Play("sound", "music/phone_02.mp3")
                add "minigames/closet keypad/dial false_off.png"
                add "minigames/closet keypad/dial true_on.png"
            else:

                timer 0.1 action Play("sound", "music/alarm_beep.mp3")
                add "minigames/closet keypad/dial false_on.png"
                add "minigames/closet keypad/dial true_off.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

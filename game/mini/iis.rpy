


screen medallion_puzzle_screen():
    modal True
    zorder 1
    default top = []
    default xp = [367,670,973,1276]
    default b1 = 0
    default b2 = 0
    default b3 = 0
    default b4 = 0

    add "mini/medallion_puzzle.jpg" at truecenter

    vbox:
        button:
            text "Leave"
            action Hide("medallion_puzzle_screen")

    for ii,i in enumerate(top):
        add "mini/{}/b.png".format(i) xpos xp[ii] yalign .25

    if not b1:
        button:
            add "mini/1/a.png"
            action SetScreenVariable("b1", 1), AddToSet(top, 1)
            yalign .97 xpos 200 background None

    if not b2:
        button:
            add "mini/2/a.png"
            action SetScreenVariable("b2", 1), AddToSet(top, 2)
            yalign .97 xpos 600 background None

    if not b3:
        button:
            add "mini/3/a.png"
            action SetScreenVariable("b3", 1), AddToSet(top, 3)
            yalign .97 xpos 1000 background None

    if not b4:
        button:
            add "mini/4/a.png"
            action SetScreenVariable("b4", 1), AddToSet(top, 4)
            yalign .97 xpos 1400 background None

    if b1 and b2 and b3 and b4:
        if top == [2,3,4,1]:
            vbox:
                text "{size=50}Correct{/size}"
                xpos .4
                ypos .85
            button:
                action [Hide("medallion_puzzle_screen"), SetVariable("medallion_puzzle_solve", True), Return("goto_officef1")]


        else:
            timer 1 action [Show("medallion_puzzle_screen"), SetScreenVariable("top", []), SetScreenVariable("b1", 0), SetScreenVariable("b2", 0), SetScreenVariable("b3", 0), SetScreenVariable("b4", 0)]
            vbox:
                text "{size=50}incorrect, try again{/size}"
                xpos .4
                ypos .85
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

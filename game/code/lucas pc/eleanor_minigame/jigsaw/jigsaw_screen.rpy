screen jigsaw(isJigSaw):
    modal True

    imagebutton:
        idle Null()
        mouse "interaction_m"
        area (1712, 4, 207, 76)
        action Hide("jigsaw"), Return("goto_lucaspc")

    default path_to = "code/lucas pc/eleanor_minigame/jigsaw/images/"
    add path_to + "minigame_art.jpg"

    frame:
        area 430, 120, 230, 40
        background None
        text str(isJigSaw.timer.current) align .5, 1. size 32

    draggroup:
        area 140, 190, 1650, 820
        for en, file in enumerate(isJigSaw.files):
            drag as carmen:

                drag_name file
                frame:
                    background None
                    xysize 230, 230
                    add path_to + file size 227, 227
                drag_handle (0, 0, 227, 227)
                dragged isJigSaw.droppable
                pos isJigSaw.left_positions[en]

    if not isJigSaw.is_valid:
        timer 1.:
            repeat True
            if not isJigSaw.timer.is_over:
                action isJigSaw.timer.tick
            else:
                action isJigSaw.restart, isJigSaw.timer.restart, renpy.restart_interaction
    else:
        timer .33:
            action Return("win")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

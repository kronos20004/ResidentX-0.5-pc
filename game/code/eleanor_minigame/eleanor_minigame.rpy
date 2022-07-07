init python:

    import random

    def generate_directions(num=4):
        """
        Randomly generate a sequence of directions as a list, and reset
        appropriate minigame values.

        Parameters:
        -----------
        num : int
            The number of directions to generate.

        Result:
        -------
        string[]
            Return a list strings representing directions. Also resets the
            value of minigame_success to False and resets quicktime_seq to
            an empty list.
        """
        
        store.minigame_success = False
        store.quicktime_seq = [ ]
        
        directions = []
        for i in range(num):
            
            directions.append(random.choice(['up', 'down', 'right', 'left']))
        return directions

    def add_to_list(item, the_list, correct_list):
        """
        Add item to the_list if it corresponds to the next item in the sequence
        given by correct_list.

        Parameters:
        -----------
        item : string
            One of 'up', 'down', 'left', or 'right'. The direction that was
            pressed.
        the_list : string[]
            The current sequence of directions that have been pressed by
            the player.
        correct_list : string[]
            The correct sequence of directions the player must press.

        Result:
        -------
            If the player pressed the next item in the sequence, it is added
            to the_list. If they made a mistake, it causes the screen to shake.
        """
        
        try:
            if correct_list[len(the_list)] == item:
                the_list.append(item)
            else:
                
                
                renpy.show_layer_at(shake, layer='screens')
        except:
            return
        if the_list == correct_list:
            store.minigame_success = True



transform shake:
    xpos 0 ypos 0
    linear 0.03 xpos -30 ypos 30
    linear 0.03 xpos 0 ypos -30
    linear 0.03 xpos 30 ypos 30
    linear 0.03 xpos 0 ypos -30
    linear 0.03 xpos 30 ypos 30
    linear 0.03 xpos 0 ypos 0


default quicktime_seq = [ ]

default correct_seq = [ ]

default minigame_success = False



define 2 orientation = {'left' : arrow_left, 'right' : arrow_right,
        'down' : arrow_down, 'up' : arrow_up}








define stage_1_directions = 3
define stage_2_directions = 4
define stage_3_directions = 6
define stage_1_time = 6.0
define stage_2_time = 4.5
define stage_3_time = 4.5



define test_minigame = False


define block_minigame_rollback = True





image controller_arrow = "minigames/eleanor_minigame/arrow_tutorial_up.png"
image controller_arrow_hover = "minigames/eleanor_minigame/arrow_tutorial_up_hover.png"

image controller_background = "minigames/eleanor_minigame/wheel_button_bg.png"




image arrow = Transform("minigames/eleanor_minigame/minigame_tutoring_wheelup.png", zoom=0.6)
image arrow_selected = Transform('minigames/eleanor_minigame/minigame_tutoring_wheelup_selected.png', zoom=0.6)





image bar_empty = Frame("minigames/eleanor_minigame/empty_bar_minigame1.png", 45, 20)
image bar_full = Frame("minigames/eleanor_minigame/full_bar_minigame1.png", 45, 20)



label quicktime_minigame():
    if now(["evening","night"]):
        scene event_tutoring_bg_1_alt
        if eleanor_story == 7:
            show eleanor_lucas tutorial_night default defaultz
    elif now(["morning","afternoon"]):
        scene event_tutoring_bg_1
        if eleanor_story == 7:
            show eleanor_lucas tutorial default defaultz

        elif eleanor_story == 15:
            show eleanor_lucas tutorial default defaultz pose3

        elif eleanor_story == 25:
            show eleanor_lucas tutorial default defaultz pose4

    show minigame_tutoring_ui2

    $ correct_seq = generate_directions(stage_1_directions)
    call screen quicktime(correct_seq, stage_1_time)

    if block_minigame_rollback:
        $ renpy.block_rollback()
    if quicktime_seq != correct_seq:
        $ minigame_success = False

        return


    $ correct_seq = generate_directions(stage_2_directions)
    call screen quicktime(correct_seq, stage_2_time)
    if block_minigame_rollback:
        $ renpy.block_rollback()
    if quicktime_seq != correct_seq:
        $ minigame_success = False

        return


    $ correct_seq = generate_directions(stage_3_directions)
    call screen quicktime(correct_seq, stage_3_time)
    if quicktime_seq == correct_seq:
        $ minigame_success = True
    elif True:
        $ minigame_success = False
    if block_minigame_rollback:
        $ renpy.block_rollback()
    return



screen quicktime(directions, t):

    style_prefix 'quicktime'

    hbox:
        align (0.095, 0.570)
        for index, d in enumerate(directions):
            if quicktime_seq and len(quicktime_seq) > index:
                add 'arrow_selected' at orientation[d]
            else:
                add 'arrow' at orientation[d]


    frame:
        has hbox:
            spacing -50
        use arrow_button('left')
        vbox:
            use arrow_button('up')
            null height 137
            use arrow_button('down')
        use arrow_button('right')

    use minigame_timer(t)

    timer 0.5 action If(minigame_success, Return(), NullAction()) repeat True

style quicktime_hbox:
    align (0.5, 0.5)

style quicktime_vbox:
    spacing -25



style quicktime_frame:
    background "controller_background"
    padding (0, 0)
    xysize (367, 367)
    align (0.52, 0.1)



screen arrow_button(direction):

    fixed:
        at orientation[direction]
        xysize (125, 125)

        button:
            xysize (1, 1) align (0.5, 0.5)
            keysym "pad_dp" + direction + "_press"
            action [Function(add_to_list, item=direction,
                the_list=quicktime_seq, correct_list=correct_seq),
                If(minigame_success, Hide('minigame_timer'), None)]

        button:
            xysize (136, 136)
            background 'controller_arrow'
            hover_background 'controller_arrow_hover'
            keysym 'K_' + direction.upper()
            action [Function(add_to_list, item=direction,
                the_list=quicktime_seq, correct_list=correct_seq),
                If(minigame_success, Hide('minigame_timer'), None)]



transform arrow_right:
    rotate 90 align (0.5, 0.5)

transform arrow_left:
    rotate 90 yzoom -1 align (0.5, 0.5)

transform arrow_down:
    yzoom -1

transform arrow_up:
    pass


screen minigame_timer(count_time=5):

    if not test_minigame:
        timer count_time:
            repeat False
            action Return()

    bar:
        value AnimatedValue(0, count_time, count_time, count_time)
        style 'countdown_bar'




style countdown_bar:
    left_gutter 28
    right_gutter 35
    left_bar 'bar_full'
    right_bar 'bar_empty'
    xysize (540, 80)
    pos (120, 65)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

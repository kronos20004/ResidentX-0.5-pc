
init python:
    class map_swap:
        def __init__(self, lst):
            self.lst = lst
            self.current = 0
        
        def add(self, x, l = 0):
            r = [x, l]
            if r not in self.lst:
                self.lst.append(r)
        def next(self):
            if self.current < len(self.lst)-1:
                self.current += 1
        
        def back(self):
            if self.current > 0:
                self.current -= 1
        
        
        def set(self, page):
            self.current = page
        
        def ret(self):
            return self.lst[self.current]

default map_swapper = map_swap(
    [
        "mapf1",
        "hall",
        "basement",
        "attic_map",
        "backyard_map",
        "konami_backyard_map",
    ]
)

screen map_swap_scr(m=map_swapper):
    modal True
    zorder 2
    add "menu_map_bg" xalign 0.5 yalign 0.5




















    imagebutton:
        idle "images/map/map_exit_idle.png"
        hover "images/map/map_exit_hover.png"
        action [Hide("map_swap_scr"), Hide("navigation")]
        xpos 0.803 ypos 0.835



    key 'b' action Function(m.set, 2)
    key 'a' action Function(m.set, 0)
    use expression m.ret()


    vbox:
        yalign .125 xalign 0.123
        imagebutton:
            action Function(m.set, 2)
            idle "map basementi"
            hover "map basementh"
        imagebutton:
            action Function(m.set, 0)
            idle "map floori"
            hover "map floorh"
        imagebutton:
            action Function(m.set, 1)
            idle "map floor2i"
            hover "map floor2h"
        imagebutton:
            action Function(m.set, 3)
            idle "map attici"
            hover "map attich"
        imagebutton:
            action Function(m.set, 4)
            idle "map backyardi"
            hover "map backyardh"

        if konami_entrance_access == True:
            imagebutton:
                action Function(m.set, 5)
                idle "map konamibackyardi"
                hover "map konamibackyardh"


screen mapf1():

    zorder 1 tag maps
    frame:
        background None
        add "images/map/map f1/map_f1.png"
        pos (600, 200)

        if medallion_map_icon == True:
            imagebutton:
                idle "icon_medallions"

                action NullAction()

                if medallion_puzzle_solve == True:
                    tooltip "Solved the medallion"
                else:
                    tooltip "Missing a piece"
                xpos 190
                ypos 170

        if mail_map_icon == True:
            imagebutton:
                idle "map_icon_mail"
                action NullAction()
                tooltip "A mailbox"
                xpos 970
                ypos 170


        if tv_map_icon == True:
            imagebutton:
                idle "map_icon_tv"
                action NullAction()
                tooltip "Tv"
                xpos 560
                ypos 410


        if chest_map_icon == True:
            imagebutton:
                idle "icon_chest"
                action NullAction()
                tooltip "A chest"
                xpos 10
                ypos 170

        if leo_laptop_map_icon == True:
            imagebutton:
                idle "icon_laptop"
                action NullAction()
                tooltip "Leo's Laptop"
                xpos 10
                ypos 330


    $ tooltip = GetTooltip()
    if tooltip:
        add "menu_map_box" xalign 0.5 yalign 0.2
        text "{b}[tooltip]{/b}" xalign 0.5 yalign 0.22


screen hall():

    zorder 1 tag maps
    frame:
        background None
        add "map_f2"
        pos (600, 150)


        if secret_keypad_map == True:
            imagebutton:
                idle "icon_dialpad"
                action NullAction()
                tooltip "Secret Keypad"
                xpos 370
                ypos 150

        if bailey_map_cross == True:
            imagebutton:
                idle "icon_cross"
                action NullAction()
                tooltip "Bailey isn't home"
                xpos 550
                ypos 440


        if pc_lucas_map == True:
            imagebutton:
                idle "map_icon_pc"
                action NullAction()
                tooltip "My PC"
                xpos 110
                ypos 530


    $ tooltip = GetTooltip()
    if tooltip:
        add "menu_map_box" xalign 0.5 yalign 0.2
        text "{b}[tooltip]{/b}" xalign 0.5 yalign 0.22


screen basement():

    zorder 1 tag maps
    frame:
        background None
        add "map_basement"
        pos (850, 200)

        if mystery_brick_map_icon == True:
            imagebutton:
                idle "icon_brick"
                action NullAction()
                tooltip "A mystery hole"
                xpos 0
                ypos 250

        if mystery_stair_map_icon == True:
            imagebutton:
                idle "icon_facility"
                action NullAction()
                tooltip "Mystery path... no just no"
                xpos 220
                ypos 300
    $ tooltip = GetTooltip()
    if tooltip:
        add "menu_map_box" xalign 0.5 yalign 0.2
        text "{b}[tooltip]{/b}" xalign 0.5 yalign 0.22

screen attic_map():

    zorder 1 tag maps
    frame:
        background None
        add "map_attic"
        pos (850, 340)


        if door_map_icon == True:
            imagebutton:
                idle "icon_door"
                xpos 260
                ypos 130
                if attic_hidden_door == False:
                    tooltip "Door is locked"
                else:
                    tooltip "Unlocked the door"
                action NullAction()


        if atticwindow_map_icon == True:
            imagebutton:
                idle "icon_window"
                action NullAction()
                tooltip "can't see far"
                xpos 320
                ypos 7


        if boardinfo_map_icon == True:
            imagebutton:
                idle "map_icon_info"
                action NullAction()
                tooltip "White Board filled with informations"
                xpos 5
                ypos 15

        if atticstrange_map_icon == True:
            imagebutton:
                idle "icon_strange_computer"
                action NullAction()
                tooltip "A strange computer"
                xpos 5
                ypos 160

    $ tooltip = GetTooltip()
    if tooltip:
        add "menu_map_box" xalign 0.5 yalign 0.2
        text "{b}[tooltip]{/b}" xalign 0.5 yalign 0.22

screen backyard_map():

    zorder 1 tag maps
    frame:
        background None
        add "map_backyard"
        pos (700, 140)











screen konami_backyard_map():

    zorder 1 tag maps
    frame:
        background None
        add "gui_map_konami_backyard"
        pos (700, 140)


    $ tooltip = GetTooltip()
    if tooltip:
        add "menu_map_box" xalign 0.5 yalign 0.2
        text "{b}[tooltip]{/b}" xalign 0.5 yalign 0.22
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

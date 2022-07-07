
init python:
    class map_swap2:
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
                renpy.show_screen("map{}".format(self.current+1), _tag = "maps_screen2")
        
        def back(self):
            if self.current > 0:
                self.current -= 1
                renpy.show_screen("map{}".format(self.current+1), _tag = "maps_screen2")
        
        
        def ret(self):
            return self.lst[self.current]

default map_swapper2 = map_swap2(
    [
        "map1",
        "map2",
        "map3",
    ]
)

screen map_swap_scr2(m=map_swapper2):
    modal True
    zorder 2

    add "ui_quickies_homescreen"




    key 'd' action Function(m.next)
    key 'a' action Function(m.back)
    use expression m.ret()



    hbox:
        imagebutton:
            idle Null()
            mouse "interaction_m"
            action Hide("map_swap_scr2"), Hide("map1"), Hide("map2"), Hide("map3")
            area (1806, 2, 106, 105)



    button:
        xalign 0.0
        yalign 1.0
        action Function(m.back)
        add "ui_quickies_previous"

    button:
        xalign 1.0
        yalign 1.0
        action Function(m.next)
        add "ui_quickies_next"


screen map1():

    zorder 2 tag maps
    if shop_first_time == False:
        timer 0.1 action SetVariable("shop_first_time", True), Function(msg.msg, "A shop ? Looks cool")

    hbox:
        xalign 0.12
        yalign 0.61
        spacing 10


        imagebutton:
            if item_lens_shop == True:
                idle "quikies_item_lens_sold"
            else:
                idle "quikies_item_lens"
            if item_lens_shop == False:
                if main_mc.cash < 25:
                    action Function(msg.msg, "You have insufficient money.")
                    mouse "interaction_m"

                else:
                    action SetVariable("item_lens_shop", True), SetVariable("item_lens_arrival", 1), Function(main_mc.lose_cash, 25), Function(msg.msg, "You will get a message from Quickies!")


                    mouse "interaction_m"
            else:
                action NullAction()
                mouse "deny_m"


        imagebutton:
            if item_manga_shop == True:
                idle "quikies_item_manga_sold"
            else:
                idle "quikies_item_manga"
            idle "quikies_item_manga"
            if item_manga_shop == False and item_manga_buy == True:
                if main_mc.cash < 15:
                    action Function(msg.msg, "You have insufficient money.")
                    mouse "interaction_m"

                else:
                    action SetVariable("item_manga_shop", True), SetVariable("item_manga_arrival", 1), Function(main_mc.lose_cash, 15), Function(msg.msg, "You will get a message from Quickies!")
                    mouse "interaction_m"
            else:
                action NullAction()
                mouse "deny_m"
            xpos 130

        imagebutton:
            idle "quikies_item_gen5"
            action NullAction()
            xpos 315


screen map2():

    zorder 2 tag maps
    hbox:
        xalign 0.2
        yalign 0.61
        spacing 10
        imagebutton:
            idle "quikies_item_bunnysuit1"
            action NullAction()

        imagebutton:
            idle "quikies_item_gawkgawk"
            action NullAction()
            xpos 180

        imagebutton:
            idle "quikies_item_vitamins"
            action NullAction()
            xpos 400

screen map3():

    zorder 2 tag maps
    hbox:
        xalign 0.2
        yalign 0.61
        spacing 10

        if christmas_enable == 0:

            imagebutton:
                idle "quikies_item_gawkgawk"
                action NullAction()
                xpos -190
        else:

            imagebutton:
                if item_christmastree_shop == True:
                    idle "quikies_item_tree_sold"

                else:
                    idle "quikies_item_tree"

                if item_christmastree_shop == False:
                    if main_mc.cash < 15:
                        action Function(msg.msg, "You have insufficient money.")
                        mouse "interaction_m"

                    else:
                        action SetVariable("item_christmastree_shop", True), SetVariable("item_christmastree_arrival", 1), Function(main_mc.lose_cash, 15), Function(msg.msg, "You will get a message soon !")
                        mouse "interaction_m"
                else:
                    action NullAction()
                    mouse "deny_m"


            imagebutton:
                if item_christmassanta_shop == True:
                    idle "quikies_item_santa_sold"
                    xpos 100
                else:
                    idle "quikies_item_santa"
                    xpos 100
                if item_christmassanta_shop == False:
                    if main_mc.cash < 25:
                        action Function(msg.msg, "You have insufficient money.")
                        mouse "interaction_m"

                    else:
                        action SetVariable("item_christmassanta_shop", True), SetVariable("item_christmassanta_arrival", 1), Function(main_mc.lose_cash, 25), Function(msg.msg, "You will get a message soon !")
                        mouse "interaction_m"
                else:
                    action NullAction()
                    mouse "deny_m"

            imagebutton:
                idle "quikies_item_gawkgawk"
                action NullAction()
                xpos 240
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc















































































init python:
    class LocationWashroomf1(Location):
        title="washroom F1"
        def scene(self,elements):
            elements.append("images/sadie_house/washing_room/bg_washroom{dark}.jpg")
            
            
            
            if eleanor_story == 34:
                elements.append([(279, 739),"images/sadie_house/washing_room/inter_eleanorbra{dark}_{state}.png", "eleanor_bra_laundry_interact", "*^"])
            
            
            elements.append([(0, 1),"images/sadie_house/washing_room/inter_doorwashroom1{dark}_{state}.png", "goto_hallwayf1", "*>"])
            
            
            elements.append([(362, 419),"images/sadie_house/washing_room/wash_machine{dark}_{state}.png", "laundry_machine_inter", "*^"])
















default loc_washroomf1 = LocationWashroomf1()

label goto_washroomf1:
    call set_location ("loc_washroomf1") from _call_set_location_13
    show screen main_hud_icon

    return


label eleanor_bra_laundry_interact:
    $ spareitem_eleanor = True
    hide screen main_hud_icon
    show lucas normal default pose37 at left with dissolve
    pause
    show lucas normal default_talk pose37 at left
    l_mc "this must be it."
    l_mc "I should hold on to it for her"
    l_mc ". . ."
    l_mc "Hmmm"
    show lucas normal puzzle pose37 at left


    show lucas normal puzzle_d pose37 at left
    l_mc "S-N-F-F S-N-I-F-F"
    show lucas normal default_talk pose37 at left
    l_mc "wow it still has her rose scented smell on it."
    l_mc "I can’t get her out of my head"
    l_mc "I just want to fap at least once with her bra and the image she sent me"
    l_mc "now I have her signature smell"
    l_mc "I better take this upstairs to my room in privacy."
    hide lucas normal default_talk pose37 at left with dissolve

    pause
    show item_bra_1 at truecenter with dissolve
    pause
    $ inv.append(item_bra1)
    hide item_bra_1 at truecenter with dissolve
    show screen item_updated_notify with dissolve
    $ eleanor_story += 1
    jump goto_washroomf1
    return

label laundry_machine_inter:
    if chores_unlocked == False:
        l_mc ". . . ?"
        return
    elif True:
        menu:
            "Work ?" if True:
                if now(["monday", "tuesday"]):
                    l_mc "Alright, let's get started"
                    jump clean_laundry_start
                    return
                elif True:

                    l_mc "Can't, only once per week. Every monday & tuesday !"
                    jump goto_washroomf1
                    return
            "Nah" if True:

                jump goto_washroomf1
                return

        label clean_laundry_start:
            hide screen main_hud_icon
            show black with dissolve
            scene chores_laundry_01
            hide black
            pause
            l_mc "Let's grab the clothe"
            show chores_laundry_02 with Dissolve(.3)
            pause
            show chores_laundry_02 with vpunch
            pause
            hide chores_laundry_02 with Dissolve(.3)
            l_mc "There we go."
            $ random_cash_range = renpy.random.randint(9,17)
            $ main_mc.got_cash(random_cash_range)

            show screen money_earn_display with Dissolve(.3)


            $ renpy.scene()
            $ now.advance()
            show screen main_hud_icon
            jump goto_washroomf1
            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

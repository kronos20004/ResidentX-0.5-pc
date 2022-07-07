


























































init python:
    class LocationHallwayf1(Location):
        title="Hallway F1"
        def scene(self,elements):
            elements.append("images/sadie_house/hallway_f1/bg_f1hallway{dark}.jpg")
            
            
            
            elements.append([(1027,230),"images/sadie_house/hallway_f1/inter_backdoor2{dark}_{state}.png", "goto_backyard", "*>"])
            
            
            elements.append([(483,56),"images/sadie_house/hallway_f1/inter_doorgarage2{dark}_{state}.png", "goto_garagef1", "*>"])
            
            
            elements.append([(817,175),"images/sadie_house/hallway_f1/inter_doorwashroom2{dark}_{state}.png", "goto_washroomf1", "*>"])
            
            
            if go_back_btn == True:
                elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_livingf1", "*>"])











default loc_hallwayf1 = LocationHallwayf1()

label goto_hallwayf1:
    call set_location ("loc_hallwayf1") from _call_set_location
    show screen main_hud_icon


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

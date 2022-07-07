












































































init python:
    class LocationGaragef1(Location):
        title="Garage F1"
        def scene(self,elements):
            elements.append("images/sadie_house/garage/bg_garage{dark}.jpg")
            
            
            
            if char_at("van","garage") and not is_talking("van"):
                elements.append([(929, 397),"images/sadie_house/garage/inter_minivan{dark}_{state}.png", "garage_van_inter", "*^"])  
            
            
            
            elements.append([(1597, 880),"images/sadie_house/garage/inter_measuringtape{dark}_{state}.png", "garage_tape_inter", "*^"])  
            
            
            elements.append([(0,87),"images/sadie_house/garage/inter_doorgarage1{dark}_{state}.png", "goto_hallwayf1", "*>"])
            
            
            elements.append([(519, 44),"images/sadie_house/garage/inter_shovel{dark}_{state}.png", "$blocked$","@^SHOVEL" ])











default loc_garagef1 = LocationGaragef1()

label goto_garagef1:
    call set_location ("loc_garagef1") from _call_set_location_14
    show screen main_hud_icon




    return

label garage_tape_inter:
    l_mc "A measuring tape, cool"
    return

label garage_van_inter:
    l_mc "[sadie_refer_input]'s van, don't think I can drive it yet"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

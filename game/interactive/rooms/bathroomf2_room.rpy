

init python:
    class LocationBathroomf2(Location):
        title="Bathroom F2"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/bathroom_f2/bg_bathroom{dark}.jpg")
            elif now(["night"]):
                elements.append("images/sadie_house/bathroom_f2/bg_bathroom_midnight.jpg")
            
            
            elements.append([(34, 66),"images/sadie_house/bathroom_f2/inter_mirror{dark}_{state}.png", "bathroom_cabinet_inter", "*^"])
            
            
            
            elements.append([(916,233),"images/sadie_house/bathroom_f2/inter_showerdoor1{dark}_{state}.png","$blocked$", None])
            
            
            elements.append([(1300, 911),"images/sadie_house/roamingbutton_goback.png", "goto_hallwayf2", "*^"])











default loc_bathroomf2 = LocationBathroomf2()

label goto_bathroomf2:
    call set_location ("loc_bathroomf2") from _call_set_location_6
    show screen main_hud_icon

    if eleanor_story == 22:
        jump eleanor_third_session_bath
        return

    return


label bathroom_cabinet_inter:
    "Nothing to see here"
    jump goto_bathroomf2
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

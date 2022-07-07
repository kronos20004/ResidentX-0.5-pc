init python:
    class LocationKonamiBackyard(Location):
        title="Konami Backyard"
        def scene(self,elements):
            elements.append("images/konami_house/konami backyard/location_konami_backyard{dark}.jpg")
            
            
            
            
            elements.append([(888, 499),"images/konami_house/konami backyard/inter_doorkonami1{dark}_{state}.png", "konami_lobby_inter", "*>"])
            
            
            if go_back_btn == True:
                elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_backyard2", "*>"])

default loc_konamibackyard = LocationKonamiBackyard()

label goto_konami_backyard:
    call set_location ("loc_konamibackyard") from _call_set_location_29
    show screen main_hud_icon

    return

label konami_lobby_inter:
    if konami_story == 13:
        jump konami_event_3
        return


    jump goto_konami_lobby
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

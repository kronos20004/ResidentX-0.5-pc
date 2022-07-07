init python:
    class LocationKonamiRoom(Location):
        title="Konami Room"
        def scene(self,elements):
            elements.append("images/konami_house/konami room/location_konami_bedroomkonami{dark}.jpg")
            
            
            
            
            elements.append([(755, 568),"images/konami_house/konami room/inter_konami_bedkonami1{dark}_{state}.png", "$blocked$", None])
            
            
            
            
            
            
            
            elements.append([(169, 238),"images/konami_house/konami room/inter_konami_doorexit1{dark}_{state}.png", "goto_konami_hallway", "*>"])

default loc_konamiroom = LocationKonamiRoom()

label goto_konami_room:
    call set_location ("loc_konamiroom") from _call_set_location_27
    show screen main_hud_icon
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

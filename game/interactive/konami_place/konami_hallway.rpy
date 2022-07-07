init python:
    class LocationKonamiHallway(Location):
        title="Konami Hallway"
        def scene(self,elements):
            elements.append("images/konami_house/konami hallway/location_konami_hallway{dark}.jpg")
            
            
            
            
            elements.append([(737, 0),"images/konami_house/konami hallway/inter_konami_bedroomkonami{dark}_{state}.png", "konami_door_inter", "*>"])
            
            
            
            elements.append([(1163, 0),"images/konami_house/konami hallway/inter_konami_bedroommommy{dark}_{state}.png", "$blocked$", None])
            
            
            
            elements.append([(602, 838),"images/konami_house/konami hallway/inter_konami_staircase2{dark}_{state}.png", "goto_konami_lobby", "*>"])

default loc_konamihallway = LocationKonamiHallway()

label goto_konami_hallway:
    call set_location ("loc_konamihallway") from _call_set_location_36
    show screen main_hud_icon
    return

label konami_door_inter:
    if konami_story == 20 and now(["monday","tuesday","wednesday","thursday","friday"]) and now(["afternoon"]):
        jump konami_event_5
        return

    if konami_door_access == True:
        jump goto_konami_room
        return
    l_mc "Nope. Seems like it is locked"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

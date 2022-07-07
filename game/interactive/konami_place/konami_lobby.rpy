init python:
    class LocationKonamiLobby(Location):
        title="Konami Lobby"
        def scene(self,elements):
            elements.append("images/konami_house/konami lobby/location_konami_lobby{dark}.jpg")
            
            
            
            
            elements.append([(712, 483),"images/konami_house/konami lobby/inter_konami_doorbathroom1{dark}_{state}.png", "$blocked$", None])
            
            
            
            elements.append([(850, 113),"images/konami_house/konami lobby/inter_konami_staircase1{dark}_{state}.png", "goto_konami_hallway", "*>"])
            
            
            
            elements.append([(850, 911),"images/sadie_house/roamingbutton_goback.png", "goto_konami_backyard", "*>"])

default loc_konamilobby = LocationKonamiLobby()

label goto_konami_lobby:
    call set_location ("loc_konamilobby") from _call_set_location_28
    show screen main_hud_icon

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

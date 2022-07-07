






























































































init python:
    class Locationlobbyf1(Location):
        title="Lobby F1"
        def scene(self,elements):
            if now(["morning", "afternoon", "evening"]):
                elements.append("images/sadie_house/lobby_f1/bg_lobby{dark}.jpg")
            elif now(["night"]):
                elements.append("images/sadie_house/lobby_f1/bg_lobby_midnight.png")
            
            if christmas_decoration_enable == True:
                if now(["morning", "afternoon", "evening"]):
                    elements.append("images/sadie_house/lobby_f1/lobby_christmas{dark}.png")
                elif now(["night"]):
                    elements.append("images/sadie_house/lobby_f1/lobby_christmas_midnight.png")
            
            
            
            elements.append([(386,519),"images/sadie_house/lobby_f1/inter_chairdiner1{dark}_{state}.png","$blocked$", None])
            
            
            if eleanor_story == 2:
                elements.append([(882,448),"images/sadie_house/lobby_f1/inter_couch1{dark}_{state}.png","$blocked$", None])
            elif sadie_story == 3:
                elements.append([(882,448),"images/sadie_house/lobby_f1/inter_couch1{dark}_{state}.png", "lobby_sadie_story_lock", "*>"])
            else:
                elements.append([(882,448),"images/sadie_house/lobby_f1/inter_couch1{dark}_{state}.png", "goto_livingf1", "*>"])
            
            
            if eleanor_story == 2:
                elements.append([(1375,508),"images/sadie_house/lobby_f1/inter_kitchen1{dark}_{state}.png","$blocked$", None])
            else:
                elements.append([(1375,508),"images/sadie_house/lobby_f1/inter_kitchen1{dark}_{state}.png", "goto_kitchenf1", "*>"])
            
            
            
            if eleanor_story == 2:
                elements.append([(1099,146),"images/sadie_house/lobby_f1/inter_staircase2{dark}_{state}.png","$blocked$", None])
            else:
                elements.append([(1099,146),"images/sadie_house/lobby_f1/inter_staircase2{dark}_{state}.png", "goto_hallwayf2", "*>"])
            
            
            elements.append([(850, 911),"images/sadie_house/roamingbutton_frontdoor.png", "goto_frontf1", "*^"])
            
            
            
            
            
            
            
            
            
            if now(["evening"]):
                if char_at("sadiecouch","sadieliv") == True: 
                    elements.append([(882,397),"images/sadie_house/lobby_f1/CharButton_Sadie3Alt.png", None])
                
                
                if random_tv_screen == 1:
                    elements.append([(679,342),"images/sadie_house/lobby_f1/inter_tv2_night.png", None])
                
                elif random_tv_screen == 2:
                    elements.append([(679,342),"images/sadie_house/lobby_f1/inter_tv2_night_alt.png", None])



default loc_lobbyf1 = Locationlobbyf1()

label goto_lobbyf1:
    call set_location ("loc_lobbyf1") from _call_set_location_8
    show screen main_hud_icon

    return


label lobby_sadie_story_lock:
    l_mc "I'm hungry"
    jump goto_lobbyf1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

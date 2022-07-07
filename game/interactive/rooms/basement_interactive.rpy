






































































































































































































init python:
    class LocationBasement(Location):
        title="Basement"
        def scene(self,elements):
            elements.append("images/sadie_house/basement/bg_basement{dark}.jpg")
            
            
            
            elements.append([(231,517),"images/sadie_house/basement/inter_brick{dark}_{state}.png", "basement_brick_inter", "*^"])
            
            
            
            if handsaw_pickup == False:
                elements.append([(1495,752),"images/sadie_house/basement/inter_handsaw{dark}_{state}.png", "basement_saw_inter", "*^"])
            
            
            
            if not loc_basement["basement_hatch_open"]:
                elements.append([(436,873),"images/sadie_house/basement/inter_basementhatch1{dark}_{state}.png", "basement_hatch_inter", "*^"])
            else:
                if now(["morning", "afternoon", "evening"]):
                    elements.append([(436,873),"images/sadie_house/basement/inter_basementhatch1{dark}_{state}.png", "basement_hatch_inter", "*^"])
                if now("night"):
                    elements.append([(325,561),"images/sadie_house/basement/inter_basementhatch2{dark}_{state}.png", "basement_hatch_inter", "*^"])
            
            
            
            
            elements.append([(295,193),"images/sadie_house/basement/inter_staircase1{dark}_{state}.png", "goto_livingf1", "*>"])
            
            
            elements.append([(439,390),"images/sadie_house/basement/inter_fusebox{dark}_{state}.png", "basement_powerbox_inter", "*^"])













default loc_basement = LocationBasement()

label goto_basement:
    call set_location ("loc_basement") from _call_set_location_7
    show screen main_hud_icon


    return



label basement_brick_inter:

    if item_dreamkey in inv and facility_story == 3:
        if now(["morning", "afternoon", "evening"]):
            hide screen main_hud_icon
            if now(["morning", "afternoon"]):
                scene basement_wallbrick_bg_day
            elif True:
                scene basement_wallbrick_bg_night

            l_mc "Wait a second. That oddly shaped object I found in my bed. The shape has an uncanny resemblance to the shape of this brick"
            l_mc "I'll step back for now. ."
            l_mc "I should come back once [sadie_refer_input] is asleep. This could be another one of this house’s secrets. [leo_refer_input] did ask me to keep quiet, so I’ll just do that for now"
            jump goto_basement
            return

        elif now("night"):
            hide screen main_hud_icon
            l_mc "That strange object I found in my bed has uncanny resemblance to the shape of this brick"
            l_mc "[leo_refer_input] did ask me to keep quiet about anything strange I find in this house"
            l_mc "[sadie_refer_input] is asleep already, I should investigate. . "
            scene basement_wallbrick_bg_night
            pause
            l_mc "sure enough, it looks just like the brick"
            l_mc "ah what the hell, what could I possibly happen now?"
            l_mc "Lets see if anything happens"
            show basement_wallbrick_lucas1
            l_mc "The hole is the exact same size"
            l_mc "I'm almost too scared to insert it all the way through"
            l_mc "but fuck it, let's do it"
            hide basement_wallbrick_lucas1
            show basement_wallbrick_lucas2
            pause
            hide basement_wallbrick_lucas2
            show basement_wallbrick_lucas3
            l_mc "and bayum!"
            l_mc "Perfect fit"
            l_mc "Now it's vibrating, making my hand feel fuzzy"
            hide basement_wallbrick_lucas3
            l_mc ". . ."
            l_mc "Well.. what did that do ?"
            stop music
            scene basement_hatch1 with Dissolve(.3)
            play sound "music/hidden_wall_01.wav"
            pause(.5)
            scene basement_hatch2
            show basement_hatch_light with Dissolve(.3)
            pause
            l_mc "Jesus, you have to be kidding me right now"
            l_mc "This is by far the creepiest thing I've seen so far"
            l_mc "How in the hell has this been here the whole time without us knowing"
            l_mc "What has [leo_refer_input] been hiding from us? Who even is he?"
            l_mc "Should I even go down there?"
            l_mc "I want to take a quick glimpse"
            l_mc ". . ."
            l_mc "I better not though"
            l_mc "Too much risk & excitement to take in"
            l_mc "I'll come back another day"
            l_mc "I have the key, so I can come back whenever I want"
            l_mc "I have a lot to think about for now. Probably won’t even get any sleep now."
            $ mystery_stair_map_icon = True

            play music "music/music4.mp3"
            $ facility_story += 1
            $ loc_basement["basement_hatch_open"] = True
            show screen map_updated_notify with dissolve
            jump goto_basement
            return

        elif facility_story == 4:
            hide screen main_hud_icon
            l_mc "Fuck off, come back later my dude. REACHED THE END OF THIS CONTENT SORRY"
            jump goto_basement
            return
    elif True:
        l_mc "...."
        return

    if mystery_brick_map_icon == False:
        $ mystery_brick_map_icon = True
        show screen map_updated_notify with dissolve
        return
    jump goto_basement
    return

    hide screen main_hud_icon
    if now("morning", "afternoon"):
        if facility_story == 4:
            scene basement_wallbrick_bg_day
            l_mc "I already have checked this hole, there is nothing to see here for now"
            jump goto_basement
            return
        elif True:
            scene basement_wallbrick_bg_day
            l_mc "What is this? . . "
            l_mc "This odd brick has been here for as long as I can remember. Don’t know what it’s for."
            l_mc "Probably some unfinished construction?"
            l_mc "This hole goes in pretty deep"
            jump goto_basement
            return
    elif now("evening", "night"):
        if facility_story == 4:
            scene basement_wallbrick_bg_night
            l_mc "I already have checked this hole, there is nothing to see here for now"
            return
        elif True:
            scene basement_wallbrick_bg_night
            l_mc "What is this? . . "
            l_mc "This odd brick has been here for as long as I can remember. Don’t know what it’s for."
            l_mc "Probably some unfinished construction?"
            l_mc "This hole goes in pretty deep"
            jump goto_basement
            return
    jump goto_basement
    return

label basement_saw_inter:
    hide screen main_hud_icon
    show lucas normal pose4 default_d_talk at left with Dissolve(.5)
    l_mc "A saw ?"
    l_mc "I should pick this up"
    show lucas normal pose10 puzzle_d_talk
    l_mc "Could be useful"
    show lucas normal pose10 default
    $ inv.append(item_handsaw)
    $ handsaw_pickup = True

    "Handsaw acquried !"
    show screen item_updated_notify with dissolve
    jump goto_basement
    return

label basement_hatch_inter:
    if facility_story == 4 and now("night"):
        l_mc "NOOO, just no."
        jump goto_basement
        return
    elif True:
        l_mc ". . ?"
        l_mc "Yeah, there is nothing here"
        jump goto_basement
        return

label basement_powerbox_inter:
    l_mc "Powerbox? seems like this can probably shut the lights off"
    jump goto_basement
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

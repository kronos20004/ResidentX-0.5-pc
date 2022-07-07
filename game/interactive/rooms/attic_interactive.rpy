


















































































































































































init python:
    class LocationAttic(Location):
        title="Attic"
        def scene(self,elements):
            elements.append("images/sadie_house/attic/bg_attic{dark}.jpg")
            
            
            elements.append([(330, 708),"images/sadie_house/attic/inter_hatchattic{dark}_{state}.png", "goto_hallwayf2", "*>"])
            
            
            
            if attic_paint == False:
                elements.append([(0, 182),"images/sadie_house/attic/inter_doorattic1{dark}_{state}.png", "attic_paint_interaction", "*>"])
            else:
                elements.append([(40, 176),"images/sadie_house/attic/inter_doorattic2{dark}_{state}.png", "attic_paint_interaction", "*>"])
            
            
            elements.append([(480, 443),"images/sadie_house/attic/inter_gramaphone{dark}_{state}.png", "attic_gramophone_inter", "*^"])
            
            
            elements.append([(0, 699),"images/sadie_house/attic/inter_dvdxxx{dark}_{state}.png", "attic_dvd_inter", "*^"])
            
            
            
            
            if scope_attic1 == True:
                elements.append([(700, 302),"images/sadie_house/attic/inter_windowattic2{dark}_{state}.png", "attic_window2_inter", "*^"])
            else:
                elements.append([(700, 302),"images/sadie_house/attic/inter_windowattic1{dark}_{state}.png", "attic_window_inter", "*^"])













default loc_attic = LocationAttic()

label goto_attic:
    call set_location ("loc_attic") from _call_set_location_9
    show screen main_hud_icon



    return


label attic_gramophone_inter:
    "A gramophone, huh."
    jump goto_attic
    return

label attic_door_inter:
    if door_map_icon == False:
        show screen map_updated_notify with dissolve
        $ door_map_icon = True
        return
    if attic_paint_discovered == False:
        l_mc "What in the world is this door?"
        l_mc "Why would a strange painting be used to cover this up ?. ."
        l_mc "That's some lousy job of trying to hide such an obvious door"

        l_mc "anyways.... I wonder"
        l_mc "What is in that door?"

        l_mc "The damn thing won't nudge"
        l_mc "I assume it's locked from the other side, since it won't open on this side"
        $ attic_paint_discovered = True
        jump goto_attic
        return
    elif True:
        l_mc "Can't open the door.. seems to be locked on the other side"
        jump goto_attic
        return

label attic_dvd_inter:
    "A dvd.. Don't really need this"
    jump goto_attic
    return

label attic_window_inter:
    if atticwindow_map_icon == False:
        $ atticwindow_map_icon = True
        show screen map_updated_notify with dissolve           
        "Seems interesting out there... not going to look right now"
        jump goto_attic
        return
    l_mc "Nothing to see here."
    jump goto_attic
    return

label attic_window2_inter:
    if now(["morning", "afternoon"]):
        l_mc "Not now. I need to wait until night time for me to use the telescope."
        jump goto_attic
        return
    if now(["evening", "night"]) and jada_story == 2:
        hide screen main_hud_icon
        show lucas normal pose4 default at left with moveinleft
        show sadie normal pose1 default at right with moveinright
        pause
        show sadie normal pose1 default_talk
        l_sadie "There you are honey."
        show sadie normal pose1 default
        show lucas normal pose4 default_talk
        l_mc "What’s up?"
        show sadie normal pose1 happy_talk
        show lucas normal pose4 default
        l_sadie "So, I have to tell you something. I finally got my first Yoga student to teach!"
        show sadie normal pose1 happy
        show lucas normal pose4 alert_talk
        l_mc "What, really?"
        show sadie normal pose1 default
        show lucas normal pose4 default_talk
        l_mc "That’s amazing. I knew someone would recognize your talent sooner or later"
        l_mc "And when are you starting classes?"
        show lucas normal pose4 default
        show sadie normal pose1 happy_talk
        l_sadie "Just Saturdays and Sundays for now. I only have one student to teach but you’ll see, I’ll soon get more members that want to learn."
        show sadie normal pose1 happy
        show lucas normal pose4 glad_talk
        l_mc "Well, I’m happy for you, [sadie_refer_input]."
        show lucas normal pose4 glad
        show sadie normal pose1 smirk_talk
        l_sadie "And of course, you're welcome to come into the yoga room when I have classes if you’d like. I could always use that extra hand."
        show lucas normal pose4 glad_talk
        show sadie normal pose1 smirk
        l_mc "Mmmm…. Ill think about it but no promises. "
        show lucas normal pose4 glad
        show sadie normal pose1 default_talk
        l_sadie "If you do decide to join, just walk in. All day on Saturdays and Sundays so don’t forget me."
        show sadie normal pose1 awe_talk
        l_sadie "Goodnight sweetie."
        show sadie normal pose1 awe
        show lucas normal pose4 glad_talk
        l_mc "Goodnight."
        hide sadie normal pose1 default at right with moveoutright
        pause
        show lucas normal pose4 mkay
        l_mc ". . ."
        show lucas normal pose4 mkay_talk
        l_mc "what was I going to do again before I got interrupted…?"
        show lucas normal pose4 alert_talk
        l_mc "Oh right, the telescope. But on second thought, maybe I shouldn’t."
        show lucas normal pose4 puzzle_talk
        l_mc "Could be too risky. I may get caught this time and that’d be some really bad news."
        show lucas normal pose4 sad_talk
        l_mc "I better just chill for a while from the whole spying."
        show lucas normal pose4 glad_talk
        l_mc "As for [sadie_refer_input], maybe I should take her up on that offer. Could be interesting."
        show lucas normal pose4 glad_talk
        l_mc "Saturdays and Sundays, won’t forget !"
        hide lucas normal pose4 default at right with moveoutleft
        show screen main_hud_icon
        $ renpy.scene()
        $ jada_story += 1
        return

    if now(["evening","night"]) and jada_story == 0:
        window hide
        show black with dissolve
        hide screen main_hud_icon
        pause
        show event_windowpeeking_jada_01 zorder 1 with fade
        hide black
        l_mc "Hmmm. . . honestly, I was hoping to see a lot more stars tonight."
        l_mc "Kind of hard to see any stars with all the city’s light pollution."
        l_mc "Especially with all these houses blasting the power of the sun into my eyes."
        l_mc "what is this? I think, I finally found something that’s caught my interest."
        hide event_windowpeeking_jada_01
        show event_windowpeeking_jada 3 with Dissolve(.1)
        l_mc "Jada?! That’s one of my [sadie_relationship_input]’s friends."
        l_mc "I’ve met her a few times and damn is she fine if I say so myself."
        l_mc "This should definitely make up for the lack of stars just fine."
        show event_windowpeeking_jada 4 with dissolve
        l_mc "What a gorgeous frame she has. "
        l_mc "Almost the embodiment of perfection. "
        l_mc "I’d do almost anything to get a shot at her."
        show event_windowpeeking_jada 5
        l_mc "Huh ?"
        l_mc "does she see me? There's no way she can see me unless the lens of the telescope is glimmering"
        show event_windowpeeking_jada 6
        l_mc "Crap! Have to cut the show a little short for tonight. "
        hide event_windowpeeking_jada 6
        show black
        pause
        hide black
        show lucas normal pose4 alert at left with Dissolve(.1)
        pause
        show lucas normal pose4 alert_talk
        l_mc "Damn, I really hope she didn’t see me."
        l_mc "She could tell my [sadie_relationship_input] if she knows it was me. I’d be dead for sure."
        show lucas normal pose4 happy_talk
        l_mc "that shine from the telescope could’ve been anything for all she knows."
        l_mc "I think I’m good though. No need to worry myself anymore. Just have to put it behind me and act like nothing’s wrong."
        show lucas normal pose4 sad_talk
        l_mc "I’ll leave the telescope here for now."
        show lucas normal pose4 happy_talk
        l_mc "I can try tomorrow night again and see if she’s at her window again."
        hide lucas normal pose4 happy_talk with dissolve
        $ renpy.scene()
        $ jada_story += 1
        jump goto_attic
        return
    l_mc "Not now."
    jump goto_attic
    return



label attic_paint_interaction:
    if attic_paint == False:
        hide screen main_hud_icon
        show lucas normal pose4 assured at left with Dissolve(0.2)
        pause
        show lucas normal pose4 puzzle_talk
        l_mc "Hm......"
        l_mc "This painting looks like something oddly familiar"
        show lucas normal pose4 puzzle
        pause
        l_mc "*ahem*"
        show lucas normal pose13 mkay
        show lucas normal pose13 mkay_talk with Dissolve(0.2)
        l_mc "There seems to be something behind"
        show lucas normal pose4 default_talk
        l_mc "Ahh, gotta move this painting"
        show lucas normal pose4 puzzle
        pause 
        l_mc ". . . ."
        show lucas normal pose5 happy_talk with Dissolve(0.1)
        $ attic_paint = True
        l_mc "There we go, moved it !"
        hide lucas normal pose5 happy_talk with Dissolve(0.1)
        jump goto_attic
        return

    if attic_hidden_door == False:
        l_mc "Can't open the door.. seems to be locked on the other side"
        return
    elif True:
        jump goto_attic2
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

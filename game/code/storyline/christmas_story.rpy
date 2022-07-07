transform sadie_christmas_position:
    xpos 490
    ypos 262

transform lucas_santa_couch_postiion:
    xpos 740
    ypos 360

label christmas_l_1:
    hide screen main_hud_icon
    show black
    $ christmas_decoration_enable = True

    $ exit_btn = False
    centered "{color=ffff}{size=80}{font=gui/fonts/acumin_regular.otf}{b} 1 Hour later{/b}{/font}{/size}{/color}"
    hide black with dissolve


    show lucas normal pose4 default at center
    pause
    show lucas normal default_talk
    l_mc "Well, that doesn’t look too bad If I say so myself. I did some fine work, now I can’t wait to see her reaction. She’s going to have her Christmas if it’s the last thing I do."
    l_mc "Gonna go to sleep now."
    hide lucas normal
    show black with dissolve
    centered "{color=ffff}{size=80}{font=gui/fonts/acumin_regular.otf}{b} Next day {/b}{/font}{/size}{/color}"
    show charsadie_christmas_sight at sadie_christmas_position
    hide black with dissolve
    pause
    l_mc "[sadie_refer_input] ?"
    hide charsadie_christmas_sight with dissolve
    pause
    show sadie normal pose default at right with easeinright
    show lucas normal pose4 default at left with easeinleft
    pause
    show sadie normal pose default_talk
    l_sadie "Lucas, did you do all this?"
    show sadie normal pose default
    show lucas normal pose4 happy_talk
    l_mc "Marry early Christmas [sadie_refer_input]."
    show lucas normal pose4 happy
    show sadie normal pose awe_talk
    l_sadie "I don’t know what to say. You’ll actually make me cry."
    show lucas normal pose4 happy_talk
    show sadie normal pose awe
    l_mc "Tears of joy, I hope. But it isn’t over yet, just wait until next Thursday on Christmas. I’ll make you cry even more; I hope."
    show lucas normal pose4 happy
    show sadie normal pose awe_talk
    l_sadie "Come here sweetie."

    hide lucas normal with Dissolve(.15)
    hide sadie normal with Dissolve(.15)
    show sadie universal_hug pose default with Dissolve(.15)
    pause
    show sadie universal_hug relief
    l_sadie "Thank you honey, I really mean it. You’ll always be my everything, just Don’t tell bailey I said that."
    l_mc "I feel the same way. We can always have each other if nothing else."
    l_sadie "You better mean it."
    l_mc "Always."

    pause
    hide sadie universal_hug relief

    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    show lucas normal pose4 default_talk
    l_mc "I’ll be off now but come Thursday night, and it’ll be a good Christmas just like the ones we used to have."
    show lucas normal pose4 default
    show sadie normal pose default_talk
    l_sadie "Can’t wait dear, bye."
    show sadie normal pose default
    show lucas normal pose4 default_talk
    l_mc "Bye."

    hide lucas normal with easeoutleft
    hide sadie normal with easeoutright

    show black with dissolve
    centered "{color=ffff}{size=80}{font=gui/fonts/acumin_regular.otf}{b} Next Thursday Midnight {/b}{/font}{/size}{/color}"
    $ christmas_story += 1
    jump goto_lucasroom
    return

label christmas_l_2:
    hide screen main_hud_icon
    show lucas normal pose4 default
    l_mc "[sadie_refer_input] is waiting for me downstairs now. I better get that costume on my desk and wear before I head downstairs."
    l_mc "Let's grab the outfit"
    $ lucas_wearsanta_suit = True
    "*Grabs*"
    hide lucas normal pose4 default
    pause
    show lucas santa pose default with dissolve
    pause
    play sound "music/audio_zipper_01.wav" 
    stop music fadeout 1.0
    play music "music/christmas_jazz.mp3" fadein 1.0
    l_mc "Fits a little tight but should work perfect for her."

    l_mc "Ho h . . .*ahem*"
    show lucas santa pose suprised
    l_mc "HO ho HO!"
    hide lucas santa pose default with dissolve

    $ christmas_story += 1
    jump goto_livingf1
    return




label christmas_l_3:
    hide screen main_hud_icon
    show black
    pause
    hide black with dissolve
    show lucas santa pose default at left with easeinleft
    l_mc "HO ho HOOOO!"
    show sadie normal pose default at right with easeinright
    pause
    show sadie normal default_talk
    l_sadie "Lu… I mean… Santa!? I got my own little Santa?"
    show sadie normal happy_talk
    l_sadie "Best Christmas ever!"
    show sadie normal happy
    show lucas santa pose sure
    l_mc "I heard from your #1 fan that someone’s been good this year, so come now child."
    show lucas santa pose default
    l_mc "Let me hear your wishes for someone as special as you deserves a little more attention."
    hide sadie normal
    hide lucas santa

    show black zorder 1 with dissolve
    show sadiexmas_event 1 zorder 0
    hide black with dissolve
    l_mc "(That night we had was very special and probably will be one of the most memorable ones.)"
    l_mc "(I haven’t felt this close with her in long time and seeing her this happy was the best Christmas present I’ll ever receive.)"
    l_mc "(I just want to see her this joyful for as long as I can.) "
    show sadiexmas_event 2 with dissolve
    l_mc "(And for some odd reason, even with all the things that have been happening in our lives, none of that mattered that night.)"
    l_mc "(To share this moment just between the two of us, it washed everything away)"
    l_mc "(Merry Christmas [sadie_refer_input].)"
    hide sadiexmas_event
    show black with Dissolve(.15)
    hide black with dissolve

    show lucas santa pose default at center with Dissolve(.15)
    l_mc "The night is over and she’s gone off to sleep now. Somehow, I think she’ll have a goodnight sleep tonight."
    l_mc "That turned out to be much better than I thought it would’ve been. I just hope it turns out the same way next year. It wouldn’t be so bad if it was just me and her again."
    l_mc "I can only hope."
    l_mc "I’ll clean this place up though so she doesn’t have to do so tomorrow morning."
    l_mc "We sure did make a mess in here. I guess things get messy when you're having fu . . . "
    play sound "music/crack_rop.wav"
    show lucas santa pose suprised
    l_mc "What’s that? What is that noise I’m hearing?"
    stop sound fadeout 0.3
    l_mc "Sounds like it’s pretty close to me. It actually sounds like its coming from the chimney."
    show lucas santa pose mkay
    l_mc "Must be those damn racoons. I better shoo them away or they’ll make a mess of this place once they fit in through that chimney."
    stop music fadeout 1.0

    show black zorder 1 with dissolve
    show event_xmas_chimmey 1 zorder 1
    hide black with dissolve
    pause
    l_mc "(Let’s see)"
    l_mc "(Kind of hard to tell but I think it’s those racoons)"
    l_mc "(They are getting closer.)"
    l_mc "Alright you damn critters, this is no place for you so get lost. Come on now, scram!"
    show event_xmas_chimmey 2 with Dissolve(.15)
    play sound "music/crack_rop.wav"
    $ renpy.pause( 0.2 )
    stop sound fadeout 0.5
    l_unkown "what? Dammit!"
    stop sound
    l_mc "(What? Racoons don’t talk, it’s an intruder!?)"
    l_mc "Hey! What the hell do you think you're doing up there!?"
    l_mc "Get out of here before I call the cops!"
    l_unkown "No wait. You got it all wrong"
    l_unkown "Shit, I’m slipping."
    l_mc "I don’t care just go back up the way you came from!"
    l_unkown "I can’t hold on, move out of the way!"
    play sound "music/crack_rop.wav"
    $ renpy.pause( 0.2 )
    stop sound fadeout 0.5
    show event_xmas_chimmey 3 with Dissolve(.15)
    l_mc "No, you get out of th . . . oh."
    l_unkown "Falling through!!"
    hide event_xmas_chimmey
    play sound "music/crash_fall.mp3"
    show black zorder 2 with hpunch
    show event_xmas_facesitting 1 zorder 1

    stop sound fadeout 0.6
    pause
    hide black with dissolve
    l_mc "Auugh…"
    l_unkown "Ouch."
    l_unkown "Dammit kid, I told you to get out of the way. Now look at me."
    l_mc "Look at you? How about you look at me?"
    l_mc "You’re literally sitting on my face! Now get off."
    l_unkown "Hold on, I think I pulled something."
    l_mc "How are you not embarrassed, woman?"
    l_unkown "Oh, shut up you poor thing, other people would pay for this moment you know."
    l_mc "Yeah yeah, I get it already so just get your ass up off me already."
    show event_xmas_facesitting 2 with Dissolve(.15)
    l_unkown "Oh my, it seems you . . . uhh"
    hide event_xmas_facesitting
    show event_xmas_touchyhand 1
    l_mc "Yes, I know. What did you expect? You're still sitting on my face."
    l_mc "I think you're healed enough already to get up, don’t you?"

    l_unkown "What? Oh. . . right right. Sorry honey. I’m feeling good now."
    l_unkown "getting off."

    show black with Dissolve(.15)
    hide event_xmas_touchyhand
    hide event_xmas_facesitting
    pause
    play music "music/christmas_jazz.mp3" fadein 1.0
    hide black with Dissolve(.15)
    show lucas santa pose default dirt at left with easeinleft
    show claus normal pose1 default at right with easeinright

    pause
    show lucas santa pose angry
    l_mc "You have some nerve lady, stay right there and don’t try to run while I call the cops."
    show claus normal pose4 sas_talk
    l_unkown "You can’t do that, I’m not an intruder."
    show claus normal pose1 sas
    show lucas santa pose sure
    l_mc "Than what would you call it?"
    show claus normal pose1 default_talk
    l_unkown "Don’t you see my outfit?"
    show claus normal pose1 default
    show lucas santa pose mkay
    l_mc "You're Santa Claus, so what? I’m Santa too, hooray."
    l_mc "Doesn’t make it any better you sneaking in through my chimney."
    show lucas santa pose assured
    l_mc "What other excuse do you have before I make the call"
    show claus normal pose4 sas_talk
    l_unkown "I’m not Santa Claus you moron, I’m Mrs. Claus. As in his wife!"

    l_unkown "Does it look Like I have a huge gut or large beard to boast?"
    show claus normal pose1 sas
    show lucas santa pose puzzled
    l_mc "Even if that were true, wouldn’t you be a lot older? Looks like you're just wearing a wig to me."
    show lucas santa pose default
    l_mc "And It’s Santa’s Job to come in with the presents, not his wife’s."
    l_mc "The Jig is up you dirty crook, I’m dialing right now."
    show claus normal pose1 default_talk
    l_unkown "Well could a fake do this?"
    show claus normal pose1 ara
    pause
    show claus normal pose2 ara
    pause
    show claus normal pose2 ara magic1 with Dissolve(.15)
    pause
    show claus normal pose3 ara magic2 with Dissolve(.15)
    pause
    show overlay_sparkles at claus_sparkle_position with Dissolve(0.15)
    pause

    show overlay_sparkles at claus_sparkle_position3 with ease
    show lucas santa pose default none
    hide overlay_sparkles with Dissolve(0.15)
    pause
    show claus normal pose2 ara magic1 with Dissolve(.15)
    pause
    show claus normal pose2 ara none with Dissolve(.15)
    pause
    show claus normal pose ara none
    pause
    show lucas santa pose suprised
    l_mc "What the? How did you?"
    l_mc "But that doesn't make . . ."
    show claus normal pose1 default_talk
    l_claus "any sense, right? Like I said kid."
    show claus normal pose1 default_talk
    l_claus "I’m the real deal. Now put that phone away, so I can do my job here."
    l_claus "I don’t have all night. There’s still about a thousand more homes I have to break into and get this over with already."
    show lucas santa pose sure
    show claus normal pose default
    l_mc "You really are her, but how . . . why?"
    l_mc "And you don't look like an old lady at all."
    show lucas santa pose default
    show claus normal pose ara_talk
    l_claus "It's magic alright. I don't age anymore and it'd be too difficult to explain anyways. How else do you think santa has been doing it for years?"
    show claus normal pose ara
    l_mc "Hey, do you think we take a photo together?"
    show claus normal pose4 sas_talk
    l_claus "Absolutely not. You really think I can have some random guy take pictures of Santa’s wife?"
    show claus normal pose1 sas
    show lucas santa pose sad
    l_mc "Awe but why? It’s not like people would believe me anyways, even with a photo."
    l_mc "They'd just think you're a cosplayer."
    show claus normal pose1 default_talk
    l_claus "Hush now kid. Let's just get this over with."
    show lucas santa pose default
    l_claus "You're Lucas, right ? guess you’ve been somewhat good this year so that’s why I brought a present."
    show claus normal pose1 default
    l_mc "Oh nice. But why are you here exactly? I thought your husband was the one to deliver gifts."
    show claus normal pose1 default_talk
    l_claus "Yessss but lately his ass hasn’t been doing anything except sitting on his fat ass all day."
    l_claus "And I know he’s been fucking that elf, trissy behind my back as well. "
    show claus normal pose1 sas
    l_claus "* Dirty old asshole. I swear I’ll divorce his ass and take everything, even the reindeers. I just have to act as I haven’t seen anything for now.*"
    show lucas santa pose assured
    l_mc "Marriage problems huh?"
    show claus normal pose1 default_talk
    show lucas santa pose default
    l_claus "Oh damn. You weren’t supposed to hear that."
    show claus normal pose1 default
    show lucas santa pose sad
    l_mc "Feels bad."
    show claus normal pose default_talk
    l_claus "So now you know, you gonna make fun of me?"
    show claus normal pose default
    show lucas santa pose suprised
    l_mc "Why would I? It’s a sucky situation to be in."
    show lucas santa pose default
    show claus normal pose sas_talk
    l_claus "Right? I bet he’s sticking that dick inside that dirty little elf right now, the slut!"
    show claus normal pose sas
    show lucas santa pose assured
    l_mc "Well at least you haven’t had to sleep with him, right?"
    show lucas santa pose default
    show claus normal pose sas_talk with hpunch
    l_claus "That’s the problem, I haven’t had any action in YEARS! He’s been giving it all to her."
    show claus normal pose4 default_talk
    l_claus "Sorry if I’m rambling too much so thanks for listening kid."
    show claus normal pose default
    l_mc "Awe it’s no problem at all, go all out if you want."
    show claus normal pose default_talk
    l_claus "I’ll get back at him one day I swear it."
    show claus normal pose ara
    l_claus "Hmmmmmmm...."
    pause
    show lucas santa pose puzzled
    l_mc "What?"
    l_claus "Hm. . ."
    show lucas santa pose mkay
    l_mc "Ok, you're freaking me out now."
    show claus normal pose4 default_talk
    l_claus "Hey Lucas, who else is in the house ?"
    show claus normal pose default
    show lucas santa pose default
    l_mc "Just me and my [sadie_relationship_input] upstairs but she's sleeping right now and a heavy sleeper at that."
    show claus normal pose default_talk
    l_claus "Ok this could work."
    l_mc "What could work ?"
    show claus normal pose default_talk
    l_claus "why don’t we turn the light on and sit down; I think I’m still a little sore from the fall earlier. "
    show claus normal pose default
    show lucas santa pose sure
    l_mc "Sure, go ahead and rest before you have to go back."

    show black with Dissolve(.15)
    hide claus normal pose
    hide lucas santa pose
    show event_couch_nightalt
    show lucas santa_c pose default at lucas_santa_couch_postiion
    show event_couch_clausepose 1 at left
    pause
    hide black with Dissolve(.15)
    show lucas santa_c pose default_t
    l_mc "I thought you wanted to sit down."
    l_mc "Doesn’t your leg still hurt or something?"
    show lucas santa_c pose default
    l_claus "Na, feeling better already."
    show lucas santa_c pose mkay_t
    l_mc "Oh, alright than, guess I’ll stand back up again for no reason."
    show lucas santa_c pose mkay
    l_claus "Hold on Lucas, just sit there for a sec will ya?"
    show lucas santa_c pose mkay_t
    l_mc "Why though ?"
    show lucas santa_c pose mkay
    l_claus "Don’t worry about it and just sit still. "
    l_claus "Now tell me, are you seeing anybody right now, a love interest perhaps?"
    show lucas santa_c pose mkay_t
    l_mc "What’s it to you? Does that matter right now?"
    show lucas santa_c pose mkay
    l_claus "I’ll just take that as a no, so I’ll start moving on now."
    l_claus "Look, you already know my little home dilemma with Santa and how I want to get back at him so I figured you could help with that little problem."
    show lucas santa_c pose default_t
    l_mc "How would I do that? Don’t you two live in the north pole or something? And I’m no couples counseling advisor either."
    l_mc "Doubt I could possibly help you, sorry."
    show lucas santa_c pose default

    show lucas santa_c pose default
    show event_couch_clausepose 2 with Dissolve(.15)
    pause
    l_claus "Oh I think you can. I'm sure we'll find a solution."
    l_claus "And besides, you already have that outfit on so. Why don't you be my new Santa ?"
    show event_couch_clausepose 3 with Dissolve(.15)
    pause
    show lucas santa_c pose shock
    l_mc "Holy shit."
    show lucas santa_c pose default
    l_claus "Now now. No fowl language from you or I can't give you this gift for being too naughty"
    l_mc "*Gulp*"
    show event_couch_clausepose 4 with Dissolve(.15)
    pause   
    l_claus "Awe, much better."
    l_claus "You just be my good little Santa and sit there. let your good old wife give you some love."
    show lucas santa_c pose default_t
    l_mc "R. . . really ?"
    show lucas santa_c pose default
    show event_couch_clausepose 5 at center with Dissolve(.15)
    pause 
    l_claus "Of course, you are my husband after all; are you not? {p} And I still haven’t forgotten how your little friend down south reacted to how my ass was smudging your face not too long ago."
    l_claus "And look at him now, he seems pretty happy don’t you think?"
    show lucas santa_c pose default_t
    l_mc "Very much."
    show lucas santa_c pose default
    l_mc "(This really is the best Christmas ever!)"
    show event_couch_clausepose 6 with Dissolve(.15)
    pause
    l_claus "My goodness, he sure is lively isn’t he."
    l_claus "Well, I think I should help out now. We can’t send you off to bed with this thing so swollen."
    l_claus "It might do you damage if we left this unsettled. "
    l_mc "(Thank you Santa for neglecting your hotass wife.)"
    show black with Dissolve(.15)
    hide event_couch_clausepose
    hide lucas santa_c pose
    hide event_couch_nightalt
    jump claus_blowjob_navigation

image claus_blowjob_anim_2:
    "anim_xmas_blowy 1"
    0.09
    "anim_xmas_blowy 2"
    0.09
    "anim_xmas_blowy 3"
    0.09
    "anim_xmas_blowy 4"
    0.09
    "anim_xmas_blowy 5"
    0.09
    "anim_xmas_blowy 6"
    0.09
    "anim_xmas_blowy 7"
    0.09
    "anim_xmas_blowy 8"
    0.09
    "anim_xmas_blowy 9"
    0.09
    repeat

image claus_blowjob_anim_1:
    "anim_xmas_blowy 1"
    0.07
    "anim_xmas_blowy 2"
    0.07
    "anim_xmas_blowy 3"
    0.07
    "anim_xmas_blowy 4"
    0.07
    "anim_xmas_blowy 5"
    0.07
    "anim_xmas_blowy 6"
    0.07
    "anim_xmas_blowy 7"
    0.07
    "anim_xmas_blowy 8"
    0.07
    "anim_xmas_blowy 9"
    0.07
    repeat

label claus_blowjob_navigation:
    scene claus_blowjob_anim_2
    if _return == "claus_bj_1":
        hide claus_blowjob_anim_2
        scene claus_blowjob_anim_1
        l_mc "Crap ! Not so fast! If you keep going a this pace !"
    elif _return == "claus_bj_2":
        hide claus_blowjob_anim_1
        scene claus_blowjob_anim_2
    call screen claus_blowjob_interactive(current=_return)
    jump claus_blowjob_navigation




screen claus_blowjob_interactive(current=""):

    imagebutton:
        action Jump("claus_blowjob_end")
        idle "animbutton_bust"
        mouse "interaction_m"
        xalign 0.99
        yalign 0.94

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("claus_bj_1" if current == "claus_bj_2" else "claus_bj_2")
            idle ("speedx2_btn" if current == "claus_bj_2" else "speedx1_btn")
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94
    else:
        imagebutton:
            action Return("claus_bj_1")
            idle "speedx1_btn"
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94


label claus_blowjob_end:
    show white with dissolve
    show anim_xmas_blowy 10
    pause
    hide black with Dissolve(.15)
    l_mc "Dang, I’m so sorry. I didn’t mean to."
    l_mc "You just wouldn’t stop"
    show anim_xmas_blowy 11 with Dissolve(.15)
    l_claus "*Pfuaah*"
    l_mc "(So much in her mouth)"
    l_mc "(I fucked up)"

    show black with Dissolve(.15)
    pause
    $ renpy.scene()
    show event_couch_nightalt
    show lucas santa_c pose default at lucas_santa_couch_postiion
    show event_couch_clausepose 6 at center
    pause
    hide black with Dissolve(.15)
    l_claus "Don’t sweat it kid. I didn’t stop for a reason."
    l_claus "I wanted you to shoot it inside, it’s been so long since I’ve had the scent of a mans sperm cloud my mouth."
    l_claus "Oh nostalgia."
    show lucas santa_c pose default_t
    l_mc "Wow, I guess that long lifespan of yours has taught you some tricks, hasn’t it?"
    l_mc "But… I want to keep going ! Quick, Lay down."
    show lucas santa_c pose default
    l_claus "Eager one, are you?"
    l_claus "Just how I like it, now be a dear and get up real quick"
    show lucas santa_c pose default_t
    l_mc "Yes Mam!"
    show lucas santa_c pose default
    show black with Dissolve(.15)
    pause
    $ renpy.scene()
    jump claus_sex_navigation

image claus_sex_anim_1:
    "anim_xmas_sex 1"
    0.06
    "anim_xmas_sex 2"
    0.06
    "anim_xmas_sex 3"
    0.06
    "anim_xmas_sex 4"
    0.06
    "anim_xmas_sex 5"
    0.06
    "anim_xmas_sex 6"
    0.06
    "anim_xmas_sex 7"
    0.06
    "anim_xmas_sex 8"
    0.06
    "anim_xmas_sex 9"
    0.06
    repeat

image claus_sex_anim_2:
    "anim_xmas_sex 1"
    0.1
    "anim_xmas_sex 2"
    0.1
    "anim_xmas_sex 3"
    0.1
    "anim_xmas_sex 4"
    0.1
    "anim_xmas_sex 5"
    0.1
    "anim_xmas_sex 6"
    0.1
    "anim_xmas_sex 7"
    0.1
    "anim_xmas_sex 8"
    0.1
    "anim_xmas_sex 9"
    0.1
    repeat

label claus_sex_navigation:

    scene claus_sex_anim_2
    if _return == "claus_sex_1":
        hide claus_sex_anim_2
        scene claus_sex_anim_1
        l_claus "Go faster Lucas! I need it."
    elif _return == "claus_sex_2":
        hide claus_sex_anim_1
        scene claus_sex_anim_2
    call screen claus_sex_interactive(current=_return)

    jump claus_sex_navigation




screen claus_sex_interactive(current=""):

    imagebutton:
        action Jump("claus_sex_end")
        idle "animbutton_bust"
        mouse "interaction_m"
        xalign 0.99
        yalign 0.94

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("claus_sex_1" if current == "claus_sex_2" else "claus_sex_2")
            idle ("speedx2_btn" if current == "claus_sex_2" else "speedx1_btn")
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94
    else:
        imagebutton:
            action Return("claus_sex_1")
            idle "speedx1_btn"
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94

label claus_sex_end:
    show white with dissolve
    show anim_xmas_sex_01_bust 1
    show anim_xmas_sex_whiteout zorder 1
    pause
    hide black with Dissolve(.15)
    l_claus "You sure shot a lot inside me again."
    l_mc "Your body was driving me nuts."
    l_claus "I see that."
    show anim_xmas_sex_01_bust 2 with dissolve
    pause
    l_claus "Pullout out nice and slowly"
    l_mc "*mmm*"
    l_claus "That's it"
    l_claus "My goodness, you weren’t kidding."
    l_claus "I guess you were pretty pent up as well."
    l_claus "Look at all the cum."
    l_claus "You really had spunk in you kid, not bad at all."
    l_mc "Thanks, but it was just because you turned me on so much."
    l_claus "Glad my old body could still turn a man on these days."
    l_mc "Of course, are you kidding me? Your husband is a total idiot for cheating on you."
    l_mc "If I was your husband, I’d be having sex with you every single day."
    l_claus "Wow, some charmer you are. I can tell you’ll be turning a lot of heads in the future."
    l_claus "Now let’s get dressed, it’s time for me to leave."

    show black zorder 2 with Dissolve(.15)
    pause
    $ renpy.scene()
    $ christmas_story += 1

    call set_location ("loc_livingf1") from _call_set_location_38
    pause
    hide black with Dissolve(.15)
    show lucas santa pose default at left with easeinleft
    show claus normal pose1 default at right with easeinright
    pause
    l_mc "You sure you can’t stay longer?"
    show claus normal pose1 default_talk
    l_claus "Sorry but I still have tons of other homes to visit and I’ve already spent a lot of time here."
    show claus normal pose1 default
    l_mc "Can I see you again? I know living in the north pole might be sort of troubling with distance and all."
    show claus normal pose1 default_talk
    l_claus "Maybe if you behave for me, I’ll pay you another visit next year."
    show claus normal pose default_talk
    l_claus "Who knows, I may have divorced that fat Santa by then so we’ll see what happens next Christmas."
    show claus normal pose default
    show lucas santa pose shut
    l_mc "I’d like that. We just had sex but I’m already drooling for your second visit."
    show lucas santa pose assured
    l_mc "I forgot to ask, but I never saw your reindeers. Could I"
    show claus normal pose default_talk
    l_claus "Maybe next year. I’m pretty off schedule already and the base back home might start to suspect something."
    l_claus "Not that the fat basterd at home would care anyways."
    show lucas santa pose default
    l_claus "I better be off. Look out for more noise in the chimney next year and maybe someone will land on your face again"
    show claus normal pose1 default
    show lucas santa pose sure
    l_mc "Please do."
    show claus normal pose1 default_talk
    l_claus "Bye kiddo."
    show claus normal pose1 default
    show lucas santa pose default
    l_mc "See yeah."
    hide claus normal pose1 with moveoutright
    show lucas santa pose default at center with ease
    show lucas santa pose mkay
    l_mc "And she's gone."
    l_mc "I can't wait to see her again already, gonna have wet dreams for sure now until then."
    show lucas santa pose suprised
    l_mc "???"
    l_mc "She forgot something here. She must have overlooked this when she feel through the chimney."
    show event_xmas_presentbox 1 zorder 2 with Dissolve(0.2)
    pause
    l_mc "She must’ve forgot this right before we both got distracted. I guess, I can hold onto it for now since she did forget to give me my Christmas present before she left."
    l_mc "And its not like I can mail it to her in the north pole."
    l_mc "Let me open it now than."
    show event_xmas_presentbox 2 with Dissolve(0.2)
    l_mc "What is this? Some outfit? Another Santa costume?"
    l_mc "Wait whaaaaaaat? "
    l_mc "Is this supposed to be some sexy lingerie? What kind of people was she going to deliver presents to?"
    l_mc "I’ll just hold onto it for now. Don’t think I can actually give this to anybody at the moment. Maybe sometime in the future."
    l_mc "I better hide it from [sadie_refer_input] though."
    l_mc "[sadie_refer_input]. . ."
    l_mc "Wonder what she’d look lik… wearing… thi."
    l_mc "No no. what am I thinking. "
    l_mc "I’ll just stop before My mind starts wandering off like crazy."
    l_mc "I should just go to sleep now while my mind is still sane."
    show black with Dissolve(0.15)
    hide claus normal pose1
    pause
    hide event_xmas_presentbox with Dissolve(0.2)
    centered "{color=ffff}{size=80}{font=gui/fonts/acumin_regular.otf}{b} You reached the end of this Christmas Content {p} \n Free roam will now be enabled {p}\n {color=#f00} Merry Christmas ! {/color} {/b}{/font}{/size}{/color}"




    $ sadiecouch_talking = False
    $ exit_btn = True
    $ christmas_story += 1
    jump goto_livingf1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

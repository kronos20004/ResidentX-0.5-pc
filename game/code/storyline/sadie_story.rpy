

label sadie_bathroom_1:


    hide screen main_hud_icon
    scene hallwayf2 bathroom peek 1
    show lucas normal pose4 puzzle_talk at left with moveinleft
    l_mc "[sadie_refer_input]?"
    show lucas normal pose4 puzzle_talk with Dissolve(0.1)
    l_mc "Hello ?"
    show lucas normal pose4 puzzle with Dissolve(0.1)
    l_sadie "Oh!"
    l_sadie "Sorry, I was in the middle of doing something."
    l_sadie "Did you get it honey?"
    show lucas normal pose4 puzzle_talk with Dissolve(0.1)
    l_mc "Yeah, found it. How do you want me to…?"

    show lucas normal pose4 puzzle with Dissolve(0.1)
    l_sadie "Oh, just slide it in through the door. Please and thank you."
    l_sadie "I left it a little open for you."
    hide lucas normal pose4 default
    show char_lucas_doorpeek_outfit_1 with dissolve
    l_mc "Ok, guess I'll be coming in just a little. . ."
    pause
    hide char_lucas_doorpeek_outfit_1
    show char_lucas_doorpeek_outfit_2 with dissolve
    l_mc "Wait. . ."
    pause
    hide char_lucas_doorpeek_outfit_2
    scene hallwayf2 bathroom peek 2 with dissolve
    pause







    scene event_bahtroomdoor_sadie 1 with dissolve
    window hide
    pause

    l_mc "Oohhhh shiiii…"

    pause
    l_sadie "What was that honey ?"
    scene event_bahtroomdoor_sadie 2
    l_sadie "Oh, you left it on the floor. Thank you dear."



    scene event_bahtroomdoor_sadie 3 with dissolve
    pause
    scene hallwayf2 bathroom peek 2 with dissolve



    show lucas normal pose4 happy with Dissolve(0.1)
    l_sadie "And don’t forget, I left you some food downstairs in the kitchen. I’ll see you in a few minutes after I finish up here."
    show lucas normal default_talk
    l_mc "Okay, thanks."
    show lucas normal puzzle
    l_mc "(What the hell [sadie_refer_input], that view was… something else.)"
    hide lucas normal with moveoutleft
    $ inv.remove(item_sadiebusinessoutfit)
    $ sadie_story += 1
    jump goto_hallwayf2
    return

transform lucas_kitchen_pos:
    xpos 0.505
    ypos 264

transform lucas_kitchen_pos1:
    xpos 0.513
    ypos 0.1

label sadie_chapter_1_kitchen:
    window hide
    hide screen main_hud_icon
    scene cutscene_bg_breakfest with dissolve
    show sadie business pose default at left with moveinleft:
        xzoom -1
    show lucas kitchennew pose break1 at lucas_kitchen_pos with dissolve
    pause
    show lucas kitchennew pose2 break3 at lucas_kitchen_pos with dissolve
    pause
    show lucas kitchennew pose break4 at lucas_kitchen_pos with dissolve
    pause
    show sadie business pose default_talk
    l_sadie "Hey lucas."
    show lucas kitchennew pose break5 at lucas_kitchen_pos with dissolve
    show sadie business pose default
    l_mc "(crunchy)"
    show sadie business pose default_talk
    l_sadie "How do you like the food ?"
    pause
    show sadie business pose default
    show lucas kitchennew pose break1 at lucas_kitchen_pos with dissolve
    pause 
    show lucas kitchennew pose break5 at lucas_kitchen_pos with dissolve
    pause 0.1
    show lucas kitchennew pose break6 at lucas_kitchen_pos with dissolve
    pause 0.1
    l_mc "*Crunch crunch* ich good, janks."
    show sadie business sad_talk
    l_sadie "Honey, try not to talk with your mouth full of food."
    show sadie business sad
    show lucas kitchennew pose break5 at lucas_kitchen_pos with dissolve
    l_mc "(But you do the same)"
    show sadie business default_talk
    l_sadie "I better go to work. I'll be back later tonight."
    show sadie business default
    show lucas kitchennew pose break7 with dissolve
    l_mc "Ok [sadie_refer_input], have a good day at work."
    show lucas kitchennew pose break5 with dissolve



























    pause
    hide sadie with moveoutleft
    pause



    $ sadie_story += 1
    hide back_display1

    show screen journal_updated_notify

    jump goto_lobbyf1
    return

image couch_sleep_1 = "images/cutscene/sadie tv/poses/char_lucascouch2_alt.png"

image couch_sleep_2 = "images/cutscene/sadie tv/poses/char_lucascouch3_alt.png"

transform sadie_businees_night_sit:
    xpos 350
    ypos 300

transform sadie_business_night_pos:
    ypos 7
    xpos 770

transform sadie_lucas_laydowncouch:
    xalign 0.35
    yalign 1.0


transform lucas_penis_movienight1:
    xalign 0.55
    yalign 1.05

label sadie_tv_story1:

    window hide

    hide screen main_hud_icon
    scene movienight_bg_day
    show lucas tv pose default with dissolve
    $ renpy.pause(1, hard=True)
    show lucas tv pose default_t
    l_mc "Hmm. . ."

    show lucas tv pose mkay
    l_mc ". . ."
    show lucas tv pose happy_t
    l_mc "Ahh, there we go"
    l_mc "Spiderman !"
    scene back_display1 with dissolve
    show transition_card 1 with fade
    show custom_text_card "Time Passes by . . ." with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve

    show movienight_bg_night

    show couch_sleep_2
    $ renpy.pause(1, hard=True)
    l_mc "ZZZzzzzzZZ"
    play sound "music/door_close.mp3"



    show black with fade
    l_unkown "Wake up tiger"
    pause
    hide couch_sleep_2
    hide black with fade
    show movienight_bg_night

    show movienight1_4 at sadie_business_night_pos
    show lucas tv_alt pose happy
    pause
    show lucas tv_alt pose default_t
    l_mc "What?"
    hide movienight1_4
    show lucas tv_alt pose default
    show movienight1_5 at sadie_business_night_pos
    l_sadie "It’s just me darling, I’m back from work."

    hide movienight1_5
    show movienight1_4 at sadie_business_night_pos
    show lucas tv_alt pose default
    pause


    show lucas tv_alt pose default_t
    l_mc "Oh, glad you’re back. You came home pretty quick today."

    show lucas tv_alt pose default

    show movienight1_7 at sadie_business_night_pos
    l_sadie "Not at all Lucas, It’s pretty late already. Seems like you fell asleep watching TV."

    show lucas tv_alt pose default_t
    hide movienight1_7 at sadie_business_night_pos
    show movienight1_6 at sadie_business_night_pos
    l_mc "Wow, guess the time flew by without me knowing."
    show lucas tv_alt pose default
    hide movienight1_6 at sadie_business_night_pos
    show movienight1_7 at sadie_business_night_pos
    l_sadie "While you're there already, lets watch a movie yeah?"
    scene movienight1_8 with fade



    l_mc "Um sure… but you don’t want to get changed first?"
    l_sadie "Too tired to go upstairs now. Unless you carry me up the staircase and change me?"
    l_mc "No thank you."
    l_sadie "Thought so."
    l_sadie "Put on one of your movies and scooch over. I'm pooped."
    hide movienight1_6 at sadie_business_night_pos
    scene movienight_bg_night with fade
    show sadie_lucas night_tv_alt mkay awe at sadie_businees_night_sit with dissolve
    pause
    show sadie_lucas night_tv_alt glad_talk awe
    l_mc "Mkay, the movie is starting."
    show sadie_lucas night_tv_alt glad default_t
    show sadie_lucas night_tv_alt glad happy

    show transition_card 1 with fade
    show custom_text_card "20 Minutes Later. ." with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve


    show sadie_lucas night_tv_alt default awe with dissolve
    pause
    show sadie_lucas night_tv_alt default awe_t with dissolve
    l_sadie "The movie is actually pretty good."
    show sadie_lucas night_tv_alt mkay hmm_t with dissolve
    l_sadie "But I wish bailey was here to watch this too."
    show sadie_lucas night_tv_alt blank awe
    pause
    show sadie_lucas night_tv_alt angry_t awe
    l_mc "You saying I’m not good enough company for you?"
    show sadie_lucas night_tv_alt mkay assured
    pause
    show sadie_lucas night_tv_alt mkay awe_t
    l_sadie "Of-course that’s not what I mean silly. It’s just that we haven’t seen her in a while since she’s been off to college."
    show sadie_lucas night_tv_alt mkay_t awe
    l_mc "Right . . ."
    show sadie_lucas night_tv_alt grumpyz smirk_t
    l_sadie "Wait a minute… are you getting jealous because I suggested I wanted my daughter here as well?"
    show sadie_lucas night_tv_alt grumpy_talk smirk
    l_mc "What? No way, I could care less."
    show sadie_lucas night_tv_alt mkay smirk_t
    l_sadie "It’s okay honey, I understand. Don’t worry about it, you're all I need right now, My big boooy!"
    show sadie_lucas night_tv_alt mkay awe_t
    l_sadie "Mkay ?"
    show sadie_lucas night_tv_alt sure_talk awe
    l_mc "Sure."
    stop music
    show transition_card 1 with fade
    hide sadie_lucas night_tv_alt
    show custom_text_card "1 Hour Later. . ." with dissolve
    pause
    hide transition_card
    show movienight1_23 with dissolve
    hide custom_text_card with dissolve

    pause
    l_mc "(Looks like she fell asleep, guess she really was tired from work after-all.)"
    l_mc "(But damn she’s heavy, has she been eating more? Probably shouldn’t tell her that.)"
    l_mc "(Well, I don’t want to wake her up, she’s been working pretty hard.)"
    l_mc "She’s like a cute little cat you shouldn’t wake up. A very big and heavy cat."

    l_mc "(I suppose, this is the rest of my night. Not a very bad way to end it off.)"
    l_mc "(sleep tight.)"

    pause
    hide movienight1_23
    show movienight1_24
    pause



    show transition_card 1 zorder 1 with fade
    show movienight_bg_day
    hide movienight_bg_night
    hide movienight1_24
    show custom_text_card "Next Morning . . ." zorder 1 with dissolve
    pause
    hide transition_card
    show movienight1_25 at sadie_lucas_laydowncouch with dissolve
    hide custom_text_card with dissolve

    pause
    l_mc "Errr"
    l_mc "(What the . . . I feel squished. . .)"
    l_mc "(What’s this fluff I’m grabbing here?)"
    l_mc "(Shit.)"
    l_mc "(Crap crap. I’ve read enough hentai to know where this is going. I have to nudge my ass out of here somehow.)"
    hide movienight1_25
    show movienight1_26 at sadie_lucas_laydowncouch
    l_mc "(Oh no, is my penis getting hard too?)"
    l_mc "(It’s just morning wood. A normal sign that I’m a young and healthy man, is all.)"
    l_mc "(But this still doesn’t help my predicament.)"
    hide movienight1_26
    show movienight1_27 at sadie_lucas_laydowncouch
    pause
    hide movienight1_27
    show movienight1_28 at sadie_lucas_laydowncouch
    l_mc "(I can feel my dick bulging out now.)"
    l_mc "(Of all the times, now isn’t the time you dickhead.) "
    l_mc "(Go back down dammit!)"
    l_sadie "Hmmm…?"
    hide movienight1_25
    hide movienight1_26
    hide movienight1_27
    hide movienight1_28

    show movienight1_29 at sadie_lucas_laydowncouch with dissolve
    l_mc "(Dammit, I think she’s waking up.)"
    l_mc "(Ok ok. Just act cool and pretend to still be sleeping.)"
    l_sadie "Mmm…"
    l_sadie "Lucas?"
    hide movienight1_29
    scene movienight_pov1
    show movienight1 31

    show movienight1 30
    l_mc "(I’m just sleeping. I’m just sleeping.)"

    show movienight1 31
    l_sadie "Lucas ?"

    show movienight1 30
    l_mc "Oh."
    l_mc "Yeah *ahem* what’s up? Oh, were you still sleeping on me?"

    show movienight1 31
    l_sadie "I’m sorry, I guess I knocked out pretty easy last night."

    show movienight1 30

    l_mc "No no, don’t worry about it. I barely even noticed."
    l_mc "You were as light as a blanket anyways."

    show movienight1 31
    l_sadie "Oh really? "
    show movienight1 30
    l_mc "Um… sure."
    show movienight1 31
    l_sadie "Well, you sure are gaining points with the ladies. I do put in a lot of effort to keep my figure."
    show movienight1_30_penis at lucas_penis_movienight1 with dissolve
    pause
    l_mc "(More importantly, she’s sitting right on my penis.)"
    l_mc "(My body should not be feeling this way.)"
    l_mc "(My penis keeps rising.)"
    hide movienight1_31
    hide movienight1_30_penis
    show movienight_sweatingbullets zorder 1 with dissolve
    l_mc "(Shit!!! what do I say now?! Is my existence over?)"
    l_sadie "What is this?"
    l_mc "(Damn, not good. The rubbing friction is making me feel weird.)"
    l_mc "Wait [sadie_refer_input], It’s just the remote control somewhere under the blanket. I’ll get it out after you get off."
    l_sadie "Oh, that’s right. I better get off now. Sorry to bother you like that."
    l_sadie "Don’t be afraid to knock me off next time I fall asleep like that."
    l_mc "No worry."














    $ renpy.scene()
    show black
    pause
    hide black

    $ exit_btn = False
    call set_location ("loc_livingf1") from _call_set_location_39
    show sadie normal pose14 default at right with moveinright
    show lucas normal pose3 default at left with moveinleft
    pause
    show lucas normal pose3 puzzle_d
    l_mc "(The airhead didn’t even notice. That innocence is going to get her in trouble one day.)"
    show lucas normal pose3 puzzle
    show sadie normal assured_talk
    l_sadie "Oh jeez… I’m pretty sweaty. I should’ve changed before watching the movie."
    show sadie normal smirk_talk
    l_sadie "I really need to go take a shower."
    show sadie normal smirk
    show lucas normal pose3 alert_talk
    l_mc "Ok, see ya later."

    hide sadie normal at right with moveoutright
    show lucas normal pose3 alert
    l_mc "(Well, that just happened.)"
    pause
    hide lucas normal pose3 with moveoutleft
    $ exit_btn = True
























    $ sadie_info_1 = True

    play music "music/music4.mp3"
    pause
    $ sadie_story += 1
    show screen journal_updated_notify with dissolve
    jump goto_livingf1
    return


label lucas_sadie_sleep_event1:

    scene bg_bedlucas_alt
    hide screen main_hud_icon
    show bg_bedlucas_doorclosed_alt
    show lucas sleep_night sleep1
    l_mc "errr"
    show lucas sleep_night sleep2
    ". . . ."
    scene black with dissolve
    scene bg_bedlucas
    show bg_bedlucas_dooropen
    show lucas sleep_day pose sleep1
    l_mc "ZzzZZzzZZZZzzz. . ."

    play music "music/music4.mp3"
    show bg_bedlucas_dooropen_sadie with dissolve
    l_sadie "Jeez"
    l_sadie "That boy"
    l_sadie "Is he going to be sleeping in so late into the day now ?"
    l_sadie "I'll have to wake you up than won't I ?"
    l_mc "ZzzZZzzZZZZzzz"
    scene bg dreamshower
    show pov_blur_1 zorder 1
    show dream sadie1 with dissolve
    l_mc ". ."
    hide pov_blur_1
    show pov_blur_2 zorder 1
    l_mc "Wh.. what ?"
    l_mc "so. . . perfect. . can I . ."
    hide pov_blur_2 with dissolve
    show dream sadie2 with dissolve
    pause
    show dream sadie3
    l_sadie "hey there little pervert"
    l_mc "He. . hey"
    l_sadie "What's the matter ?"
    l_sadie "something here catch your eyes ?"
    l_sadie "if you're just going to stand there drooling on the floor"
    l_sadie "Why don't you come a little closer"
    l_mc "but are you sure i can . . "
    l_sadie "come on big boy"
    l_sadie "How long have I known you"
    l_sadie "You shouldn't be shy around me, isn't it natural for us to take showers together ?"
    l_sadie "We used to do it long time ago"
    l_mc "Well "
    l_mc "Maybe you do make a point"
    l_mc "It's just bonding right ?"
    show dream_hand with dissolve
    show dream sadie2
    pause
    show dream sadie3
    l_sadie "but before you come closer, you mind waking up you sleepy head ?"
    l_mc "hu?!?"
    l_sadie "Come on Lucas, wake up"
    hide dream sadie1
    hide dream sadie2
    hide dream sadie3
    show dream_tit_bathroom
    pause
    scene black with dissolve
    l_mc "wait . . . but"
    pause
    scene grey
    show pov_blur_1 zorder 1
    pause
    show sadie pov1 zorder 0 with dissolve
    pause
    l_sadie "Wakey wakey, eggs and bakey"
    hide pov_blur_1
    show pov_blur_2 zorder 1
    pause
    show sadie pov2 with dissolve
    l_sadie "oh, you're finally up"
    l_sadie "Do you know what time it is already ?"
    l_mc "huu. . ."
    l_sadie "you can't be sleeping all day"
    show sadie pov3 with dissolve
    l_mc "wow. . "
    show sadie pov4 with dissolve
    l_sadie "Wow what ?"
    l_sadie "You still half-asleep there?"
    l_sadie "Come on hon. stop daydreaming"
    l_sadie "You're still half-asleep"
    show sadie pov3
    l_sadie "(I wonder what he was just dreaming about)"
    l_sadie "(He still hasn't snapped out of it completely)"
    hide pov_blur_2
    l_mc "Huh ??"

    scene black with dissolve
    scene bg_bedlucas
    show bg_bedlucas_doorclosed
    show lucas sleep_day pose ohshit

    show sadie lucas_bed pose default
    pause
    show lucas sleep_day pose ohshit_t
    l_mc "[sadie_refer_input] ?"
    show sadie lucas_bed pose default_t
    show lucas sleep_day pose ohshit
    l_sadie "The one and only"


    pause

    show sadie lucas_bed pose awe
    show lucas sleep_day ohshit2
    l_mc "(HOLY SH#@&T!!)"
    pause
    show lucas sleep_day pose2 wake_t
    l_mc "Wh . . what are you doing here ?"

    pause
    show sadie lucas_bed pose2 awe_t

    show lucas sleep_day pose2 sleep
    l_sadie "waking you up. I can’t have you sleeping all day."
    l_sadie "I don't want you to start building up a bad habit of sleeping in . ."
    show sadie lucas_bed pose2 awe
    pause
    show lucas sleep_day pose3 sleep
    show sadie lucas_bed pose3 default_d
    l_sadie "(Wha . . .)"
    pause
    show sadie lucas_bed pose4
    l_sadie "Oh my"
    pause
    show lucas sleep_day ohshit2
    l_mc "(Crap.. I think I just better play it off and act dumb)"
    show lucas sleep_day wake_t
    show sadie lucas_bed pose4 default
    l_mc "I"
    l_mc "I don't know what this is [sadie_refer_input]"
    l_mc "It just started happening to me"
    l_mc "I swear"
    pause
    show lucas sleep_day blush sleep
    show sadie lucas_bed pose4 awe_t
    l_sadie "oh that’s ok sweety"
    l_sadie "I’m pretty sure this is just normal for boys your age"
    l_sadie "Don't be embarrased about it"
    show sadie lucas_bed pose4 awe_down
    show lucas sleep_day blush wake_t
    l_mc "Really ?"
    l_mc "You don't think this is weird ?"
    show sadie lucas_bed pose4 awe_t
    show lucas sleep_day blush sleep
    l_sadie "How could I"
    l_sadie "I heard that these kind of things happen to people before "
    show sadie lucas_bed pose4 awe_down
    show lucas sleep_day blush ohshit
    l_mc "(Wait. . . does she not know about morning wood ? how dumb can she really. . uh)"
    l_mc "(I know her and [leo_refer_input] weren't the closest couple but still. How rarely did they even sleep in the same bed?)"
    l_mc "(How does she even have a daughter older than me ?)"
    show sadie lucas_bed pose4 default_t
    show lucas sleep_day pose2 none sleep
    l_sadie "I don't really know about this boy stuff"
    l_sadie "If you are really worried, maybe we can learn about your situation together on the internet"
    l_sadie "So you're not so concerned about it"

    show sadie lucas_bed pose4 default_d
    show lucas sleep_day pose wake_t
    l_mc "No no no"
    l_mc "I think I'll be fine"
    show sadie lucas_bed pose4 default_t
    show lucas sleep_day pose sleep2
    l_sadie "uhm.. ok well. Let me know anytime"
    show sadie lucas_bed pose4 default
    show lucas sleep_day pose2 ohshit
    l_mc "(hu? What would she do about it anyway? She doesn't even know much about this to begin with)"
    show lucas sleep_day pose2 wake_t
    l_mc "Yeah I will"
    l_mc "I think i'll just get up now"
    pause
    show sadie lucas_bed pose2 default
    show lucas sleep_day pose2 sleep
    l_sadie "Ok, I'll just go way now . .bye"
    hide sadie lucas_bed pose3 default with dissolve
    show lucas sleep_day pose3 sleep
    pause
    show lucas sleep_day pose3 ohshit2
    pause
    hide lucas sleep_day pose3 ohshit2
    show char_lucas_bed_off at left with dissolve
    l_mc "What the {b}hell{/b} was that ?"
    l_mc "That was too close for comfort"
    l_mc "And what was that crazy dream ? And . . my boner ?"
    l_mc "It's the second time now that I have a boner involving her"
    l_mc "But there's no way its because of her"
    l_mc ".. {b}no way{/b}"
    l_mc "Just a coincidence of morning wood in both situation"
    l_mc "So far"
    l_mc "Dreams are just fragments of my imagination, nothing real"
    l_mc "Just because it happened in my dreams doesn't mean it can happen in reality"

    l_mc "She just caught me at a bad timing is all"
    l_mc "Don't even want to think about it anymore"
    l_mc "Let's just get the day started already"
    pause

    $ now.advance()
    $ sadie_story += 1




    call set_location ("loc_lucasroom") from _call_set_location_10

    play music "music/music4.mp3"




    show lucas normal pose34 default with dissolve
    $ renpy.pause ()
    hide lucas normal pose34 default with dissolve
    show lucas normal pose35 default with dissolve
    l_mc "Alright, lets get started"

    show screen journal_updated_notify with dissolve
    jump goto_lucasroom
    return


image sadie_bedroomdressup = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup_Bg.jpg"
image sadie_bedroomdressup1 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup1.jpg"
image sadie_bedroomdressup2 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup2.jpg"
image sadie_bedroomdressup3 = "images/cutscene/sadie_bedroom_scene/Sadie_DressUp3 alt.jpg"
image sadie_bedroomdressup4 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup4.jpg"
image sadie_bedroomdressup5 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup5.jpg"
image sadie_bedroomdressup6 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup6.jpg"
image sadie_bedroomdressup7 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup7.jpg"
image sadie_bedroomdressup8 = "images/cutscene/sadie_bedroom_scene/Sadie_Dressup8.jpg"

label sadie_event2:
    hide screen main_hud_icon

    scene sadie_bedroomdressup1 with Dissolve(0.01)
    l_mc "(Am I really doing this right now)"
    l_mc "(This is really bad. My eyes won’t be able to look away at this point)"
    scene sadie_bedroomdressup2 with dissolve
    l_mc "(Damn, how am I supposed to justify this to myself now?)"
    l_mc "(It’s not normal for someone to be spying on their [sadie_relationship_input] while she’s undressing)"
    l_mc "(Stop before she completely takes that small ass shirt off)"
    l_mc "(No, it's really going to come off)"
    scene sadie_bedroomdressup3 with dissolve
    l_mc "(Dear lawd have mercy!)"
    l_mc "(My goodness.) "
    scene sadie_bedroomdressup4 with dissolve
    l_mc "God DAMN!"
    l_sadie "Huh? You say something dear ?"
    l_sadie "Did you find anything yet?"
    l_mc "Ye… yeah, I DID! Almost done changing here."
    pause
    scene sadie_bedroomdressup5 with dissolve
    l_mc "(My eyes won't diverge. They don't even blink. What's going on)"
    l_mc "(My primal instincts are taking over after seeing my own [sadie_relationship_input])"
    l_mc "(This isn’t right, this isn’t right! I should be stopping myself.)"
    pause
    scene sadie_bedroomdressup6 with dissolve
    l_sadie "You say something again?"
    l_mc "No no, I'm almost done changing here"
    l_sadie "Ok, I’m not done here so just wait in there a bit longer please"
    l_sadie "you have enough space in there to breathe right?"
    l_mc "Yeah, not a problem. Just take your time"
    l_mc "(Wait a second. You should be rushing to get dressed quicker.)"
    l_mc "(I’m feeling my nether regions getting tighter.)"
    pause
    scene sadie_bedroomdressup7 with dissolve
    l_mc "(It’s too late. I’m completely hard now.)"
    l_mc "(This isn’t a case of normal morning wood anymore.)"
    l_mc "(This is a case of being a MAN!)"
    l_mc "(I shouldn’t be ok with this though.)"
    pause
    scene sadie_bedroomdressup8 with dissolve
    l_sadie "You done getting dressed yet?"
    l_mc "Just about done here. I take it your still not done"
    l_sadie "Yeah, sorry. I’m pretty slow. But you wouldn’t be peaking, right?"

    l_mc "What?! Of course not. You're my [sadie_relationship_input]. What kind of degenerate do you take me for?"

    l_sadie "Just kidding."
    l_sadie "But I wouldn’t put it past you, you're still a growing boy."
    l_mc "What are you on about woman. Just get it over with already, it’s stuffy in here and hard to breath."
    $ sadie_story += 1
    pause
    jump goto_sadiecloset
    return

    pause

transform lucas_sit_yoga_position:
    xpos .2
    ypos .38

transform sadie_sit_yoga_position:
    xpos .52
    ypos .38

label yoga_sadie_event1:
    hide screen main_hud_icon



    show lucas workoutpose pose3 default at left with moveinleft
    show sadie workout pose default at right with moveinright
    $ sadie_yogabtn = False
    pause
    show lucas workoutpose pose3 default_talk
    l_mc "Alright let’s start. you ready?"
    show lucas workoutpose pose3 default
    show sadie workout pose assured_talk
    l_sadie "Not really but let’s just do it already, before I change my mind."


    l_mc "Stop complaining Lucas, It’s only yoga."
    show lucas workoutpose pose3 default
    pause
    jump remake_yogascene
    return

label remake_yogascene:
    show black with dissolve
    show event_yoga_sadie 1
    hide black with dissolve
    pause
    l_mc "As one could imagine, this pretty much went as expected. Not a lot of focus on the task at hand from my part"
    l_mc "I probably should’ve resisted more to be honest."
    l_mc "Now I’ll probably be thinking about this moment all day, maybe all week."
    show event_yoga_sadie 2 with dissolve
    pause
    l_mc "Why is yoga with a partner so damn sexual?"
    l_mc "Probably something only a couple should be doing."
    l_mc "I swear, my [sadie_refer_input] lack of awareness around the house, makes things more difficult for me."
    l_mc "Why can’t she just be more normal."
    show event_yoga_sadie 3 with dissolve
    pause
    l_mc "Something was rising and it wasn’t these yoga poses"
    l_mc "I knew I should’ve fapped before coming here."
    l_mc "I could only hope that any of the rubbing friction wouldn’t make me explode."
    show event_yoga_sadie 4 with dissolve
    pause
    l_mc "Every second felt like a minute and every minute like an hour."
    l_mc "I tried to think of anything to keep my mind off what was going on."
    l_mc "I came so close to busting so many times, I was literally being edged by my own [sadie_refer_input] without her even knowing."
    l_mc "It was only a miracle that we finished right before I finished."
    show black with fade
    hide event_yoga_sadie
    pause
    show lucas workoutpose pose7 default at left with Dissolve(.15)
    show sadie workout pose default at right with Dissolve(.15)
    hide black with dissolve

    pause
    show sadie workout pose2 default_talk
    l_sadie "See honey, that wasn’t so bad now, was it? Pretty easy right?"
    show sadie workout pose default
    show lucas workoutpose pose7 default_talk
    l_mc "Maybe for you [sadie_refer_input]. but I was pretty hard… I mean it was pretty hard!"
    show sadie workout pose assured_talk
    show lucas workoutpose pose7 default
    l_sadie "You feeling well? I didn’t push you too hard, did I?"
    show sadie workout pose assured
    show lucas workoutpose pose7 sure_talk
    l_mc "What? No, not at all. I just wasn’t very flexible."
    show lucas workoutpose pose7 sure_talk
    l_mc "Anyways, I gotta go now."
    show sadie workout pose default_talk
    show lucas workoutpose pose7 sure
    l_sadie "So soon? Why are you in such a rush. You looked panicked."
    show sadie workout pose default
    show lucas workoutpose pose7 default_talk
    l_mc "Nothing to worry about, just need to use the bathroom. I’m about to cu… I mean pee my pants. Gotta rush!"
    l_mc "See ya!"
    hide lucas workoutpose pose3 with moveoutleft
    pause
    $ yoga_sadie_ended = True
    show sadie workout pose1 assured
    l_sadie "(Well, that was weird. He looked a little red.)"
    l_sadie "(I just never know with that boy. But I’m glad he’s doing more things with me.)"
    show sadie workout pose default
    l_sadie "(I like the connecting.)"
    l_sadie "(Maybe I’ll go with some easier poses next time.)"
    $ lucas_scope = True
    jump goto_lucasroom
    return















































    pause

label sadie_yoga_grind_control:
    $ loc = "sadie_yoga_grind_control"
    hide screen main_hud_icon
    scene anim_yoga01_bg

    if yoga_grind1 == True:
        show yoga_sadie_grind1
    if yoga_grind2 == True:
        show yoga_sadie_grind1
    if yoga_grind3 == True:
        show yoga_sadie_grind2
    if yoga_grind4 == True:
        show yoga_sadie_grind3

    call screen yoga_grind_control_screen



    $ result = _return

    if result == "yoga_grind_next_inter":
        $ yoga_grind1 = False
        $ yoga_grind2 = True
        l_sadie "That's it honey, just hold me tight"
        l_sadie "Nice and firm"
        l_mc "(These unintentional sexual innuendos really need to stop)"
        l_sadie "I can feel my legs burning up a little"
        l_mc "I'm feeling a little hot as well"
        l_mc "Maybe we should stop here"
        l_sadie "Oh come on, just a little more and we're almost done"
        l_mc "(Yeah, that's what I'm afraid of, I can't hold on much longer!)"


    if result == "yoga_grind_fast_inter":
        $ yoga_grind2 = False
        $ yoga_grind3 = True

    if result == "yoga_grind_final_inter":
        $ yoga_grind3 = False
        $ yoga_grind4 = True
        l_mc "(Oh now , I'm at my limit. I have to stop her or I really will cum on her)"
        l_mc "Wait [sadie_refer_input] I'm about to have a leg cramp!!!"
        l_sadie "What ?!?"

    if result == "yoga_grind_end_inter":
        hide yoga_sadie_grind3
        $ yoga_grind4 = False
        $ yoga_grindend = True
        show yoga_sadie_endgrind
        pause
        scene nutting face meme with dissolve
        l_mc "(WOWwwwww..... That...... was amazing ... I can'..)"
        l_mc "(NO NO, get yourself together here. YOU JUST CAME right beneath her....)"
        pause
        scene anim_yoga01_bg with dissolve
        show anim_yoga01_dialogue_01
        pause
        show anim_yoga01_dialogue_02
        l_mc "oh man"
        show anim_yoga01_dialogue_03
        l_sadie "are you alright baby?"
        l_sadie "I’m so sorry, let me get off"
        show anim_yoga01_dialogue_02
        l_mc "no no! just stay here for a bit. My leg is still sensitive, so it will hurt more if you move right now"
        l_mc "(Damn, that really just happened with my [sadie_refer_input]. I have to come up with something so she won’t notice my mess once I get her off me)"
        show anim_yoga01_dialogue_03
        l_sadie "Does anything else hurt beside your leg?"
        show anim_yoga01_dialogue_02
        l_mc "Um yeah, I think I felt my abs and groin cramp up as well"
        l_mc "(That's it!)"
        l_mc "I think I'm good now, you can get off"
        hide anim_yoga01_dialogue_02
        $ yoga_sadie_ended = True
        jump goto_loc_yogaroom
        return


    $ renpy.jump(loc)

screen yoga_grind_control_screen():

    if yoga_grind1 == True:
        imagebutton:
            idle "animbutton_next"
            xpos .1
            ypos .85
            action Return("yoga_grind_next_inter")

    if yoga_grind2 == True:
        imagebutton:
            idle "animbutton_speedup"
            xpos .1
            ypos .85
            action Return("yoga_grind_fast_inter")

    if yoga_grind3 == True:
        imagebutton:
            idle "animbutton_next"
            xpos .1
            ypos .85
            action Return("yoga_grind_final_inter")

    if yoga_grind4 == True:
        imagebutton:
            idle "animbutton_bust"
            xpos .1
            ypos .65
            action Return("yoga_grind_end_inter")


label sadie_video_anim1:



    hide screen lucas_main_folder
    $ yoga_grind1 = True
    scene black
    jump sadie_yoga_grind_control1
    return

label sadie_yoga_grind_control1:
    $ loc = "sadie_yoga_grind_control1"
    hide screen main_hud_icon
    scene anim_yoga01_bg

    if yoga_grind1 == True:
        show yoga_sadie_grind1
    if yoga_grind2 == True:
        show yoga_sadie_grind1
    if yoga_grind3 == True:
        show yoga_sadie_grind2
    if yoga_grind4 == True:
        show yoga_sadie_grind3

    call screen yoga_grind_control_screen1



    $ result = _return

    if result == "yoga_grind_next_inter1":
        $ yoga_grind1 = False
        $ yoga_grind2 = True
        l_sadie "That's it honey, just hold me tight"
        l_sadie "Nice and firm"
        l_mc "(These unintentional sexual innuendos really need to stop)"
        l_sadie "I can feel my legs burning up a little"
        l_mc "I'm feeling a little hot as well"
        l_mc "Maybe we should stop here"
        l_sadie "Oh come on, just a little more and we're almost done"
        l_mc "(Yeah, that's what I'm afraid of, I can't hold on much longer!)"


    if result == "yoga_grind_fast_inter1":
        $ yoga_grind2 = False
        $ yoga_grind3 = True

    if result == "yoga_grind_final_inter1":
        $ yoga_grind3 = False
        $ yoga_grind4 = True
        l_mc "(Oh now , I'm at my limit. I have to stop her or I really will cum on her)"
        l_mc "Wait [sadie_refer_input] I'm about to have a leg cramp!!!"
        l_sadie "What ?!?"

    if result == "yoga_grind_end_inter1":
        hide yoga_sadie_grind3
        $ yoga_grind4 = False
        $ yoga_grindend = True
        show yoga_sadie_endgrind
        pause
        scene nutting face meme with dissolve
        l_mc "(WOWwwwww..... That...... was amazing ... I can'..)"
        l_mc "(NO NO, get yourself together here. YOU JUST CAME right beneath her....)"
        pause
        scene anim_yoga01_bg with dissolve
        show anim_yoga01_dialogue_01
        pause
        show anim_yoga01_dialogue_02
        l_mc "oh man"
        show anim_yoga01_dialogue_03
        l_sadie "are you alright baby?"
        l_sadie "I’m so sorry, let me get off"
        show anim_yoga01_dialogue_02
        l_mc "no no! just stay here for a bit. My leg is still sensitive, so it will hurt more if you move right now"
        l_mc "(Damn, that really just happened with my [sadie_refer_input]. I have to come up with something so she won’t notice my mess once I get her off me)"
        show anim_yoga01_dialogue_03
        l_sadie "Does anything else hurt beside your leg?"
        show anim_yoga01_dialogue_02
        l_mc "Um yeah, I think I felt my abs and groin cramp up as well"
        l_mc "(That's it!)"
        l_mc "I think I'm good now, you can get off"
        hide anim_yoga01_dialogue_02

        $ renpy.scene()
        jump goto_lucaspc
        return


    $ renpy.jump(loc)

screen yoga_grind_control_screen1():

    if yoga_grind1 == True:
        imagebutton:
            idle "animbutton_next"
            xpos .1
            ypos .85
            action Return("yoga_grind_next_inter1")

    if yoga_grind2 == True:
        imagebutton:
            idle "animbutton_speedup"
            xpos .1
            ypos .85
            action Return("yoga_grind_fast_inter1")

    if yoga_grind3 == True:
        imagebutton:
            idle "animbutton_next"
            xpos .1
            ypos .85
            action Return("yoga_grind_final_inter1")

    if yoga_grind4 == True:
        imagebutton:
            idle "animbutton_bust"
            xpos .1
            ypos .65
            action Return("yoga_grind_end_inter1")






label sadie_movietalk2:
    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    show sadie normal default_talk
    l_sadie "Nothing special. Just bored out of my mind."
    l_sadie "I’m sure some of your company could cheer me up though."
    show sadie normal default
    show lucas normal puzzle
    l_mc "(Oh boy, why did I ask?)"
    show lucas normal assured_talk
    l_mc "Uhm. Suurrree."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Some enthusiasm you have."
    l_sadie "I got it! Let’s watch a movie tonight!"
    show sadie normal happy
    show lucas normal glad_talk
    l_mc "Alright, I’m down with that. Don’t forget, you did say I could choose that horror movie I wanted this time."
    show sadie normal assured_talk
    show lucas normal glad
    l_sadie "You still remember that part? Dammit."
    show sadie normal assured
    show lucas normal default_talk
    l_mc "No take backs, a promise is a promise."
    show sadie normal assured_talk
    show lucas normal default
    l_sadie "Fiiiinee. Whatever, but I’m going to be holding on tight. I don’t deal with horror and you know that."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Do as you wish but you cant close your eyes."

    show sadie normal default_talk
    show lucas normal default
    l_sadie "Ok, I’ll wait for you. Bye."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Bye."
    $ sadie_story += 1
    jump sadie_couch_interaction
    return


label sadie_movietalk2_kitchen:
    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    show sadie normal default_talk
    l_sadie "Nothing special. Just bored out of my mind."
    l_sadie "I’m sure some of your company could cheer me up though."
    show sadie normal default
    show lucas normal puzzle
    l_mc "(Oh boy, why did I ask?)"
    show lucas normal assured_talk
    l_mc "Uhm. Suurrree."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Some enthusiasm you have."
    l_sadie "I got it! Let’s watch a movie tonight!"
    show sadie normal happy
    show lucas normal glad_talk
    l_mc "Alright, I’m down with that. Don’t forget, you did say I could choose that horror movie I wanted this time."
    show sadie normal assured_talk
    show lucas normal glad
    l_sadie "You still remember that part? Dammit."
    show sadie normal assured
    show lucas normal default_talk
    l_mc "No take backs, a promise is a promise."
    show sadie normal assured_talk
    show lucas normal default
    l_sadie "Fiiiinee. Whatever, but I’m going to be holding on tight. I don’t deal with horror and you know that."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Do as you wish but you cant close your eyes."

    show sadie normal default_talk
    show lucas normal default
    l_sadie "Ok, I’ll wait for you. Bye."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Bye."
    $ sadie_story += 1
    jump sadie_kitchen_int_label
    return


label sadie_inter_convo2:
    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    show sadie normal default
    show lucas normal default_talk
    l_mc "You ever think of spending time together that doesn’t involve more yoga?"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "No yoga? Why not?"
    show sadie normal default
    show lucas normal default_talk
    l_mc "I’m not saying we can’t do more yoga but I think I’d also Like to hang out and do something else instead."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "I’m always open to ideas. As long as you’re there by my side, I’ll be happy."
    l_sadie "We could go hiking, or minigolf. Like an actual date."
    show sadie normal happy
    show lucas normal mkay
    l_mc "(A date?)"
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Or just go for a swim in the pool. It’s been a while since we have."
    show sadie normal happy
    show lucas normal what
    l_mc "(I’d rather avoid that last one. I don’t think seeing her in a bikini would do me very good in the emotional state that I’m currently in.)"
    show sadie normal default_talk
    show lucas normal default
    l_sadie "Well… it’s been so long since we’ve spent any time together."
    l_sadie "You with school and me with more work hours."
    show sadie normal sad_talk
    l_sadie "I miss the old us that used to go out more often. "
    l_sadie "And you were always so attached to me, well you still kind of are."
    show sadie normal default
    show lucas normal puzzle_talk
    l_mc "Ok, you can stop now."
    show sadie normal smirk_talk
    show lucas normal puzzle
    l_sadie "Don’t be shy you little mama’s boy. I’ve spoiled you the most you know?"
    show sadie normal default
    show lucas normal assured_talk
    l_mc "What does that mean? You love me more than Bailey?"
    show sadie normal grump_talk
    show lucas normal assured
    l_sadie "That’s not what I said."
    show sadie normal grumpy
    show lucas normal assured_talk
    l_mc "But you meant it and you can’t take it back."
    show sadie normal default_talk
    show lucas normal default
    l_sadie "I don’t have favorites, so I have no idea what you mean."
    show sadie normal default
    show lucas normal default_talk
    l_mc "Yeah, you keep telling yourself that, but we both know you love me more."
    show sadie normal default_talk
    show lucas normal default
    l_sadie "Don’t ever tell bailey that Lucas."
    show sadie normal default
    show lucas normal default_talk
    l_mc "I doubt shed care anyways. She’s more attached to me than she is to you anyways."
    show sadie normal default_talk
    show lucas normal default
    l_sadie "That’s true. "
    l_sadie "Anyways, back to the main topic we had. "
    l_sadie "We’ll figure something out eventually dear. We have plenty of time and no rush."
    show sadie normal default
    show lucas normal default_talk
    l_mc "yeah, no rush. We’ll do more things together, back like the older days."
    l_mc "I better leave you to it before we keep talking forever. Catch you later."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Love you. "
    show sadie normal happy
    show lucas normal glad_talk
    l_mc "Love you too. "
    $ sadie_convo1_done = True

    jump sadie_couch_interaction
    return



label sadie_bedz_interaction:
    $ sadiebedz_talking = True
    hide screen main_hud_icon





    show sadiez_base at right with dissolve

    show lucas normal pose4 default at left with dissolve
    label sadie_bedroomchoice:
        menu:
            "I'm here ! " if sadie_story == 16:
                window hide
                hide sadiez_base
                show sadie normal pose7 default at right with Dissolve(.15)
                show lucas normal pose4 default_talk at left with Dissolve(.15)
                l_mc "Alright [sadie_refer_input], I’m here."
                show sadie normal pose7 default_talk at right
                show lucas normal pose4 default at left
                l_sadie "Thank you for doing this honey."
                hide sadie normal pose7
                hide lucas normal pose4




                show sadie universal_hugz pose16 with Dissolve(.15)
                pause
                show sadie universal_hugz pose17 with Dissolve(.15)
                l_sadie "Just for tonight, I swear. I only want to feel your comfort since you made me watch that scary movie. You make me feel better."
                show sadie universal_hugz pose18 with Dissolve(.15)
                l_mc "I get it. I’ll be here with you tonight."
                show sadie universal_hugz pose19 with Dissolve(.15)


                l_sadie "Ok, let’s get in bed then."
                pause
                hide universal_hugz pose20

                show sadie normal pose7 default at right with Dissolve(.15)
                show lucas normal pose24 default at left with Dissolve(.15)
                pause

                show sadie normal pose7 default_talk
                l_sadie "Is that what you're going to wear though, honey?"
                show sadie normal pose7 default
                show lucas normal pose24 mkay_talk
                l_mc "Uhm, Well I usually sleep nude… I feel too hot If I sleep with clothes on but… I guess I’ll leave my underwear on."
                show sadie normal pose7 default_talk
                show lucas normal pose24 mkay
                l_sadie "That’ll do just fine."
                show sadie normal pose11 default_talk
                l_sadie "And it’s not like I haven’t seen your body before anyways. I am your [sadie_relationship_input]."
                show sadie normal pose7 default
                show lucas normal pose24 default_talk
                l_mc "I know that, you’ve told me many times before. Let’s just sleep now."
                show lucas normal pose24 default
                show sadie normal pose12 default_talk
                l_sadie "OK honey, Come to bed."
                hide lucas normal pose24
                hide sadie normal pose12
                jump sadie_bed_scenef
                return
            "Beta: Change Clothe" if True:

                "Not available for non-patron build. Patron build required."
                jump sadie_bedroomchoice
                return
            "Sleepy ?" if True:


                show lucas normal pose4 default_talk
                l_mc "Going to sleep ?"
                show lucas normal pose4 default
                $ sadiez_face = "default talk"
                l_sadie "Yep"
                $ sadiez_face = "assured talk"
                l_sadie "Very soon."
                $ sadiez_face = "default"
                jump sadie_bedroomchoice
                return
            "Leave" if True:

                $ sadiebedz_talking = False
                jump goto_sadieroom
                return

    jump goto_sadieroom
    return


label sadie_bed_scenef:

    show event_bedtime_sadie_01 1 with Dissolve(.15)
    pause
    show event_bedtime_sadie_01 2 with Dissolve(.15)
    l_sadie "Come here baby, give me warmth."
    show event_bedtime_sadie_01 1 with Dissolve(.15)
    l_mc "*gulp*"
    show event_bedtime_sadie_01 2 with Dissolve(.15)
    l_sadie "Quickly now. Cold air is getting in so don’t make me wait, you already gave me your word."
    show event_bedtime_sadie_01 1 with Dissolve(.15)
    l_mc "Sure thing. I’m coming in."
    l_mc "(Who would’ve ever thought I’d be sleeping with my [sadie_relationship_input] again.)"
    l_mc "(This sight gives me so much nostalgia. She’d always greet me the same way when I’d come to sneak in bed with her. Always with a smile and open arms. The sight hasn’t changed at all.)"


    play sound "music/sounds/blanket_f.mp3"
    pause

    show event_bedtime_sadie_01 3 with Dissolve(.15)
    pause
    show event_bedtime_sadie_01 4 with Dissolve(.15)
    l_sadie "Wow, I really missed this."
    show event_bedtime_sadie_01 3 with Dissolve(.15)
    l_mc "(I think I did too.)"
    l_mc "(The warmth is still the same. I can feel her heart beating and her subtle breathing hitting my skin.)"
    l_mc "(The touch of her skin is still so warm and soft just as I remembered it.)"
    l_mc "(I remember now, why I used to sneak into her bed. It’s all coming back.)"
    show event_bedtime_sadie_01 5 with Dissolve(.15)
    l_mc "I love you [sadie_refer_input]."
    show event_bedtime_sadie_01 4 with Dissolve(.15)
    l_sadie "I love you too baby."


    show black with dissolve
    hide event_bedtime_sadie_01
    show event_bedtime_sadie_01 6

    show sadie bedface default
    show lucas bedface default
    hide black with dissolve

    pause
    show lucas bedface default_talk
    l_mc "I suppose, this isn’t so bad after all."
    show sadie bedface awe_talk
    show lucas bedface default
    l_sadie "You see? I told ya."
    l_sadie "A part of me misses the day when you'd climb into my bed."
    show sadie bedface awe
    show lucas bedface mkay_talk
    l_mc "Yes, but I’m not so little anymore, am I? "
    show sadie bedface default_talk
    show lucas bedface mkay
    l_sadie "That doesn’t matter Lucas, you're still my little boy. You always will be."
    show sadie bedface assured_talk
    l_sadie "And besides, its only use us in here. No one has else to know."
    show sadie bedface default
    show lucas bedface glad_talk
    l_mc "I guess you're right. As long as you don’t tell anybody. Especially Bailey. "
    show sadie bedface smirk_talk
    show lucas bedface glad
    l_sadie "Not in a million years. You know how jealous she get."
    show sadie bedface happy_talk
    l_sadie "Lets try to sleep now alright?"
    show sadie bedface happy
    show lucas bedface sure_talk
    l_mc "Sure thing. Goodnight [sadie_refer_input]."
    show sadie bedface happy_talk
    show lucas bedface sure
    l_sadie "Goodnight baby."




    show black with dissolve
    hide event_bedtime_sadie_01 6
    hide sadie bedface default
    hide lucas bedface shut
    show transition_card 1 with fade
    hide black
    show custom_text_card "Next morning . ." with dissolve
    pause
    hide transition_card
    show event_bedtime_sadie_01 7
    hide custom_text_card with dissolve


    l_mc "Zzzzzzz."
    show event_bedtime_sadie_01 8
    pause
    show event_bedtime_sadie_01 9
    l_sadie "My little boy. I wish we did this more often. Why did you ever stop asking for my company?"
    l_sadie "I wonder what he’s dreaming about right now."
    l_sadie "I hope it’s about me."
    show event_bedtime_sadie_01 8
    l_mc "Zzzzzzz."
    show black with dissolve
    hide event_bedtime_sadie_01


    stop music
    play music "music/audio_shower_01.mp3"
    l_unkown "Lucas baby, time to wake up."
    l_mc "What, who? Where am I."
    l_mc "What’s that noise I’m hearing? Water?"




    show sadie_beddreamboob_anim
    hide black with dissolve
    l_sadie "Hey Lucas."
    "[sadie_refer_input]!?"
    l_sadie "Care to join? You look really sweaty."
    "What the hell is going on? Why am I here?"
    l_sadie "What do you mean? Didn’t we used to take baths together?"
    "Well yeah but baths are different from taking showers with your [sadie_relationship_input]."
    l_sadie "It’s fine honey. Like I’ve told you before, there isn’t a part of you that I haven’t seen before so there isn’t anything to be ashamed of. Come here and wash my back, will you?"


    show dream_hand with dissolve
    l_mc "Are you sure about this?"
    l_sadie "Its only natural for us to take baths and showers together. Nothing has changed just because you're a little taller now. I know you want to feel my warmth too, don’t you?"
    l_mc "Maybe you're right, I guess."
    l_mc "It’s just natural for us. I just have to accept it."
    l_mc "I want your warmth, it’s only our way of bonding."
    l_sadie "Like what you see? Come close and we can do some bonding."
    l_sadie "I want those arms wrapped around me right now."
    l_mc "Me too."
    l_mc "I want to wash your body if you’d let me."
    l_sadie "Than come here."
    l_sadie "Hey Lucas, wake up honey."
    l_mc "What? What’s…"
    l_sadie "Wake up, no more dreaming. It’s getting late."
    l_mc "Late? What are you talking…?"
    l_mc "Wait, am I dreaming. No wait, just a little longer."
    l_mc "I’m almost there."
    stop music 

    show black with dissolve
    play music "music/music4.mp3"
    hide dream_hand
    hide sadie_beddreamboob_anim
    show event_bedtime_sadie_01 9
    hide black with dissolve

    l_mc "Uh… "
    show event_bedtime_sadie_01 10
    l_mc "(My face is so soft. This is the best pillow Ive ever slept on.)"
    l_mc "(Where am I? I don’t remember My pillow feeling this good.)"
    show event_bedtime_sadie_01 11
    l_sadie "There you are."
    show event_bedtime_sadie_01 12
    l_sadie "Finally awake?"
    show event_bedtime_sadie_01 13
    l_mc "Yeah, what’s going on?"
    show event_bedtime_sadie_01 12
    l_sadie "Sorry honey but I have to get up and get some work done early today."
    l_sadie "Not that I don’t mind your love and company though. We’d be like this all morning if it were up to me."
    show event_bedtime_sadie_01 14
    l_mc "(Wait a second…)"
    l_mc "(This isn’t my pillow. [sadie_refer_input]?!) "

    show event_bedtime_sadie_01 15 with dissolve
    pause
    show event_bedtime_sadie_01 16
    l_mc "Oh yeah, right. Sorry [sadie_refer_input]. I didn’t realize I was holding you down."
    show event_bedtime_sadie_01 17
    l_sadie "Don’t worry. I loved it. I haven’t had any sleep as good as this in a long time."
    l_sadie "Your warmth put me at ease the whole night that I slept like a baby."
    show event_bedtime_sadie_01 16
    l_mc "Really? Cool cool. "
    show event_bedtime_sadie_01 17
    l_sadie "I’m sorry I dragged you into this again. I know you’re a big boy now, so I won’t ask again."
    show event_bedtime_sadie_01 18 with dissolve
    pause
    show event_bedtime_sadie_01 19
    l_sadie "You won’t have to sleep with me again if you don’t want to."
    show event_bedtime_sadie_01 18
    l_mc "Well... I kinda… I… I wouldn’t mind."
    l_mc "I remembered why I used to sneak into your bed when I was younger now."
    l_mc "You make me feel so… calm, so at ease."
    show event_bedtime_sadie_01 19
    l_sadie "Lucas."
    show event_bedtime_sadie_01 18
    l_mc "So, I wouldn’t mind doing this more as long as it’s ok with you."
    show event_bedtime_sadie_01 19
    l_sadie "Anytime honey, anytime you want. You can sleep in my arms every night if you choose so."
    show event_bedtime_sadie_01 18
    l_mc "That’d be nice. For now, I better get up now so you can go do your work."
    show event_bedtime_sadie_01 19
    l_sadie "Thanks. "

    $ now.advance()
    show black with dissolve
    hide event_bedtime_sadie_01
    hide black with dissolve
    show sadie normal pose7 default at right with moveinright
    show lucas normal pose24 default at left with moveinleft
    pause
    show sadie normal happy_talk
    l_sadie "Thanks for the night, Lucas. I’m really happy you wouldn’t mind doing it more often."
    show sadie normal happy
    show lucas normal default_talk
    l_mc "Me too. I slept like a baby. I felt the same as It used to."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "I’m glad you say that, It felt the same for me as well."
    show sadie normal happy
    show lucas normal happy_talk
    l_mc "I’ll see you around [sadie_refer_input]."
    show sadie normal happy_talk
    show lucas normal happy




    $ sadiebedz_talking = False
    l_sadie "Bye honey."


    hide sadie normal pose7 default at right with moveoutright

    show lucas normal default_d
    l_mc "(So much happened it’s hard to take in but most importantly, that weird dream.)"
    show lucas normal puzzle_d
    l_mc "(If I try to remove those kinds of thoughts from my head, I’d have to completely stay away from her. And I’d hate to do that.) "
    show lucas normal default_d
    l_mc "(I’ll just have to accept them from here on out but I can never let her know about my dreams and the boner dilemma I keep having.)"
    l_mc "(I won’t push her away though.) "
    show lucas normal assured
    l_mc "(I just can’t stay away from her. My issues are my own and I’ll deal with them. One day at a time.)"

    hide lucas normal pose24 default at left with moveoutleft
    show black with dissolve
    show custom_text_card2 "You have reached the end of [sadie_refer_input]’s story content for now.{vspace=30} Sorry but do come back for the next update that will progress her story even further" with dissolve
    pause
    $ renpy.notify("Sadie's clothe not enabled (Patron only.)")

    hide custom_text_card2

    $ sadie_story += 1

    hide black
    jump goto_lucasroom
    return

image sadie_beddreamboob_anim:
    "anim_bedtimedream_01 1"
    0.1
    "anim_bedtimedream_01 2"
    0.1
    "anim_bedtimedream_01 3"
    0.1
    "anim_bedtimedream_01 4"
    0.1
    "anim_bedtimedream_01 5"
    0.1
    "anim_bedtimedream_01 6"
    0.1
    "anim_bedtimedream_01 7"
    0.1
    "anim_bedtimedream_01 8"
    0.1
    repeat

label sadie_work_talk:
    show sadie normal assured_talk
    show lucas normal default
    l_sadie "Draining! Lately my shoulders have been getting stiff for walking from house to house with so many clients."
    show sadie normal assured
    show lucas normal puzzle_d_talk
    l_mc "I guess being a real-estate agent is tough on your body isn’t it."
    show sadie normal awe_talk
    show lucas normal puzzle
    l_sadie "It is, but it’s fine. I have you to come back to every day so I really don’t have too much to complain about."

    window hide
    hide lucas normal
    hide sadie normal

    show sadie universal_hugz pose1 with dissolve
    pause
    show sadie universal_hugz pose2 with dissolve
    pause
    show sadie universal_hugz pose3 with dissolve
    pause


    hide universal_hugz
    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    pause
    show lucas normal default_talk
    l_mc "Just take it easier on yourself [sadie_refer_input]."
    show lucas normal default
    show sadie normal default_talk
    l_sadie "Maybe if you could give me a little massage on my back, I’d feel 1000%% better!"
    show lucas normal glad_talk
    show sadie normal default
    l_mc "I’d love to if I knew how. Maybe I’ll become a massage therapist in the future just for you."
    show lucas normal default
    show sadie normal awe_talk
    l_sadie "You’d do that just for your old [sadie_relationship_input]? how lovely you are Lucas. I’ve raised such a fine man."
    show lucas normal happy_talk
    show sadie normal default
    l_mc "You're not that old and I love you [sadie_relationship_input]."
    show lucas normal default
    show sadie normal awe_talk
    l_sadie "Love you too honey."

    jump sadie_balcony_interaction
    return

label sadie_schooltalk_inter:
    show sadie normal default
    show lucas normal sad_talk
    l_mc "Hey [sadie_refer_input], about my whole situation at school."
    show sadie normal sad_talk
    show lucas normal sad
    l_sadie "We talked about this honey. I’m not mad at you, just a little disappointed. "
    show sadie normal default_talk
    l_sadie "You could have handled it a little better but in the end, you did the right thing by stepping in, and I’m proud of you for that."
    show sadie normal awe_talk
    l_sadie "Had it not been for you, who knows what that other kid would’ve done to your teacher."
    show sadie normal awe
    show lucas normal puzzle_d_talk
    l_mc "Yeah, I still wanted to apologize for putting you through this with me. I’ll try to do better next time."
    show sadie normal awe_talk
    show lucas normal default
    l_sadie "It’s ok honey, I’ll always be here for you when you need me."
    show sadie normal happy_talk
    l_sadie "Now drop the subject. I don’t want you to worry about it any longer."
    show sadie normal happy
    show lucas normal default_talk
    l_mc "Thanks, I love you."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Love you too dear. "
    jump sadie_balcony_interaction
    return

label sadie_work_talkz:
    show sadie normal assured_talk
    show lucas normal default
    l_sadie "Draining! Lately my shoulders have been getting stiff for walking from house to house with so many clients."
    show sadie normal assured
    show lucas normal puzzle_d_talk
    l_mc "I guess being a real-estate agent is tough on your body isn’t it."
    show sadie normal awe_talk
    show lucas normal puzzle
    l_sadie "It is, but it’s fine. I have you to come back to every day so I really don’t have too much to complain about."

    window hide
    hide lucas normal
    hide sadie normal

    show sadie universal_hugz pose1 with dissolve
    pause
    show sadie universal_hugz pose2 with dissolve
    pause
    show sadie universal_hugz pose3 with dissolve
    pause


    hide universal_hugz
    show sadie normal pose default at right with Dissolve(.15)
    show lucas normal pose4 default at left with Dissolve(.15)
    pause
    show lucas normal default_talk
    l_mc "Just take it easier on yourself [sadie_refer_input]."
    show lucas normal default
    show sadie normal default_talk
    l_sadie "Maybe if you could give me a little massage on my back, I’d feel 1000%% better!"
    show lucas normal glad_talk
    show sadie normal default
    l_mc "I’d love to if I knew how. Maybe I’ll become a massage therapist in the future just for you."
    show lucas normal default
    show sadie normal awe_talk
    l_sadie "You’d do that just for your old [sadie_relationship_input]? how lovely you are Lucas. I’ve raised such a fine man."
    show lucas normal happy_talk
    show sadie normal default
    l_mc "You're not that old and I love you [sadie_relationship_input]."
    show lucas normal default
    show sadie normal awe_talk
    l_sadie "Love you too honey."

    jump kitchen_sadie_inter
    return

label sadie_schooltalk_interz:
    show sadie normal default
    show lucas normal sad_talk
    l_mc "Hey [sadie_refer_input], about my whole situation at school."
    show sadie normal sad_talk
    show lucas normal sad
    l_sadie "We talked about this honey. I’m not mad at you, just a little disappointed. "
    show sadie normal default_talk
    l_sadie "You could have handled it a little better but in the end, you did the right thing by stepping in, and I’m proud of you for that."
    show sadie normal awe_talk
    l_sadie "Had it not been for you, who knows what that other kid would’ve done to your teacher."
    show sadie normal awe
    show lucas normal puzzle_d_talk
    l_mc "Yeah, I still wanted to apologize for putting you through this with me. I’ll try to do better next time."
    show sadie normal awe_talk
    show lucas normal default
    l_sadie "It’s ok honey, I’ll always be here for you when you need me."
    show sadie normal happy_talk
    l_sadie "Now drop the subject. I don’t want you to worry about it any longer."
    show sadie normal happy
    show lucas normal default_talk
    l_mc "Thanks, I love you."
    show sadie normal happy_talk
    show lucas normal default
    l_sadie "Love you too dear. "

    jump kitchen_sadie_inter
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

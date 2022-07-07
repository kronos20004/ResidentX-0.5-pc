label eleanor_first_event:
    hide screen main_hud_icon
    play sound "music/doorbell_03.mp3"
    pause
    show lucas normal pose4 alert at left with moveinleft
    show eleanor normal pose default at right with moveinright
    pause
    show lucas normal pose4 alert_talk
    $ eleanor_gallery_profile = True
    $ renpy.notify("Eleanor's Gallery Unlocked")
    l_mc "Ms. Eleanor ?"
    show lucas normal pose4 happy_talk
    l_mc "What are you doing here?"
    show lucas normal pose4 happy
    show eleanor normal pose1 default_talk
    l_eleanor "I'm here to talk to you about some business pertaining to your education"
    show lucas normal pose4 sad_talk
    show eleanor normal pose1 default
    l_mc "My education? But I’ve been suspended until the end of the semester"
    l_mc "I'm going to fail my semester finals by the time I come back anyways"
    show lucas normal pose4 sad_talk
    l_mc "Being suspended from school for so long, I won’t be able to learn anything for those final exams"
    show lucas normal pose4 puzzle
    show eleanor normal pose3 default_talk
    l_eleanor "Well that’s exactly what I’ve come to talk about"
    l_eleanor "I won't be taking much of your time so lets just get to it"
    show sadie business pose default at dual_character_position with moveinleft:
        xzoom -1
    pause
    show sadie business default_talk
    show lucas normal pose4 puzzle
    show eleanor normal pose default
    l_sadie "Oh hello Ms. Eleanor"
    l_sadie "You here to see Lucas ?"
    show sadie business default
    show lucas normal pose4 default
    show eleanor normal pose default_talk
    l_eleanor "Yes, I've come to give him an offer"
    show lucas normal pose4 default_talk
    show eleanor normal pose default
    l_mc "Offer ? . ."
    show lucas normal pose4 default
    show eleanor normal pose default_talk
    l_eleanor "I came to offer Lucas my support"
    l_eleanor "Since you don’t have much hope to pass your final exams without any classes, I’m sure I can help you out a little"
    show sadie business happy_talk
    show eleanor normal pose default
    l_sadie "Oh really? Any help for him would be much appreciated"
    l_sadie "You know he's not a bad kid, he only wanted to help you"
    show sadie business happy
    show lucas normal pose4 puzzle_d
    show eleanor normal pose default_talk
    l_eleanor "Well in any case, breaking another's kid's jaw while he's on the ground was a bit overboard"
    show lucas normal pose4 puzzle
    l_eleanor "Even if Lucas was there to help me, he shouldn't have done that"
    show lucas normal pose4 puzzle_d_talk
    show eleanor normal pose down
    l_mc "I get it already, can you just say why you're really here?"
    show sadie business pose2 grump_talk
    show lucas normal pose4 blank
    l_sadie "Lucas ! be nicer"
    show sadie business grumpy

    show eleanor normal pose default_talk
    l_eleanor "Don't mind that, Sadie. You're right Lucas"
    l_eleanor "Since you did help me against that perverted student, the least I could do is help you pass your final exams"
    show lucas normal pose4 mkay_talk
    show sadie business default
    show eleanor normal pose default
    l_mc "And how would you possibly help me?"
    l_mc "I just said it already, I can't come back to school"
    show lucas normal pose4 mkay
    show eleanor normal pose1 default_talk
    l_eleanor "There is no need for that"
    show lucas normal pose4 alert
    l_eleanor "At my request, the school has authorized me to come over and give you private tutoring sessions"
    l_eleanor "but just because I’m doing this for you, don’t think that what you did to that kid was right"
    show sadie business happy_talk
    show eleanor normal pose default
    show lucas normal pose4 happy
    l_sadie "Oh wow! Isn’t that great dear?"
    show sadie business happy
    show lucas normal pose4 happy_talk
    l_mc "Wow, thanks Ms. Eleanor. I don’t know what to say. This way I won’t be flunking a grade"
    show sadie business happy_talk
    show lucas normal pose4 happy
    l_sadie "Yes, we can’t thank you enough. It’s been pretty hard for us lately so you just brought a little sunshine to our hearts"
    show sadie business happy
    show eleanor normal pose1 default_talk
    l_eleanor "No need to thank me, It was the least I could do for him"
    l_eleanor "I'll give you a call first to let you know when I'm ready to start our tutor sessions. After that, you can just call me over when you have free time to get some tutoring"
    l_eleanor "Of course, I still have to teach at school, so I won't be available in the mornings. You can give me a call in the afternoons and I'll be here"
    l_eleanor "And this still means no slacking off. You have to call me often. I have alot to teach you, so you can catch up with the rest of your classmates"
    show lucas normal pose4 puzzle_talk
    show eleanor normal pose default
    l_mc "How are you going to teach me so many subjects all by yourself?"
    show lucas normal pose4 puzzle
    show eleanor normal pose default_talk
    l_eleanor "I've taught many subjects over my years of education. You couldn't have gotten a better tutor to help you"
    show lucas normal pose4 default_talk
    show eleanor normal pose default
    l_mc "Well If you say so"
    show lucas normal pose4 default
    show sadie business happy_talk
    l_sadie "Thank you so much again, I'll leave him in your hands"
    l_sadie "And I'll make sure to stay on top of him, you'll be getting calls from him often"
    show sadie business happy
    show eleanor normal pose2 default_talk
    l_eleanor "Okay then, I'll be off now, I have to head back to school so you two take care"
    show sadie business pose happy
    show eleanor normal pose3 default
    show lucas normal pose4 default_talk
    l_mc "Thanks for stopping by"
    show sadie business happy_talk
    show lucas normal pose4 default
    l_sadie "Goodbye"
    show sadie business happy
    show eleanor normal pose3 default_talk
    l_eleanor "Keep in touch"
    hide eleanor normal pose default at right with moveoutright
    pause
    show sadie business happy_talk at right with dissolve:
        xzoom 1
    l_sadie "Isn't that just great dear ?"
    show sadie business default
    show lucas normal default_talk
    l_mc "Yeah, I was expecting to flunk the whole grade. Now I have a better chance to pass my grade"
    show sadie business default_talk
    show lucas normal default
    l_sadie "Once she gives you the first call, you better call her often to catch up on your studies"
    l_sadie "Well I have to go to work now too. I’ll see you later tonight. goodbye honey"
    show sadie business happy
    show lucas normal default_talk
    l_mc "Bye [sadie_refer_input]. I'll see you later"
    "Eleanor added to the contact"
    hide sadie business default at dual_character_position with moveoutright
    show lucas normal default
    pause
    hide lucas normal pose4 default at left with moveoutleft
    $ eleanor_story += 1
    $ quest_log_active.add("eleanor")
    $ contact_list.append((e, "phone_screen/ui_phone_contact_eleanor.png"))
    jump goto_frontf1
    return

label eleanor_second_event:
    hide screen main_hud_icon
    play sound "music/doorbell_03.mp3"
    pause
    show lucas normal pose4 default at left with moveinleft
    show eleanor normal pose default at right with moveinright
    pause
    show eleanor normal pose default_talk
    show lucas normal pose4 default
    l_eleanor "Hey Lucas"
    show eleanor normal pose default
    show lucas normal pose4 default_talk
    l_mc "Eleanor, thanks for coming by today"
    show eleanor normal pose default_talk
    show lucas normal pose4 default
    l_eleanor "ehem* it’s “Ms. Eleanor” to you"
    show eleanor normal pose default
    show lucas normal pose4 default_talk
    l_mc "I’m sorry. I’m just not used to having a teacher at my house. I’m probably just a little nervous"
    show eleanor normal pose1 default_talk
    show lucas normal pose4 default
    l_eleanor "what would you be nervous for? all we are doing is studying"
    show eleanor normal pose default
    show lucas normal pose4 default_talk
    l_mc "yeah, I know. It’s just that I’m not sure what to expect is all"
    show eleanor normal pose3 default_talk
    show lucas normal pose4 default
    l_eleanor "Studying"
    l_eleanor "What else would I be here for?"
    show eleanor normal pose default
    show lucas normal pose4 mkay
    l_mc "(Jesus, having my beautiful teacher here is making me nervous all of a sudden. I just got to act cool and learn whatever I can from her)"
    show eleanor normal pose default
    show lucas normal pose4 default_talk
    l_mc "You're right, I'm sorry. Should we just get started than?"
    show eleanor normal pose default_talk
    show lucas normal pose4 default
    l_eleanor "Yes, shall we go to your room then"
    show eleanor normal pose default
    show lucas normal pose4 assured_talk
    l_mc "My room you say?"
    show eleanor normal pose default_talk
    show lucas normal pose4 assured
    l_eleanor ". . .well where else? You have a desk and a computer there don't you?"
    show eleanor normal pose default
    show lucas normal pose4 default_talk
    l_mc "Right, of course. Let me take you up"
    $ eleanor_story += 1
    jump goto_lucasroom
    return

label eleanor_teaching_event1:
    hide screen main_hud_icon


    $ eleanor_btn_lucasroom = False
    show lucas normal pose4 default at left with Dissolve(.3)
    show eleanor normal pose default at right with Dissolve(.3)
    show lucas normal pose4 default_talk
    l_mc "Alright, this is my humble adobe"
    show lucas normal pose4 default
    show eleanor normal pose1 default_talk
    l_eleanor "Well, it's not bad. Just like any other boy's room I suppose. This should do just fine for us"
    show lucas normal pose4 default_talk
    show eleanor normal pose2 default
    l_mc "So, what now ?"
    show lucas normal pose4 default
    show eleanor normal pose2 default_talk
    l_eleanor "So now we learn. I brought some books and some study guides for you"
    l_eleanor "I’ll be teaching you your general eds and a few electives so you're well prepared. "
    show lucas normal pose4 default_talk
    show eleanor normal pose default
    l_mc "Sounds good. I’m ready to start"
    while True:
        hide screen main_hud_icon
        call quicktime_minigame () from _call_quicktime_minigame
        if minigame_success:

            jump won_minigame1
        "Try again. . ."


label won_minigame1:
    if now(["morning","afternoon"]):
        scene event_tutoring_bg_1

    elif now(["evening","night"]):
        scene event_tutoring_bg_1_alt

    show eleanor_lucas tutorial_night default_talk defaultz
    l_eleanor "well that wasn’t so hard was it?"
    show eleanor_lucas tutorial_night default defaultz_talk
    l_mc "well not with you helping me out"
    l_mc "you're always an amazing teacher so It was pretty easy to trust you"
    show eleanor_lucas tutorial_night default_talk defaultz
    l_eleanor "Oh well thank you. I don’t think I’ve ever had a student compliment me for my actual teaching ability. Its always been superficial things like how I look or dress rather than what I can do"
    l_eleanor "Well not to say you aren’t pretty but I just like learning from you. When others see a strict teacher, I just see someone trying to help me out."
    show eleanor_lucas tutorial_night default defaultz
    l_mc "(I just called my teacher pretty. What the hell am I thinking)"
    show eleanor_lucas tutorial_night default_talk defaultz
    l_eleanor "All this coming from a delinquent student of mine. What a surprising turn of events"
    show eleanor_lucas tutorial_night default defaultz_talk
    l_mc "Hey, you know I only did what I did to that student to help you out."
    show eleanor_lucas tutorial_night default_talk defaultz
    l_eleanor "Don’t worry Lucas, I know you’re not a bad kid. That’s why I’m here after all"
    l_eleanor "I wouldn’t be here if I didn’t trust you as well or if I knew you’d just slack off and didn’t take this seriously"
    l_eleanor "Anyways, I think that’s enough for today and I better be off as well."
    $ eleanor_btn_lucasroom = True
    $ eleanor_story += 1
    jump goto_lucasroom
    return


label eleanor_third_event:
    hide screen main_hud_icon
    show lucas normal pose4 default at left with moveinleft
    show eleanor normal pose default at right with moveinright
    show lucas normal pose4 default_talk
    l_mc "Hey Eleanor. Thanks for coming again"

    show eleanor normal pose down at right
    show lucas normal pose4 default
    pause
    show eleanor normal pose down_talk at right
    l_eleanor "What was that Lucas?"
    show eleanor normal pose down at right
    show lucas normal pose4 default_talk
    l_mc "What ?"
    show eleanor normal pose1 default_talk at right
    show lucas normal pose4 default_talk
    l_eleanor "It’s “Ms. Eleanor” to you still. Don’t think just because we aren’t in a class setting, you can call my name however you please."
    show eleanor normal pose default at right
    show lucas normal pose4 default_talk
    l_mc "I’m sorry Elea. . . sorry sorry. It’s just that I’m not still used to seeing you out of class and much less seeing you in my home. I’ll try to remember."
    show eleanor normal pose rest_talk at right
    show lucas normal pose4 default
    l_eleanor "well I hope you do."
    show eleanor normal pose pain_talk at right
    l_eleanor "ok, let’s go up to your room and get started alrea . . . ouch!"
    show eleanor normal pose rage_talk at right
    l_eleanor "Dammit."
    show eleanor normal pose pain at right
    show lucas normal pose4 mkay_talk
    l_mc "What?! You okay?"
    l_mc "Do you need to lay down"
    show eleanor normal pose pain_talk at right
    show lucas normal pose4 mkay
    l_eleanor "No no, I’m good. It’s just my back and neck pains. They go away after a while"
    l_eleanor "I’ll be fine. I just have to remove my top shirt for now."
    show lucas normal pose4 default
    show eleanor normal pose8 pain_talk at right with dissolve

    l_eleanor "this damn bra"
    show eleanor normal pose9 pain at right with dissolve
    pause
    show eleanor normal pose10 pain at right with dissolve
    pause
    show eleanor normal pose11 pain at right with dissolve
    pause
    show eleanor normal pose12 default at right with dissolve
    pause
    show lucas normal pose4 mkay
    l_mc "(did she say bra? Is it too tight or something?)"
    show lucas normal pose4 default
    show eleanor normal pose12 default_talk at right

    l_eleanor "Alright Lucas, let's go upstairs"
    show lucas normal pose4 default
    show eleanor normal pose12 default at right
    l_mc "(Dayum. I don’t think she’s ever worn just a tight shirt at school)"
    pause
    $ eleanor_story += 1
    jump goto_lucasroom
    return


label eleanor_teaching_event2:
    menu:
        "Ready ?" if True:
            jump eleanor_teaching_event2z
        "Not yet" if True:
            return

label eleanor_teaching_event2z:
    while True:
        hide screen main_hud_icon
        call quicktime_minigame () from _call_quicktime_minigame_1
        if minigame_success:

            jump won_minigame2
        "Try again. . ."

label won_minigame2:
    if now(["evening","night"]):
        scene event_tutoring_bg_1_alt

    if now(["morning","afternoon"]):
        scene event_tutoring_bg_1
    show eleanor_lucas tutorial default_talk pose3 defaultz
    l_eleanor "well that wasn’t so hard was it?"
    hide eleanor_lucas tutorial default_talk pose3 defaultz
    scene event_tutoring_1_1 with Dissolve(0.3)
    pause
    scene event_tutoring_1_3 with Dissolve(0.3)
    l_mc "oh finally? You sure were hard today."
    scene event_tutoring_1_2 with Dissolve(0.3)
    l_eleanor "Well I can’t go easy on you. If anything, I have to go twice as hard on you so you can keep up with the rest of the students."
    scene event_tutoring_1_3 with Dissolve(0.3)
    l_mc "Yeah, I understand. Not holding you it against you. I know you're doing it how you think it’s best."
    scene event_tutoring_1_2 with Dissolve(0.3)
    l_eleanor "Well I appreciate your understanding. Very mature of you. Most students would’ve just thrown a temper tantrum and blown off my lectures but not you Lucas."
    scene event_tutoring_1_3 with Dissolve(0.3)
    l_mc "No worries, I just like learning from you in particular and you put it all in a soothing manner."
    l_mc "Like I can actually listen to you and just forget about whatever else is going on in class besides you."
    l_mc "It’s just the way you talk and look in class"
    scene event_tutoring_1_5 with Dissolve(0.3)
    l_eleanor "You trying to flatter me boy?"
    scene event_tutoring_1_6 with Dissolve(0.3)
    l_mc "Not at all, I’m just being honest I swear. Nothing of the sort"
    scene event_tutoring_1_2 with Dissolve(0.3)
    l_eleanor "riiiiight. I’ve never heard a student talk so kindly of me. Makes me wonder if there’s any ulterior motives behind your flattering words"
    l_eleanor "Something you're not telling me Lucas?"
    scene event_tutoring_1_7 with Dissolve(0.3)
    l_mc "(awe crap. What else can I say to her? I’m not looking very good here)"
    scene event_tutoring_1_6 with Dissolve(0.3)
    l_mc "I . . . I better get up now and stretch my legs since this session is over you know? You should be going home, right?"
    scene event_tutoring_1_8 with Dissolve(0.3)
    pause
    scene event_tutoring_1_11 with Dissolve(0.3)
    pause
    scene white with fade
    scene event_tutoring_1_10 with vpunch
    l_mc "I . . . hhmmppfff!?"
    scene event_tutoring_1_9 with Dissolve(0.3)
    l_eleanor "Lucas!?"
    scene event_tutoring_1_10 with Dissolve(0.3)
    l_mc "I’m show showry"
    scene event_tutoring_1_9 with Dissolve(0.3)
    l_eleanor "If you really are sorry than get your face off my breasts!"
    scene event_tutoring_1_10 with Dissolve(0.3)
    l_mc "oh, right right"
    l_mc "(I hate to part ways but I can’t kiss them forever)"
    $ eleanor_story += 1
    hide screen main_hud_icon
    jump goto_lucasroom
    return
    pause

label eleanor_teaching_event2zz:
    hide screen main_hud_icon
    show lucas normal pose4 default at left with Dissolve(.3)
    show eleanor normal pose12 default at right with Dissolve(.3)

    show lucas normal pose4 default
    show eleanor normal pose10 grumpy_talk at right
    l_eleanor "what the hell was that Lucas?"
    show lucas normal pose4 sad_talk at left
    show eleanor normal pose14 grumpy at right
    l_mc "I’m sorry I’m sorry. It wasn’t my intention"
    show lucas normal pose4 default_d_talk at left
    l_mc "I was just getting up and then I bumped into you. An honest mistake"
    show lucas normal pose4 sad at left
    show eleanor normal pose14 rage_talk at right
    l_eleanor "A mistake?!"
    show lucas normal pose4 default_d_talk at left
    show eleanor normal pose12 grumpy at right
    l_mc "it’s just that they are so big and I didn’t have enough space to . . ."
    show lucas normal pose4 what at left

    l_mc "(Oh shit! what am I saying)"
    show lucas normal pose4 default at left
    show eleanor normal pose13 default_talk at right
    l_eleanor "Big? Lucas . . ."
    show lucas normal pose4 default_talk at left
    show eleanor normal pose12 default at right
    l_mc "I’m just really nervous right now. I’m sorry again."
    l_mc "I don’t know what I’m saying anymore, it happened so fast and I didn’t have time to react."
    show lucas normal pose4 default at left
    show eleanor normal pose15 down_talk mouth_cover at right
    l_eleanor "No, you're right Lucas, I’m the one who should be sorry."
    show eleanor normal pose12 down_talk none at right
    l_eleanor "I was too close and it wasn’t your fault. I know you didn’t do it on purpose so let’s just leave it at that please. The quicker we forget about this, the better."
    show lucas normal pose4 default_talk at left
    show eleanor normal pose12 default blush at right
    l_mc "Yeah, you're right. Let’s just move on"

    show lucas normal pose4 default at left
    show eleanor normal pose12 default_talk blush at right
    l_eleanor "I’ll just be leaving now. I’ll see you later"
    l_eleanor "you keep working hard"
    show lucas normal pose4 default_talk at left
    hide eleanor normal pose12 default_talk blush with moveoutright
    l_mc "ok see you later?"
    show lucas normal pose4 mkay at left
    l_mc "(She’s leaving so quick. She’s definitely embarrassed.)"

    show lucas normal pose4 mkay_talk at left
    l_mc "yep, that was awkward alright."

    show lucas normal pose4 default at left with moveinleft
    show sadie normal pose1 default at right with moveinright
    pause
    show sadie normal pose1 default_talk at right with Dissolve(0.3)
    l_sadie "Hey Lucas, why did Eleanor just speed walk past me and barge out the door? Her face was beet red."

    show sadie normal pose1 grump_talk at right
    l_sadie "what did you say to her mister?"
    l_sadie "you mind explaining yourself?"
    show sadie normal pose1 grumpy at right
    show lucas normal pose4 default_talk at left
    l_mc "it was nothing [sadie_refer_input]"
    l_mc "she just got a phone call all of a sudden and left. Maybe it was some family matter?"
    l_mc "you have to believe me"
    show sadie normal pose1 default_talk at right
    show lucas normal pose4 default at left
    l_sadie "alright then sweetie"
    l_sadie "I believe you. I do"
    show sadie normal pose1 happy_talk at right
    l_sadie "I’m so proud you’re still keeping up with your studies"
    show sadie normal pose1 default at right
    pause
    window hide
    show sadie normal pose2 happy at right
    pause
    hide lucas normal pose4 default
    show sadie universal_hugz pose1 at center with Dissolve(0.2)
    pause
    show sadie universal_hugz pose2 at center with Dissolve(0.2)
    pause
    show sadie universal_hugz pose3 at center with Dissolve(0.2)



    l_mc "(great. More physical contact with my well-endowed [sadie_refer_input]"
    l_mc "(Just what I needed after the whole incident with Ms. Eleanor to calm down my blood pressure.)"
    $ now.advance()
    hide sadie universal_hug close pose at center with moveoutbottom
    $ eleanor_story += 1
    jump goto_lucasroom
    return

label eleanor_third_session:
    hide screen main_hud_icon
    show lucas normal default pose4 at left with moveinleft
    show eleanor normal rage pose6 bird_poop at right with moveinright
    pause
    show lucas normal default_talk pose4 at left
    l_mc "Hello Ms. Elean . . ."
    show lucas normal puzzle_talk pose4 at left
    l_mc "Woah. . . what happen to you out there? Is that paint on you?"
    show lucas normal puzzle pose4 at left
    show eleanor normal rage_talk pose1 at right
    l_eleanor "paint would've been much better but no, I had the misfortune to be at the wrong place, wrong time"
    l_eleanor "Now I have a bird's fecal matter all over me just as I got out of my car"
    show eleanor normal rage_talk pose2 at right
    l_eleanor "So, what should I do now. . ."
    show lucas normal default_talk pose4 at left
    show eleanor normal grumpy pose2 at right
    l_mc "You can take shower in the bathroom upstair. It would be a shame if you had to go all the way back to your house to get cleaned up."
    show lucas normal default pose4 at left
    show eleanor normal default_talk pose2 at right
    l_eleanor "But what about your [sadie_refer_input] ? Shouldn't we ask her first if it's ok for me to use your shower ?"
    show lucas normal default_talk pose4 at left
    show eleanor normal default pose2 at right
    l_mc "Nah, it'll be fine. She's at work anyways so you'll be fine"
    show lucas normal default pose4 at left
    show eleanor normal glad_talk pose2 at right
    l_eleanor "oh, thank you Lucas. I better go take that shower asap before it leaves a nasty stain in my hair."
    show lucas normal default_talk pose4 at left
    show eleanor normal glad pose2 at right
    l_mc "Alright, I'll take you to the bathroom"
    $ eleanor_story += 1
    scene black with Dissolve(0.3)
    jump goto_bathroomf2
    return

label eleanor_third_session_bath:
    hide screen main_hud_icon
    show lucas normal default pose4 at left with Dissolve(0.2)
    show eleanor normal default pose2 bird_poop at right with Dissolve(0.2)
    pause
    show lucas normal default_talk pose4 at left
    l_mc "ok, this is it. Feel free to use whatever you want in here and there's plenty of towels as well."
    l_mc "I’ll go grab you a spare set of clothes so you don’t have to walk around in those all day. My [sadie_relationship_input] should have plenty of clothes that fit you."
    show eleanor normal default_talk pose2 bird_poop
    show lucas normal default pose4 at left
    l_eleanor "ok, but what about these clothes I have on right now?"
    show eleanor normal default pose2 bird_poop
    show lucas normal default_talk pose4 at left
    l_mc "I can just throw them in the washer machine downstairs for you so it should be clean by the time you leave today."
    show eleanor normal default_talk pose2 bird_poop
    show lucas normal default pose4 at left
    l_eleanor "It’s fine Lucas, I’ll put my dirty outfit in your laundry machines myself once I’m done with my shower."
    l_eleanor "I really can’t thank you enough for this. It was already a bad day today at school and then the bird poop all over me."
    l_eleanor "Getting clean will at least put me in a better mood for the day"
    show eleanor normal default pose2 bird_poop
    show lucas normal default_talk pose4 at left
    l_mc "don’t mention it. I’d help you out any day."
    show eleanor normal smirk pose2 bird_poop
    show lucas normal glad_talk pose4 at left

    l_mc "I meant . . . like"
    l_mc "As in just helping out with basic stuff you know?"
    show eleanor normal smirk_talk pose2 bird_poop
    show lucas normal glad pose4 at left
    l_eleanor "right"
    show eleanor normal glad pose2 bird_poop
    show lucas normal default_talk pose4 at left
    l_mc "Ha.. ha ok. I'll just leave you to it"
    l_mc "I'll be back with some clothes. I'll slip in the spare outfit by the door if you just leave it cracked open a bit"
    show eleanor normal default_talk pose2 bird_poop
    show lucas normal default pose4 at left
    l_eleanor "Ok , I'll be right here. I'll be undressing , so I can't really have you here to check me out"
    show eleanor normal glad pose2 bird_poop
    show lucas normal glad_talk pose4 at left
    l_mc "Ok !"
    hide eleanor normal glad pose2 bird_poop
    hide lucas normal glad_talk pose4 at left
    $ eleanor_story += 1
    jump goto_hallwayf2
    return


label eleanor_third_session_bath2:
    hide screen main_hud_icon
    scene hallwayf2 bathroom peek 3 with dissolve
    l_mc "oh damn. If this is a preview of what’s about to come, I’m in for one hell of a show."





    show hallwayf2_bathroom_transparent zorder 1 at right
    show eleanor normal pose20 default with dissolve
    window hide
    pause
    show eleanor normal pose22 default with dissolve
    pause
    hide eleanor normal pose22 default
    show char_eleanor_suitalt_undressing5_alt with dissolve
    pause
    hide char_eleanor_suitalt_undressing5_alt
    show eleanor normal pose16 default with dissolve
    l_mc "Look at those tits . ."


    show eleanor normal pose17 default with dissolve
    pause
    hide eleanor normal pose17
    show char_eleanor_suitalt_skirt3 with dissolve
    pause
    hide char_eleanor_suitalt_skirt3
    show eleanor normal pose32 default with dissolve
    pause
    show eleanor normal pose38 default with dissolve
    pause
    hide eleanor normal pose38 default with dissolve
    show eleanor normal pose39 default with dissolve
    pause
    hide eleanor normal pose39 default with dissolve
    show eleanor normal pose40 default with dissolve
    pause
    hide eleanor normal pose40 default
    show char_eleanor_undieshalf_undressing8 with dissolve
    pause
    hide char_eleanor_undieshalf_undressing8
    show eleanor normal pose41 default with dissolve
    pause

    l_mc "she’s going into the shower now. I better go back to the closet and get a better angle of the show."
    l_mc "Let me just drop her clothe here"
    $ inv.remove(item_spareoutfit)
    $ eleanor_story += 1


    scene black with dissolve
    pause
    scene event_peephole_2 with dissolve
    pause

    l_mc "Alright here we go."
    l_mc "at long last. If this doesn’t get me to stop thinking about my [sadie_relationship_input] as an attractive woman, then I don’t know what will."
    scene peephole_pov5 with dissolve
    show peephole_pov5_overlay zorder 1
    show showerposing_eleanor_pose 1 at center with dissolve
    play music "music/audio_shower_01.mp3"
    l_mc "God dayum!"
    l_mc "Welp now’s a good time to start fapping if there ever was one."
    show showerposing_eleanor_pose 2 with dissolve
    pause
    show showerposing_eleanor_pose 3 at position_align_1 with dissolve
    pause
    hide showerposing_eleanor_pose with dissolve
    window hide
    show eleanor_showerass_anim
    $ eleanor_gallery_1_unlocked = True
    $ renpy.notify("Eleanor video 1 unlocked")
    jump eleanor_shower_navigation




label eleanor_shower_dialogue1:

    scene black
    pause
    scene peephole_pov5 with dissolve
    show peephole_pov5_overlay zorder 1
    show showerposing_eleanor_pose 1 at center with dissolve
    play music "music/audio_shower_01.mp3"
    l_mc "God dayum!"
    l_mc "Welp now’s a good time to start fapping if there ever was one."
    show showerposing_eleanor_pose 2 with dissolve
    pause
    show showerposing_eleanor_pose 3 at position_align_1 with dissolve
    pause
    hide showerposing_eleanor_pose with dissolve
    window hide
    show eleanor_showerass_anim
    jump eleanor_shower_navigation1


label eleanor_shower_navigation1:
    hide screen main_hud_icon
    show screen eleanor_shower_animdonebtn
    if _return == "eleanor_shower_btn_ass1":
        if ele_shower_ass_seen == False:
            $ ele_shower_ass_seen = True

        hide eleanor_showerpussy_anim
        show eleanor_showerass_anim

    if _return == "eleanor_shower_btn_pussy1":
        if ele_shower_front_seen == False:
            $ ele_shower_front_seen = True

        hide eleanor_showerass_anim
        show eleanor_showerpussy_anim

    call screen eleanor_shower_asspussy_interactive1(current=_return)
    jump eleanor_shower_navigation1


screen eleanor_shower_animdonebtn():
    if ele_shower_ass_seen == True and ele_shower_front_seen == True:
        imagebutton:
            action Play("music", "music/Elbe.mp3"), Hide("eleanor_shower_animdonebtn"),Jump("goto_lucaspc")
            idle "animbutton_done"
            mouse "interaction_m"
            xalign 0.94
            yalign 0.2



screen eleanor_shower_asspussy_interactive1(current=""):

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("eleanor_shower_btn_ass1" if current == "eleanor_shower_btn_pussy1" else "eleanor_shower_btn_pussy1")
            idle ("animbutton_pose1" if current == "eleanor_shower_btn_pussy1" else "animbutton_pose2")
            mouse "interaction_m"
            xalign 0.94
            yalign 0.4
    else:
        imagebutton:
            action Return("eleanor_shower_btn_ass1")
            idle "animbutton_pose1"
            mouse "interaction_m"
            xalign 0.94
            yalign 0.4

        imagebutton:
            action Return("eleanor_shower_btn_pussy1")
            idle "animbutton_pose2"
            mouse "interaction_m"
            xalign 0.94
            yalign 0.6

label eleanor_vid1_bck:
    call set_location ("loc_lucaspc") from _call_set_location_23
    jump goto_lucaspc
    return

label eleanor_third_session_bath2_1:
    stop music fadeout 1.0

    play music "music/music4.mp3"
    scene black with dissolve
    pause
    l_mc "well that was something else. I’m never forgetting that view, it’s now burned into soul."
    l_mc "but I should go to my room quickly and wait for her there before she gets out the shower."
    jump goto_lucasroom
    return

label eleanor_shower_navigation:
    hide screen main_hud_icon
    show screen eleanor_shower_animdonebtn1
    if _return == "eleanor_shower_btn_ass1":
        if ele_shower_ass_seen1 == False:
            $ ele_shower_ass_seen1 = True

        hide eleanor_showerpussy_anim
        show eleanor_showerass_anim

    elif _return == "eleanor_shower_btn_pussy1":
        if ele_shower_front_seen1 == False:
            $ ele_shower_front_seen1 = True
        hide eleanor_showerass_anim
        show eleanor_showerpussy_anim


    call screen eleanor_shower_asspussy_interactive1(current=_return)
    jump eleanor_shower_navigation

screen eleanor_shower_animdonebtn1():
    if ele_shower_ass_seen1 == True and ele_shower_front_seen1 == True:
        imagebutton:
            action Play("music", "music/Elbe.mp3"), Hide("eleanor_shower_animdonebtn1"), Jump("eleanor_third_session_bath2_1")
            idle "animbutton_done"
            mouse "interaction_m"
            xalign 0.94
            yalign 0.2



screen eleanor_shower_asspussy_interactive1(current=""):

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("eleanor_shower_btn_ass1" if current == "eleanor_shower_btn_pussy1" else "eleanor_shower_btn_pussy1")
            idle ("animbutton_pose1" if current == "eleanor_shower_btn_pussy1" else "animbutton_pose2")
            mouse "interaction_m"
            xalign 0.94
            yalign 0.4
    else:







        imagebutton:
            action Return("eleanor_shower_btn_pussy1")
            idle "animbutton_pose2"
            mouse "interaction_m"
            xalign 0.94
            yalign 0.4




label eleanor_story_third_sessionz:
    hide screen main_hud_icon
    l_mc "I better just act cool, like I didn't just see what I just saw."
    show transition_card 1 with fade
    hide event_bedtime_sadie_01 4
    show custom_text_card "30 Minutes later. . " with dissolve
    pause
    hide custom_text_card with dissolve
    hide transition_card

    show lucas normal pose3 default at left with moveinleft
    show eleanor normal pose26 default at right with moveinright
    pause
    show eleanor normal pose26 glad_talk at right
    l_eleanor "Thanks so much for letting me use your shower."
    l_eleanor "I really needed that"
    show lucas normal pose3 default_talk at left
    show eleanor normal pose26 glad at right
    l_mc "I bet you did, that bird was a real jerk (Thank you bird)."
    show lucas normal pose3 default at left
    show eleanor normal pose27 default_talk at right
    l_eleanor "I've already put my dirty outfit in your washing machine as well , so thanks."
    show lucas normal pose3 default_talk at left
    show eleanor normal pose26 default at right
    l_mc "and you still look good in that outfit as well . . I mean."
    show lucas normal pose3 mkay at left
    l_mc "(God dammit! What is it about her that makes me keep spouting things out loud)?"
    show lucas normal pose3 default at left
    show eleanor normal pose28 default_talk at right
    l_eleanor "Well, I suppose I’ll let you flatter me this time but we should get back to your tutoring now Lucas. We’ve already wasted enough time."
    show lucas normal pose3 default_talk at left
    show eleanor normal pose26 default at right
    l_mc "Right, just settle yourself in and I'll be with you in a minute"
    show lucas normal pose3 default at left
    show eleanor normal pose26 default_talk at right
    l_eleanor "I'll be waiting."
    hide lucas normal pose3 default with moveoutleft
    hide eleanor normal pose26 default_talk with moveoutright
    $ eleanor_story += 1
    jump goto_lucasroom
    return

label eleanor_teaching_event3:
    menu:
        "Ready ?" if True:
            jump eleanor_teaching_event3z
        "Not yet" if True:
            jump goto_lucasroom
            return

label eleanor_teaching_event3z:
    while True:
        hide screen main_hud_icon
        call quicktime_minigame () from _call_quicktime_minigame_2
        if minigame_success:
            $ eleanor_story += 1

            jump goto_lucasroom
            return
        "Try again. . ."


label eleanor_closet_peek1:

    scene event_peephole_1 with dissolve
    l_mc "What's this? I can see some shimmer of light coming out from behind the closet."
    scene event_peephole_2 with dissolve
    l_mc "Is this what I think it is? Only one way to find out."
    scene peephole_pov4 with dissolve
    show peephole_pov5_overlay


    l_mc "Oh crap"
    l_mc "I can see the whole damn shower from here."
    l_mc "I feel kind of weird doing this but my body & mind can't help itself."
    l_mc "crap, I better go take this outfit to Eleanor before I forget."
    l_mc "I might just be able to come back here while she’s getting herself clean if I’m quick enough."
    jump goto_sadiecloset
    return




label eleanor_story_third_end:
    hide screen main_hud_icon
    show eleanor normal pose26 default at right with dissolve
    show lucas normal pose4 default at left with dissolve
    pause
    show eleanor normal pose26 default_talk at right
    show lucas normal pose4 default at left
    l_eleanor "Great work today Lucas."
    l_eleanor "That was easy work today."
    show eleanor normal pose26 default at right
    show lucas normal pose4 default_talk at left
    l_mc "Yeah, it was child's play today."
    show eleanor normal pose25 pain_talk at right
    show lucas normal pose4 default at left
    l_eleanor "and I didn't have much back and neck pain to hold me back from teaching properly today."
    show eleanor normal pose25 pain at right
    show lucas normal pose4 mkay at left
    l_mc "(Must be those massive puppers she's carrying around that's hurting her so much)."
    show eleanor normal pose26 pain at right
    show lucas normal pose4 assured_talk at left
    l_mc "You must be in a lot of pain"
    show eleanor normal pose26 default at right
    l_mc "don’t you have someone special at home that can help you with the pain? Like a nice massage."
    show eleanor normal pose26 down_talk at right
    show lucas normal pose4 default at left
    l_eleanor "no one has cared for me in while so no massage therapy unless I pay for it unfortunately."
    show eleanor normal pose26 down at right
    show lucas normal pose4 default_talk at left
    l_mc "you can’t be serious. Someone like you must have a special person waiting at home for you?"
    show eleanor normal pose26 down_talk at right
    show lucas normal pose4 default at left
    l_eleanor "well not really. I’ve been by myself for a long time now. Its been ages since I’ve. . ."

    show eleanor normal pose26 puzzled_talk at right
    l_eleanor "Wait, why am I telling you this ?"
    l_eleanor "it's really none of your concern Lucas."
    show eleanor normal pose26 default_talk at right
    l_eleanor "Don't worry about my social problems. You just worry about yourself."
    show eleanor normal pose26 puzzled at right
    l_eleanor "(was I really about to tell him how lonely I am? What was I thinking?)"
    show eleanor normal pose26 default at right
    show lucas normal pose4 mkay_talk at left
    l_mc "I didn’t mean to intrude. I was just a little worried, that’s all."
    show eleanor normal pose29 mouth_cover glad at right
    show lucas normal pose4 mkay at left
    l_eleanor "(He’s worried about me? Why would he be. None of my students at school ever seem to be concerned with my well-being.)"
    show eleanor normal pose26 none puzzled at right
    show lucas normal pose4 default_talk at left
    l_mc "I’ll stop asking. Sorry to bother"
    show eleanor normal pose26 default_talk at right
    show lucas normal pose4 default at left
    l_eleanor "No lucas, It's fine"
    l_eleanor "I’m just not used to people worrying about me, is all. No less by a student."
    l_eleanor "I should be sorry for being a bit hard sometimes. I know everybody at school sees me as their grumpy teacher"
    show eleanor normal pose27 default_talk at right
    l_eleanor "you must be thinking the same way and I don’t blame you."
    show eleanor normal pose26 default at right
    show lucas normal pose4 puzzle_talk at left
    l_mc "what are you talking about? I don’t see you as a grumpy old teacher in any way."
    show lucas normal pose4 default_talk at left
    l_mc "maybe a little strict but I know it’s only because you care about teaching seriously."
    show lucas normal pose4 glad_talk at left
    l_mc "you're the brightest person in the entire school among all the others."
    l_mc "Always looking out for people in your own ways. Just like you’re doing for me."
    l_mc "You may be a little straight forward sometimes but here you are still. No other teacher would’ve done the same for me but you."

    show eleanor normal pose26 down_talk blush at right
    show lucas normal pose4 glad at left
    l_eleanor "Lucas . . ."
    show eleanor normal pose26 down blush at right
    show lucas normal pose4 glad_talk at left
    l_mc "you’re a good person."
    l_mc "so, don’t worry about what others think."
    show eleanor normal pose26 default blush at right
    show lucas normal pose13 mkay at left
    l_mc "(aaaand again, I’ve said too much. I keep compromising myself too much around her)"
    show eleanor normal pose26 puzzled blush at right
    l_eleanor "(This boy, what is he saying all of a sudden. Does he really see me like that?)"
    show eleanor normal pose26 default none at right
    show lucas normal pose4 default_talk at left
    l_mc "I think I talked too much. I’ll just let you leave now. I’m sure you still have a lot of things to do."
    show eleanor normal pose26 default_talk none at right
    show lucas normal pose4 default at left
    l_eleanor "to think that it would be you to uplift me today of all people."
    l_eleanor "the one who assaulted another student for me."
    show eleanor normal pose26 glad_talk none at right
    l_eleanor "I appreciate that Lucas. I really do."
    show eleanor normal pose28 glad_talk none at right
    l_eleanor "you have no idea how much those words mean to me."
    show eleanor normal pose26 default none at right
    show lucas normal pose4 default_talk at left

    l_mc "Yeah, no sweat"
    show eleanor normal pose26 default_talk none at right
    show lucas normal pose4 default at left
    l_eleanor "I’m just going to go retrieve my clean outfit from downstairs now and leave. It should be ready by now."
    show eleanor normal pose26 default none at right
    show lucas normal pose4 default_talk at left
    l_mc "keep the spare outfit for now. You can just return it next time you come over"
    show eleanor normal pose26 default_talk none at right
    show lucas normal pose4 default at left
    l_eleanor "Thanks, you keep in touch"
    show eleanor normal pose26 default none at right
    show lucas normal pose4 default_talk at left
    l_mc "Bye, I'll text you soon"
    show eleanor normal pose26 default_talk none at right
    show lucas normal pose4 default at left
    l_eleanor "Bye"
    hide eleanor normal pose26 with moveoutright
    hide lucas normal pose4 default with moveoutleft
    $ now.advance()
    $ eleanor_story += 1
    jump goto_lucasroom
    return


label eleanor_fourth_session:
    hide screen main_hud_icon
    show lucas normal default pose4 at left with moveinleft
    show eleanor normal default pose5 at right with moveinright
    pause
    show eleanor normal default_talk pose5
    l_eleanor "Hey, Lucas nice to see you"
    show eleanor normal default pose5
    show lucas normal default_talk pose4
    l_mc "Likewise."
    show lucas normal assured pose5
    l_mc "(She’s glad to see me?)"
    show eleanor normal down_talk pose5
    show lucas normal default pose4
    l_eleanor "and I’ve come with the spare outfit you let me borrow as well."
    show eleanor normal default pose
    show lucas normal default_talk pose38
    l_mc "thanks, I’ll take that"
    show eleanor normal default_talk pose1
    show lucas normal default pose4
    l_eleanor "say, have you seen my bra anywhere. I must have dropped it when I took my clothes home. And now I can’t find it anywhere."
    show eleanor normal default pose
    show lucas normal mkay_talk pose4
    l_mc "uhm, haven’t seen it here but I'll let you know if I do."
    show eleanor normal puzzled_talk pose
    show lucas normal default pose4
    l_eleanor "Please do"
    l_eleanor "I came here hoping you found It. So, the whole day I had nothing to support my . . . my . . .top weight"

    show eleanor normal default blush pose
    pause
    show lucas normal assured pose4
    l_mc "(nothing to support her. Top weight? Has she been walking around at school all day with those things barking everywhere? Must have drove all the other male students crazy)"
    show eleanor normal yawn blush pose
    show lucas normal default pose4
    l_eleanor "now, let’s go upstairs and . . . EEEUUUAAAAHHHHHHH-AAAAAAHHHH"
    show eleanor normal tired none pose
    show lucas normal what pose4
    l_mc "woah there. Tired much?"
    show eleanor normal tired_talk pose
    show lucas normal assured pose4
    l_eleanor "It’s nothing. Don’t worry about me."
    show lucas normal default pose4
    l_eleanor "just been busy with heavy amounts of work all day."
    show eleanor normal yawn pose
    l_eleanor "lets get your tutoring started quickly before I fall aslee . . . Gnawwwwwwww."
    show eleanor normal tired pose
    show lucas normal mkay_talk pose4
    l_mc "yeah you're definitely tired"
    show lucas normal mkay_talk pose4
    l_mc "you know you can just take a break if you’d like. No need to push yourself today"
    show eleanor normal default_talk pose
    show lucas normal default pose4
    l_eleanor "No no. that won’t be necessary. I’m the heaviest sleeper you’ll ever meet."
    l_eleanor "letting me sleep could be dangerous. I may not wake up until tomorrow morning if you do let me fall asleep."
    show eleanor normal default pose
    show lucas normal default_talk pose4
    l_mc "at least, let me make you a cup of coffee"
    l_mc "so, why don’t you head upstairs and I’ll come up in a few minutes with some pick-me-up coffee. How does that sound?"
    show eleanor normal glad_talk pose
    show lucas normal default pose4
    l_eleanor "you're being an angel Lucas. Thanks for this."
    show eleanor normal yawn pose
    l_eleanor "I’ll go wait upstai . . . huuurrrrrrr."
    show eleanor normal tired pose
    show lucas normal default_talk pose4
    l_mc "Yup. See you in a bit."
    hide eleanor normal tired pose with dissolve
    show lucas normal default pose4
    pause
    scene black with dissolve
    "10 minutes later"
    scene bg_kitchen_midnight with dissolve
    show lucas normal default pose36 with dissolve
    " . . ."
    show lucas normal default_talk pose36
    l_mc "Alright, time to go wake her up some more."
    $ eleanor_story += 1
    jump eleanor_event_fourth_bed

label eleanor_event_fourth_bed:
    scene black with dissolve
    hide screen main_hud_icon
    scene bg_bedlucas_alt
    show bg_bedlucas_doorclosed_night
    show char_eleanor_bedroom1_laying1_alt
    l_mc "Hey Eleanor I have your coffee now."
    l_eleanor "ZZZzzzZZzzZ"
    l_mc "Awe damn it! I'm too late"
    scene event_tutoring_4_sleeping with dissolve
    l_mc "I really don’t want to wake her up now. I should just let her sleep."
    l_mc "Other guys at school would kill me if they knew Ms. Eleanor was sleeping on my bed."
    l_mc "She really does look tired."
    l_mc "She deserves to sleep."
    scene event_tutoring_4_frame3_alt with dissolve
    pause
    scene black with dissolve
    scene bg_bedlucas_alt
    show bg_bedlucas_doorclosed_night


    show char_eleanor_bedroom1_laying9_alt with dissolve
    pause
    hide char_eleanor_bedroom1_laying9_alt
    show char_eleanor_bedroom1_laying5_alt with dissolve
    l_mc "Well this is going to make it harder to fall asleep."
    hide char_eleanor_bedroom1_laying5_alt
    show char_eleanor_bedroom1_laying8_alt
    l_mc "I can only try"
    hide char_eleanor_bedroom1_laying8_alt
    show char_eleanor_bedroom1_laying5_alt
    l_mc "So beautiful"
    hide char_eleanor_bedroom1_laying5_alt
    show char_eleanor_bedroom1_laying2_alt
    window hide
    pause
    $ daytime = "midnight"
    scene black with dissolve
    pause
    scene event_tutoring_4_sleeping_pov
    show pov_blur_1 zorder 1
    l_mc "(hu? I feel warm)"
    hide pov_blur_1
    show pov_blur_2 zorder 1
    l_mc "(my whole body is covered and warm. Better than blankets)"
    hide pov_blur_2 with dissolve
    l_mc "(Ms. Eleanor!? Oh shit, not again. Last time I was in this situation with [sadie_refer_input] I barely got away clean.)"
    l_mc "(Why is this happening again?)"
    l_mc "(So close though and she smells so nice)"
    l_mc "(She did say she was a heavy sleeper so I’m sure she won’t wake up if I just stay a little longer, right?)"
    l_mc "(my god, she’s not wearing a bra. I can see through her shirt pretty clearly.)"
    l_mc "(maybe I can go just a little further without her waking up)"
    l_mc "(Screw this. I can’t hold back anymore.)"
    l_mc "(This may be a way to forget about [sadie_refer_input] in a lewd manner for good.)"
    l_mc "(I’ve been in this situation before so maybe this time I can go further with Ms. Eleanor and see what happens.)"
    l_mc "(I’ll Just have to make sure she doesn’t wake up.)"
    l_mc "(at least she’s a heavy sleeper I might as well take a shot)"
    scene black with dissolve
    play sound "music/audio_zipper_01.wav"
    pause
    play sound "music/audio_clothbrushing_01.wav"
    pause
    scene eleanor_thighgrind2_anim
    jump eleanor_bedgrind_navigation



label eleanor_bedgrind_navigation:
    if _return == "eleanor_bedgrind_ass":
        hide eleanor_thighgrind_anim
        scene eleanor_thighgrind2_anim
        l_mc "(this is incredible)"

    elif _return == "eleanor_bedgrind_top":
        hide eleanor_thighgrind2_anim
        scene eleanor_thighgrind_anim
        l_mc "(I can’t stop my hips anymore)"

    call screen eleanor_bedgrind_asstop_interactive1(current=_return)
    jump eleanor_bedgrind_navigation




screen eleanor_bedgrind_asstop_interactive1(current=""):

    imagebutton:
        action Jump("eleanor_bedgrind_end")
        idle "animbutton_bust"
        mouse "interaction_m"
        xalign 0.99
        yalign 0.94

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("eleanor_bedgrind_ass" if current == "eleanor_bedgrind_top" else "eleanor_bedgrind_top")
            idle ("animbutton_camera1" if current == "eleanor_bedgrind_top" else "animbutton_camera2")
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94
    else:
        imagebutton:
            action Return("eleanor_bedgrind_ass")
            idle "animbutton_camera1"
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94































label eleanor_bedgrind_end:
    scene black
    hide eleanor_thighgrind_anim
    hide eleanor_thighgrind2_anim
    scene eleanor_thighgrind_anim2
    l_mc "(Oh damn, I’m about ready to finish.)"
    l_mc "(here it comes!!!)"
    scene white with flash
    scene anim_grinding_eleanor 9
    pause
    scene anim_grinding_eleanor 10
    window hide
    pause
    hide anim_grinding_eleanor 10
    scene anim_grinding_eleanor2 11
    window hide
    pause
    l_mc "(I actually came with my teacher’s thighs. Nobody would ever believe this and even if they did, they would kill me for taking Ms. Eleanor first.)"
    l_mc "(that really took a lot of energy. I’m feeling so relaxed.)"

    $ eleanor_gallery_2_unlocked = True
    $ renpy.notify("Eleanor video 2 unlocked")
    pause
    scene black with dissolve
    scene bg_bedlucas_alt
    show overlay_lucas_elanor_nut zorder 2 at Position(xpos=683, ypos=1050)
    show bg_bedlucas_doorclosed_night


    show char_eleanor_bedroom1_laying3_alt with dissolve
    pause
    show char_eleanor_bedroom1_laying2_alt
    l_mc "(So . . . sleep . . . EEEUUUAAAAHHHHHHH-AAAAAAHHHH"
    pause
    $ now.advance()
    scene black with dissolve
    scene bg_bedlucas
    show bg_bedlucas_doorclosed
    show char_eleanor_bedroom1_laying2
    show overlay_lucas_elanor_nut zorder 2 at Position(xpos=683, ypos=1050)
    pause
    l_eleanor "Lucas?! What are you doing here!?"
    hide char_eleanor_bedroom1_laying2
    show char_eleanor_bedroom1_laying7
    pause
    hide char_eleanor_bedroom1_laying7
    show char_eleanor_bedroom1_laying5
    l_mc "Hmmm? What"
    hide char_eleanor_bedroom1_laying5
    show char_eleanor_bedroom1_laying4
    l_eleanor "Why are you in my bed !?"
    hide char_eleanor_bedroom1_laying4
    show char_eleanor_bedroom1_laying5
    l_mc "Uhm. . "
    hide char_eleanor_bedroom1_laying5
    show char_eleanor_bedroom1_laying6
    l_mc "(Crap I forgot to wake up first)"
    scene black with dissolve
    $ eleanor_story += 1
    jump goto_lucasroom
    return



label eleanor_thigh_grind_video:

    scene black
    play sound "music/audio_zipper_01.wav"
    pause
    play sound "music/audio_clothbrushing_01.wav"
    pause
    scene eleanor_thighgrind2_anim
    jump eleanor_bedgrind_navigation1
    return



label eleanor_bedgrind_navigation1:
    if _return == "eleanor_bedgrind_ass1":
        hide eleanor_thighgrind_anim
        scene eleanor_thighgrind2_anim
        l_mc "(this is incredible)"

    elif _return == "eleanor_bedgrind_top1":
        hide eleanor_thighgrind2_anim
        scene eleanor_thighgrind_anim
        l_mc "(I can’t stop my hips anymore)"

    call screen eleanor_bedgrind_asstop_interactive2(current=_return)
    jump eleanor_bedgrind_navigation1




screen eleanor_bedgrind_asstop_interactive2(current=""):

    imagebutton:
        action Jump("eleanor_bedgrind_end1")
        idle "animbutton_bust"
        mouse "interaction_m"
        xalign 0.99
        yalign 0.94

    if "" != current and isinstance(current, basestring):
        imagebutton:
            action Return("eleanor_bedgrind_ass1" if current == "eleanor_bedgrind_top1" else "eleanor_bedgrind_top1")
            idle ("animbutton_camera1" if current == "eleanor_bedgrind_top1" else "animbutton_camera2")
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94
    else:







        imagebutton:
            action Return("eleanor_bedgrind_top1")
            idle "animbutton_camera2"
            mouse "interaction_m"
            xalign 0.005
            yalign 0.94

label eleanor_bedgrind_end1:
    scene black
    hide eleanor_thighgrind_anim
    hide eleanor_thighgrind2_anim
    scene eleanor_thighgrind_anim2
    l_mc "(Oh damn, I’m about ready to finish.)"
    l_mc "(here it comes!!!)"
    scene white with flash
    scene anim_grinding_eleanor 9
    pause
    scene anim_grinding_eleanor 10
    window hide
    pause
    hide anim_grinding_eleanor 10
    scene anim_grinding_eleanor2 11
    window hide
    pause
    l_mc "(I actually came with my teacher’s thighs. Nobody would ever believe this and even if they did, they would kill me for taking Ms. Eleanor first.)"
    l_mc "(that really took a lot of energy. I’m feeling so relaxed.)"
    jump goto_lucaspc
    return

label eleanor_event_fourth_end:
    hide screen main_hud_icon
    show lucas normal default pose4 at left with Dissolve(0.2)
    show eleanor normal puzzled pose at right with Dissolve(0.2)
    pause
    show lucas normal default_talk head_sweat pose4
    l_mc "Ms. Eleanor, it’s not what It looks like so don’t freak out please.."
    show lucas normal default pose4
    show eleanor normal puzzled_talk pose
    l_eleanor "wait a second, I’m still in your room?"
    show lucas normal default_talk none pose4
    show eleanor normal default pose
    l_mc "Yes, that’s what I’m saying. You're still in my room."
    l_mc "you fell asleep on my bed last night and I couldn’t wake you up so I just let you sleep for the night."
    l_mc "I only slept beside you."
    show lucas normal default pose4
    show eleanor normal default_talk pose
    l_eleanor "oh. . . is that so? I’m so sorry I took your bed"
    show lucas normal default_talk pose4
    show eleanor normal default pose
    l_mc "don’t worry about it. You didn’t bother me much if at all."
    show lucas normal happy_talk pose4
    show eleanor normal default pose
    l_mc "you slept like an angel and only warmed up the bed so you made it easier for me to sleep as well."
    show lucas normal happy pose4
    show eleanor normal glad blush pose
    pause
    show lucas normal happy pose4
    show eleanor normal glad_talk none pose
    l_eleanor "well yes but a teacher still shouldn’t take their student’s bed like I did. It’s inappropriate."
    show eleanor normal default_talk pose2
    l_eleanor "I still need to apologize. I should be the one helping you out but time after time, I’m the one always being helped out instead"
    show lucas normal default_talk pose4
    show eleanor normal default pose
    l_mc "Nonsense, I really can’t thank you enough for everything you're doing."
    l_mc "I’d help you out now and million more times if I had too Ms. Eleanor."
    show lucas normal default_talk pose4
    show eleanor normal default_talk pose
    l_eleanor "that’s enough Lucas."
    show eleanor normal grumpy pose
    show lucas normal what pose4
    l_mc "what?"
    show eleanor normal grumpy_talk pose
    l_eleanor "There's no need to call me by “Ms.” anymore, you can just call me Eleanor from now on."
    show eleanor normal glad pose
    show lucas normal glad_talk pose4
    l_mc "really?"
    show lucas normal assured_talk pose4
    l_mc "but I thought it bothered you."
    l_mc "it’s going to be weird when students just call you “Eleanor” now"
    show eleanor normal default_talk pose
    show lucas normal default pose4
    l_eleanor "not other students Lucas"
    l_eleanor "just you"
    show eleanor normal default pose
    show lucas normal default_talk pose5
    l_mc "just me? you don’t mind?"
    show eleanor normal default_talk pose
    show lucas normal default pose4
    l_eleanor "well as long as we aren’t in school it should be fine"
    show eleanor normal default pose
    show lucas normal mkay_talk pose4
    l_mc "why the sudden change?"
    show eleanor normal down_talk pose
    show lucas normal mkay pose4
    l_eleanor "well you've just been . ."
    show eleanor normal down pose
    show lucas normal default pose4
    show sadie normal pose default at dual_character_position with moveinleft:
        xzoom -1
    pause
    show eleanor normal default pose
    show sadie normal default_talk
    l_sadie "Ms. Eleanor? What are you doing here?"
    l_sadie "It’s no wonder I never saw you leave the house last night"
    show sadie normal grump_talk pose1
    l_sadie "what’s going on here?"
    show sadie normal grumpy pose
    show lucas normal puzzle_talk pose4
    l_mc "It’s a misunderstanding. She just fell asleep here from so much exhaustion last night. I didn’t want to disturb her so I just let her be"
    show sadie normal default
    show lucas normal puzzle pose4
    show eleanor normal down_talk pose
    l_eleanor "it’s just as Lucas says. It’s my fault and I’m sorry for causing trouble here"
    show eleanor normal glad_talk pose
    l_eleanor "but Lucas was such gentlemen and even slept on his couch over there all by himself. That’s all that happened."
    show eleanor normal glad pose
    show lucas normal puzzle pose4
    l_mc "(she’s lying for me? She doesn’t want [sadie_refer_input] know we slept in the same bed.)"
    show eleanor normal default pose
    show lucas normal default pose4
    show sadie normal default_talk
    l_sadie "Oh really? Sorry for misconstruing the information."
    l_sadie "you’ve been working so hard with teaching at school and then helping Lucas out as well."
    show sadie normal sad_talk
    l_sadie "we must have been draining all your energy."
    show sadie normal sad
    show eleanor normal default_talk pose1
    l_eleanor "It’s my job to help out students as best I can. Especially my most caring ones."
    show sadie normal default_talk
    show eleanor normal default pose
    show lucas normal default pose4

    l_sadie "Well if you ever find yourself completely exhausted again, please don’t be afraid to spend the night here again."
    show sadie normal sad_talk pose
    l_sadie "I’d hate to see you so tired after all the help you’ve been giving."
    l_sadie "and you drive around so much from your home to school and then here."
    l_sadie "why don’t you just spend the night over from now on when if you come here so late at night"
    show sadie normal default_talk pose
    l_sadie "It’s only me and Lucas in the house so you won’t be a bother to anybody."
    show sadie normal default pose
    show eleanor normal default_talk pose1
    l_eleanor "I really appreciate the offer but wouldn’t I just be taking up your beds?"
    show eleanor normal default pose
    show lucas normal default_talk pose4
    l_mc "not a problem. I can just sleep on my couch again."
    show lucas normal default pose4
    show sadie normal default_talk pose
    l_sadie "or he can even come sleep in my room while you sleep in his."
    show lucas normal assured pose4
    show sadie normal default pose
    l_mc "(I can sleep in her room?)"
    show lucas normal default pose4
    show sadie normal happy_talk pose
    l_sadie "we can figure out the sleeping arrangements later."
    l_sadie "you can even borrow some pajamas or whatever you may need from me."
    show sadie normal happy pose
    show eleanor normal glad_talk pose
    l_eleanor "well thanks so much for the support from the both of you."
    show eleanor normal glad pose
    l_eleanor "(I better get going now. I’ll see you two again and make sure to take you up on your offer if I come tutoring at night)"
    show lucas normal default_talk pose4
    l_mc "anytime. I’ll catch you again soon Eleanor"
    show eleanor normal glad_talk pose
    show lucas normal default pose4
    l_eleanor "yes Lucas, thanks for letting me stay again. I’ll catch you around"
    show eleanor normal default pose
    show sadie normal grumpy pose
    l_sadie "(Did he just call her only by her name?)"
    pause
    show eleanor normal default_talk pose
    l_eleanor "and goodbye Sadie"
    show sadie normal default_talk pose
    l_sadie "I’ll walk you."
    show sadie normal default_talk pose
    l_sadie "and make sure to clean your room Lucas"
    show sadie normal default pose
    show lucas normal default_talk pose4
    l_mc "yeah sure."
    show lucas normal assured pose4
    hide sadie normal default pose with moveoutleft
    hide eleanor normal default pose with moveoutright
    pause

    show lucas normal assured_talk pose4
    l_mc "I can’t believe, she’s even letting me call her by just her name. of all her students why is she letting me? She’s always been real stern about her teacher title."

    l_mc "and now there's a possibility that she could start spending the nights over in my room while I take my couch or sleep in [sadie_refer_input]'s room. I wonder where she expects me to sleep in her room though?"
    show lucas normal what pose4
    l_mc "that was one hell of a night I’ll be sure to never forget."
    show lucas normal default pose4
    hide lucas normal default pose4 with moveoutleft
    $ eleanor_story += 1
    jump goto_lucasroom
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

label sadie_movie_7night:
    hide screen main_hud_icon
    hide screen my_invisible_choice   
    scene movienight_bg_night
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "Alright [sadie_refer_input], you ready ?"
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "Yes, and I promise not to fall asleep again."
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "Ok, just give me a second to find the right movie."
    l_mc "Ok, let’s go with a scary movie."
    show sadie_lucas_def night_tv_alt default grumpyt
    l_sadie "Noooo, you know I don’t do good with horror, baby."
    show sadie_lucas_def night_tv_alt glad_talk grumpyz
    l_mc "Come on, you’ll like this one."
    show sadie_lucas_def night_tv_alt glad grumpyt
    l_sadie "No! We can do your scary movie next time."
    show sadie_lucas_def night_tv_alt default assured_t
    l_sadie "Can we just go with a comedy tonight? I just want something funny."
    show sadie_lucas_def night_tv_alt puzzled assured
    l_mc "Fiiiine. You’ll get your way. I’ll choose a funny movie."
    show sadie_lucas_def night_tv_alt

    jump tv_scene_show
    pause

label sadie_movie_7nightz:
    scene back_display1 with dissolve
    show transition_card 1 with fade
    show custom_text_card "1 Hour Later" with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve
    scene movienight_bg_night
    show sadie_lucas_def night_tv_alt default awe_t
    stop music
    l_sadie "So, how are you holding up with your whole school situation?"
    show sadie_lucas_def night_tv_alt head9 awe
    l_mc "*Sigh* I dunno. Sometimes I try not to think about it. It’s still pretty hard to take it that I’ll have to repeat a whole school year and fall behind everybody else."
    show sadie_lucas_def night_tv_alt mkay sad_talk

    l_sadie "I’m sorry dear. We don’t have to talk about it if you don’t want to."
    show sadie_lucas_def night_tv_alt glad_talk defaultz
    l_mc "Now I’ll have to spend another year here with you instead of being at college by myself. A damn shame I say."
    show sadie_lucas_def night_tv_alt glad grumpyt
    l_sadie "“A damn shame”. What do you mean by that?"
    show sadie_lucas_def night_tv_alt head20 grumpyz
    l_mc "What?"
    show sadie_lucas_def night_tv_alt head19 grumpyt
    l_sadie "Is it so bad to be around your [sadie_relationship_input]? I guess I didn’t realize I was being such a bother."
    l_sadie "Excuse me for being such a caring [sadie_relationship_input]."
    show sadie_lucas_def night_tv_alt glad_talk grumpyz
    l_mc "[sadie_refer_input]."
    show sadie_lucas_def night_tv_alt glad grumpyt
    l_sadie "What?"
    show sadie_lucas_def night_tv_alt happy_t grumpyz
    l_mc "I’m kidding."
    show sadie_lucas_def night_tv_alt happy1 assured_t
    l_sadie "Mhhmm. Right."
    show sadie_lucas_def night_tv_alt happy_t assured
    l_mc "I’m serious. I was only joking with you. I love being around you."
    show sadie_lucas_def night_tv_alt glad_talk defaultz
    l_mc "Although you have to admit, I did get you pretty good."
    show sadie_lucas_def night_tv_alt glad sure_talk
    l_sadie "Ok ok, don’t worry. I’ll get you back boy. Mark my words, one way or another."
    show sadie_lucas_def night_tv_alt glad_talk defaultz
    l_mc "shh. Back to the movie, a good part is coming up."




    show transition_card 1 with fade
    show custom_text_card "An hour passes by " with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve
    scene movienight_bg_night
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "That was pretty funny. We need to watch the sequel now."
    show sadie_lucas_def night_tv_alt head20 awe
    l_mc "That’s a big no. nothing compared to the first one. They don’t even have the same actor, Jimmy Carrey as the main protagonist. Total waste of time."
    show sadie_lucas_def night_tv_alt blank awe_t
    l_sadie "Well, we can watch that horror movie you really wanted to but next time."

    show sadie_lucas_def night_tv_alt cocky_t awe
    l_mc "Awesome. You won’t be disappointed, and you’ll have me with you so it won’t be as scary"
    show sadie_lucas_def night_tv_alt default assured_t
    l_sadie "That’s what you said last time we watched a horror movie but ok."
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "And I also wanted to ask you something."
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "Ask what?"
    show sadie_lucas_def night_tv_alt default smirk_t
    l_sadie "Could you be my yoga partner for a day? I’ve really needed some company since I have no one to do yoga with. It could be a lot of fun. What do you say?"

    show sadie_lucas_def night_tv_alt head20 happy
    l_mc "You know I really do want to spend more time with you but I can barely do a split to save my life"

    show sadie_lucas_def night_tv_alt head19 default_t
    l_sadie "Come on, it’s not like you have anything better to do since you got yourself suspended from school."

    show sadie_lucas_def night_tv_alt mkay_talk defaultz
    l_mc "Ouch, that hurt but if you really want me to help you out with yoga, I’ll do it."

    show sadie_lucas_def night_tv_alt mkay smirk_t
    l_sadie "Yes! You make me so happy, give into my demand’s boy!"

    show sadie_lucas_def night_tv_alt puzzled happy
    l_mc "Yeah whatever, when do you want to yoga it up?"

    show sadie_lucas_def night_tv_alt blank smirk_t
    l_sadie "It’s too late now to do it but we can do it together."

    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "Just make sure to come and visit me at the Balcony during the day. I’ll always be there. "

    show sadie_lucas_def night_tv_alt default smirk_t
    l_sadie "Ditch me and I’ll never talk to you again."

    show sadie_lucas_def night_tv_alt glad_talk defaultz
    l_mc "Ight, I’ll be there, pinky swear."

    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "Ok already, let’s both go to bed now. It’s getting really late now."

    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "Sweet dreams, I’ll see you at the Balcony. "

    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "Goodnight, dear. "

    $ sadie_story += 1
    $ sadie_night_couch_watching = True
    $ now.advance()

    play music "music/music4.mp3"
    show screen journal_updated_notify with dissolve
    $ renpy.scene()
    jump goto_livingf1
    return


label sadie_movie_8night:
    scene movienight_bg_night
    show sadie_lucas_def night_tv_alt default defaultz
    pause
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "Ok, [sadie_refer_input]. you know what time it is."
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "Yeah yeah."
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "Spooky night!"
    show sadie_lucas_def night_tv_alt default grumpyt
    l_sadie "Just start already will yeah. Let’s get this over with."
    l_sadie "Put that scary movie on that you wanted to."
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "And I better not hear you complain if I squeeze you too tightly."
    show sadie_lucas_def night_tv_alt default defaultz

    jump tv_scene_show
    return

label sadie_movie_8nightz:
    scene movienight_bg_night
    show sadie_lucas_def night_tv_alt default defaultz
    pause
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "This is what I’m talking about. "
    l_mc "You’ll like this one. "
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "If you say so."
    show sadie_lucas_def night_tv_alt default defaultz
    show transition_card 1 with fade
    show custom_text_card "1 Hour later. ." with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve
    show sadie_lucas_def night_tv_alt default assured_t
    l_sadie "I don’t know about this Lucas; this is really scary."
    l_sadie "I don’t know how you can watch these things."
    show sadie_lucas_def night_tv_alt mkay_talk assured
    l_mc "That’s the point. You have to get scared. I’m here with you anyways so you’ll be fine."
    show sadie_lucas_def night_tv_alt mkay default_t
    l_sadie "And what about when the movie is over and I have to go to sleep?"
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "You still get scared that badly huh? You haven’t changed."
    l_mc "Just keep watching. Some scary parts are coming up."
    show transition_card 1 with fade
    show sadie_lucas_def night_tv_alt default default
    show custom_text_card "One more hour later . ." with dissolve
    pause
    hide transition_card
    hide custom_text_card with dissolve
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "I’m glad that’s over."
    show sadie_lucas_def night_tv_alt grumpy_talk defaultz
    l_mc "Awe come on; it wasn’t that bad. The sequel is much scarier anyways."
    show sadie_lucas_def night_tv_alt grumpy assured_t
    l_sadie "How am I going to sleep after that? I’ll probably have nightmares."
    show sadie_lucas_def night_tv_alt mkay assured
    l_mc "(She’s still such a baby with these things.)"
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "I wouldn’t mind if you came to sleep with me tonight sweetie?"
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "What do you mean? Don’t be silly [sadie_refer_input]. Are you really that terrified?"
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "I told you, did I not? “I do not do horror”. I also told you to not complain If I get too scared"
    show sadie_lucas_def night_tv_alt mkay defaultz
    l_mc "(But she’s the one complaining.)"
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "So, take responsibility and sleep with me tonight."
    show sadie_lucas_def night_tv_alt defaultt defaultz
    l_mc "[sadie_refer_input], you can’t be serious. Maybe I used to do it when I was younger but I’m older now. "
    show sadie_lucas_def night_tv_alt default default_t
    l_sadie "I don’t care. You're still by little boy as long as you live under my roof."
    l_sadie "But if you really don’t care about your [sadie_relationship_input] so much than sleep in your own room and leave me all by myself."
    show sadie_lucas_def night_tv_alt blank defaultz
    l_mc "(Is she trying to make me feel bad?)"
    show sadie_lucas_def night_tv_alt cocky_t defaultz
    l_mc "Fine! I’ll sleep with you. Just for one night though, that should be enough to get your fears over with."
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "Yaaay! I knew you cared about me."
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "Yeah whatever."
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "You used to crawl into my bed to sleep with me all the time. This isn’t so different honey. I just miss those moments. It always made me happy to feel your warmth. "
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "You got what you wanted. I’m going to leave now but I’ll go to your bedroom at night."
    show sadie_lucas_def night_tv_alt default awe_t
    l_sadie "Ok honey, I’ll be waiting. "
    l_sadie "I love you baby."
    show sadie_lucas_def night_tv_alt defaultt awe
    l_mc "Love you too."
    show sadie_lucas_def night_tv_alt default awe
    $ sadie_info_2 = True

    show black with dissolve
    $ sadie_story += 1
    $ sadiecouch_talking = False
    $ now.advance()
    $ exit_btn = True
    show screen journal_updated_notify with dissolve
    $ renpy.scene()
    jump goto_livingf1
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

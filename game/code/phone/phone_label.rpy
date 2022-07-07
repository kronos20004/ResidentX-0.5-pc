

























label eleanor_convo_1():
    e "Hey Lucas, are you ready to begin our private tutoring sessions ?"
    mc "Wait what? when?"
    e "I'm available at tuesday or thursday during the evening."
    e "So I will come around those days"
    e "Be prepared and ready"
    mc "Ah yes, sure"
    mc "I'll open the door when you are here"
    e "Ok lucas, see you soon !"

    $ eleanor_story += 1








    return

label eleanor_convo_2():
    e "You should be able to start your module now"
    e "I completely forgot to assign the quiz into the module"
    e "Finish it as soon as possible !"
    $ eleanor_story += 1
    return


label eleanor_convo_3():
    mc "Hey, I completed the module again"
    e "Great !, I'll be there during the morning "
    e "See you then"
    mc "Ok"
    $ eleanor_story += 1
    return

label eleanor_convo_4():
    e "hey Lucas?"
    mc " yeah, what’s up Eleanor?"
    e "I’m still missing my bra I lost at your house."
    e "have you had any luck finding it?"
    mc "No not yet. I haven’t been looking sorry"
    mc "I’ll start looking now"
    mc "but I’m not sure what it looks like. I could confuse it for one of my [sadie_relationship_input]'s bras."
    mc "how will I know what to look for?"
    e "I guess you're right well. . ."
    e "I suppose I can send you an old picture I took for reference"
    mc "picture?"
    e "yes, but you must promise me you will delete it right away afterwards."
    e "can you promise me that?"
    mc "of course Eleanor. I’ll do whatever you say"
    e "thank you Lucas"
    e "sext_eleanor_01" (img=True)

    mc " Woah, got it crystal clear now Eleanor. I’ll be deleting this now."
    e "thanks. Would be embarrassing if that got out"
    mc "now, is there any place you think you could have dropped it?"
    e "nothing that comes to mind. I just remember grabbing all my stuff in a rush that day and leaving"
    e "So, I must’ve dropped it in or near the laundry room maybe."
    mc "Ok I’ll make sure too take a look. I’ll let you know if I find it"
    e "thanks Lucas, keep in touch"
    mc "Will do"
    $ eleanor_story += 1
    return


label konami_convo_1():
    mc "Hey konami, you still awake ?"
    k "Hey Lucas, I'm still up"
    mc "just wanted to know when you want to hang out?"
    k "we really are hanging out?"
    mc "Yeah, are we not ?"
    mc "so when and where?"
    k "How about just the treehouse for now? I’m more comfortable there for now"
    mc "more comfortable ?"
    mc "you an introvert as well?"
    k "well, if that’s how you want to put it >:("
    k "if you’re just going to keep making fun of me, I’m not sure I should hang out with you"
    mc "Relax, that was just light banter"
    mc "Tree house is cool, I don't mind at all"
    k "Ok then"
    k "I guess we get to hangout and know about each other"
    k "Bailey never really mentioned you or cared to introduce us"
    mc "I'm not suprised at all"
    mc "that’s the usual Bailey I grew up with. Always overprotective of me"
    mc "Super clingy as well"
    mc "Let's just say she is super sensitive"
    mc "Since she isn't around, atleast I got to know she had a friend"
    k "I had no idea she was super sentitive about you"
    mc "When do you want to meet at the treehouse?"
    k "I’ll be there a few nights. Even if you don’t show up, I like to catch some fresh air up there and read sometimes."
    mc "how come I never noticed? I really need to go up there more often."
    mc "Sounds good, I'll see you then"
    mc "It's pretty late now, I might aswell head to sleep"
    mc "Good night konami"
    k "Goodnight !"
    $ konami_story += 1
    return

label konami_convo_2():
    k "Going to be at the treehouse during the day if you want to come over"
    mc "Sure, I might stop by and see what's up"
    k "k, I'll be there."
    $ konami_story += 1
    return

label konami_convo_3():
    k "Hey, can I use your pool ?"
    mc "My pool? That’s pretty random but sure, fine by me."
    mc "I’ll just tell my [sadie_relationship_input] you’ll be over so she won’t freak out"
    k "would she mind?"
    mc "Nope, you're all good so go ahead whenever you want"
    k "K thanks!"
    k "I’ll probably be there during the weekend, Saturday or Sunday "
    mc "sounds good, I’ll stop by"
    $ konami_story += 1
    return

label konami_convo_4():
    mc "Hey I got the mangas you like. Can I come over to drop them off?"
    k "Yes. Come over during the afternoon."
    mc "And your mother won’t mind?"
    k "She doesn’t come home from work till late so you’ll be fine."
    mc "So, she would mind . . . -_-"
    k "It’s fine, just make sure to come in through the same hole in the fence that I do."
    k "And knock on my back door. Only during the afternoon."
    mc "Alright. I’ll be there."
    $ konami_entrance_access = True
    return

label konami_convo_5():
    k "Hey, sorry about the other day with my mom."
    mc "It’s fine, things happen."
    k "I better Lay low though."
    k "Thankfully, my mom still doesn’t know who you are."
    mc "Thank God."
    k "I’ll probably come back to the treehouse on the weekdays since it might be a bit risky to hang out at my place."
    mc "Ok, I guess it’s the only way."
    mc "I’ll eventually come over and find you there than."
    k "I’ll be there."
    k "Gotta go my mom is coming, bye."
    mc "Back to the treehouse. Great."
    $ konami_story += 1
    return

label konami_convo_6():
    k "Lucas"
    k "Can you come over to my house again?"
    mc "but your mom?"
    k "don’t worry, she won’t be here this time."
    k "just come at the same time as last time."
    k "I’ll leave the door unlocked so just walk in and come to my bedroom."
    k "Bye."
    mc "suuuuure. Bye"
    $ konami_story += 1
    hide phone_contacts
    jump konami_phoneshort_event5
    return

label konami_convo_7():
    mc "Hey, thanks for what you did."
    k "I wanted to do it anyways."
    k "But this time we really better lay low."
    k "My mom is super determined to find you. I don’t think you’ll get away next time if she sees you. "
    mc "Really!? But I want to see you again. "
    k "Me too, but it’s for the best. Probably won’t be able to see you for a while Lucas."
    k "I’ll let you know when the coast looks clear."
    mc "Mkay. I hope I do see you sooner rather than later. "
    mc "I'll see you around"
    k "Bye Lucas."
    mc "Bye."
    jump konami_phoneshort_event5z
    return



label quickies_convo_1():
    q "Your packages Has arrived at your doorstep."
    return

label quickies_convo_2():
    q "Your packages Has arrived at your doorstep."
    return

label quickies_convo_3():
    q "Your packages Has arrived at your doorstep."
    return

label quickies_convo_4():
    q "Your packages Has arrived at your doorstep."
    return

label quickies_convo_5():
    q "Your packages Has arrived at your doorstep."
    return

label quickies_convo_6():
    q "Your packages Has arrived at your doorstep."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

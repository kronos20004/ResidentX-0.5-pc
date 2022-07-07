init -5 python:

    def check_for_conversations():
        """
        A function which runs every time Ren'Py executes Python in script.
        Used to detect when conversations should become available and a
        notification should be shown to the player.

        Result:
        --------
            If a points threshold is reached, adds the corresponding label to
            the associated ChatCharacter to make that label available to jump
            to the next time the player selects that contact from the list.
        """
        
        
        
        if hasattr(store, 'point_thresholds'):
            point_thresholds = store.point_thresholds
            for key in point_thresholds.keys():
                if not hasattr(store, key):
                    return
        else:
            
            return
        
        try:
            
            
            for var, values in point_thresholds.items():
                points = getattr(store, var)
                
                for i in range(0, len(values), 2):
                    thresh = values[i]
                    lbl = values[i+1]
                    if points >= thresh:
                        
                        if lbl not in store.unlocked_phone_convos:
                            store.unlocked_phone_convos.add(lbl)
                            
                            who = store.points_dict[var]
                            who.label_list.append(lbl)
                            
                            
                            
                            renpy.show_screen('item_message_name', name=who.name)
                            renpy.show_screen('item_message_notify')
                        else:
                            continue
        except Exception as e:
            
            
            print("ERROR in the Python callback:", e)


    class ChatCharacter(store.object):
        """
        A class for messenger characters which keeps track of information
        such as name and profile picture.

        Attributes:
        -----------
        name : string
            The name or nickname of this character as it should appear
            in the messenger.
        prof_pic : string
            An image path to the image that will be used as this character's
            profile picture.
        msg_history : ChatEntry[]
            A list of ChatEntry objects representing messages in a conversation
            with this character.
        label_list : string[]
            A list of strings with the name of a label to jump to in order to
            play out this conversation.
        right_msgr : bool
            True if this character should be messaging from the right side
            of the screen (default is from the left side).
        """
        
        def __init__(self, name, prof_pic=False, tracked_points=None):
            """
            Create a ChatCharacter object for the messenger system.

            Parameters:
            ----------
            name : string
                The name of this character as it should appear in the messenger.
            prof_pic : string
                An image path to the image that will be used as this character's
                profile picture.
            tracked_points : string
                A string with the name of the variable that this character
                should be tracking to tell if a points threshold has been
                reached.
            """
            
            self.name = name
            self.prof_pic = prof_pic
            self.msg_history = [ ]
            self.label_list = [ ]
            if tracked_points is None:
                self.right_msgr = True
            else:
                self.right_msgr = False
                store.points_dict[tracked_points] = self
        
        
        def __call__(self, what, img=False, **kwargs):
            """
            This function makes it easier to write dialogue using a
            ChatCharacter. Dialogue can be written similarly to regular
            Ren'Py dialogue.

            Parameters:
            -----------
            what : string
                The dialogue that will be messaged by this character.
            img : bool
                True if this message contains an image.
            """
            
            try:
                
                store.who_typing = self.name
                
                t = calculate_type_time(what)
                renpy.pause(t)
                store.who_typing = None
                
                entry = ChatEntry(self, what, img)
                if not self.right_msgr:
                    self.msg_history.append(entry)
                else:
                    store.current_convo.append(entry)
                renpy.checkpoint()
                renpy.pause(0.8)
            except Exception as e:
                print("ERROR in ChatCharacter call:", e)

    class ChatEntry(object):
        """
        A class which stores needed information about a message in a
        phone conversation.

        Attributes:
        -----------
        who : ChatCharacter
            The ChatCharacter who will send this dialogue.
        what : string
            The dialogue that will be sent in the message.
        img : bool
            True if this message contains an image.
        """
        
        def __init__(self, who, what, img=False):
            self.who = who
            self.what = what
            self.img = img


    def calculate_type_time(what):
        """
        A helper function which calculates how long a character should take
        to post a message to the chat conversation.

        Parameters:
        -----------
        what : string
            The dialogue that will be sent in a message.

        Returns:
        --------
            Counts how many words are in "what" and applies a multiplier.
        """
        
        
        
        typeTime = what.count(' ') + 1.0
        
        return (typeTime / 3.0)*store.msg_speed


    def begin_viewing_msgr():
        """A helper function to set up the messenger."""
        global config
        if store.current_convo:
            store.no_animate_msg = store.current_convo[-25:]
        if 'mousedown_4' in config.keymap['rollback']:
            config.keymap['rollback'].remove('mousedown_4')

    def finish_viewing_msgr():
        """A helper function to finish displaying the messenger."""
        global config
        if ('mousedown_4' not in config.keymap['rollback']
                and store.scroll_to_rollback):
            config.keymap['rollback'].append('mousedown_4')
        store.no_animate_msg = [ ]
        store._window_auto = True
        return




    yadjValue = float("inf")
    yadj = ui.adjustment()



define config.python_callbacks = [ check_for_conversations ]


default unlocked_phone_convos = set()


default points_dict = dict()

default who_typing = None

default no_animate_msg = [ ]

default current_convo = None








define scroll_to_rollback = True



define msg_speed = 0.95



define point_thresholds = {
    'sadie_phone_points' :   [1, 'sadie_convo_1',
                        2, 'sadie_convo_2',
                        3, 'sadie_convo_3',
                        4, 'sadie_convo_4'],

    'konami_phone_points' :   [1, 'konami_convo_1',
                        2, 'konami_convo_2',
                        3, 'konami_convo_3',
                        4, 'konami_convo_4',
                        5, 'konami_convo_5',
                        6, 'konami_convo_6',
                        7, 'konami_convo_7'],

    'eleanor_phone_points' : [1, 'eleanor_convo_1',
                        2, 'eleanor_convo_2',
                        3, 'eleanor_convo_3',
                        4, 'eleanor_convo_4'],

    'quickies_phone_points' : [1, 'quickies_convo_1',
                        2, 'quickies_convo_2',
                        3, 'quickies_convo_3',
                        4, 'quickies_convo_4',
                        5, 'quickies_convo_5',
                        6, 'quickies_convo_6'],
}


default sadie_phone_points = 0
default eleanor_phone_points = 0
default konami_phone_points = 0
default quickies_phone_points = 0


define bubbles_to_keep = 25




default s = ChatCharacter("Sadie", "phone_screen/eleanor.png", 'sadie_phone_points')
default e = ChatCharacter("Eleanor", "phone_screen/messaging_avatar_eleanor.png", 'eleanor_phone_points')
default k = ChatCharacter("Konami", "phone_screen/messaging_avatar_konami.png", 'konami_phone_points')
default q = ChatCharacter("Quickies", "phone_screen/messaging_avatar_quickies.png", 'quickies_phone_points')




default mc = ChatCharacter("Lucas", "phone_screen/messaging_avatar_lucas.png")




default contact_list = [
    
    (s, "phone_screen/ui_phone_contact_sadie.png"),
    (q, "phone_screen/ui_phone_contact_quickies.png"),
   
]










screen phone_notification(name):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "A conversation is available with [name]"

    timer 3.25 action Hide('phone_notification')



screen messenger(who=None, back_available=False, anim=True):
    tag phone

    python:


        if not back_available:
            yadj.value = yadjValue
        elif back_available and yadj.value == yadjValue:
            yadj.value = 0.0
        if who is None or who.msg_history is None:
            chatlog = [ ]
        else:
            chatlog = who.msg_history


    button:
        background "phone_screen/ui_phone_contacts.png"
        xysize (1920, 1080)
        if back_available:

            action [Function(finish_viewing_msgr),
                Hide('messenger'), Return()]
            at phone_exit_anim()

    frame:
        background "phone_screen/ui_phone_messaging.png"
        xysize (1920, 1080)
        if back_available:
            at phone_exit_anim()
        vbox:
            align (0.5, 1.0)
            xsize 755

            frame:
                background None
                xysize (755, 85)
                text who.name:

                    color "#6b717b"
                    bold True
                    size 40
                    align (0.8, 0.68)
                    text_align 0.8
                if back_available:


                    imagebutton:

                        idle "phone_screen/messaging_back.png"
                        hover "phone_screen/messaging_back_alt.png"
                        align (0.03, 0.5)
                        action [Show('phone_contacts')]






                if (not back_available and anim
                    and not renpy.get_screen('view_image')):

                    textbutton _("Pause"):
                        align (0.95, 0.5)
                        action Show('chat_pause', who=who)
                elif (not back_available and not anim
                    and not renpy.get_screen('view_image')):

                    textbutton _("Play"):
                        align (0.95, 0.5)
                        action Hide('chat_pause')

            hbox:

                xysize (755, 82)
                box_reverse True
                vbox:

                    frame:
                        background None
                        xysize (680, 658)
                        xalign 1.0
                        padding (20, 0)
                        has viewport:
                            id 'phone_vp'
                            xysize (680-40, 658)
                            yadjustment yadj
                            draggable True
                            mousewheel True
                        vbox:
                            xsize 680-40

                            spacing 20
                            null height 1
                            for i index id(i) in chatlog[-bubbles_to_keep:]:
                                use display_chat(i, back_available, anim)
                    frame:

                        background None
                        xysize (680, 90)
                        xalign 1.0
                        if who_typing:
                            text who_typing + " is typing...":

                                align (0.0, 0.0)
                                color "#000"
                frame:

                    background None
                    padding (0, 0)
                    xysize (755-680, 658+90)
                    bar value YScrollValue("phone_vp"):
                        xoffset 15
                        yoffset 63
                        style 'phone_scrollbar'


style phone_scrollbar:
    xysize (50, 623)
    bar_vertical True
    bar_invert True
    base_bar Null(width=50, height=623)
    thumb Frame('phone_screen/ui_phone_scroller.png', 20, 30)





screen chat_pause(who=None):
    zorder 1
    modal True
    use messenger(who=who, back_available=False, anim=False)



screen display_chat(i, back_available=False, anim=True):
    fixed:
        yfit True xfit True
        hbox:
            if i.who.right_msgr:
                box_reverse True
                xalign 1.0
            if i.who.prof_pic:


                add Transform(i.who.prof_pic,
                    
                    size=(163,163))

            vbox:

                text i.who.name:
                    color "#000"
                    if i.who.right_msgr:
                        xalign 1.0
                        text_align 1.0

                button:
                    if i.img:

                        background None
                    elif i.who.right_msgr:

                        background Frame("phone_screen/messaging_bubble.png", 100,100,150,100)


                        padding (40, 42, 90, 42)
                    else:

                        background Frame("phone_screen/messaging_bubble_alt.png", 150,100,100,100)
                        padding (90, 42, 30, 42)
                    if i.who.right_msgr:
                        xalign 1.0
                    if not back_available and anim and i not in no_animate_msg:
                        at msg_appear()
                    xmaximum 680-40-150

                    if not i.img:
                        text i.what:
                            color "#000"

                    else:


                        add Transform(i.what,
                            
                            zoom=0.65)
                        action Show('view_image', Dissolve(0.5), img=i.what)




transform msg_appear():
    zoom 0.3 alpha 0.0
    ease 0.3 zoom 1.0 alpha 1.0





screen view_image(img):
    modal True
    zorder 2
    vbox:
        align (0.5, 1.0)
        xysize (755, 82+755)
        frame:
            xysize (755, 82)
            background None
            imagebutton:

                idle "phone_screen/messaging_back.png"
                hover "phone_screen/messaging_back_alt.png"
                align (0.03, 0.5)
                action [Hide('view_image', Dissolve(0.5))]
        button:


            background "#d6d7dd"
            xysize (750, 755)
            add img align (0.5, 0.5)
            action [Hide('view_image', Dissolve(0.5))]





screen phone_button():
    zorder 1
    modal False
    textbutton _("Open Phone"):
        align (1.0, 0.0)
        background "#fffa"
        text_color "#000"
        action Show('phone_contacts')




screen phone_contacts():

    modal True tag phone

    $ tooltip = GetTooltip()

    button:
        at phone_animation()
        background "phone_screen/ui_phone_contacts.png"
        xysize (1920, 1080)

        action [Function(finish_viewing_msgr),
            Hide('phone_contacts'), Return()]

        viewport:

            id 'contact_vp'
            draggable True
            mousewheel True
            yinitial 0.0
            xysize (680, 730)
            align (0.53, 1.0)
            has vbox:
                spacing 12
            for char, img in contact_list:
                button:
                    xysize (657, 146)
                    background img
                    selected (char.msg_history or char.label_list)
                    if not char.label_list:

                        tooltip "No new conversations are available with " + char.name
                    if char.label_list:
                        add "images/phone_screen/hud_icon_messagealert.png" ypos -20 xpos -10


                    action If(char.msg_history or char.label_list,
                        [Function(begin_viewing_msgr),
                        Call('execute_phone_convo', who=char)],
                        NullAction())
            null height 20

        bar value YScrollValue("contact_vp"):
            pos (590, 384)
            style 'phone_scrollbar'


    if tooltip:
        frame:

            align (0.5, 0.2)
            xysize (529, 140)
            xpadding 50
            background Frame("menu_map_box", 270, 0)
            text "[tooltip]":
                text_align 0.5
                align (.5, .5)
                layout "subtitle"
                bold True




transform phone_animation():
    yoffset 0
    on show:
        yoffset 1080
        ease 0.5 yoffset 0
    on hide:
        yoffset 0
        ease 0.5 yoffset 1080

transform phone_exit_anim():
    yoffset 0
    on hide:
        yoffset 0
        ease 0.5 yoffset 1080



label execute_phone_convo(who):
    if who.label_list:

        $ lbl = who.label_list.pop(0)
        if not renpy.has_label(lbl):
            $ renpy.notify("WARNING: There is no label called " + lbl)
        elif True:
            $ current_convo = who.msg_history
            $ who_typing = None
            show screen messenger(who=who)
            window hide
            call expression lbl from _call_expression
            $ who_typing = None
            hide screen messenger
    call screen messenger(who=who, back_available=True)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

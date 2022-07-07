












init python:
    import time
    class msg2:
        def __init__(self, limit = 10, delay = 2):
            self.limit = limit
            self.list = []
            self.idx = 0
            self.delay = delay
        def msg(self, m):
            self.list.append([time.time(), m])
        def rem(self):
            for i in self.list:
                if i[0]+self.delay < time.time():
                    self.list.pop(0)
                else:
                    break


default msg = msg2(30)

init python:
    config.overlay_screens.append('notif')

transform notif_t(t):
    alpha 0
    ease .2 alpha 1



screen notif():
    zorder 2000
    if len(msg.list):
        timer .1 repeat True action Function(msg.rem)

    vbox:
        pos (450,790)
        for i in msg.list:
            frame:
                background None
                add "gui/dialogue_box_alt.png"
                at notif_t(msg.delay)
                text "{}".format(i[1]) xalign 0.15 yalign 0.1

screen map_updated_notify():
    zorder 5
    add "images/bubble/notification_mapupdated.png"
    timer 3 action Hide("map_updated_notify", transition = Dissolve(0.2))

screen journal_updated_notify():
    zorder 5
    add "images/bubble/notification_journalupdated.png"
    timer 3 action Hide("journal_updated_notify", transition = Dissolve(0.2))

image item_update_animation:
    "notification_itemgained_01"
    .1
    "notification_itemgained_02"
    .2
    "notification_itemgained_03"
    .5
    repeat

screen item_message_name(name):
    zorder 6
    vbox:
        xalign 0.93
        yalign 0.77
        text "{b}{color=#efe1c6}[name] {/b}{/color}" outlines [ (3, "#000000", 0, 1) ]
    timer 3.0 action Hide("item_message_name", transition = Dissolve(0.2))

screen item_message_notify():
    zorder 5
    vbox:
        xalign 0.95
        yalign 0.9
        add "notification_message"

    timer 3.0 action Hide("item_message_notify", transition = Dissolve(0.2))

screen item_updated_notify():
    zorder 5
    add "item_update_animation"

    timer 2.5 action Hide("item_updated_notify", transition = Dissolve(0.2))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

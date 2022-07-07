


transform progress_box_fade:






    xalign 0.5 yalign 0.5 alpha 0.0

    on appear:
        alpha 1.0
    on show:

        zoom .75
        linear .25 zoom 1.0 alpha 1.0
    on hide:

        linear .25 zoom 1.25 alpha 0.0

screen in_progress_box():
    modal True
    zorder 90



    key "mouseup_1" action Hide("in_progress_box", transition = Dissolve(0.2))

    imagebutton:
        idle "gui/hud/under_progress_box.png" at progress_box_fade


transform position_align_1:
    xalign 0.25
    yalign 1.0











image bathroom_room_day = "location_bathroom_day"
image bathroom_room_night = "location_bathroom_night"
image bathroom_room_midnight = "location_bathroom_midnight"





























































image go_back_btn = "gui/hud/go_back_btn.png"
image go_back_btn_h = "gui/hud/go_back_btn_h.png"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

style location_hint:
    text_align 0.5
    size 32
    color "#FFF"
    outlines [(2,"#000")]




screen location(location_id):
    layer "master"
    zorder -1
    $ elements=get_location_elements(location_id)
    $ active=renpy.get_screen("roaming")
    for el_pos,el_img,el_action,el_hint in elements:
        if isinstance(el_img,basestring):
            python:
                click_thru="#" in el_img
                el_img=el_img.strip("#")
                if isinstance(el_action,basestring) and el_action!="$blocked$":
                    el_action=Return(el_action)
            if click_thru:
                add (el_img%"idle" if "%" in el_img else el_img):
                    if el_pos:
                        pos el_pos
            else:
                imagebutton:
                    background None
                    focus_mask True
                    if el_pos:
                        pos el_pos
                    if "%s" in el_img:
                        auto el_img
                    else:
                        idle el_img
                    if active:
                        if el_action=="$blocked$":
                            mouse "deny_m"
                            action NullAction()
                        elif el_action:
                            action el_action
                    if isinstance(el_hint,basestring) and el_hint:
                        if "*" in el_hint:
                            if "^" in el_hint:
                                mouse "interaction_m"

                            elif "<" in el_hint:
                                mouse "talk_m"
                            elif ">" in el_hint:
                                mouse "door_m"

                        if "@" in el_hint:

                            if "^" in el_hint:

                                hover_foreground Text(el_hint.strip("@^<>"),style="location_hint",pos=(0.5,0.0),anchor=(0.5,1.0))
                            elif "<" in el_hint:

                                hover_foreground Text(el_hint.strip("@^<>"),style="location_hint",pos=(0.0,0.5),anchor=(1.0,0.5))
                            elif ">" in el_hint:

                                hover_foreground Text(el_hint.strip("@^<>"),style="location_hint",pos=(1.0,0.5),anchor=(0.0,0.5))
                            else:

                                hover_foreground Text(el_hint.strip("@^<>"),style="location_hint",pos=(0.5,1.0),anchor=(0.5,0.0))
                        else:
                            hovered SetVariable("hud_hint",el_hint)
                            unhovered SetVariable("hud_hint",None)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

init python:


    def get_location_elements(location_id):
        
        elements=[]
        location=getattr(store,location_id,None)
        if hasattr(location,"scene"):
            location.scene(elements)
        
        for n,el in enumerate(elements):
            if isinstance(el,basestring):
                el=[None,el]
            el=list(el[:])+[None]*(4-len(el))
            if isinstance(el[1],basestring):
                
                el[1]=el[1].format(
          tod=now.tod_name.lower(),
          dark=now.tod_dark,
          state="%s",
          )
            elements[n]=el
        return elements



    def location_reset_scene():
        
        for tag in renpy.get_showing_tags():
            if tag!="location":
                renpy.hide(tag)
        
        loc=renpy.get_screen("location")
        if not loc or loc.scope["_args"][0]!=current_location:
            renpy.show_screen("location",current_location)


default exit_roaming = False








label roaming:
    $ exit_roaming=False
    while not exit_roaming:
        $ location_reset_scene()
        call screen roaming
        $ hud_hint=None
        if isinstance(_return,basestring):
            $ _return=[_return]
        if isinstance(_return,(list,tuple)):
            call expression _return[0] pass (*_return[1:]) from _call_expression_2
    return exit_roaming,_return



label set_location(target_location):
    $ current_location=target_location
    $ location_reset_scene()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

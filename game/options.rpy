













define config.name = _("Resident X")

define config.window_auto_hide = [ 'scene', 'call screen', 'menu', "say-centered" ]



define gui.show_name = False




define config.hard_rollback_limit = 100
define config.rollback_enabled = True



define config.version = "0.5"





define gui.about = _p("""
""")






define build.name = "ResidentX"







define config.has_sound = True
define config.has_music = True
define config.has_voice = True
























define config.enter_transition = None
define config.exit_transition = None




define config.intra_transition = None




define config.after_load_transition = None




define config.end_game_transition = None
















define config.window = "hide"







define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 0





default preferences.afm_time = 15
















define config.save_directory = "ResidentXz-1556746685"






define config.window_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)


    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.rpyc', 'archive')









    build.documentation('*.html')
    build.documentation('*.txt')
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

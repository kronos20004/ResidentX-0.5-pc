init python:





















    def is_talking(char_id):
        return getattr(store,char_id+"_talking",False) or renpy.showing(char_id)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

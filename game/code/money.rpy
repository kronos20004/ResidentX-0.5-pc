init python:
    import os.path
    class player_units:
        def __init__(self, name):
            self.name = name
            self.cash = 0
        def got_cash(self, a):
            self.cash += a
        def lose_cash(self, a):
            self.cash -= a

default main_mc = player_units("lucas")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

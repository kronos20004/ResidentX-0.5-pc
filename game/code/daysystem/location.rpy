init -100 python:

    class Location(object):
        
        title="-Location-"
        
        unlocked=True
        def __init__(self):
            super(Location,self).__init__()
            self.flags={}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def scene(self,elements):
            pass
        
        def __getitem__(self,key):
            return self.flags.get(key)
        def __setitem__(self,key,value):
            self.flags[key]=value
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

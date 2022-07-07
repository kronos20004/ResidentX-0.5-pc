
define dow_names = [
  "Monday",
  "Tuesday",
  "Wednesday",
  "Thursday",
  "Friday",
  "Saturday",
  "Sunday",
  ]

define dow_short_names = [
  "Mon",
  "Tue",
  "Wed",
  "Thu",
  "Fri",
  "Sat",
  "Sun",
  ]

define tod_names = [
  "Morning",
  "Afternoon",
  "Evening",
  "Night",
  ]

define tod_dark = {
  "morning": "",
  "afternoon": "",
  "evening": "_dark",
  "night": "_dark",
  }

define tod_images = {
  "morning": "tod_morning.png",
  "afternoon": "tod_afternoon.png",
  "evening": "tod_evening.png",
  "night": "tod_night.png",
  }

init python:
    def process_time_advanced():
        
        
        
        
        pass

    class CurrentDayTime(object):
        def __init__(self,start_day=1,start_tod=0):
            self.day=start_day
            self.tod=start_tod
        
        @property
        def dow(self):
            return (self.day-1)%7
        
        @property
        def dow_name(self):
            return dow_names[self.dow]
        
        @property
        def dow_short_name(self):
            return dow_short_names[self.dow]
        
        @property
        def tod_name(self):
            return tod_names[self.tod%len(tod_names)]
        
        @property
        def tod_image(self):
            return tod_images[self.tod_name.lower()]
        
        
        
        
        @property
        def tod_dark(self):
            return tod_dark[self.tod_name.lower()]
        
        
        
        def advance(self,time_to_pass=1):
            while time_to_pass>0:
                time_to_pass-=1
                self.tod+=1
                if self.tod>=len(tod_names):
                    self.day+=1
                    self.tod=0
                process_time_advanced()
        
        def day_advance(self,days_to_pass=1):
            tods_to_pass=days_to_pass*len(tod_names)-self.tod
            self.advance(tods_to_pass)
        
        
        
        
        
        
        
        
        def __call__(self,*args):
            for arg in args:
                if isinstance(arg,basestring):
                    arg=arg.lower()
                    if arg not in (self.tod_name.lower(),self.dow_name.lower(),self.dow_short_name.lower()):
                        return False
                elif isinstance(arg,(list,tuple)):
                    arg_list=arg
                    found=False
                    for arg in arg_list:
                        if isinstance(arg,basestring):
                            arg=arg.lower()
                            if arg in (self.tod_name.lower(),self.dow_name.lower(),self.dow_short_name.lower()):
                                found=True
                        else:
                            if arg==self.day:
                                found=True
                    if not found:
                        return False
                else:
                    if arg!=self.day:
                        return False
            return True

default now = CurrentDayTime()



label advance_time:
    $ now.advance()
    return

label advance_day:
    $ now.day_advance()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

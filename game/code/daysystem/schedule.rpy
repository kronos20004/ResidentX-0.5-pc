init -250 python:

    def parse_schedule(schedule_str):
        rv={}
        
        schedule=schedule_str.splitlines()
        while schedule:
            s=schedule[0].strip()
            if s and s[0]!="#":
                break
            schedule.pop(0)
        
        dow=[]
        s=schedule.pop(0)
        i=0
        while i<len(s):
            while i<len(s) and s[i]==" ":
                i+=1
            dow_start=i
            while i<len(s) and s[i]!=" ":
                i+=1
            dow_name=s[dow_start:i].lower()
            dow.append((dow_name,dow_start))
        
        tod=[]
        for s in schedule:
            s=s.strip()
            if s and s[0]!="#":
                tod_name=s[:dow[0][1]].strip().lower()
                tod.append(tod_name)
                for n in range(len(dow)):
                    loc_act=s[dow[n][1]:(len(s) if n==len(dow)-1 else dow[n+1][1])].strip()
                    if loc_act:
                        loc,_,act=loc_act.partition("/")
                        rv[(dow[n][0],tod_name)]=(loc,act or None)
        return rv



    def schedule_now(schedule):
        
        dow=now.dow_name.lower()
        tod=now.tod_name.lower()
        
        return schedule.get((dow,tod),(None,None))




    def char_at(char_id,location_id,activity=None):
        char_scheduler=getattr(store,char_id+"_scheduler",None)
        if callable(char_scheduler):
            char_loc,char_activity=char_scheduler()
            if char_loc==location_id and (char_activity==activity or activity is None):
                return True
        return False
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

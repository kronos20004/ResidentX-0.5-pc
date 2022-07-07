





define konami_intro_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon  treeh       treeh       treeh       treeh       treeh
evening    
night      
""")

define konami_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon             
evening    treeh        treeh       treeh       treeh      treeh 
night      
""")

define konami_pool_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                                                pool        pool 
afternoon                                                              pool        pool
evening     
night      
""")









define konami_empty_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon             
evening   
night      
""")











init python:
    def konamipool_scheduler():
        rv=schedule_now(konami_pool_schedule)
        return rv

    def konami_scheduler():
        if konami_story == 1:
            rv=schedule_now(konami_intro_schedule)
            return rv
        if konami_story == 2: 
            rv=schedule_now(konami_empty_schedule)
            return rv
        if konami_story == 4 or konami_story == 5:
            rv=schedule_now(konami_schedule)
            return rv
        
        
        
        
        else:
            rv=schedule_now(konami_empty_schedule)
            return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

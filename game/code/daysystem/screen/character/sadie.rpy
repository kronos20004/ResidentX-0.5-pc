





define sadiebed_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon          
evening    
night                  sadie_b                 sadie_b                 sadie_b     sadie_b
""")

define sadiebedz_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon          
evening    
night      sadiebz                 sadiebz                 sadiebz
""")

define sadiebalcony_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                                   
afternoon              sadie_d                             sadie_d
evening                sadie_d                             sadie_d
night           
""")

define sadiekit_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon                                      kitchen                 kitchen
evening                                                          
night           
""")

define sadiecouch_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                        
afternoon          
evening    sadieliv                sadieliv    sadieliv                                               
night           
""")

define sadieyoga_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                                                yogaz       yogaz
afternoon                                                                     
evening                                                 
night           
""")









init python:
    def sadiebed_scheduler():
        rv=schedule_now(sadiebed_schedule)
        return rv

init python:
    def sadiebedz_scheduler():
        rv=schedule_now(sadiebedz_schedule)
        return rv

init python:
    def sadiecouch_scheduler():
        rv=schedule_now(sadiecouch_schedule)
        return rv

init python:
    def sadieyoga_scheduler():
        rv=schedule_now(sadieyoga_schedule)
        return rv

init python:
    def sadiebaclony_scheduler():
        rv=schedule_now(sadiebalcony_schedule)
        return rv

init python:
    def sadiekit_scheduler():
        rv=schedule_now(sadiekit_schedule)
        return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

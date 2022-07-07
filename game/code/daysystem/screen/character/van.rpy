





define van_schedule = parse_schedule("""
           monday      tuesday     wednesday   thursday    friday      saturday    sunday
morning                                                                garage      garage
afternoon              garage                  garage      garage 
evening    garage      garage      garage      garage      garage       
night      garage      garage      garage      garage      garage      garage      garage
""")









init python:
    def van_scheduler():
        rv=schedule_now(van_schedule)
        return rv
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

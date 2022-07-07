
label isJigSawGame(file_init_name="minigame_art01_block", quantity_files=9, init_time=0, end_time=16, valid_image=[], cell=3, row=3, xsize=227, ysize=227, img_format=".png"):
    $ JigSawGame = JigSaw(file_init_name, quantity_files, Timer(init_time, end_time), valid_image, cell, row, xsize, ysize, img_format)
    call screen jigsaw(JigSawGame)
    if _return == "win":
        $ renpy.notify("Student module 1 done")
        $ eleanor_story += 1
        call isJigSawGamee from _call_isJigSawGamee



    return


label isJigSawGamee(file_init_name="minigame_art02_block", quantity_files=9, init_time=0, end_time=16, valid_image=[], cell=3, row=3, xsize=227, ysize=227, img_format=".png"):
    $ JigSawGame = JigSaw(file_init_name, quantity_files, Timer(init_time, end_time), valid_image, cell, row, xsize, ysize, img_format)
    call screen jigsaw(JigSawGame)
    if _return == "win":
        $ renpy.notify("Student module 2 done")
        $ eleanor_story += 1
        jump goto_lucaspc
    return

label isJigSawGameee(file_init_name="minigame_art03_block", quantity_files=9, init_time=0, end_time=15, valid_image=[], cell=3, row=3, xsize=227, ysize=227, img_format=".png"):
    $ JigSawGame = JigSaw(file_init_name, quantity_files, Timer(init_time, end_time), valid_image, cell, row, xsize, ysize, img_format)
    call screen jigsaw(JigSawGame)
    if _return == "win":
        $ renpy.notify("Student module 3 done")
        $ eleanor_story += 1
        jump goto_lucaspc

    return


label first_jiggsaw:
    jump isJigSawGame

label second_jiggsaw:
    jump isJigSawGamee

label third_jiggsaw:
    jump isJigSawGameee
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

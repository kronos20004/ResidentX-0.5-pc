




init -999:
    define config.variants = [ "large", "pc", "touch", None ]
    define config.hw_video = False




image custom_text_card = ParameterizedText(xalign=0.5, yalign=0.5, color="#f7bc4a", font="gui/fonts/acumin_bold.otf", outlines=[ (absolute(4), "#000000", absolute(3), absolute(3)) ], size=160  )
image custom_text_card2 = ParameterizedText(xalign=0.5, yalign=0.5, color="#f7bc4a", font="gui/fonts/acumin_bold.otf", outlines=[ (absolute(4), "#000000", absolute(3), absolute(3)) ], size=35  )

image mouse door:
    "images/mouse/hud_cursor_enter.png"
    zoom 1.52





image mouse talk:
    "images/mouse/hud_cursor_speak.png"
    zoom 1.52

image mouse deny:
    "images/mouse/hud_cursor_cursor_deny.png"
    zoom 1.52





image mouse interaction:
    "images/mouse/hud_cursor_interact.png"
    zoom 1.52

image mouse default:
    "images/mouse/hud_cursor_defualt.png"
    zoom 1.52

init:

    $ flash = Fade(.25, 0, .75, color="#fff")











    $ config.mouse = {
      "default" : [("hud_cursor_defualt.png", 0,0)],
      "door_m" : [("images/mouse/hud_cursor_enter.png", 1,0)],
  
      "interaction_m" : [("images/mouse/hud_cursor_interact.png", 1,0)], 
      "talk_m" : [("images/mouse/hud_cursor_speak.png", 1,1)], 
      "deny_m" : [("images/mouse/hud_cursor_cursor_deny.png", 0,1)],
  }


transform leo_sadie_input_position:
    xalign .5
    yalign .5

image gui_input_sadie_relationship = "images/customs/input_gui/relationship_inputsadie1.png"
image gui_input_sadie_refersadie = "images/customs/input_gui/relationship_inputsadie2.png"
image gui_input_referleo = "images/customs/input_gui/relationship_inputleo2.png"
image gui_input_determineleo = "images/customs/input_gui/relationship_inputleo1.png"
default l_q = "Alien Queen"

default sadie_relationship_input = "Caretaker"
default sadie_refer_input = "Sadie"

default leo_refer_input = "Leo"
default leo_determine_input = "Caretaker"


image back_display1 = "cutscene/back_display/bck_bg1.jpg"


define flash = Fade(.25, 0.0, .75, color="#fff")

default exit_btn = True


default leo_password_input = ""
default leo_password_coreect = "resident00x"

transform dual_character_position:
    xpos 400
    ypos 0



define l_uglyb = Character("Student", color="#c2c2c2", who_outlines=[ (4, "#2c2e27") ])


define l_mc = Character("Lucas", color="#ffff", who_outlines=[ (4, "#2c2e27") ])
define l_stranger = Character("Stranger", color="#000000", who_outlines=[ (3, "#c4c4c4") ])
define l_unkown = Character("???", color="#d4d4d4", who_outlines=[ (3, "#75ad2b") ])
define l_claus = Character("Mrs. Claus", color="#fcfcfc", who_outlines=[ (3, "#75ad2b") ])
define l_mystery = Character("???", color="#000000", who_outlines=[ (3, "#c4c4c4") ])
define l_sadie = Character("[sadie_refer_input]", color="#ffff", who_outlines=[ (4, "#2c2e27") ])
define l_eleanor = Character("Ms. Eleanor", color="#ffff", who_outlines=[ (4, "#2c2e27") ])
define l_konami = Character("Konami", color="#ffff", who_outlines=[ (4, "#2c2e27") ])
define l_jada = Character("Jada", color="#ffff", who_outlines=[ (4, "#2c2e27") ])

default go_back_btn = True

default attic_paint = False
default attic_paint_discovered = False

default key_pad_unlocked = False


default chores_unlocked = False
default chores_sadie_talk = 0
default shop_first_time = False
default kitchen_sink_work = True


default journal_sadie_movienight = False


default ele_shower_ass_seen = False
default ele_shower_ass_seen1 = False
default ele_shower_front_seen = False
default ele_shower_front_seen1 = False

default eleanor_btn_lucasroom = True


default eleanor_story = 0
default spareitem_eleanor = False
default eleanor_2nd_text = False


default jada_story = 0
default jada_journal = False

default lucas_scope = False
default scope_attic1 = False
default scope_inter_1 = False




default konami_story = 0
default konami_door_access = False
default konami_treehouse = False
default konami_journal = False
default konami_discovered = False
default konami_chap1_done = False

default konami_entrance_access = False



default sadie_night_couch_keypad = False
default sadie_night_couch_watching = False
default yoga_sadie_scene = False
default yoga_sadie = False
default sadie_yogabtn = True
default sadie_convo1_done = False



default sadie_yoga_sch = 0

default yoga_grind1 = False

default yoga_grind2 = False

default yoga_grind3 = False

default yoga_grind4 = False

default yoga_grindend = False

default yoga_sadie_ended = False



default sadie_info_1 = False
default sadie_info_2 = False


default konami_info_1 = False


default lucas_pc_wallpaper = True










default attic_hidden_door = False


default handsaw_pickup = False


default random_tv_screen = renpy.random.randint(1,2)

default bookshelf_close = False
default medallion_piece_used = False


default medallion_piece = False
default office_leo_note = False
default facility_story = 0
default strangerelic_office = False
default sadie_room_chestkey = False
default strangerelic_insert = False

default office_wood_cut = False

default hidden_attic_discovered = False

default attic2_computer_solved = False
default medallion_puzzle_dialogue = False
default medallion_puzzle_solve = False
default office_strangebattery = False
default attic2_strangebattery = False




default door_map_icon = False
default atticwindow_map_icon = False
default atticstrange_map_icon = False
default boardinfo_map_icon = False



default christmas_story = 0
default christmas_enable = 0
default item_christmastree_shop = False
default item_christmastree_arrival = 0
default item_christmassanta_shop = False
default item_christmassanta_arrival = 0

default lucas_wearsanta_suit = False
default christmas_santasuit_btn = False
default christmas_treedeco_btn = False
default christmas_treedeco_used = False

default christmas_decoration_enable = False





default medallion_map_icon = False
default chest_map_icon = False
default leo_laptop_map_icon = False
default secret_keypad_map = False
default tv_map_icon = False
default mail_map_icon = False


default mystery_brick_map_icon = False
default mystery_stair_map_icon = False


default bailey_map_cross = False
default pc_lucas_map = False


default eleanor_gallery_profile = False
default eleanor_gallery_1_unlocked = False
default eleanor_gallery_2_unlocked = False

default sadie_gallery_1_unlocked = False

default konami_gallery_profile = False
default konami_gallery_1_unlocked = False

default jada_gallery_profile = False
default jada_gallery_1_unlocked = False
default jada_gallery_2_unlocked = False


default wallpaper_unlocked3 = False
default wallpaper_unlocked4 = False
default wallpaper_unlocked5 = False
default wallpaper_unlocked6 = False
default wallpaper_unlocked7 = False
default wallpaper_unlocked8 = False


default item_lens_shop = False
default item_lens_arrival = 0

default item_manga_buy = False
default item_manga_shop = False
default item_manga_arrival = 0


default item_dreamkey = Item(img="images/inventory_thumb/item_dreamkey.png",desc="{=healthui}I woke up with this thing \n next next to \n me It was from. . \n I don't remember. . \n but I've seen this \n symbol somewhere{/=}", name="{=inventoryfont}Dreamkey{/=}", h_image="", clicked=False)
default item_handsaw = Item(img="images/inventory_thumb/item_handsaw.png",desc="{=healthui}A trusty handsaw could be useful for cutting some wood{/=}", name="{=inventoryfont}Handsaw{/=}", h_image="", clicked=False)
default item_stranegbattery = Item(img="images/inventory_thumb/item_frequencybattery.png",desc="{=healthui}Found it behind that \n cliche bookshelf \n *Frequency battery \n  v04* is written on it \n I think it's supposed \n to clip onto something{/=}", name="{=inventoryfont}Strange \n Battery{/=}", h_image="", clicked=False)
default item_medallion = Item(img="images/inventory_thumb/item_medallion.png",desc="{=healthui}Could be used \n on the bookshelf.\n With the rest of the \n Medallion's. \n It has the number 1 \n attached \n on the back{/=}", name="{=inventoryfont}Medallion{/=}", h_image="", clicked=False)
default item_chestkey = Item(img="images/inventory_thumb/item_chestkey.png",desc="{=healthui}Some key I found in \n [sadie_refer_input]'s room. I'm \n sure I'll find some \n use for it.{/=}", name="{=inventoryfont}Unknown \n Key{/=}", h_image="", clicked=False)
default item_strangerelic = Item(img="images/inventory_thumb/item_relic.png",desc="{=healthui}An old present from leo .I have no idea what it's used for{/=}", name="{=inventoryfont}Strange Relic{/=}", h_image="", clicked=False)
default item_sadiebusinessoutfit = Item(img="images/inventory_thumb/item_sadiesoutit_1.png",desc="{=healthui}Her bra has a pleasent smell . . . . wait ... should I be smelling it? {/=}", name="{=inventoryfont}[sadie_refer_input]'s Half \n Outfit{/=}",h_image="", clicked=False)
default item_spareoutfit = Item(img="images/inventory_thumb/item_spareoutfit.png",desc="{=healthui}A spare outfit for \n Eleanor.{/=}", name="{=inventoryfont}Spare Outfity{/=}", h_image="", clicked=False)
default item_bra1 = Item(img="images/inventory_thumb/item_bra_1.png",desc="{=healthui}A bra.{/=}", name="{=inventoryfont}Red Bra{/=}", h_image="", clicked=False)
default item_manga1 = Item(img="images/inventory_thumb/item_manga1.png",desc="{=healthui}Nier Manga Vol 1{/=}", name="{=inventoryfont}Nier Manga{/=}", h_image="", clicked=False)
default item_lens = Item(img="images/inventory_thumb/item_lens.png",desc="{=healthui}A len piece{/=}", name="{=inventoryfont}Lens{/=}", h_image="", clicked=False)

default money = 20
default inv = []
default closet_dial_open = False
default chapter_1 = 0
default sadie_story = 0
default daytime = "day"


$ trackday = 0



$ save_name = "Saved File"





screen relationship_input():
    hbox:
        xalign .5
        yalign .535


        input:
            value VariableInputValue("sadie_relationship_input", default=True, returnable=True)
            default "TYPE ME"
            color "#ffff"
            bold True
            size 40
            length 9


screen refersadie_input():
    hbox:
        xalign .5
        yalign .535


        input:
            value VariableInputValue("sadie_refer_input", default=True, returnable=True)
            default "TYPE ME"
            color "#ffff"
            bold True
            size 40
            length 9


screen referleo_input():
    hbox:
        xalign .5
        yalign .535


        input:
            value VariableInputValue("leo_refer_input", default=True, returnable=True)
            default "TYPE ME"
            color "#ffff"
            bold True
            size 40
            length 9


screen determineleo_input():
    hbox:
        xalign .5
        yalign .535


        input:
            value VariableInputValue("leo_determine_input", default=True, returnable=True)
            default "TYPE ME"
            color "#ffff"
            bold True
            size 40
            length 9


image logo_pixel_anim:
    "opening_animation_1"
    0.14
    "opening_animation_2"
    0.14
    "opening_animation_3"
    0.14
    "opening_animation_4"
    0.14
    "opening_animation_5"
    0.14
    "opening_animation_6"
    0.14
    "opening_animation_7"
    0.2
    "opening_animation_8"
    repeat


label splashscreen:


    play sound "music/Heartbeat_01.wav"
    scene logo_pixel_anim with fade
    $ renpy.pause(3.0)
    stop sound fadeout 0.5
    scene 18plus with fade
    pause
    return


label start:
    jump start_new
























label start_new:
    show screen escape_key
    window hide
    scene bck_bg1
    $ quest_log_active.remove("eleanor")
    $ quest_log_active.remove("konami")
    $ quest_log_active.remove("jada")
    $ info_log_active.remove("konamiz")


label patron_build_check:
    menu:
        "Patron Build" if True:
            "You are not using patron build."
            jump patron_build_check
            return
        "Non Patron Build" if True:


            "Sadie outfit changes not enabled."
            "Cheat code not enabled."
            jump continue_g
            return




label continue_g:


    show sadie normal pose default at right
    show gui_input_sadie_relationship at leo_sadie_input_position
    call screen relationship_input

    hide gui_input_sadie_relationship
    if sadie_relationship_input == "":
        $ sadie_relationship_input = "Caretaker"
    "[sadie_refer_input]'s relationship with Lucas is [sadie_relationship_input]"


    show gui_input_sadie_refersadie at leo_sadie_input_position
    call screen refersadie_input
    hide gui_input_sadie_refersadie
    if sadie_refer_input == "":
        $ sadie_refer_input = "Sadie"
    "Lucas will refer to Sadie as [sadie_refer_input]"
    hide sadie normal pose default at right with dissolve

    show char_leo_01 at right with dissolve
    "Leo is Sadie's husband that has gone missing for over a year & no one knows his wherabouts"

    show gui_input_determineleo at leo_sadie_input_position
    call screen determineleo_input
    hide gui_input_determineleo
    if leo_determine_input == "":
        $ leo_determine_input = "Caretaker"
    "[leo_refer_input]'s relationship with Lucas is [leo_determine_input]"

    show gui_input_referleo at leo_sadie_input_position
    call screen referleo_input
    hide gui_input_referleo
    if leo_refer_input == "":
        $ leo_refer_input = "Leo"
    "Lucas will refer to Leo as [leo_refer_input] "
    hide char_leo_01 at right with dissolve

    scene black


    pause










    play music "music/Lexington.mp3"







    jump storyline_chapter_1

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

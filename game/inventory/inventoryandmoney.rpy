define defined_questlogs = {}
default quest_log_active = QuestLogPersons(
    "konami", "sadie", "leo", "eleanor", "jada"
)

define defined_infologs = {}
default info_log_active = QuestLogPersons(
    "sadiez", "konamiz"
)






init python:
    class Item:
        def __init__(self, img, desc, name, h_image, clicked):
            self.img = img
            self.desc = desc
            self.name = name
            self.h_image = h_image
            self.clicked = clicked

    class Quest(renpy.store.object):
        def __init__(
            self, condition, text
        ):
            self.condition = condition
            self._text = text
        
        def __repr__(self):
            return "<Quest: {0}, {1}".format(self.text, self.condition)
        
        @property
        def is_complete(self):
            return renpy.python.py_eval_bytecode(
                renpy.python.py_compile(self.condition, "eval")
            )
        
        @property
        def text(self):
            return renpy.substitute(self._text)

    class QuestLogPersons(renpy.store.object):
        def __init__(self, *persons):
            self.persons = set(persons)
        
        def add(self, person):
            self.persons.add(person)
        
        def remove(self, person):
            self.persons.discard(person)

    class QuestLog(renpy.store.object):
        _latest = _("{color=#000000}{font=fonts/Mansalva-Regular.ttf}- Support us on {a=https://patreon.com/TheRedPixel}{color=#e88833} Patreon {/color}{/a} ! \n{/font}{/color}")
        def __init__(self, _id, text):
            self._id = _id
            self._text = text
            self._inses = []
            defined_questlogs[_id] = self
            defined_infologs[_id] = self
        
        def __repr__(self):
            return "<QuestLog: {0}, {1}".format(self.text, self._inses)
        
        @property
        def opened(self):
            return [
                task for task in self._inses
                if task.is_complete
            ]
        
        @property
        def text(self):
            return renpy.substitute(self._text)
        
        def add(self, *quests):
            for quest in quests:
                if isinstance(quest, Quest):
                    self._inses.append(quest)
            return self
        
        @property
        def is_complete(self):
            return self._inses[-1].is_complete

    QuestLog(
        _id="konami",
        text=_("Konami Quest"),
    ).add(
        Quest(
            condition="konami_story == 1",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} There is something going on in the tree house\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 2",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Text konami at night\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 4",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Konami should be at the Tree House during evening\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 5",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Wait for a text next day or so.\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 6",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check her text.\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 7",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Meet her at the Treehouse during the day.\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 9",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Wait for a text next day or so.\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 10",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check Text. \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 11",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Konami should be at the pool during the \n weekends(sat/sun).\n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 13",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Buy the managa ! and \n then head to her house. \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 14",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Wait for a text next day or so.  \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 15",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check text. \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 16",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Visit Treehouse during weekends (Morning) \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 17",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She will text you at night \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 20",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Show up at her room during \n the afternoon (weekdays) \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 21",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Text Konami at night  \n {/size}{/font}{/color}")
        ), Quest(
            condition="konami_story == 23",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} You’ve reached the end of Konami’s current story content for now. Come back when Konami gets another story Update and support us on {a=https://www.patreon.com/TheRedPixel}{color=#c40e38}{b} Patreon {/b}{/color}{/a} if you’d like to \n {/size}{/font}{/color}\n")
        )
    )

    QuestLog(
        "sadie",
        text=_("[sadie_refer_input]'s Quest"),
    ).add(
        Quest(
            condition="sadie_story == 1",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} [sadie_refer_input] asks me to fetch her outfit for her. It should be inside her bedroom’s Closet.\n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 4",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} [sadie_refer_input] is at work, I think I’ll wait for her, I could watch some TV in the meantime while I wait.\n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 6",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I should see what she's up to. I better find her at the Balcony or Kitchen \n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 7 and not journal_sadie_movienight",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} We set plans to for another movie night. I’ll be sure to find her waiting in the living room when she usually watches TV. \n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 8",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I agreed to be her yoga partner so I better meet up with her at the Balcony. I'll find her somewhere around the house , maybe check the info page \n {/size}{/font}{/color}")
        ), Quest(
            condition="not sadie_night_couch_keypad and sadie_story == 5",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Talk to Sadie about the Keypad in her Closet\n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_night_couch_keypad",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s}{size=27} Keypad checked \n{/s}{/size}{/font}{/color}")
        ), Quest(
            condition="yoga_sadie_scene",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Do yoga with Sadie\n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 14",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I should see what she's up to. I better find her while she's watching some TV \n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 15",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} We set plans for another movie night so I better find her while she’s watching TV at night \n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 16",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Guess I scared her too much with the horror movie we watched and now she wants to sleep with me?! I better please her and go sleep with her in bed at night \n {/size}{/font}{/color}")
        ), Quest(
            condition="sadie_story == 17",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} You’ve reached the end of [sadie_refer_input]'s current story content for now. Come back when [sadie_refer_input] gets another story Update and support us on {a=https://www.patreon.com/TheRedPixel}{color=#c40e38}{b} Patreon {/b}{/color}{/a} if you’d like to \n {/size}{/font}{/color}")
        ),


    )
    QuestLog(
        "leo",
        text=_("Engima's Quest"),
    ).add(
        Quest(
            condition="not key_pad_unlocked",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Explore\n {/size}{/font}{/color}")
        ), Quest(
            condition="not closet_dial_open and key_pad_unlocked",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Try to unlock the keypad\n {/size}{/font}{/color}")
        ), Quest(
            condition="closet_dial_open",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s}{size=27} Keypad Unlocked \n {/size}{/s}{/font}{/color}")
        ), Quest(
            condition="not office_strangebattery and medallion_puzzle_solve",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Should find a tool to cut the wood \n {/size}{/font}{/color}")
        ), Quest(
            condition="item_stranegbattery in inv",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} What could I use the battery for ? \n {/size}{/font}{/color}")
        ), Quest(
            condition="attic2_strangebattery",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{s}{size=27} Strange battery implemented \n {/size}{/s}{/font}{/color}" )
        ), Quest(
            condition="not attic2_computer_solved and attic2_strangebattery",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Solve the cryptic computer code \n {/size}{/font}{/color}")
        ), Quest(
            condition="facility_story == 1",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Maybe should sleep during saturday or sunday \n {/size}{/font}{/color}")
        ), Quest(
            condition="facility_story == 3 and item_dreamkey in inv",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I think this dreamkey is used on something. . .\n {/size}{/font}{/color}")
        ), Quest(
            condition="facility_story == 4",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} You’ve reached the end of Leo’s current story content for now. Come back when Leo gets another story Update and support us on {a=https://www.patreon.com/TheRedPixel}{color=#c40e38}{b} Patreon {/b}{/color}{/a} if you’d like to {/size}{/font}{/color}")
        ),
    )
    QuestLog(
        "eleanor",
        text=_("Eleanor Quest"),
    ).add(
        Quest(
            condition="eleanor_story == 1",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} N/A\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 2",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check the door\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 3",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Wait for the text during Tuesday or Thursday\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 4",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check your phone.\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 5",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She will ring the bell during tuesday or thursday\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 6",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She is by the door (tuesday, or thursday) evening\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 9",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She will text you about the Module soon\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story in (10, 11)",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Complete the Module\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 12",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I will call her during her off \n which is tuesday or thursday\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 13",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}- She will ring the bell in afternoon\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 14",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She at the door (afternoon)\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 17",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Do the Module\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 18",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Wait for Text from Eleanor \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 19",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Check your text from Eleanor \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 20",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Eleanor will come in the morning \n (tuesday or thursday) \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 21",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She is at the front door (tuesday or thursday) \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 23",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Grab her clothe from [sadie_refer_input]'s Closet' \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 28",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She will ring the door at night (tuesday , thursday)\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 29",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} She is by the front door, night\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 32",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Eleanor will text you during tuesday/thursday \n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 33",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Look at the text.\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 34",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Find her Bra at the Laundry\n {/size}{/font}{/color}")
        ), Quest(
            condition="eleanor_story == 35",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} You’ve reached the end of Eleanor’s current story content for now. Come back when Eleanor gets another story Update and support us on {a=https://www.patreon.com/TheRedPixel}{color=#c40e38}{b} Patreon {/b}{/color}{/a} if you’d like to \n {/size}{/font}{/color}")
        ),
    )
    QuestLog(
        "jada",
        text=_("Jada's Quest"),
    ).add(
        Quest(
            condition="jada_story == 0",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Buy the lens\n - Interact with the Scope again\n - Afterward, check the Attic and interact with \n the scope\n {/size}{/font}{/color}")
        ), Quest(
            condition="jada_story in (1, 2)",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} I should check the scope whenever !\n {/size}{/font}{/color}")
        ), Quest(
            condition="jada_story in (3, 4, 5, 6)",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} Visit the yoga room during weekends (Morning)\n {/size}{/font}{/color}")
        ), Quest(
            condition="jada_story == 9",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=27} You’ve reached the end of Jada's current story content for now. Come back when Jada gets another story Update and support us on {a=https://www.patreon.com/TheRedPixel}{color=#c40e38}{b} Patreon {/b}{/color}{/a} if you’d like to \n {/size}{/font}{/color}")
        ),
    )



    QuestLog(
        "sadiez",
        text=_("[sadie_refer_input]'s Info"),
    ).add(
        Quest(
            condition="sadie_info_1 == True",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=26} * My [sadie_refer_input], gets off work and comes back home early during the day on {color=#a60a15}Tuesdays, Thursdays, Fridays, and Saturdays.{/color} \n {/size}{/font}{/color}")
        ),

        Quest(
            condition="sadie_info_1 == True",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=26} * She Likes to watch TV at night on {color=#a60a15} Mondays, Wednesdays, and Thursdays{/color} \n {/size}{/font}{/color}")
        ),

        Quest(
            condition="sadie_info_1 == True",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=26} * She sometimes chills at the balcony during the day on {color=#a60a15} Tuesday, and Friday {/color} \n {/size}{/font}{/color}")
        ),

        Quest(
            condition="sadie_info_2 == True",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=26} * [sadie_refer_input] is awake in her room at night on {color=#a60a15} Monday, Wednesday, and Friday{/color}  \n {/size}{/font}{/color}")
        ),

    )

    QuestLog(
        "konamiz",
        text=_("Konami's Info"),
    ).add(
        Quest(
            condition="konami_info_1 == True",
            text=_("{color=#000000}{font=fonts/Mansalva-Regular.ttf}{size=26} She like to hang around at the treehouse . {/size}{/font}{/color}")
        ),
    )

screen inventorystuff():
    default tt = Tooltip("")
    default hh = Tooltip("")
    modal True
    zorder 1
    add "gui/inventory/inventory_menu_bg.jpg" xalign 0.5 yalign 0.5
    imagebutton:
        idle "gui/inventory/item_tab_idle.png"
        hover "gui/inventory/item_tab_hover.png"
        action [Show("inventorystuff")]
        xpos 30 ypos -4
    imagebutton:
        idle "gui/inventory/journel_btn_idle.png"
        hover "gui/inventory/journel_btn_hover.png"
        action [Hide("inventorystuff"), Show("journal_screen")]
        xpos 376 ypos -2
    imagebutton:
        idle "gui/inventory/map_btn_idle.png"
        hover "gui/inventory/map_btn_hover.png"
        action [Hide("inventorystuff"), Show("map_swap_scr")]
        xpos 723 ypos 5
    imagebutton:
        idle "gui/inventory/menu_btn_idle.png"
        hover "gui/inventory/menu_btn_hover.png"
        action [Hide("inventorystuff"), ShowMenu("navigation")]
        xpos 1065 ypos 3
    imagebutton:
        idle "gui/inventory/exit_btn_idle.png"
        hover "gui/inventory/exit_btn_hover.png"
        action [Hide("inventorystuff"), Show("main_hud_icon")]
        xpos 1407 ypos 2




    fixed:
        area (134,164,1265,848)
        viewport id "inventory_vp":
            mousewheel True
            draggable True
            has hbox:
                xmaximum 1200
                box_wrap True
            for item in inv:
                window:
                    style "slot"
                    imagebutton:
                        idle item.img
                        hover item.h_image

                        xpos 30
                        ypos 25
                        action NullAction()
                        hovered [tt.Action(item.desc), hh.Action(item.name)]

            for i in range(32 - len(inv)):
                frame:
                    style "slot"
        vbar:
            value YScrollValue("inventory_vp")
            base_bar "gui/scrollbar/scroll_bar_custom.png"
            thumb "gui/scrollbar/scroll_bar_thumbu.png"
            thumb_offset 37
            pos (-83, 4)
            xysize (43, 842)
    text tt.value pos (1390,445)
    text hh.value pos (1450,200)








style slot:
    background Frame("gui/inventory/slot_blocks.png", 0,0)
    maximum (299,247)
    minimum (299,247)


screen book_view():
    modal True
    zorder 2
    default page = 0
    if page == 0:
        use book_questlog()

    elif page == 1:
        use book_inventory()

    elif page == 2:
        use bookinfo_log()

    imagebutton:
        pos (1552, 81)
        focus_mask "gui/book/gui_journal_bookmark_quests.png"
        idle "gui/book/gui_journal_bookmark_quests.png"
        hover im.MatrixColor(
            "gui/book/gui_journal_bookmark_quests.png",
            im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)
        )
        action SetLocalVariable("page", 0)

    imagebutton:
        pos (1552, 399)
        focus_mask "gui/book/gui_journal_bookmark_items.png"
        idle "gui/book/gui_journal_bookmark_items.png"
        hover im.MatrixColor(
            "gui/book/gui_journal_bookmark_items.png",
            im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)
        )
        action SetLocalVariable("page", 1)


    imagebutton:
        pos (20, 746)
        focus_mask "gui/book/gui_journal_bookmark_notesinfo.png"
        idle "gui/book/gui_journal_bookmark_notesinfo.png"
        hover im.MatrixColor(
            "gui/book/gui_journal_bookmark_notesinfo.png",
            im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)
        )
        action SetLocalVariable("page", 2)

    imagebutton:
        pos (1552, 746)
        focus_mask "gui/book/gui_journal_bookmark_exit.png"
        idle "gui/book/gui_journal_bookmark_exit.png"
        hover im.MatrixColor(
            "gui/book/gui_journal_bookmark_exit.png",
            im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)
        )
        action Hide("book_view")

style healthui_red is text:
    size 34
    color "#000"
    font "fonts/Mansalva-Regular.ttf"

style inventoryfont_red is text:
    size 40
    color "#b82323"
    font "fonts/bookfont.ttf"

style questlog_font:
    size 45
    color "#a81b11"

    font "fonts/bookfont.ttf"



style infolog_font:
    size 45
    color "#a81b11"

    font "fonts/bookfont.ttf"


screen book_inventory():
    default selected_item = None
    fixed:
        fit_first True
        align (0.5, 0.5)
        add "gui/book/gui_inventory.png"
        side "r l":
            area (850, 205, 625, 685)
            viewport id "book_inventory":
                mousewheel True
                draggable True
                xsize 565
                has vbox
                for item in inv:
                    hbox:
                        fixed:
                            fit_first True
                            xysize (140, 150)
                            frame:
                                background None
                            imagebutton:
                                align (0.5, 0.5)
                                idle Transform(
                                    item.img,
                                    maxsize=(140, 96)
                                )
                                hover Transform(
                                    item.h_image
                                    or im.MatrixColor(
                                        item.img,
                                        im.matrix.desaturate() * im.matrix.tint(0.9, 0.9, 1.0)
                                    ), maxsize=(140, 96)
                                )
                                if selected_item is item:
                                    action SetLocalVariable("selected_item", None)
                                else:
                                    action SetLocalVariable("selected_item", item)
                        fixed:
                            fit_first True
                            xysize (345, 150)

                            frame:
                                background None
                            textbutton item.name.replace("inventoryfont", "inventoryfont_red"):
                                align (0.5, 0.5)
                                if selected_item is item:
                                    action SetLocalVariable("selected_item", None)
                                else:
                                    action SetLocalVariable("selected_item", item)
                        fixed:
                            fit_first True
                            xysize (80, 96)
                            frame:
                                background None
                            add "gui/book/gui_journal_checkbox.png" align (0.5, 0.5)
                            if selected_item is item:
                                add "gui/book/gui_journal_check.png" align (0.5, 0.5)
                    add "gui/book/item_grey_line.png"

            vbar value YScrollValue("book_inventory"):
                base_bar Transform(
                    "gui/book/gui_journal_scroller.png",
                    xsize=60
                )
                thumb Transform(
                    "gui/book/gui_journal_scrollerwheel.png",
                    xsize=60
                )
                xysize (60, 685)
                xpos 0
        if selected_item is not None:
            fixed:
                fit_first True
                area (245, 240, 500, 330)
                frame:
                    background None
                add selected_item.img maxsize (500, 330) align (0.5, 0.5)
            side "l r":
                area (265, 645, 465, 185)
                viewport id "item_description":
                    mousewheel True
                    draggable True
                    xsize 445
                    text selected_item.desc.replace("healthui", "healthui_red")
                vbar value YScrollValue("item_description"):
                    base_bar Transform(
                    "gui/book/gui_journal_scroller.png",
                        xsize=20
                    )
                    thumb Transform(
                        "gui/book/gui_journal_scrollerwheel.png",
                        xsize=20
                    )
                    xysize (20, 185)
                    xpos 0
                    unscrollable "hide"

screen book_questlog():
    default selected_quest = None
    default page = 0
    fixed:
        fit_first True
        align (0.5, 0.5)
        add "gui/book/gui_questlog_alt.png"
        side "r l":
            area (190, 210, 620, 680)
            viewport id "book_questlog":
                mousewheel True
                draggable True
                xsize 560
                has vbox
                for person in quest_log_active.persons:
                    hbox:
                        fixed:
                            fit_first True
                            xysize (92, 96)
                            frame:
                                background None
                            add "gui/book/gui_journal_checkbox.png" align (0.5, 0.5)
                            if selected_quest == person:
                                add "gui/book/gui_journal_fill.png" align (0.525, 0.5)
                            add "gui/book/item_grey_line.png"
                        fixed:
                            fit_first True
                            xysize (465, 96)
                            frame:
                                background None

                            textbutton defined_questlogs.get(person).text:
                                text_style "questlog_font"
                                align (0.1, 0.5)
                                if selected_quest is person:
                                    action (
                                        SetLocalVariable("selected_quest", None),
                                        SetLocalVariable("page", 0)
                                    )
                                else:
                                    action (
                                        SetLocalVariable("selected_quest", person),
                                        SetLocalVariable("page", 0)
                                    )
            vbar value YScrollValue("book_questlog"):
                base_bar Transform(
                    "gui/book/gui_journal_scroller.png",
                    xsize=60
                )
                thumb Transform(
                    "gui/book/gui_journal_scrollerwheel.png",
                    xsize=60
                )
                xysize (60, 680)
                xpos 0
        if selected_quest is not None:
            vbox:
                pos (835, 210)
                for en, task in enumerate(
                    defined_questlogs.get(selected_quest).opened[page * 4:(page + 1) *4]
                ):
                    side "l r":
                        area (
                            0,
                            0 if en in (1, 2) else (2 if en == 3 else -2),
                            640, 170
                        )
                        fixed:
                            fit_first True
                            xysize (555, 160)
                            frame:
                                background None
                            viewport id "quest_description_{0}".format(en):
                                mousewheel True
                                draggable True
                                xsize 535
                                text task.text
                            vbar value YScrollValue("quest_description_{0}".format(en)):
                                base_bar Transform(
                                "gui/book/gui_journal_scroller.png",
                                    xsize=20
                                )
                                thumb Transform(
                                    "gui/book/gui_journal_scrollerwheel.png",
                                    xsize=20
                                )
                                xysize (20, 160)
                                xpos 535
                                unscrollable "hide"
                        fixed:
                            fit_first True
                            xysize (80, 170)
                            frame:
                                background None
                            if task.is_complete:
                                add "gui/book/gui_journal_fill.png" align (0.525, 0.48)
            if page != 0:
                textbutton "Scroll back":
                    pos (870, 910)
                    text_font "fonts/Mansalva-Regular.ttf"
                    text_color "#000"
                    action SetLocalVariable("page", page - 1)
            if page < (
                len(
                    defined_questlogs.get(selected_quest).opened
                ) / 4.0 - 1
            ):
                textbutton "Scroll forward":
                    pos (1255, 910)
                    text_font "fonts/Mansalva-Regular.ttf"
                    text_color "#000"
                    action SetLocalVariable("page", page + 1)


screen bookinfo_log():
    default selected_quest = None
    default page = 0
    fixed:
        fit_first True
        align (0.5, 0.5)
        add "gui/book/gui_notesinfo_alt.png"
        side "r l":
            area (190, 210, 620, 680)
            viewport id "book_infolog":
                mousewheel True
                draggable True
                xsize 560
                has vbox
                for person in info_log_active.persons:
                    hbox:
                        fixed:
                            fit_first True
                            xysize (92, 96)
                            frame:
                                background None
                            add "gui/book/gui_journal_checkbox.png" align (0.5, 0.5)
                            if selected_quest == person:
                                add "gui/book/gui_journal_fill.png" align (0.525, 0.5)
                            add "gui/book/item_grey_line.png"
                        fixed:
                            fit_first True
                            xysize (465, 96)
                            frame:
                                background None
                            textbutton defined_infologs.get(person).text:
                                text_style "infolog_font"
                                align (0.1, 0.5)
                                if selected_quest is person:
                                    action (
                                        SetLocalVariable("selected_quest", None),
                                        SetLocalVariable("page", 0)
                                    )
                                else:
                                    action (
                                        SetLocalVariable("selected_quest", person),
                                        SetLocalVariable("page", 0)
                                    )
            vbar value YScrollValue("book_infolog"):
                base_bar Transform(
                    "gui/book/gui_journal_scroller.png",
                    xsize=60
                )
                thumb Transform(
                    "gui/book/gui_journal_scrollerwheel.png",
                    xsize=60
                )
                xysize (60, 680)
                xpos 0
        if selected_quest is not None:
            vbox:
                pos (835, 210)
                for en, task in enumerate(
                    defined_infologs.get(selected_quest).opened[page * 4:(page + 1) *4]
                ):
                    side "l r":
                        area (
                            0,
                            0 if en in (1, 2) else (2 if en == 3 else -2),
                            640, 170
                        )
                        fixed:
                            fit_first True
                            xysize (555, 160)
                            frame:
                                background None
                            viewport id "quest_description_{0}".format(en):
                                mousewheel True
                                draggable True
                                xsize 535
                                text task.text
                            vbar value YScrollValue("quest_description_{0}".format(en)):
                                base_bar Transform(
                                "gui/book/gui_journal_scroller.png",
                                    xsize=20
                                )
                                thumb Transform(
                                    "gui/book/gui_journal_scrollerwheel.png",
                                    xsize=20
                                )
                                xysize (20, 160)
                                xpos 535
                                unscrollable "hide"
                        fixed:
                            fit_first True
                            xysize (80, 160)
                            frame:
                                background None


            if page != 0:
                textbutton "Scroll back":
                    pos (870, 910)
                    text_font "fonts/Mansalva-Regular.ttf"
                    text_color "#000"
                    action SetLocalVariable("page", page - 1)
            if page < (
                len(
                    defined_infologs.get(selected_quest).opened
                ) / 4.0 - 1
            ):
                textbutton "Scroll forward":
                    pos (1255, 910)
                    text_font "fonts/Mansalva-Regular.ttf"
                    text_color "#000"
                    action SetLocalVariable("page", page + 1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

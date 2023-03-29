# Register the submod
init -990 python in mas_submod_utils:
    Submod(
        author="wowm",
        name="Reactions",
        description="Some more things for Monika to react to.",
        version="1.0.0"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Reactions",
            user_name="wowm03",
            repository_name="wowm_reactions",
            submod_dir="/Submods",
            extraction_depth=2
        )

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_notion",
            category=["Notion"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_notion:
    python:
        notion_quips = [
            "Dropping down some notes? [player]?",
            "Looking good! :)",
            "That's really neat... keep it up! <3",
            "Hmm.. maybe I can take a peak at your journal... hehe, just kidding!",
            "What are you writing? [player]?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            notion_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_notion')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_lifeat",
            category=["lifeat.io"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_lifeat:
    python:
        lifeat_quips = [
            "That's a nice background you have there, [player]!",
            "Good luck with your work! [player]!",
            "Would you share a room with me and study together? <3"
        ]

        wrs_success = mas_display_notif(
            m_name,
            lifeat_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_lifeat')
    return


init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ao3",
            category=["archiveofourown"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ao3:
    python:
        ao3_quips = [
            "What are you reading? [player]?",
            "They're really talented writers, aren't they?"
            "Enjoying yourself, [player]? Hehe, I'm glad! <3"
            "Oooo, that's looking good..."
        ]

        wrs_success = mas_display_notif(
            m_name,
            ao3_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ao3')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_anki",
            category=["Anki"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_anki:
    python:
        anki_quips = [
            "Is it working well for you?",
            "Good luck!",
            "Do you know the answer..? :0",
            "Stay focus! ^^",
            "Keep going!"
        ]

        wrs_success = mas_display_notif(
            m_name,
            anki_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_anki')
    return


init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gc",
            category=["classroom.google"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gc:
    python:
        gc_quips = [
            "What classes did you join?",
            "Check if you have any assigned assignments!",
            "I better not see a missing assignment...",
            "What's that class about?",
            "Are you the teacher or the student?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            gc_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_gc')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_webtoon",
            category=["webtoons.com"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_webtoon:
    python:
        webtoon_quips = [
            "What are you reading? :0",
            "That looks interesting!",
            "What's popular on there?",
            "Mind if I take a peek at your subscribed? Hehe",
            "{i}whispering:{/i} I recommend Omniscient Reader's Viewpoint and The World After the Fall!",
            "What would you recommend me to read?"
        ]

        wrs_success = mas_display_notif(
            m_name,
            webtoon_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_webtoon')
    return

init 10 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tl",
            category=["translate.google"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tl:
    python:
        tl_quips = [
            "Translate this! kanada liefert energiesicherheit und klimaschutz",
            "Do you know what this means..? 親愛的?",
            "حبيبي~",
            "mahal kita!",
            "それはいいね!"
        ]

        wrs_success = mas_display_notif(
            m_name,
            tl_quips,
            'Window Reactions'
        )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_tl')
    return

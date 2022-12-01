#init python:
#    config.rollback_enabled = False

# Определение персонажей игры
define author = Character(None)
define grisha = Character('Гриша', color="#4682B4",callback = name_callback, cb_name = "grisha")
define angelina = Character('Ангелина', color="#DB7093", image ='angelina',  callback = name_callback, cb_name = "angelina")
define lyonya = Character('Лёня', color="#32CD32", image ='lyonya', callback = name_callback, cb_name = "lyonya")
define valya = Character('Валя', color="#FF8C00", image ='valya', callback = name_callback, cb_name = "valya")
define girl = Character('Девушка', color="#FF8C00", image ='girl', callback = name_callback, cb_name = "girl")
define boy = Character('Парень', color="#32CD32", image ='boy', callback = name_callback, cb_name = "boy")
define barman = Character('Бармен', color="#888888", image ='barman', callback = name_callback, cb_name = "barman")
define abuser = Character('Обидчик', color="#888888", image ='abuser', callback = name_callback, cb_name = "abuser")
define defender = Character('Защитник', color="#888888", image ='defender', callback = name_callback, cb_name = "defender")
define sanya = Character('Саня', color="#888888", image ='sanya', callback = name_callback, cb_name = "sanya")
define pryamorukov = Character('Пряморуков', color="#ffffff", image ='pryamorukov', callback = name_callback, cb_name = "pryamorukov")
define fichaev = Character('Фичаев', color="#ffffff", image ='fichaev', callback = name_callback, cb_name = "fichaev")
define potemkin = Character('Потемкин', color="#ffffff", image ='potemkin', callback = name_callback, cb_name = "potemkin")
define roommate = Character('Соседка', color="#888888", image ='roommate', callback = name_callback, cb_name = "roommate")
define aslan = Character('Аслан', color="#ffd966", image ='aslan', callback = name_callback, cb_name = "aslan")
define kostya = Character('Костя', color="#888888", image ='kostya', callback = name_callback, cb_name = "kostya")
define boy_club = Character('Парень', color="#888888", image ='boy_club', callback = name_callback, cb_name = "boy_club")
define girl_club = Character('Девушка', color="#888888", image ='girl_club', callback = name_callback, cb_name = "girl_club")
define studman = Character('Чувак из студсовета', color="#888888", image ='studman', callback = name_callback, cb_name = "studman")
define alina = Character('Алина', color="#de62df", image ='alina',  callback = name_callback, cb_name = "alina")
define gay = Character('Парень', color="#caedff", image ='gay',  callback = name_callback, cb_name = "gay")
define coach = Character('Тренер', color="#888888", image ='coach',  callback = name_callback, cb_name = "coach")
define zhurkin = Character('Журкин', color="#888888", image ='zhurkin',  callback = name_callback, cb_name = "zhurkin")
define sokratova = Character('Сократова', color="#888888", image ='sokratova',  callback = name_callback, cb_name = "sokratova")

# Черты характера Гриши
define grisha_smart = False
define grisha_attentive = False
define grisha_romantic = False
define grisha_kind = False

# Ключевые баллы
define difficult = False
define screamer = False
define ang_score = 0
define lyonya_score = 0
define undergraduate = False
define valya_score = 0
define exam_score = 0
define diplom = 0
define detective = False
define time_detective = False
define alina_score = 0
define dance_partner_ang = False
define dance_partner_alina = False
define love = False
define best_end = 0
define worth_end = 0

# Баллы экзаменов
define exam_pryam_1q = False
define exam_pryam_2q = False
define exam_pryam_3q = False
define exam_fich_1q = False
define exam_fich_2q = False
define exam_fich_3q = False
define exam_music_1 = False
define exam_music_2 = False
define exam_music_3 = False
define exam_cinema_1 = False
define exam_cinema_2 = False
define exam_cinema_3 = False
define exam_internet_1 = False
define exam_internet_2 = False
define exam_internet_3 = False
define exam_potemkin = 0
define call_lyonya = False
define fifty_fifty = False
define gosexam = 0

# Таймер
define time = 0
define timer_range = 0
define timer_jump = 0
define timer_score = False

# Музыка и звуки
define audio.neutral_1 = "/music/neutral_1.mp3"
define audio.neutral_2 = "/music/neutral_2.mp3"
define audio.neutral_3 = "/music/neutral_3.mp3"
define audio.neutral_4 = "/music/neutral_4.mp3"
define audio.disco_1 = "/music/disco_1.mp3"
define audio.disco_2 = "/music/disco_2.mp3"
define audio.fighting = "/music/fighting.mp3"
define audio.detectiv = "/music/detectiv.mp3"
define audio.knock_knock = "/music/knock_knock.mp3"
define audio.door = "/music/door.mp3"
define audio.close_door = "/music/close_door.mp3"
define audio.oxxxymiron = "/music/oxxxymiron.mp3"
define audio.cringe = "/music/cringe.mp3"
define audio.disturb = "/music/disturb.mp3"
define audio.sad = "/music/sad.mp3"
define audio.sigame = "/music/sigame.mp3"
define audio.answer_wrong = "/music/answer_wrong.mp3"
define audio.applause = "/music/applause.mp3"
define audio.zemfira = "/music/zemfira.mp3"
define audio.lp = "/music/lp.mp3"
define audio.gradusy = "/music/gradusy.mp3"
define audio.medlyak = "/music/medlyak.mp3"
define audio.waltz = "/music/waltz.mp3"
define audio.solemn = "/music/solemn.mp3"
define audio.mill_start = "/music/mill_start.mp3"
define audio.mill_ques = "/music/mill_ques.mp3"
define audio.mill_right = "/music/mill_right.mp3"
define audio.mill_wrong = "/music/mill_wrong.mp3"
define audio.mill_call = "/music/mill_call.mp3"

# Инициализация файлов
init:
    # Инициализация фонов
    # 1 сентября
    image bg_vk_lenta = "/background/1_september/vk_phone_lenta.jpg"
    image bg_lock_screen = "/background/1_september/lock_screen.jpg"
    image central_entrance = "/background/1_september/central_entrance.jpg"
    image bg_doors = "/background/1_september/doors.jpg"
    image phone_map = "/background/1_september/phone_map.png"
    image aud = "/background/1_september/auditorium.jpg"
    image black = "/background/1_september/black.jpg"
    image art_demo = "/background/1_september/art_demo.jpg"

    # 1 курс
    image bg_autumn = "/background/1_year/autumn.jpg"
    image central_entrance_blur = "/background/1_september/central_entrance_blur.jpg"
    image club = "/background/1_year/club.jpg"
    image dance_floor = "/background/1_year/dance_floor.jpg"
    image bar_ = "/background/1_year/bar.jpg"
    image bar_blur = "/background/1_year/bar_blur.jpg"
    image before_aud = "/background/1_year/before_aud.jpg"
    image before_aud_blur = "/background/1_year/before_aud_blur.jpg"
    image aud_blur = "/background/1_september/auditorium_blur.jpg"
    image shop = "/background/1_year/shop.jpg"
    image tables = "/background/1_year/tables.jpg"
    image art_1_year = "/background/1_september/art_demo.jpg"

    # Экзамен Пряморукова
    image exam_pryam_start = "/background/1_year/exam_pryam_start.jpg"
    image exam_pryam_2_3_grisha_full_pryam = "/background/1_year/exam_pryam_2_3_grisha_full_pryam.jpg"
    image exam_pryam_full_grisha_2_3_pryam = "/background/1_year/exam_pryam_full_grisha_2_3_pryam.jpg"
    image exam_pryam_1_3_grisha_full_pryam = "/background/1_year/exam_pryam_1_3_grisha_full_pryam.jpg"
    image exam_pryam_full_grisha_1_3_pryam = "/background/1_year/exam_pryam_full_grisha_1_3_pryam.jpg"
    image exam_pryam_2_3_grisha_2_3_pryam = "/background/1_year/exam_pryam_2_3_grisha_2_3_pryam.jpg"
    image exam_pryam_0_grisha_full_pryam = "/background/1_year/exam_pryam_0_grisha_full_pryam.jpg"
    image exam_pryam_1_3_grisha_2_3_pryam = "/background/1_year/exam_pryam_1_3_grisha_2_3_pryam.jpg"
    image exam_pryam_2_3_grisha_1_3_pryam = "/background/1_year/exam_pryam_2_3_grisha_1_3_pryam.jpg"
    image exam_pryam_full_grisha_0_pryam = "/background/1_year/exam_pryam_full_grisha_0_pryam.jpg"
    image q3_pryam = "/background/1_year/q3_pryam.png"

    # Экзамен Фичаева
    image exam_fich_start = "/background/1_year/exam_fich_start.jpg"
    image exam_fich_2_3_grisha_full_fich = "/background/1_year/exam_fich_2_3_grisha_full_fich.jpg"
    image exam_fich_full_grisha_2_3_fich = "/background/1_year/exam_fich_full_grisha_2_3_fich.jpg"
    image exam_fich_1_3_grisha_full_fich = "/background/1_year/exam_fich_1_3_grisha_full_fich.jpg"
    image exam_fich_full_grisha_1_3_fich = "/background/1_year/exam_fich_full_grisha_1_3_fich.jpg"
    image exam_fich_2_3_grisha_2_3_fich = "/background/1_year/exam_fich_2_3_grisha_2_3_fich.jpg"
    image exam_fich_0_grisha_full_fich = "/background/1_year/exam_fich_0_grisha_full_fich.jpg"
    image exam_fich_1_3_grisha_2_3_fich = "/background/1_year/exam_fich_1_3_grisha_2_3_fich.jpg"
    image exam_fich_2_3_grisha_1_3_fich = "/background/1_year/exam_fich_2_3_grisha_1_3_fich.jpg"
    image exam_fich_full_grisha_0_fich = "/background/1_year/exam_fich_full_grisha_0_fich.jpg"
    image q2_fich = "/background/1_year/q2_fich.png"

    # 2 курс
    image bg_winter = "/background/2_year/winter.jpg"
    image entance = "/background/2_year/entrance.jpg"
    image door = "/background/2_year/door.jpg"
    image aslan_apartment = "/background/2_year/aslan_apartment.jpg"
    image street = "/background/2_year/street.jpg"
    image street_2 = "/background/2_year/street_2.jpg"
    image photo_valya = "/background/2_year/photo_valya.png"
    image virgin_club = "/background/2_year/virgin_club.jpg"
    image club_unitech = "/background/2_year/club_unitech.jpg"
    image art_2_year_cool = "/background/1_september/art_demo.jpg"
    image art_2_year_sad = "/background/1_september/art_demo.jpg"
    image screen_george = "/background/2_year/screen_george.png"

    # 3 курс
    image tablo = "/background/3_year/tablo.png"
    image tablo_music_1 = "/background/3_year/tablo_music_1.png"
    image tablo_music_2 = "/background/3_year/tablo_music_2.png"
    image tablo_music_3 = "/background/3_year/tablo_music_3.png"
    image tablo_cinema_1 = "/background/3_year/tablo_cinema_1.png"
    image tablo_cinema_2 = "/background/3_year/tablo_cinema_2.png"
    image tablo_cinema_3 = "/background/3_year/tablo_cinema_3.png"
    image tablo_internet_1 = "/background/3_year/tablo_internet_1.png"
    image tablo_internet_2 = "/background/3_year/tablo_internet_2.png"
    image tablo_internet_3 = "/background/3_year/tablo_internet_3.png"
    image forest = "/background/3_year/forest.jpg"
    image plakat = "/background/3_year/plakat.png"
    image viktorina = "/background/3_year/viktorina.jpg"
    image cafe = "/background/3_year/cafe.jpg"
    image baz = "/background/3_year/baz.jpg"
    image flower_store = "/background/3_year/flower_store.jpg"
    image art_3_year_ang_win = "/background/1_september/art_demo.jpg"
    image art_3_year_defeat = "/background/1_september/art_demo.jpg"
    image art_3_year_alina_win = "/background/1_september/art_demo.jpg"

    # 4 курс
    image park = "/background/4_year/park.jpg"
    image mill_1_ques = "/background/4_year/mill_1_ques.png"
    image mill_2_ques = "/background/4_year/mill_2_ques.png"
    image mill_3_ques = "/background/4_year/mill_3_ques.png"
    image mill_4_ques = "/background/4_year/mill_4_ques.png"
    image mill_5_ques = "/background/4_year/mill_5_ques.png"
    image mill_1_ques_50 = "/background/4_year/mill_1_ques_50.png"
    image mill_2_ques_50 = "/background/4_year/mill_2_ques_50.png"
    image mill_3_ques_50 = "/background/4_year/mill_3_ques_50.png"
    image mill_4_ques_50 = "/background/4_year/mill_4_ques_50.png"
    image mill_5_ques_50 = "/background/4_year/mill_5_ques_50.png"
    image ring = "/background/4_year/ring.png"
    image art_best_end = "/background/4_year/art_best_end.jpg"
    image art_neutral_end = "/background/4_year/art_neutral_end.jpg"
    image art_neutral_end_valya = "/background/4_year/art_neutral_end_valya.jpg"
    image art_bad_end = "/background/4_year/art_bad_end.jpg"

    # Инициализация спрайтов
    # Ангелина
    image ang_usual = At("/sprites/angelina/angelina_usual.png", sprite_highlight('angelina'))
    image ang_angry = At("/sprites/angelina/angelina_angry.png", sprite_highlight('angelina'))
    #image ang_usual_winter = At("/sprites/angelina/angelina_usual_winter.png", sprite_highlight('angelina'))
    #image ang_funny = At("/sprites/angelina/angelina_funny.png", sprite_highlight('angelina'))
    #image ang_sad = At("/sprites/angelina/angelina_sad.png", sprite_highlight('angelina'))
    #image ang_happiness = At("/sprites/angelina/angelina_happiness.png", sprite_highlight('angelina'))
    #image ang_annoy = At("/sprites/angelina/angelina_annoy.png", sprite_highlight('angelina'))
    #image ang_usual_dress = At("/sprites/angelina/angelina_usual_dress.png", sprite_highlight('angelina'))
    #image ang_happiness_dress = At("/sprites/angelina/angelina_happiness_dress.png", sprite_highlight('angelina'))
    #image ang_sad_dress = At("/sprites/angelina/angelina_sad_dress.png", sprite_highlight('angelina'))

    # Лёня
    image lyonya_usual = At("/sprites/lyonya/lyonya_usual.png", sprite_highlight('lyonya'))
    image lyonya_confused = At("/sprites/lyonya/lyonya_confused.png", sprite_highlight('lyonya'))
    #image lyonya_confused_winter = At("/sprites/lyonya/lyonya_confused_winter.png", sprite_highlight('lyonya'))
    #image lyonya_emotional = At("/sprites/lyonya/lyonya_emotional.png", sprite_highlight('lyonya'))
    #image lyonya_emotional_winter = At("/sprites/lyonya/lyonya_emotional_winter.png", sprite_highlight('lyonya'))
    #image lyonya_happiness = At("/sprites/lyonya/lyonya_happiness.png", sprite_highlight('lyonya'))
    #image lyonya_angry = At("/sprites/lyonya/lyonya_angry.png", sprite_highlight('lyonya'))
    #image lyonya_angry_winter = At("/sprites/lyonya/lyonya_angry_winter.png", sprite_highlight('lyonya'))
    #image lyonya_sad = At("/sprites/lyonya/lyonya_sad.png", sprite_highlight('lyonya'))
    #image lyonya_usual_suit = At("/sprites/lyonya/lyonya_usual_suit.png", sprite_highlight('lyonya'))
    image boy_usual = At("/sprites/lyonya/lyonya_usual.png", sprite_highlight('boy'))

    # Валя
    image valya_usual = At("/sprites/valya/valya_usual.png", sprite_highlight('valya'))
    #image valya_hypnosis = At("/sprites/valya/valya_hypnosis.png", sprite_highlight('valya'))
    #image valya_annoy = At("/sprites/valya/valya_annoy.png", sprite_highlight('valya'))
    image girl_usual = At("/sprites/valya/valya_usual.png", sprite_highlight('girl'))

    # Второстепенные персонажи
    image defender = At("/sprites/sanya/sanya_angry.png", sprite_highlight('defender'))
    image sanya_angry = At("/sprites/sanya/sanya_angry.png", sprite_highlight('sanya'))
    image sanya_usual = At("/sprites/sanya/sanya_usual.png", sprite_highlight('sanya'))
    image barman = At("/sprites/other/barman.png", sprite_highlight('barman'))
    image abuser = At("/sprites/other/abuser.png", sprite_highlight('abuser'))
    #image aslan = At("/sprites/other/aslan.png", sprite_highlight('aslan'))
    #image kostya_usual = At("/sprites/other/kostya_usual.png", sprite_highlight('kostya'))
    #image kostya_phone = At("/sprites/other/kostya_phone.png", sprite_highlight('kostya'))
    #image girl_club = At("/sprites/other/girl_club.png", sprite_highlight('girl_club'))
    #image potemkin_usual = At("/sprites/potemkin/potemkin_usual.png", sprite_highlight('potemkin'))
    #image studman = At("/sprites/other/studman.png", sprite_highlight('studman'))
    #image gay = At("/sprites/other/gay.png", sprite_highlight('gay'))
    #image zhurkin = At("/sprites/other/zhurkin.png", sprite_highlight('zhurkin'))
    #image sokratova = At("/sprites/other/sokratova.png", sprite_highlight('sokratova'))

    # Пряморуков
    #image pryamorukov_usual = At("/sprites/pryamorukov/pryamorukov_usual.png", sprite_highlight('pryamorukov'))
    #image pryamorukov_angry = At("/sprites/pryamorukov/pryamorukov_angry.png", sprite_highlight('pryamorukov'))
    #image pryamorukov_wound = At("/sprites/pryamorukov/pryamorukov_wound.png", sprite_highlight('pryamorukov'))

    # Фичаев
    #image fichaev_usual = At("/sprites/fichaev/fichaev_usual.png", sprite_highlight('fichaev'))
    #image fichaev_sad = At("/sprites/fichaev/fichaev_sad.png", sprite_highlight('fichaev'))
    #image fichaev_wound = At("/sprites/fichaev/fichaev_wound.png", sprite_highlight('fichaev'))

    # Алина
    #image alina_usual = At("/sprites/alina/alina_usual.png", sprite_highlight('alina'))
    #image alina_usual_dress = At("/sprites/alina/alina_usual_dress.png", sprite_highlight('alina'))
    #image alina_sad = At("/sprites/alina/alina_sad.png", sprite_highlight('alina'))

# Main
label start:
    call first_september
    call first_year
    call second_year
    call third_year
    call fourth_year
    return

transform alpha_dissolve:
    alpha 0.0
    linear 0.01 alpha 1.0
    on hide:
        linear 0.01 alpha 0

# Определение персонажей игры
define author = Character(None)
define grisha = Character('Гриша', color="#4682B4")
define angelina = Character('Ангелина', color="#DB7093", image ='angelina',  callback = name_callback, cb_name = "angelina")
define lyonya = Character('Лёня', color="#32CD32", image ='lyonya', callback = name_callback, cb_name = "lyonya")
define valya = Character('Валя', color="#FF8C00", image ='valya', callback = name_callback, cb_name = "valya")
define girl = Character('Девушка', color="#FF8C00", image ='girl', callback = name_callback, cb_name = "girl")
define boy = Character('Парень', color="#32CD32", image ='boy', callback = name_callback, cb_name = "boy")
define barman = Character('Бармен', color="#888888", image ='barman', callback = name_callback, cb_name = "barman")
define abuser = Character('Обидчик', color="#888888", image ='abuser', callback = name_callback, cb_name = "abuser")
define defender = Character('Защитник', color="#888888", image ='defender', callback = name_callback, cb_name = "defender")
define sanya = Character('Саня', color="#888888", image ='sanya', callback = name_callback, cb_name = "sanya")

# Черты характера Гриши
define grisha_smart = False
define grisha_attentive = False
define grisha_romantic = False
define grisha_kind = False

# Ключевые баллы
define screamer = False
define ang_score = 0
define lyonya_score = 0
define undergraduate = False
define valya_score = 0
define exam_score = 0
define diplom = 0
define exam_pryam_1q = False
define exam_pryam_2q = False
define exam_pryam_3q = False

# Музыка и звуки
define audio.neutral_1 = "/music/neutral_1.mp3"
define audio.neutral_2 = "/music/neutral_2.mp3"
define audio.disco_1 = "/music/disco_1.mp3"
define audio.disco_2 = "/music/disco_2.mp3"
define audio.fighting = "/music/fighting.mp3"

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
    image art_demo = "/background/1_september/art.jpg"

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

    # Инициализация спрайтов
    # Спрайты Ангелины
    image ang_usual = At("/sprites/angelina/angelina_usual.png", sprite_highlight('angelina'))
    image ang_angry = At("/sprites/angelina/angelina_angry.png", sprite_highlight('angelina'))

    # Спрайты Лёни
    image lyonya_usual = At("/sprites/lyonya/lyonya_usual.png", sprite_highlight('lyonya'))
    image lyonya_confused = At("/sprites/lyonya/lyonya_confused.png", sprite_highlight('lyonya'))
    image boy_usual = At("/sprites/lyonya/lyonya_usual.png", sprite_highlight('boy'))

    # Спрайты Вали
    image valya_usual = At("/sprites/valya/valya_usual.png", sprite_highlight('valya'))
    image girl_usual = At("/sprites/valya/valya_usual.png", sprite_highlight('girl'))

    # Спрайты Сани
    image defender = At("/sprites/sanya/sanya_angry.png", sprite_highlight('defender'))
    image sanya_angry = At("/sprites/sanya/sanya_angry.png", sprite_highlight('sanya'))
    image sanya_usual = At("/sprites/sanya/sanya_usual.png", sprite_highlight('sanya'))

    # Второстепенные персонажи
    image barman = At("/sprites/other/barman.png", sprite_highlight('barman'))
    image abuser = At("/sprites/other/abuser.png", sprite_highlight('abuser'))

    # Пряморуков
    image pryamorukov_usual = At("/sprites/pryamorukov/pryamorukov_usual.png", sprite_highlight('pryamorukov'))
    image pryamorukov_angry = At("/sprites/pryamorukov/pryamorukov_angry.png", sprite_highlight('pryamorukov'))
    image pryamorukov_wound = At("/sprites/pryamorukov/pryamorukov_wound.png", sprite_highlight('pryamorukov'))

# Main
label start:
    call first_september
    call first_year
    return

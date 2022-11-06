# Определение персонажей игры
define author = Character(None)
define grisha = Character('Гриша', color="#4682B4")
define angelina = Character('Ангелина', color="#DB7093", image ='angelina',  callback = name_callback, cb_name = "angelina")
define lyonya = Character('Лёня', color="#32CD32", image ='lyonya', callback = name_callback, cb_name = "lyonya")
define valya = Character('Валя', color="#FF8C00", image ='valya', callback = name_callback, cb_name = "valya")
define girl = Character('Девушка', color="#FF8C00", image ='girl', callback = name_callback, cb_name = "girl")
define boy = Character('Парень', color="#32CD32", image ='boy', callback = name_callback, cb_name = "boy")

# Черты характера Гриши
define grisha_smart = False
define grisha_attentive = False
define grisha_romantic = False
define grisha_kind = False

# Ключевые баллы
define screamer = False
define ang_score = 0

# Музыка и звуки
define audio.neutral_1 = "/music/neutral_1.mp3"

# Инициализация файлов
init:
    # Инициализация фонов
    image bg_vk_lenta = "/background/1_september/vk_phone_lenta.jpg"
    image bg_lock_screen = "/background/1_september/lock_screen.jpg"
    image central_entrance = "/background/1_september/central_entrance.jpg"
    image bg_doors = "/background/1_september/doors.jpg"
    image phone_map = "/background/1_september/phone_map.png"
    image aud = "/background/1_september/auditorium.jpg"
    image black = "/background/1_september/black.jpg"
    image art_demo = "/background/1_september/art.jpg"


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

# Main
label start:
    call first_september
    return

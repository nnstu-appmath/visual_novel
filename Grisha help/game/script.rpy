# Определение персонажей игры
define grisha = Character('Гриша', color="#4682B4")
define angelina = Character('Ангелина', color="#DB7093")
define lyonya = Character('Лёня', color="#32CD32")
define valya = Character('Валя', color="#FF8C00")

# Черты характера Гриши
define grisha_smart = False
define grisha_attentive = False
define grisha_romantic = False
define grisha_kind = False

# Инициализация файлов
init:
    # Инициализация фонов
    image bg_vk_lenta = "/background/1_september/vk_phone_lenta.jpg"
    image bg_lock_screen = "/background/1_september/lock_screen.jpg"

    # Инициализация спрайтов
    # Спрайты Ангелины

    # Спрайты Лёни

    # Спрайты Вали

# Main
label start:
    jump first_september
    return

# 1 сентября - демо
label first_september:
    jump scene_1
    return

# Сцена 1 - Гриша дома
label scene_1:
    scene bg_vk_lenta
    with fade
    grisha "О, тест \"какая ты свинка по жизни\". Надо пройти."
    "*тык*"
    menu:
        "Какая ты свинка?"
        "Умный чел. Интеллектуальный":
            $ grisha_smart = True
        "Внимательный чел. Наблюдательный":
            $ grisha_attentive = True
        "Романтичный чел. Созерцательный":
            $ grisha_romantic = True
        "Добрый чел. Позитивный":
            $ grisha_kind = True
    scene bg_lock_screen
    with fade
    grisha "Класс. Ой-й-й, я уже опаздываю, по-моему."
    return

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

#Ключевые баллы
define screamer = False
define ang_score = 0

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
    image ang_usual = "/sprites/angelina/usual.png"
    image ang_angry = "/sprites/angelina/angry.png"
    # Спрайты Лёни
    image lyonya_usual = "/sprites/lyonya/usual.png"
    # Спрайты Вали
    image valya_usual = "/sprites/valya/usual.png"

# Main
label start:
    call first_september
    return

# 1 сентября - демо
label first_september:
    call scene_1
    call scene_2
    call scene_3
    call scene_4
    call scene_5
    "Спасибо за прохождение демо-версии игры!"
    scene black with fade
    pause (2.0)
    return

# Сцена 1 - Гриша дома
label scene_1:
    pause(1.0)
    scene bg_vk_lenta with fade
    grisha "О, тест \"какая ты свинка по жизни\". Надо пройти."
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
    scene bg_lock_screen with fade
    grisha "Класс. Ой-й-й, я уже опаздываю, по-моему."
    return

#Сцена 2 - Гриша сбивает Ангелину
label scene_2:
    scene central_entrance with fade
    "Стоит теплый осенний денек. Гриша бежит на собрание 1 сентября,
    ведь он сильно опаздывает и уже пропустил торжественную линейку.
    При входе на лестнице Гриша случайно задевает девушку, которая из-за
    него роняет телефон."
    show ang_usual with dissolve
    if grisha_kind:
        grisha "Ой, извини, пожалуйста, не хотел"
        $ ang_score += 1
        angelina "Ничего страшного"
        grisha "Не разбился?"
        angelina "Нет, все хорошо"
    else:
        menu:
            "Что ответить ей?"
            "Гриша: Ой, извини, пожалуйста, не хотел":
                $ ang_score += 1
                angelina "Ничего страшного"
                grisha "Не разбился?"
                angelina "Нет, все хорошо"
            "Молча пробежать":
                pass
            "Гриша: В телефоне меньше залипай":
                hide ang_usual
                show ang_angry
                angelina "Сама разберусь!"
    hide ang_angry
    return

#Сцена 3 - лабиринт из дверей
label scene_3:
    show bg_doors with fade
    show phone_map at left with dissolve
    grisha "Так, а какая аудитория? 31-А-56. Боже, что это и где это?
    Налево, направо, прямо, налево, направо, прямо. Кому нужны эти карты?
    Сам найду."
    hide phone_map
    call doors_1
    return

label doors_1:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            call doors_2
        "Прямо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_1
        "Направо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_1
    return

label doors_2:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_2
        "Прямо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_2
        "Направо":
            call doors_3
    return

label doors_3:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_3
        "Прямо":
            call doors_4
        "Направо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_3
    return

label doors_4:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            call doors_5
        "Прямо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_4
        "Направо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_4
    return

label doors_5:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_5
        "Прямо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_5
        "Направо":
            call doors_6
    return

label doors_6:
    scene bg_doors with fade
    menu:
        "Куда пойти?"
        "Налево":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_6
        "Прямо":
            return
        "Направо":
            if renpy.random.randint(1, 20) == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_6
    return

label scream:
    $ screamer = True
    scene black with fade
    grisha "Так, мне ЯВНО не сюда..."
    $ renpy.movie_cutscene("/images/background/1_september/screamer.mpeg")
    return

label wrong_way:
    with fade
    grisha "Так, не сюда, вернусь, пожалуй"
    return

#Сцена 4 - Гриша встречает Лёню и Валю
label scene_4:
    scene aud with fade
    "Гриша нашел аудиторию, но похоже, что большинство уже разошлось.
    Оставшиеся ребята собирают свои вещи."
    grisha "Э-э-э, привет?"
    show valya_usual at right
    with dissolve
    Character('Девушка', color="#FF8C00") "Привет, ты кто?"
    grisha "Дэ-э-э, я - Гриша Орехов, у меня тут вообще собрание должно быть...
    э-э-э, организационное..."
    show lyonya_usual at left
    with dissolve
    Character('Парень', color="#32CD32") "Оно уже закончилось, ты малясь опоздал."
    grisha "Черт. Я многое пропустил? Что было?"
    Character('Девушка', color="#FF8C00") "Рассказали про обучение, про
    специальность. Старшекурсники поделились инфой, что на сессии надо драться
    с преподами"
    grisha "Чего-о-о?"
    Character('Парень', color="#32CD32") "Хотя я не верю этому. Кстати,
    меня Лёня зовут."
    Character('Девушка', color="#FF8C00") "А я Валя."
    grisha "Приятно познакомиться. Ладно, я пожалуй пойду тогда."
    lyonya "Встретимся на парах."
    grisha "Угу, до встречи."
    return

#Сцена 5 - Конец демо
label scene_5:
    scene central_entrance with fade
    grisha "Ну и денек, конечно. Что ж будет дальше в этом унитехе..."
    scene art_demo with fade
    $ renpy.notify("Вы прошли эпизод \"1 сентября\"")
    return

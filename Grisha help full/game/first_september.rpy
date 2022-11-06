# 1 сентября
label first_september:
    call scene_1
    call scene_2
    call scene_3
    call scene_4
    call scene_5
    scene black with fade
    pause (2.0)
    return

# Сцена 1 - Гриша дома
label scene_1:
    scene black with fade
    author "Выберите уровень сложности"
    menu:
            "Все в твоих руках":
                $ difficult = True
            "Характер решает все":
                $ difficult = False
    pause(1.0)
    if difficult:
        pass
    else:
        scene bg_vk_lenta with fade
        play music neutral_1 fadein 1
        grisha "О, тест \"какая ты свинка по жизни\". Надо пройти."
        menu:
            "Умный чел. Интеллектуальный":
                $ grisha_smart = True
            "Внимательный чел. Наблюдательный":
                $ grisha_attentive = True
            "Романтичный чел. Созерцательный":
                $ grisha_romantic = True
            "Добрый чел. Позитивный":
                $ grisha_kind = True
    scene bg_lock_screen with fade
    grisha "Ой-й-й, я уже опаздываю, по-моему."
    return

#Сцена 2 - Гриша сбивает Ангелину
label scene_2:
    scene central_entrance with fade
    author "Стоит теплый осенний денек. Гриша бежит на собрание 1 сентября,
    ведь он сильно опаздывает и уже пропустил торжественную линейку.
    При входе на лестнице Гриша случайно задевает девушку, которая из-за
    него роняет телефон."
    show ang_usual at right with dissolve
    if grisha_kind:
        grisha "Ой, извини, пожалуйста, не хотел"
        $ ang_score += 1
        angelina "Ничего страшного"
        grisha "Не разбился?"
        angelina "Нет, все хорошо"
    else:
        menu:
            "Гриша: Ой, извини, пожалуйста, не хотел":
                $ ang_score += 1
                angelina "Ничего страшного"
                grisha "Не разбился?"
                angelina "Нет, все хорошо"
            "Молча пробежать":
                pass
            "Гриша: В телефоне меньше залипай":
                hide ang_usual
                show ang_angry at right with dissolve
                angelina "Сама разберусь!"
    hide ang_angry
    return

#Сцена 3 - лабиринт из дверей
label scene_3:
    show bg_doors with fade
    if difficult:
        author "Так, а какая аудитория? 31-А-56. Боже, что это и где это? Сам найду."
    else:
        show phone_map at left with dissolve
        grisha "Так, а какая аудитория? 31-А-56. Боже, что это и где это?
        Прямо, прямо, налево, налево, направо, направо. Кому нужны эти карты?
        Сам найду."
        hide phone_map
    call doors_1
    return

label doors_1:
    scene bg_doors with fade
    define random = 0
    menu:
        "Налево":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_1
        "Прямо":
            call doors_2
        "Направо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_1
    return

label doors_2:
    scene bg_doors with fade
    menu:
        "Налево":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_2
        "Прямо":
            call doors_3
        "Направо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_2
    return

label doors_3:
    scene bg_doors with fade
    menu:
        "Налево":
            call doors_4
        "Прямо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_3
        "Направо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_3
    return

label doors_4:
    scene bg_doors with fade
    menu:
        "Налево":
            call doors_5
        "Прямо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_4
        "Направо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_4
    return

label doors_5:
    scene bg_doors with fade
    menu:
        "Налево":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_5
        "Прямо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
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
        "Налево":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_6
        "Прямо":
            if difficult == True:
                $random = renpy.random.randint(1, 5)
            else:
                $random = renpy.random.randint(1, 10)
            if random == 1 and not screamer:
                call scream
            else:
                call wrong_way
            call doors_6
        "Направо":
            return
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
    author "Гриша нашел аудиторию, но похоже, что большинство уже разошлось.
    Оставшиеся ребята собирают свои вещи."
    grisha "Э-э-э, привет?"
    show girl_usual at right with dissolve
    girl "Привет, ты кто?"
    grisha "Дэ-э-э, я - Гриша Орехов, у меня тут вообще собрание должно быть...
    э-э-э, организационное..."
    show boy_usual at left with dissolve
    boy "Оно уже закончилось, ты малясь опоздал."
    grisha "Черт. Я многое пропустил? Что было?"
    girl "Рассказали про обучение, про
    специальность. Старшекурсники поделились инфой, что на сессии надо драться
    с преподами"
    grisha "Чего-о-о?"
    boy "Хотя я не верю этому. Кстати, меня Лёня зовут."
    girl "А я Валя."
    grisha "Приятно познакомиться. Ладно, я пожалуй пойду тогда."
    hide boy_usual
    show lyonya_usual at left
    lyonya "Встретимся на парах."
    grisha "Угу, до встречи."
    return

#Сцена 5 - Конец демо
label scene_5:
    scene central_entrance with fade
    grisha "Ну и денек, конечно. Что ж будет дальше в этом унитехе..."
    scene art_demo with fade
    $ renpy.notify("Вы прошли эпизод \"1 сентября\"")
    pause(4.0)
    return

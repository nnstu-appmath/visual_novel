# 3 курс
label third_year:
    call scene_31
    call scene_32
    call scene_33
    call scene_34
    call scene_35
    call scene_36
    call scene_42
    scene art_2_year_sad with fade
    $ renpy.notify("Вы прошли эпизод \"3 курс\"")
    pause(4.0)
    scene black with fade
    pause (2.0)
    return

# Начало 3 курса
label scene_31:
    play music neutral_3 fadein 1 fadeout 1 volume 0.5
    scene auditorium with fade
    author "Третий курс. Студенты приходят на очередную пару. Внезапно в аудиторию заходит
    какой-то чел из студсовета."
    show studman with dissolve
    studman "Ребята, отвлеку вас на пару минут. У нас ежегодно проходит конкурс
    красоты \"Мисс Унитех\". В этом году с крутыми призами. Очень ждем всех
    красивых и талантливых девушек нашего университета на отброчный кастинг!"
    hide studman with dissolve
    show ang_usual at right with dissolve
    angelina "Хм... пойти или нет... Гриш, как считаешь?"
    menu:
        "\"Сходи обязательно!\"":
            $ ang_score += 1
        "\"Че там делать, только время тратить на ерунду\"":
            if valya_score < 0:
                show lyonya_usual at left with dissolve
                lyonya "Ой, не слушай его, он ничего не понимает. Попробуй -
                если не получится, то ничего страшного"
            else:
                show valya_usual at left with dissolve
                valya "Ой, не слушай его, он ничего не понимает. Попробуй -
                если не получится, то ничего страшного"
    angelina "Ладно, попробую. Главное, чтобы успела подготовиться к экзамену
    Потемкина. Его же перенесли из-за событий с Валей."
    grisha "Не переживай, сдашь, ты же староста :)"
    return

# Перед экзаменом Потемкина
label scene_32:
    scene before_aud with fade
    author "Через полчаса начнется экзамен Потемкина. Ангелина уже прискакала
    к аудитории, как самая ответственная. Лёня же пришел так рано,
    потому что захотел повторить материал. Почему Гриша пришел так рано?
    Да кто его знает..."
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show ang_happiness with dissolve
        show valya_usual at right with dissolve
    else:
        show ang_happiness at right with dissolve
    angelina "Я прошла кастинг!!!"
    grisha "Супер, поздравляем!"
    angelina "Там будет несколько туров, мне будет
    нужна ваша помощь. И это не обсуждается."
    if valya_score < 0:
        lyonya "Посмотрим.........."
    else:
        valya "Посмотрим"
    grisha "Ладно. Ты хоть к экзамену подготовилась?"
    angelina "А как же! Все шпоры спрятала :)"
    lyonya "Понимаю"
    hide lyonya_usual with dissolve
    hide ang_happiness with dissolve
    hide valya_usual with dissolve
    show potemkin_usual with dissolve
    potemkin "Орехов, пройдем-те"
    grisha "А че так рано? Еще полчаса."
    potemkin "Орехи надо собирать в первую очередь"
    grisha "Че?"
    potemkin "Проходите."
    return

# Экзамен Потемкина
label scene_33:
    scene auditorium with fade
    show potemkin_usual with dissolve
    potemkin "День добрый! Готовы к экзамену? Пора начинать"
    grisha "Дела отстой"
    play music sigame fadein 1 fadeout 1 volume 0.5
    hide potemkin_usual with dissolve
    show potemkin_usual at right with dissolve
    show tablo at left with dissolve
    call exam_sigame
    call exam_sigame
    call exam_sigame
    call exam_sigame
    call exam_sigame
    if exam_potemkin == 5:
        $exam_score += 1
        $diplom += 1
        potemkin "Поражаюсь такими великими знаниями студента. Вижу, что вы
        тщательно готовились по трудам таких классиков как Эйнштейн, Ньютон и
        Потемкин."
    if 2 < exam_potemkin < 5:
        $exam_score += 1
        potemkin "Средний результат. Студенты могли бы и лучше изучать материал."
    if exam_potemkin < 3:
        potemkin "Страшно осознавать, какой уровень знаний у нынешних студентов.
        Стыдно..."
    return

label exam_sigame:
    author "Выбирайте категорию"
    if exam_music_1 and exam_music_2 and exam_music_3:
        menu:
            "Кино":
                if exam_cinema_2 and exam_cinema_3:
                    show tablo_cinema_1 at left
                    $ exam_cinema_1 = True
                    call cinema_1
                    return
                if exam_cinema_1 and exam_cinema_3:
                    show tablo_cinema_2 at left
                    $ exam_cinema_2 = True
                    call cinema_2
                    return
                if exam_cinema_1 and exam_cinema_2:
                    show tablo_cinema_3 at left
                    $ exam_cinema_3 = True
                    call cinema_3
                    return
                if exam_cinema_3:
                    menu:
                        "Кино 1":
                            show tablo_cinema_1 at left
                            $ exam_cinema_1 = True
                            call cinema_1
                            return
                        "Кино 2":
                            show tablo_cinema_2 at left
                            $ exam_cinema_2 = True
                            call cinema_2
                            return
                if exam_cinema_2:
                    menu:
                        "Кино 1":
                            show tablo_cinema_1 at left
                            $ exam_cinema_1 = True
                            call cinema_1
                            return
                        "Кино 3":
                            show tablo_cinema_3 at left
                            $ exam_icinema_3 = True
                            call cinema_3
                            return
                if exam_cinema_1:
                    menu:
                        "Кино 2":
                            show tablo_cinema_2 at left
                            $ exam_cinema_2 = True
                            call cinema_2
                            return
                        "Кино 3":
                            show tablo_cinema_3 at left
                            $ exam_cinema_3 = True
                            call cinema_3
                            return
                menu:
                    "Кино 1":
                        show tablo_cinema_1 at left
                        $ exam_cinema_1 = True
                        call cinema_1
                        return
                    "Кино 2":
                        show tablo_cinema_2 at left
                        $ exam_cinema_2 = True
                        call cinema_2
                        return
                    "Кино 3":
                        show tablo_cinema_3 at left
                        $ exam_cinema_3 = True
                        call cinema_3
                        return
            "Интернет":
                if exam_internet_2 and exam_internet_3:
                    show tablo_internet_1 at left
                    $ exam_internet_1 = True
                    call internet_1
                    return
                if exam_internet_1 and exam_internet_3:
                    show tablo_internet_2 at left
                    $ exam_internet_2 = True
                    call internet_2
                    return
                if exam_internet_1 and exam_internet_2:
                    show tablo_internet_3 at left
                    $ exam_internet_3 = True
                    call internet_3
                    return
                if exam_internet_3:
                    menu:
                        "Интернет 1":
                            show tablo_internet_1 at left
                            $ exam_internet_1 = True
                            call internet_1
                            return
                        "Интернет 2":
                            show tablo_internet_2 at left
                            $ exam_internet_2 = True
                            call internet_2
                            return
                if exam_internet_2:
                    menu:
                        "Интернет 1":
                            show tablo_internet_1 at left
                            $ exam_internet_1 = True
                            call internet_1
                            return
                        "Интернет 3":
                            show tablo_internet_3 at left
                            $ exam_internet_3 = True
                            call internet_3
                            return
                if exam_internet_1:
                    menu:
                        "Интернет 2":
                            show tablo_internet_2 at left
                            $ exam_internet_2 = True
                            call internet_2
                            return
                        "Интернет 3":
                            show tablo_internet_3 at left
                            $ exam_internet_3 = True
                            call internet_3
                            return
                menu:
                    "Интернет 1":
                        show tablo_internet_1 at left
                        $ exam_internet_1 = True
                        call internet_1
                        return
                    "Интернет 2":
                        show tablo_internet_2 at left
                        $ exam_internet_2 = True
                        call internet_2
                        return
                    "Интернет 3":
                        show tablo_internet_3 at left
                        $ exam_internet_3 = True
                        call internet_3
                        return
    if exam_cinema_1 and exam_cinema_2 and exam_cinema_3:
        menu:
            "Музыка":
                if exam_music_2 and exam_music_3:
                    show tablo_music_1 at left
                    $ exam_music_1 = True
                    call music_1
                    return
                if exam_music_1 and exam_music_3:
                    show tablo_music_2 at left
                    $ exam_music_2 = True
                    call music_2
                    return
                if exam_music_1 and exam_music_2:
                    show tablo_music_3 at left
                    $ exam_music_3 = True
                    call music_3
                    return
                if exam_music_3:
                    menu:
                        "Музыка 1":
                            show tablo_music_1 at left
                            $ exam_music_1 = True
                            call music_1
                            return
                        "Музыка 2":
                            show tablo_music_2 at left
                            $ exam_music_2 = True
                            call music_2
                            return
                if exam_music_2:
                    menu:
                        "Музыка 1":
                            show tablo_music_1 at left
                            $ exam_music_1 = True
                            call music_1
                            return
                        "Музыка 3":
                            show tablo_music_3 at left
                            $ exam_music_3 = True
                            call music_3
                            return
                if exam_music_1:
                    menu:
                        "Музыка 2":
                            show tablo_music_2 at left
                            $ exam_music_2 = True
                            call music_2
                            return
                        "Музыка 3":
                            show tablo_music_3 at left
                            $ exam_music_3 = True
                            call music_3
                            return
                menu:
                    "Музыка 1":
                        show tablo_music_1 at left
                        $ exam_music_1 = True
                        call music_1
                        return
                    "Музыка 2":
                        show tablo_music_2 at left
                        $ exam_music_2 = True
                        call music_2
                        return
                    "Музыка 3":
                        show tablo_music_3 at left
                        $ exam_music_3 = True
                        call music_3
                        return
            "Интернет":
                if exam_internet_2 and exam_internet_3:
                    show tablo_internet_1 at left
                    $ exam_internet_1 = True
                    call internet_1
                    return
                if exam_internet_1 and exam_internet_3:
                    show tablo_internet_2 at left
                    $ exam_internet_2 = True
                    call internet_2
                    return
                if exam_internet_1 and exam_internet_2:
                    show tablo_internet_3 at left
                    $ exam_internet_3 = True
                    call internet_3
                    return
                if exam_internet_3:
                    menu:
                        "Интернет 1":
                            show tablo_internet_1 at left
                            $ exam_internet_1 = True
                            call internet_1
                            return
                        "Интернет 2":
                            show tablo_internet_2 at left
                            $ exam_internet_2 = True
                            call internet_2
                            return
                if exam_internet_2:
                    menu:
                        "Интернет 1":
                            show tablo_internet_1 at left
                            $ exam_internet_1 = True
                            call internet_1
                            return
                        "Интернет 3":
                            show tablo_internet_3 at left
                            $ exam_internet_3 = True
                            call internet_3
                            return
                if exam_internet_1:
                    menu:
                        "Интернет 2":
                            show tablo_internet_2 at left
                            $ exam_internet_2 = True
                            call internet_2
                            return
                        "Интернет 3":
                            show tablo_internet_3 at left
                            $ exam_internet_3 = True
                            call internet_3
                            return
                menu:
                    "Интернет 1":
                        show tablo_internet_1 at left
                        $ exam_internet_1 = True
                        call internet_1
                        return
                    "Интернет 2":
                        show tablo_internet_2 at left
                        $ exam_internet_2 = True
                        call internet_2
                        return
                    "Интернет 3":
                        show tablo_internet_3 at left
                        $ exam_internet_3 = True
                        call internet_3
                        return
    if exam_internet_1 and exam_internet_2 and exam_internet_3:
        menu:
            "Кино":
                if exam_cinema_2 and exam_cinema_3:
                    show tablo_cinema_1 at left
                    $ exam_cinema_1 = True
                    call cinema_1
                    return
                if exam_cinema_1 and exam_cinema_3:
                    show tablo_cinema_2 at left
                    $ exam_cinema_2 = True
                    call cinema_2
                    return
                if exam_cinema_1 and exam_cinema_2:
                    show tablo_cinema_3 at left
                    $ exam_cinema_3 = True
                    call cinema_3
                    return
                if exam_cinema_3:
                    menu:
                        "Кино 1":
                            show tablo_cinema_1 at left
                            $ exam_cinema_1 = True
                            call cinema_1
                            return
                        "Кино 2":
                            show tablo_cinema_2 at left
                            $ exam_cinema_2 = True
                            call cinema_2
                            return
                if exam_cinema_2:
                    menu:
                        "Кино 1":
                            show tablo_cinema_1 at left
                            $ exam_cinema_1 = True
                            call cinema_1
                            return
                        "Кино 3":
                            show tablo_cinema_3 at left
                            $ exam_icinema_3 = True
                            call cinema_3
                            return
                if exam_cinema_1:
                    menu:
                        "Кино 2":
                            show tablo_cinema_2 at left
                            $ exam_cinema_2 = True
                            call cinema_2
                            return
                        "Кино 3":
                            show tablo_cinema_3 at left
                            $ exam_cinema_3 = True
                            call cinema_3
                            return
                menu:
                    "Кино 1":
                        show tablo_cinema_1 at left
                        $ exam_cinema_1 = True
                        call cinema_1
                        return
                    "Кино 2":
                        show tablo_cinema_2 at left
                        $ exam_cinema_2 = True
                        call cinema_2
                        return
                    "Кино 3":
                        show tablo_cinema_3 at left
                        $ exam_cinema_3 = True
                        call cinema_3
                        return
            "Музыка":
                if exam_music_2 and exam_music_3:
                    show tablo_music_1 at left
                    $ exam_music_1 = True
                    call music_1
                    return
                if exam_music_1 and exam_music_3:
                    show tablo_music_2 at left
                    $ exam_music_2 = True
                    call music_2
                    return
                if exam_music_1 and exam_music_2:
                    show tablo_music_3 at left
                    $ exam_music_3 = True
                    call music_3
                    return
                if exam_music_3:
                    menu:
                        "Музыка 1":
                            show tablo_music_1 at left
                            $ exam_music_1 = True
                            call music_1
                            return
                        "Музыка 2":
                            show tablo_music_2 at left
                            $ exam_music_2 = True
                            call music_2
                            return
                if exam_music_2:
                    menu:
                        "Музыка 1":
                            show tablo_music_1 at left
                            $ exam_music_1 = True
                            call music_1
                            return
                        "Музыка 3":
                            show tablo_music_3 at left
                            $ exam_music_3 = True
                            call music_3
                            return
                if exam_music_1:
                    menu:
                        "Музыка 2":
                            show tablo_music_2 at left
                            $ exam_music_2 = True
                            call music_2
                            return
                        "Музыка 3":
                            show tablo_music_3 at left
                            $ exam_music_3 = True
                            call music_3
                            return
                menu:
                    "Музыка 1":
                        show tablo_music_1 at left
                        $ exam_music_1 = True
                        call music_1
                        return
                    "Музыка 2":
                        show tablo_music_2 at left
                        $ exam_music_2 = True
                        call music_2
                        return
                    "Музыка 3":
                        show tablo_music_3 at left
                        $ exam_music_3 = True
                        call music_3
                        return
    menu:
        "Музыка":
            if exam_music_2 and exam_music_3:
                show tablo_music_1 at left
                $ exam_music_1 = True
                call music_1
                return
            if exam_music_1 and exam_music_3:
                show tablo_music_2 at left
                $ exam_music_2 = True
                call music_2
                return
            if exam_music_1 and exam_music_2:
                show tablo_music_3 at left
                $ exam_music_3 = True
                call music_3
                return
            if exam_music_3:
                menu:
                    "Музыка 1":
                        show tablo_music_1 at left
                        $ exam_music_1 = True
                        call music_1
                        return
                    "Музыка 2":
                        show tablo_music_2 at left
                        $ exam_music_2 = True
                        call music_2
                        return
            if exam_music_2:
                menu:
                    "Музыка 1":
                        show tablo_music_1 at left
                        $ exam_music_1 = True
                        call music_1
                        return
                    "Музыка 3":
                        show tablo_music_3 at left
                        $ exam_music_3 = True
                        call music_3
                        return
            if exam_music_1:
                menu:
                    "Музыка 2":
                        show tablo_music_2 at left
                        $ exam_music_2 = True
                        call music_2
                        return
                    "Музыка 3":
                        show tablo_music_3 at left
                        $ exam_music_3 = True
                        call music_3
                        return
            menu:
                "Музыка 1":
                    show tablo_music_1 at left
                    $ exam_music_1 = True
                    call music_1
                    return
                "Музыка 2":
                    show tablo_music_2 at left
                    $ exam_music_2 = True
                    call music_2
                    return
                "Музыка 3":
                    show tablo_music_3 at left
                    $ exam_music_3 = True
                    call music_3
                    return
        "Кино":
            if exam_cinema_2 and exam_cinema_3:
                show tablo_cinema_1 at left
                $ exam_cinema_1 = True
                call cinema_1
                return
            if exam_cinema_1 and exam_cinema_3:
                show tablo_cinema_2 at left
                $ exam_cinema_2 = True
                call cinema_2
                return
            if exam_cinema_1 and exam_cinema_2:
                show tablo_cinema_3 at left
                $ exam_cinema_3 = True
                call cinema_3
                return
            if exam_cinema_3:
                menu:
                    "Кино 1":
                        show tablo_cinema_1 at left
                        $ exam_cinema_1 = True
                        call cinema_1
                        return
                    "Кино 2":
                        show tablo_cinema_2 at left
                        $ exam_cinema_2 = True
                        call cinema_2
                        return
            if exam_cinema_2:
                menu:
                    "Кино 1":
                        show tablo_cinema_1 at left
                        $ exam_cinema_1 = True
                        call cinema_1
                        return
                    "Кино 3":
                        show tablo_cinema_3 at left
                        $ exam_icinema_3 = True
                        call cinema_3
                        return
            if exam_cinema_1:
                menu:
                    "Кино 2":
                        show tablo_cinema_2 at left
                        $ exam_cinema_2 = True
                        call cinema_2
                        return
                    "Кино 3":
                        show tablo_cinema_3 at left
                        $ exam_cinema_3 = True
                        call cinema_3
                        return
            menu:
                "Кино 1":
                    show tablo_cinema_1 at left
                    $ exam_cinema_1 = True
                    call cinema_1
                    return
                "Кино 2":
                    show tablo_cinema_2 at left
                    $ exam_cinema_2 = True
                    call cinema_2
                    return
                "Кино 3":
                    show tablo_cinema_3 at left
                    $ exam_cinema_3 = True
                    call cinema_3
                    return
        "Интернет":
            if exam_internet_2 and exam_internet_3:
                show tablo_internet_1 at left
                $ exam_internet_1 = True
                call internet_1
                return
            if exam_internet_1 and exam_internet_3:
                show tablo_internet_2 at left
                $ exam_internet_2 = True
                call internet_2
                return
            if exam_internet_1 and exam_internet_2:
                show tablo_internet_3 at left
                $ exam_internet_3 = True
                call internet_3
                return
            if exam_internet_3:
                menu:
                    "Интернет 1":
                        show tablo_internet_1 at left
                        $ exam_internet_1 = True
                        call internet_1
                        return
                    "Интернет 2":
                        show tablo_internet_2 at left
                        $ exam_internet_2 = True
                        call internet_2
                        return
            if exam_internet_2:
                menu:
                    "Интернет 1":
                        show tablo_internet_1 at left
                        $ exam_internet_1 = True
                        call internet_1
                        return
                    "Интернет 3":
                        show tablo_internet_3 at left
                        $ exam_internet_3 = True
                        call internet_3
                        return
            if exam_internet_1:
                menu:
                    "Интернет 2":
                        show tablo_internet_2 at left
                        $ exam_internet_2 = True
                        call internet_2
                        return
                    "Интернет 3":
                        show tablo_internet_3 at left
                        $ exam_internet_3 = True
                        call internet_3
                        return
            menu:
                "Интернет 1":
                    show tablo_internet_1 at left
                    $ exam_internet_1 = True
                    call internet_1
                    return
                "Интернет 2":
                    show tablo_internet_2 at left
                    $ exam_internet_2 = True
                    call internet_2
                    return
                "Интернет 3":
                    show tablo_internet_3 at left
                    $ exam_internet_3 = True
                    call internet_3
                    return
    return

label ans_right:
    play sound applause volume 0.5
    $ exam_potemkin += 1
    potemkin "Верно"
    return

label ans_wrong:
    play sound answer_wrong volume 0.5
    return

label ans_time:
    potemkin "Время вышло"
    return

label music_1:
    author "Прослушайте композицию"
    play music zemfira volume 0.5
    author "Кто автор?"
    play music sigame fadein 1 fadeout 1 volume 0.5
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Земфира":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Диана Арбенина":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Земфира"
        "Слава":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Земфира"
    return

label music_2:
    author "Прослушайте композицию"
    play music lp volume 0.5
    author "Кто автор?"
    play music sigame fadein 1 fadeout 1 volume 0.5
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Green Day":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Linkin Park"
        "Linkin Park":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Papa Roach":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Linkin Park"
    return

label music_3:
    author "Прослушайте композицию"
    play music gradusy volume 0.5
    author "Кто автор?"
    play music sigame volume 0.5
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Бумбокс":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Градусы"
        "Градусы":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Корни":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Градусы"
    return

label cinema_1:
    author "В каком фильме НЕ летали на космическом корабле?"
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Интерстеллар":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Назад в будущее"
        "Назад в будущее":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Стражи галактики":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Назад в будущее"
    return

label cinema_2:
    author "Какой актер сыграл Бэтмена в последней экранизации?"
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Роберт Паттинсон":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Бэн Аффлек":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Роберт Паттинсон"
        "Кристиан Бэйл":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Роберт Паттинсон"
    return

label cinema_3:
    author "Из какого фильма знаменитая фраза \"ДИМОООООН!\""
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Бумер":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Бригада":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Бумер"
        "Брат":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Бумер"
    return

label internet_1:
    author "Что означает слово «пехота» на молодежном сленге?"
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Наталья Морская пехота":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - 500 рублей"
        "500 рублей":
            $timer_score = True
            hide screen countdown
            call ans_right
        "Пешеходы":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - 500 рублей"
    return

label internet_2:
    author "Какая из частей GTA самая продаваемая?"
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "GTA: Vice City":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - GTA V"
        "GTA V":
            $timer_score = True
            hide screen countdown
            call ans_right
        "GTA: San Andreas":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - GTA V"

    return

label internet_3:
    author "Какая из этих компаний самая крупная в Корее?"
    $ timer_score = False
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'ans_time'
    show screen countdown
    menu:
        "Huawei":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Samsung"
        "Xiaomi":
            $timer_score = True
            hide screen countdown
            call ans_wrong
            potemkin "Правильный ответ - Samsung"
        "Samsung":
            $timer_score = True
            hide screen countdown
            call ans_right
    return

# После экзамена Потемкина
label scene_34:
    play music neutral_3 fadein 1 fadeout 1 volume 0.5
    scene before_aud with fade
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show ang_usual with dissolve
        show valya_usual at right with dissolve
    else:
        show ang_usual at right with dissolve
    angelina "Ну че? Как?"
    grisha "Пойдет"
    angelina "Кстати, забыла сказать, что первый тур в конкурсе заключается в
    том, что бы прыгнуть с тарзанки. Я боюсь капец."
    grisha "Можем прийти поддержать морально"
    if valya_score > 0:
        valya "Да-да, давайте"
    else:
        lyonya "Да-да, давайте"
    angelina "Если это мне конечно поможет..."
    lyonya "Не помешает, в любом случае"
    return

# Первый этап конкурса - тарзанка
label scene_35:
    scene forest with fade
    author "Первый этап конкурса \"Мисс Унитех\" проходит в городском парке.
    Участницы стоят и ждут очередь на тарзанку. Лёня подготовил плакаты
    с поддержкой Ангелины и ее портрет"
    show plakat at right with dissolve
    show lyonya_usual at left with dissolve
    grisha "Мы че в детском лагере?"
    lyonya "Это поднимет ее боевой дух!!!"
    grisha "Ладно, как скажешь"
    author "Гриша и Лёня кричат слова в поддержку Ангелины."
    lyonya "АНГЕЛИНА ВПЕРЕД!"
    grisha "А может без детских кричалок?"
    lyonya "Давай тоже кричи"
    grisha "Ладно. АНГЕЛИНА ДАВАЙ!"
    author "Ангелину это явно подбадривало. Хоть и смотрелось
    достаточно кринжово."
    hide plakat with dissolve
    show alina_usual at right with dissolve
    grisha "(Че на меня так пялит одна из участниц? Может
    у меня еда на лице? Или волосы торчат?)"
    hide alina_usual with dissolve
    lyonya "Эй, ты че задумался?"
    grisha "А? Ничего."
    hide lyonya_usual with dissolve
    author "Настала очередь Ангелины. Перед прыжком Ангелина
    начала надевать экипировку и запуталась в ней."
    show ang_usual with dissolve
    angelina "Гриша, помоги"
    if grisha_kind:
        $ ang_score += 1
        grisha "Так, дай сюда. Вот. Всё."
        angelina "Спасибо большое."
        grisha "Удачи!"
    else:
        menu:
            "Помочь самому":
                $ ang_score += 1
                grisha "Так, дай сюда. Вот. Всё."
                angelina "Спасибо большое"
                grisha "Удачи!"
            "Попросить инструктора помочь":
                grisha "Молодой человек! У нас тут проблемка возникла"
                angelina "Спасибо"
    hide ang_usual with dissolve
    author "Ангелина все-таки разбежалась и прыгнула... Успешно!"
    show lyonya_usual at left with dissolve
    lyonya "Круто как! Я бы тоже прыгнул. Когда-нибудь"
    if valya_score > 0:
        show valya_usual at right with dissolve
        valya "Ой, а мне страшно прыгать вот так вот. Вдруг разобьюсь, умру..."
        hide valya_usual with dissolve
    hide lyonya_usual with dissolve
    author "Ангелина возвращается на исходную точку и
    группа поддержки в лице ее друзей прибежали к ней."
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show ang_usual with dissolve
        show valya_usual at right with dissolve
    else:
        show ang_usual at right with dissolve
    angelina "Это было очень страшно! Но мне понравилось :)"
    grisha "Я бы тебе за храбрость цветы подарил, но не знаю какие любишь"
    angelina "Мы с тобой уже третий год вместе учимся, ты не знаешь, что пионы?"
    grisha "Буду иметь ввиду"
    author "Очень незаметно подошла другая участница.
    Грише показалась она знакомой."
    if valya_score > 0:
        hide valya_usual with dissolve
        show alina_usual at right with dissolve
    else:
        show alina_usual with dissolve
    alina "Ангелин, у тебя такая хорошая команда поддержки. Парни хорошие такие."
    angelina "Да, мне тоже нравится. Это кстати Лёня и Гриша."
    lyonya "Приятно познакомиться."
    grisha "(Че она так смотрит на меня?)"
    alina "Ну ладно, не буду мешать вам, еще увидимся."
    hide alina_usual with dissolve
    angelina "Спасибо, что пришли поддержать!"
    grisha "Да всегда пожалуйста"
    return

# Второй этап - викторина
label scene_36:
    play music sigame fadein 1 fadeout 1 volume 0.5
    scene viktorina with fade
    author "Спустя некоторое время наступил второй этап конкурса -
    интеллектуальный. Лёня с Гришей пришли посмотреть на это."
    show lyonya_usual at right with dissolve
    lyonya "Че как, как думаешь кто выиграет?"
    grisha "Ну, у Ангелины есть все шансы, она ж умная"
    hide lyonya_usual with dissolve
    show studman at left with dissolve
    studman "Итак начнем же наш интеллектуальный этап!"
    author "Гриша не очень сильно вслушивался в сами вопросы. Он лишь
    болел за Ангелину. Но в какой-то момент Ангелина замешкалась."
    show ang_usual at right with dissolve
    studman "Вы можете воспользоваться своей подсказкой
    и попросить помощи у человека из зала."
    angelina "Гриша, помоги."
    author "Гриша на самом деле не до конца понял вопрос"
    if grisha_smart:
        $ ang_score += 1
        grisha "Азия?"
        studman "Верно! Следующий вопрос."
        grisha "Фух..."
    else:
        menu:
            "Подсказать возможно неправильный ответ":
                $ ang_score += 1
                grisha "Азия?"
                studman "Верно! Следующий вопрос."
                grisha "Фух..."
            "Промолчать, потому что не уверен в правильности ответа":
                angelina "Э-э-э, Африка?"
                studman "Неверно! Следующий вопрос."
    hide ang_usual with dissolve
    author "В процессе игры одна из соперниц - Алина - тоже не знала ответ.
    Но именно в этот момент Гриша услышал вопрос и точно знал на него ответ."
    show alina_usual at right with dissolve
    alina "Подскажите кто-нибудь!"
    menu:
        "Подсказать точно правильный ответ":
            $ alina_score += 1
            grisha "Петр I"
            studman "Верно!"
        "Не подсказывать":
            alina "Александр II"
            studman "Неверно!"
    hide alina_usual with dissolve
    studman "На этом наш интеллектуальный этап заканчивается и победителем
    сегодняшней игры становится..."
    if alina_score == 1:
        studman "Ангелина Муравьева и Алина Сафонова. Ничья!"
        hide studman with dissolve
        play music neutral_3 fadein 1 fadeout 1 volume 0.5
        author "Крайне недовольная Ангелина подходит к Грише с явными претензиями"
        show ang_annoy at right with dissolve
        angelina "Ты зачем ей подсказал???"
        grisha "Ну я точно знал ответ, а она просила помощи"
        angelina "Она конкурентка!"
        grisha "Ну у вас же ничья"
        angelina "Неважно!!!"
        show alina_usual with dissolve
        alina "Гриш, спасибо большое, выручил. Могу отблагодарить, пригласив
        на кофе."
        angelina "А мы с Лёней в клуб собираемся!"
        if valya_score > 0:
            angelina "Еще Валя присоединится!"
        show lyonya_usual at left with dissolve
        lyonya "Вообще-то у меня дела..."
        angelina "Эй!"
        lyonya "А. Да, идешь с нами?"
        menu:
            "Пойти с Алиной в кафе":
                $ alina_score += 1
                call scene_37
            "Пойти с Ангелиной и Лёней в клуб":
                $ ang_score += 1
                call scene_39
    else:
        studman "Ангелина Муравьева! Поздравлем"
        hide studman with dissolve
        play music neutral_3 fadein 1 fadeout 1 volume 0.5
        author "Радостная победой Ангелина бежит к Грише и Лёне"
        show ang_happiness at right with dissolve
        show lyonya_usual at left with dissolve
        angelina "Супер, я очень рада! Спасибо, что пришли посмотреть.
        Может сходим в клуб?"
        lyonya "Давай в тот, в котором был день первокурсника!"
        if valya_score > 0:
            angelina "И Валю позовем"
        grisha "Го"
        call scene_39
    return

# Кафе с Алиной
label scene_37:
    scene cafe with fade
    show alina_usual with dissolve
    author "Гриша и Алина сидят в кафе. Гриша решил сегодня
    побыть на диете и заказал не двойную, а обычную порцию пельменей"
    alina "Еще раз спасибо за помощь!"
    grisha "Да не за что"
    author "...неловкое молчание..."
    grisha "Вкусный кофе..."
    angelina "Да..."
    menu:
        "Спросить про конкурс":
            grisha "А ты зачем пошла на этот конкурс? Проявить себя?"
            alina "Мне вообще очень важно выиграть этот конкурс. У меня кошка
            болеет крабом. Денег нет на лекарства и лечение. При выигрыше дают
            денежный приз и я на него рассчитываю. Я надеюсь на помощь друзей"
            menu:
                "\"Можешь на меня рассчитывать\"":
                    $ alina_score += 1
                    alina "Спасибо ;)"
                "Промолчать":
                    pass
        "Узнать ее увлечения":
            $ alina_score += 1
            grisha "А чем ты увлекаешься?"
            alina "Я много читаю. Также занимаюсь танцами. В детстве пела в хоре.
            Сейчас занимаюсь флористикой, люблю цветы, особенно гипсофилы, еще
            начала делать украшения ручной работы. Вот в конкурсе участвую.
            А ты чем любишь заниматься?"
            grisha "Э-э-э.... Да люблю в игры играть..."
            alina "Понятно"
        "Продолжить неловко молчать":
            pause (1.5)
            alina "Может расскажешь о себе?"
            grisha "Э-э-э.... Да люблю в игры играть... Учусь... Особо ничего
            интересного"
            alina "А я вот много читаю. Также занимаюсь танцами.
            В детстве пела в хоре. Сейчас занимаюсь флористикой,
            люблю цветы, особенно гипсофилы, еще начала делать
            украшения ручной работы. Вот в конкурсе участвую."
    author "Алина нежно кладет свою руку на руку Гриши. Гриша слегка смутился и
    непринужденно взял свою чашку с кофе."
    author "До конца некоего \"свидания\" они общались на отдаленные темы,
    слегка смущаясь от неловкости"
    alina "Официант, а можно счет?"
    menu:
        "Заплатить за счет":
            $alina_score += 1
            alina "Не стоило, я же тебя пригласила сюда за твою помощь.
            Спасибо большое. Приятно было провести время с тобой вдвоем"
            author "На прощание Алина целует Гришу в щечку"
        "Дать Алине оплатить счет":
            alina "Спасибо за вечер. Надеюсь еще посидим так же"
            author "На прощание Алина целует Гришу в щечку"
    call scene_38
    return

# Ангелина недовольна свиданием Гриши с Алиной
label scene_38:
    scene auditorium with fade
    author "На следующий день Ангелина всю первую пару сверлила Гришу
    недовольным взглядом."
    show ang_usual with dissolve
    angelina "Ну как вы с Алиной за кофе сходили???"
    grisha "А что?"
    angelina "Да так... Интересно просто..."
    if alina_score > 2:
        grisha "Приятно посидели, поболтали. Рассказала о себе. Хорошая девушка."
        hide ang_usual
        show ang_annoy
        angelina "Хорошая???"
        grisha "Ну да. А что?"
        angelina "Да ничего!"
    else:
        grisha "Странный вечерок был, посидели и посидели. Ничего необычного."
        angelina "Ну ладно!!!"
    return

# Клуб после викторины
label scene_39:
    scene club with fade
    play music disco_1 fadein 1 fadeout 1 volume 0.3
    author "Вечером ребята собрались в клубе, чтобы расслабится и отметить
    окончание этапа конкурса. Они опять танцуют под странный тектоник, что и
    на первом курсе"
    show lyonya_usual at left with dissolve
    show ang_usual at right with dissolve
    grisha "Они вообще меняют репертуар?"
    lyonya "Клевая музыка же!"
    grisha "Ты на первом курсе тоже самое мне сказал"
    lyonya "Я не изменяю своим вкусам"
    if valya_score > 0:
        lyonya "Валя кстати обещала присоединиться к нам попозже"
        angelina "Как у вас с Валей кстати, Лёнь?"
        hide lyonya_usual
        show lyonya_confused at left
        lyonya "А что? А как? А-а-а.... Да все хорошо! А что ты имеешь ввиду?"
        angelina "Ой, не делай вид, что не понимаешь :)"
        lyonya "Э-э-э...."
        grisha "Ну скажи, что мутите, чо ты :)"
        lyonya "Ничего мы не мутим!!! Хорошие друзья."
        grisha "А хотел бы?"
        hide lyonya_confused
        show lyonya_usual at left
        lyonya "Я не отвечаю на такие вопросы"
        hide ang_usual
        show ang_funny at right
        angelina "Ладно-ладно :)"
        hide ang_funny
        show ang_usual at right
    else:
        angelina "Лёнь, ты как кстати. Ну.. после того, что на втором курсе
        было?"
        lyonya "Может не будем вспоминать это? Я еще не пережил это"
        grisha "Да ладно, найдешь себе новую пассию"
        lyonya "Да она была лучшей! Ты никогда не поймешь, что такое настоящая
        любовь"
    author "Кто бы мог подумать, но Алина тоже оказалась в этом клубе и решила
    подойти ко всем."
    show alina_usual with dissolve
    alina "Ой, вы тоже тут! Как настроение?"
    lyonya "Все гуд"
    author "Лёня внезапно отошел по неотложным делам"
    hide lyonya_usual with dissolve
    alina "Гриш, может пойдем на танцпол потанцуем?"
    hide ang_usual
    show ang_annoy at right
    author "Лицо Ангелины резко стало недовольным"
    menu:
        "Потанцевать с Алиной":
            $ alina_score += 1
            scene dance_floor with fade
            show alina_usual with dissolve
            author "Алина слегка касается руки Гриша и смотрит на него."
            menu:
                "Взять Алину за руку в ответ":
                    play music medlyak fadein 1 fadeout 1 volume 0.3
                    call dance_alina
                    call scene_41
                "Отстраниться":
                    scene bar_ with fade
                    author "Гриша возвращается к барной стойке к Ангелине и Лёне."
                    show lyonya_usual at left with dissolve
                    show ang_annoy at right with dissolve
                    if valya_score > 0:
                        author "За это время приехала Валя."
                        show valya_usual with dissolve
                    grisha "Лёнь, все нормально? Ты жив?"
                    lyonya "Да, просто шаурма на остановке была..."
                    grisha "Все, давай без подробностей."
                    angelina "Ну а вы, потанцевали с Алиночкой?"
                    grisha "Ну подрыгались под музыку, как и все на танцполе.
                    А что ты так переживаешь?"
                    angelina "Отстань"
                    hide ang_annoy
                    show ang_usual at right
                    if valya_score > 0:
                        author "Лёня и Валя увлеклись разговором между собой"
                        lyonya "Помнишь?"
                        valya "Да-да, такое не забудешь. Круто было!"
                        hide lyonya_usual with dissolve
                        hide valya_usual with dissolve
                    else:
                        hide lyonya_usual with dissolve
                    show gay at left with dissolve
                    gay "О, привет, Ангел."
                    angelina "Сколько раз говорила, не называть меня так :)
                    Давно не виделись. Как у тебя дела?"
                    gay "Все по-старому, моя хорошая, работаю. А ты как?"
                    angelina "Да вот в конкурсе участвую..."
                    author "Гриша немножко напрягся от появления этого парниши."
                    if valya_score > 0:
                        menu:
                            "Пригласить Ангелину на медленный танец":
                                grisha "Ангелин, может потанцуем?"
                                angelina "Ну пойдем"
                                scene dance_floor with fade
                                play music medlyak fadein 1 fadeout 1 volume 0.3
                                call dance_angelina
                                call scene_41
                            "Поболтать с Лёней и Валей":
                                hide ang_usual with dissolve
                                hide gay with dissolve
                                call scene_bar_valya
                                call scene_41
                    else:
                        menu:
                            "Пригласить Ангелину на медленный танец":
                                grisha "Ангелин, может потанцуем?"
                                angelina "Ну пойдем"
                                scene dance_floor with fade
                                play music medlyak fadein 1 fadeout 1 volume 0.3
                                call dance_angelina
                                call scene_41
                            "Поболтать с Лёней":
                                hide ang_usual with dissolve
                                hide gay with dissolve
                                call scene_bar_lyonya
                                call scene_41
        "Пригласить еще Ангелину":
            $ ang_score += 1
            grisha "Ангелин, пошли с нами тоже"
            angelina "Ладно..."
            scene dance_floor with fade
            show alina_usual at left with dissolve
            show ang_usual at right with dissolve
            play music medlyak fadein 1 fadeout 1 volume 0.3
            author "Ребята танцуют втроем. Спустя пару песен
            музыка сменилась на медленную."
            grisha "Тут что, еще и медляки есть?"
            menu:
                "Пригласить на медляк Алину":
                    hide ang_usual with dissolve
                    hide alina_usual with dissolve
                    show alina_usual with dissolve
                    call dance_alina
                    call scene_41
                "Пригласить на медляк Ангелину":
                    pass
                    call scene_41
                "Уйти за барную стойку":
                    pass
                    call scene_41
    return

# Медляк с Алиной
label dance_alina:
    $ alina_score += 1
    author "Плавная музыка заставляет многих людей
    уйти из центра танцпола. Но Гриша и Алина пошли
    танцевать медленный танец. В процессе Гриша замечает как
    Ангелина уходит."
    alina "Куда ты все время смотришь?"
    grisha "Да никуда, неважно"
    author "Танец заканчивается и они идут к Лёне."
    scene bar_ with fade
    play music disco_2 fadein 1 fadeout 1 volume 0.3
    if valya_score > 0:
        show alina_usual with dissolve
        author "За время танцев приехала Валя, и Лёня мило болтал с ней
        за барной стойкой"
        show lyonya_usual at left with dissolve
        show valya_usual at right with dissolve
        grisha "Привет, Валь"
        valya "Привет"
    else:
        show alina_usual at right with dissolve
        show lyonya_usual at left with dissolve
    grisha "А куда Ангелина ушла?"
    lyonya "Не знаю, она очень резко собралась и убежала,
    после того как вы пошли на танцпол. Может дела появились."
    if valya_score > 0:
        valya "А нечего с конкурентками танцевать"
    grisha "Ладно... Пошлите танцевать тогда"
    return

# Медляк с Ангелиной
label dance_angelina:
    $ alina_score += 1
    author "Плавная музыка заставляет многих людей
    уйти из центра танцпола. Но Гриша и Ангелина пошли
    танцевать медленный танец."
    show ang_usual with dissolve
    grisha "Кто это с тобой так мило разговаривал?"
    angelina "Да-а-а... Старый знакомый"
    grisha "Старые знакомые не называют подруг \"моя хорошая\""
    angelina "Почему тебя это волнует?"
    grisha "Ну-у-у..."
    angelina "???"
    grisha "Да не нравится он мне и все. Не общайся с ним."
    angelina "Ладно, не парься, ему мальчики нравятся. Ты ему кстати понравился,
    если не веришь, то обернись - он так на тебя смотрит."
    hide ang_usual with dissolve
    scene bar_ with dissolve
    show gay with dissolve
    author "Гриша обернулся на барную стойку и заметил того парня,
    палящегося на... Ну вы поняли."
    grisha "......................."
    author "Гриша покраснел."
    hide gay with dissolve
    scene dance_floor with dissolve
    show ang_funny with dissolve
    angelina "Ха-ха-ха. Мы встречались с ним в школе, а потом он понял, что
    такой, ну и расстались."
    grisha "Мда..."
    hide ang_funny with dissolve
    play music disco_2 fadein 1 fadeout 1 volume 0.3
    return

# За барной стойкой с Валей
label scene_bar_valya:
    show valya_usual at right with dissolve
    show lyonya_usual at left with dissolve
    grisha "Лёнь, точно все в порядке?"
    lyonya "Д..."
    grisha "А кто этот хмырь?"
    valya "Бывший парень Ангелины вроде. Расстались,
    потому что он назвал ее чужим именем. Мужским.
    Ну ты понял... Конечно, были еще причины, но эта
    в том числе"
    grisha "А ты откуда знаешь все это, главная
    сплетница Унитеха?"
    valya "У меня свои каналы связи"
    grisha "Ладно, не нравится мне этот тип"
    valya "А Ангелина нравится? ;)"
    grisha "Э-э-э, да я просто интересуюсь, она же,
    ну-у-у, просто мне друг"
    valya "Я просто поняла :)"
    grisha "Пошлите лучше потанцуем"
    return

# За барной стойкой с Лёней
label scene_bar_lyonya:
    show lyonya_usual with dissolve
    grisha "Лёнь, точно все в порядке?"
    lyonya "Д..."
    grisha "А кто этот хмырь?"
    lyonya "Бывший парень Ангелины вроде. Расстались,
    потому что он назвал ее чужим именем. Мужским.
    Ну ты понял... Конечно, были еще причины, но эта
    в том числе"
    grisha "А ты откуда знаешь все это, главная
    сплетница Унитеха?"
    lyonya "Э-э-э, ну-у-у..."
    grisha "Ладно, не нравится мне этот тип"
    lyonya "А Ангелина нравится? ;)"
    grisha "Э-э-э, да я просто интересуюсь, она же,
    ну-у-у, просто мне друг"
    lyonya "Я просто понял :)"
    grisha "Пошли лучше потанцуем"
    return

# Конец клубешника
label scene_41:
    author "Спустя пару песен все почувствовали приятную усталость после
    насыщенного вечера и решили рзаъехаться по домам"
    return

# Репетиция бала
label scene_42:

    return
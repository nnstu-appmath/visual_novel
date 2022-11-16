# 4 курс
label fourth_year:
    call scene_47
    call scene_48
    call scene_50
    call scene_51
    call scene_52
    call scene_54
    call scene_55
    call scene_56
    call scene_57
    call scene_58
    #$ renpy.movie_cutscene("/images/background/4_year/credits.mpg")
    pause(4.0)
    return

# Журкин пугает всех госами
label scene_47:
    play music neutral_4 fadein 1 fadeout 1 volume 0.5
    scene auditorium with fade
    author "Обучение в Унитехе подходит к концу. Это был долгий путь, но дело
    осталось за малым. Все студенты, включая Гришу, уже расслабились и
    приготовились поскорее сдать все оставшиеся работы и пойти на заслуженный
    отдых от тяжелых учебных будней."
    show zhurkin with dissolve
    zhurkin "У вас остается один экзамен. Государственный экзамен. По статистике
    хотя бы несколько студентов его не сдает и отчисляется. Не расслабляйтесь,
    вас всех отчислят"
    hide zhurkin with dissolve
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    grisha "Надеюсь, это буду не я"
    lyonya "Да ладно, сдадим"
    if valya_score > 0:
        valya "А я вот тоже боюсь"
    hide lyonya_usual with dissolve
    hide valya_usual with dissolve
    hide ang_usual with dissolve
    show zhurkin with dissolve
    zhurkin "Принимать экзамен будет у вас Сократова Альбина Григорьевна.
    Готовьтесь."
    hide zhurkin with dissolve
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    grisha "Че, она Альбина Сократовна?"
    angelina "Кто это вообще?"
    grisha "Впервые слышу."
    lyonya "Звучит как что-то страшное"
    if valya_score > 0:
        valya "Может кто-то страшный?"
    else:
        angelina "Может кто-то страшный?"
    lyonya "Нет"
    return

# Ребята думают, как сдавать госы
label scene_48:
    scene before_aud with fade
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    grisha "Что делать будем?"
    angelina "Может спросить у выпускников?"
    lyonya "Хорошая идея, можно спросить кто это, и какие вопросы будут на экзамене"
    grisha "Может для начала узнаем, что за предмет?"
    if valya_score > 0:
        valya "По фамилии понятно, что философия"
    else:
        lyonya "По фамилии понятно, что философия"
    if undergraduate:
        grisha "У меня есть знакомые, которые уже выпустились. Сейчас спрошу"
        pause (1.0)
        grisha "Хм, сказали, что нам жопа..."
        angelina "Спроси, что за вопросы будут!"
        grisha "\"Каждый год вопросы меняются, это чистая лотерея,
        сдают далеко не все. В каком-то году экзамен 7 часов принимали\""
        lyonya "А темы какие хоть?"
        grisha "Да, сейчас"
        grisha "\"От политики до цвета носков у Киркорова. Просто удачи\""
        angelina "М-да, я попробую найти эту Сократовну и узнать настолько
        ли все плохо."
        grisha "Я помогу"
        if ang_score >= 8:
            angelina "Давай, пошли"
            scene bg_doors with fade
            show ang_usual at right with dissolve
            show sokratova at left with dissolve
            angelina "Здравствуйте, Альбина Григорьевна"
            sokratova "ДОБРЫЙ день, студенты"
            grisha "Вы же у нас будете принимать последний экзамен?"
            sokratova "Экзамен по такой ВАЖНОЙ науке могу принимать только я!"
            angelina "Можете поподробнее рассказать, что будет?"
            sokratova "Все, что проходили, то и будет"
            grisha "Но вы у нас ничего не вели..."
            sokratova "Философия - царица наук! Все, что вы
            изучали - это происходит от философии. УДАЧИ!"
            scene before_aud with fade
            show lyonya_usual at left with dissolve
            if valya_score > 0:
                show valya_usual with dissolve
            show ang_usual at right with dissolve
        else:
            hide ang_usual
            show ang_annoy at right
            angelina "Себе помоги!"
            with fade
            author "Ангелина вернулась с плохими новостями."
            angelina "Все плохо."
            grisha "А что плохо?"
            angelina "Она сказала, что будет все, что с ней проходили."
            if valya_score > 0:
                valya "Но мы с ней ничего не проходили"
            else:
                lyonya "Но мы с ней ничего не проходили"
            lyonya "Она вообще ничего не вела у нас"
            angelina "Вот и я об этом!"
            grisha "Дела отстой"
    else:
        angelina "Но у меня нет знакомых выпусников."
        lyonya "У меня тоже"
        grisha "Вы че, за 3 года так и не нашли себе друзей-старшеков?"
        if valya_score > 0:
            valya "А ты сам то нашел?"
        else:
            lyonya "А ты сам то нашел?"
        grisha "Нет"
        angelina "Ладно, попробую найти эту Сократовну и узнать"
        with fade
        author "Ангелина вернулась с плохими новостями."
        angelina "Все плохо."
        grisha "А что плохо?"
        angelina "Она сказала, что будет все, что с ней проходили."
        if valya_score > 0:
            valya "Но мы с ней ничего не проходили"
        else:
            lyonya "Но мы с ней ничего не проходили"
        lyonya "Она вообще ничего не вела у нас"
        angelina "Вот и я об этом!"
        grisha "Дела отстой"
    lyonya "Может быть развеемся перед экзаменом? Сходим куда-нибудь."
    grisha "Перед смертью не надышишься"
    if valya_score > 0:
        valya "Да ладно, до этой смерти еще далеко"
    else:
        lyonya "Да ладно, до этой смерти еще далеко"
    angelina "Кстати о надышимся, может на свежем воздухе пикничок устроим?
    Повторим материал какой-нибудь..."
    lyonya "Хорошая идея"
    return

# Парк
label scene_50:
    scene park with fade
    author "На выходных ребята пришли в парк"
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    lyonya "Опять ты со своим смузи из петрушки"
    grisha "Да остань ты от меня"
    lyonya "Тебе травы нарвать может?"
    grisha "Завидуешь?"
    lyonya "Фу-у-у"
    angelina "Эй, помогите еду разложить"
    grisha "Сам ты фу. Полезно между прочим"
    lyonya "Мерзость, укроп лучше"
    angelina "Гриша! Помоги!"
    grisha "Да, сейчас"
    if valya_score > 0:
        valya "Что за мужики пошли... Никакой помощи в этом доме"
        hide ang_usual
        show ang_funny at right
        angelina "Ха-ха-ха"
        hide ang_funny
        show ang_usual at right
    lyonya "Кстати, не хочу омрачать наш отдых, но вы готовились к экзамену?
    Я подобрал нужную литературу. Даже сходил в библиотеку, взял методичку
    Сократовны, изучил все..."
    grisha "Откройте окно"
    angelina "А я Смешариков смотрела. Там столько философских мыслей"
    grisha "Да, на балкончике в 4 утра столько же. Это считается?"
    if valya_score > 0:
        valya "Если ты с девушкой болтал, то нет"
    else:
        lyonya "Если ты с девушкой болтал, то нет"
    grisha "А что за стереотипы?"
    angelina "А что за девушка? Алиночка?"
    grisha "Нет, не Алиночка"
    angelina "Ладно, давайте отвлечемся от этих мыслей и покушаем"
    author "Весь оставшийся пикник ребята болтали и отдыхали, забыв о завтрашнем
    госэкзамене"
    return

# Перед госэкзаменом
label scene_51:
    scene before_aud with fade
    author "Наступило страшное. День госэкзамена"
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    angelina "Я не сдам"
    grisha "Ты так каждый раз говоришь, а потом сдаешь на 5"
    angelina "Вы не понимаете, это другое"
    lyonya "Я учил"
    if valya_score > 0:
        valya "Мы не сомневаемся"
    else:
        lyonya "Мы не сомневаемся"
    angelina "Кто первый пойдет? Чур не я"
    lyonya "Чур не я"
    if valya_score > 0:
        valya "Чур не я"
    grisha "....... черти. Ладно"
    return

# Госэкзамен
label scene_52:
    stop music
    scene auditorium with fade
    show sokratova at right with dissolve
    play sound mill_start fadeout 1 volume 0.5
    sokratova "Добрый день! Сегодняшний экзамен я хотела провести в СКАЙПЕ или
    в ЗУМЕ. Но текущие обстоятельства НЕ позволили мне так сделать."
    sokratova "Правила нашего экзамена таковы:"
    sokratova "1) Вы должны выбрать ОДИН правильный ответ из ЧЕТЫРЕХ. При выборе
    НЕПРАВИЛЬНОГО ответа - вы не сдали"
    sokratova "2) Вы можете воспользоваться ПОДСКАЗКОЙ пятьдесят на пятьдесят"
    sokratova "3) Также Вы можете ПОЗВОНИТЬ другу"
    sokratova "4) Всего ПЯТЬ вопросов"
    sokratova "5) Вы можете ответить на ТРИ и получить ЗАЧЕТ или ответить еще на
    ДВА, чтобы получить ОТЛИЧНО"
    grisha "А сколько экзамен будет идти?"
    sokratova "СЕМЬ часов"
    grisha "Дела отстой"
    sokratova "УДАЧИ!"
    call gosexam_1
    return

# 1 вопрос
label gosexam_1:
    play sound mill_ques fadein 1 fadeout 1 volume 0.5
    show mill_1_ques at left with dissolve
    menu:
        "Взять подсказку":
            menu:
                "Звонок Лёне":
                    $ call_lyonya = True
                    play sound mill_call fadein 1 fadeout 1 volume 0.5
                    grisha "Лёня, мне очень нужна твоя помощь. Что является
                    предметом философии?"
                    grisha "a) Отношения с Богом или иным высшим существом
                    б) Общие сущностные характеристики мира, отношение
                    человека к природе и обществу
                    в) Физическая реальность, ее характеристики
                    г) Принципы развития Вселенной"
                    grisha "Только быстро"
                    lyonya "Погоди, ну г) точно не подходит, а) тоже какая-то
                    хрень, а вообще ..."
                    grisha "Давай скорее"
                    lyonya "б"
                    grisha "Ты уверен?"
                    lyonya "Да я сам не знаю, ты за кого меня принимаешь,
                    это ж философия, ее кроме препода никто не знает."
                    grisha "Да она ее и придумала, наверное. Ладно, спасибо"
                    menu:
                        "а":
                            call gosexam_wrong
                        "б":
                            $ gosexam += 1
                            play sound mill_right fadein 1 fadeout 1 volume 0.5
                            sokratova "МОЛОДЕЦ! Следующий вопрос"
                            call gosexam_2
                        "в":
                            call gosexam_wrong
                        "г":
                            call gosexam_wrong
                "50/50":
                    $ fifty_fifty = True
                    show mill_1_ques_50 at left with dissolve
                    menu:
                        "б":
                            $ gosexam += 1
                            play sound mill_right fadein 1 fadeout 1 volume 0.5
                            sokratova "МОЛОДЕЦ! Следующий вопрос"
                            call gosexam_2
                        "в":
                            call gosexam_wrong
        "Выбрать ответ":
            menu:
                "а":
                    call gosexam_wrong
                "б":
                    $ gosexam += 1
                    play sound mill_right fadein 1 fadeout 1 volume 0.5
                    sokratova "МОЛОДЕЦ! Следующий вопрос"
                    call gosexam_2
                "в":
                    call gosexam_wrong
                "г":
                    call gosexam_wrong
    return

# 2 вопрос
label gosexam_2:
    if fifty_fifty:
        hide mill_1_ques_50 with dissolve
        hide mill_1_ques with dissolve
    else:
        hide mill_1_ques with dissolve
    play sound mill_ques fadein 1 fadeout 1 volume 0.5
    show mill_2_ques at left with dissolve
    if call_lyonya and not fifty_fifty:
        menu:
            "50/50":
                $ fifty_fifty = True
                show mill_2_ques_50 at left with dissolve
                menu:
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_3
                    "г":
                        call gosexam_wrong
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_3
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    elif not call_lyonya and fifty_fifty:
        menu:
            "Звонок Лёне":
                $ call_lyonya = True
                play sound mill_call fadein 1 fadeout 1 volume 0.5
                grisha "Лёня, мне очень нужна твоя помощь. Сколько запятых нужно
                поставить в предложении?"
                grisha "Когда наконец явилось солнце и разогрело землю то
                деревья и травы обдались такой сильной росой такими светящимися
                узорами глянули из темного леса ветки елей что казалось
                на эту отделку не хватило бы алмазов всей нашей земли."
                grisha "а) 3
                б) 4
                в) 5
                г) 6"
                grisha "Только быстро"
                lyonya "Погоди, ну по русскому у меня в 5 классе 4 было,
                сейчас скажу. Ну а) точно не подходит там оборот и все такое,
                г) тоже что-то многовато, а вообще ..."
                grisha "Давай скорее"
                lyonya "б"
                grisha "Ты уверен?"
                lyonya "Конечно, у меня же грамота есть за русского медвежонка"
                grisha "Ладно, спасибо"
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_3
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_3
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    elif call_lyonya and fifty_fifty:
        menu:
            "а":
                call gosexam_wrong
            "б":
                $ gosexam += 1
                play sound mill_right fadein 1 fadeout 1 volume 0.5
                sokratova "МОЛОДЕЦ! Следующий вопрос"
                call gosexam_3
            "в":
                call gosexam_wrong
            "г":
                call gosexam_wrong
    elif not call_lyonya and not fifty_fifty:
        menu:
            "Взять подсказку":
                menu:
                    "Звонок Лёне":
                        $ call_lyonya = True
                        play sound mill_call fadein 1 fadeout 1 volume 0.5
                        grisha "Лёня, мне очень нужна твоя помощь. Сколько запятых нужно
                        поставить в предложении?"
                        grisha "Когда наконец явилось солнце и разогрело землю то
                        деревья и травы обдались такой сильной росой такими светящимися
                        узорами глянули из темного леса ветки елей что казалось
                        на эту отделку не хватило бы алмазов всей нашей земли."
                        grisha "а) 3
                        б) 4
                        в) 5
                        г) 6"
                        grisha "Только быстро"
                        lyonya "Погоди, ну по русскому у меня в 5 классе 4 было,
                        сейчас скажу. Ну а) точно не подходит там оборот и все такое,
                        г) тоже что-то многовато, а вообще ..."
                        grisha "Давай скорее"
                        lyonya "б"
                        grisha "Ты уверен?"
                        lyonya "Конечно, у меня же грамота есть за русского медвежонка"
                        grisha "Ладно, спасибо"
                        menu:
                            "а":
                                call gosexam_wrong
                            "б":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_3
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
                    "50/50":
                        $ fifty_fifty = True
                        show mill_2_ques_50 at left with dissolve
                        menu:
                            "б":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_3
                            "г":
                                call gosexam_wrong
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_3
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    return

# 3 вопрос
label gosexam_3:
    if fifty_fifty:
        hide mill_2_ques_50 with dissolve
        hide mill_2_ques with dissolve
    else:
        hide mill_2_ques with dissolve
    play sound mill_ques fadein 1 fadeout 1 volume 0.5
    show mill_3_ques at left with dissolve
    if call_lyonya and not fifty_fifty:
        menu:
            "50/50":
                $ fifty_fifty = True
                show mill_3_ques_50 at left with dissolve
                menu:
                    "б":
                        call gosexam_wrong
                    "г":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        call gosexam_4
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        call gosexam_wrong
                    "в":
                        call gosexam_wrong
                    "г":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        call gosexam_4
    elif not call_lyonya and fifty_fifty:
        menu:
            "Звонок Лёне":
                $ call_lyonya = True
                play sound mill_call fadein 1 fadeout 1 volume 0.5
                grisha "Лёня, мне очень нужна твоя помощь. Как называются
                отношения между членами коллектива?"
                grisha "а) коллективистскими
                б) коммуникативными
                в) групповыми
                г) межличностными"
                grisha "Только быстро"
                lyonya "У-у-у, братан, это ты точно не по адресу, но давай
                рассуждать логически. Подходит в приницпе все, но я думаю
                в) слишком просто, а) тоже, а вообще ..."
                grisha "Давай скорее"
                lyonya "г"
                grisha "Ты уверен?"
                lyonya "Да, я погуглил"
                grisha "Ладно, спасибо"
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        call gosexam_wrong
                    "в":
                        call gosexam_wrong
                    "г":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        call gosexam_4
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        call gosexam_wrong
                    "в":
                        call gosexam_wrong
                    "г":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        call gosexam_4
    elif call_lyonya and fifty_fifty:
        menu:
            "а":
                call gosexam_wrong
            "б":
                call gosexam_wrong
            "в":
                call gosexam_wrong
            "г":
                $ gosexam += 1
                play sound mill_right fadein 1 fadeout 1 volume 0.5
                call gosexam_4
    elif not call_lyonya and not fifty_fifty:
        menu:
            "Взять подсказку":
                menu:
                    "Звонок Лёне":
                        $ call_lyonya = True
                        play sound mill_call fadein 1 fadeout 1 volume 0.5
                        grisha "Лёня, мне очень нужна твоя помощь. Как называются
                        отношения между членами коллектива?"
                        grisha "а) коллективистскими
                        б) коммуникативными
                        в) групповыми
                        г) межличностными"
                        grisha "Только быстро"
                        lyonya "У-у-у, братан, это ты точно не по адресу, но давай
                        рассуждать логически. Подходит в приницпе все, но я думаю
                        в) слишком просто, а) тоже, а вообще ..."
                        grisha "Давай скорее"
                        lyonya "г"
                        grisha "Ты уверен?"
                        lyonya "Да, я погуглил"
                        grisha "Ладно, спасибо"
                        menu:
                            "а":
                                call gosexam_wrong
                            "б":
                                call gosexam_wrong
                            "в":
                                call gosexam_wrong
                            "г":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                call gosexam_4
                    "50/50":
                        $ fifty_fifty = True
                        show mill_3_ques_50 at left with dissolve
                        menu:
                            "б":
                                call gosexam_wrong
                            "г":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                call gosexam_4
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        call gosexam_wrong
                    "в":
                        call gosexam_wrong
                    "г":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        call gosexam_4
    return

# 4 вопрос
label gosexam_4:
    sokratova "МОЛОДЕЦ! Вы можете продолжить экзамен и попробовать сдать на
    ОТЛИЧНО или уйти с ЗАЧЕТОМ"
    menu:
        "Попробовать на пятерочку":
            if fifty_fifty:
                hide mill_3_ques_50 with dissolve
                hide mill_3_ques with dissolve
            else:
                hide mill_3_ques with dissolve
            play sound mill_ques fadein 1 fadeout 1 volume 0.5
            show mill_4_ques at left with dissolve
            if call_lyonya and not fifty_fifty:
                menu:
                    "50/50":
                        $ fifty_fifty = True
                        show mill_4_ques_50 at left with dissolve
                        menu:
                            "а":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_5
                            "г":
                                call gosexam_wrong
                    "Выбрать ответ":
                        menu:
                            "а":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_5
                            "б":
                                call gosexam_wrong
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
            elif not call_lyonya and fifty_fifty:
                menu:
                    "Звонок Лёне":
                        $ call_lyonya = True
                        play sound mill_call fadein 1 fadeout 1 volume 0.5
                        grisha "Лёня, мне очень нужна твоя помощь. Нужно
                        расположить в хронологической последовательности:"
                        grisha "1) Невская битва
                        2) Битва на реке Калке
                        3) Столетняя война"
                        grisha "а) 213
                        б) 321
                        в) 231
                        г) 132"
                        grisha "Только быстро"
                        lyonya "История, конечно, не мой конек, но я попробую.
                        Ну битва на Калке была прям очень давно, так что либо
                        а) либо в) Наверное..."
                        grisha "Давай скорее"
                        lyonya "а"
                        grisha "Ты уверен?"
                        lyonya "Да, я погуглил"
                        grisha "Ладно, спасибо"
                        menu:
                            "а":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_5
                            "б":
                                call gosexam_wrong
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
                    "Выбрать ответ":
                        menu:
                            "а":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_5
                            "б":
                                call gosexam_wrong
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
            elif call_lyonya and fifty_fifty:
                menu:
                    "а":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                        call gosexam_5
                    "б":
                        call gosexam_wrong
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
            elif not call_lyonya and not fifty_fifty:
                menu:
                    "Взять подсказку":
                        menu:
                            "Звонок Лёне":
                                $ call_lyonya = True
                                play sound mill_call fadein 1 fadeout 1 volume 0.5
                                grisha "Лёня, мне очень нужна твоя помощь. Нужно
                                расположить в хронологической последовательности:"
                                grisha "1) Невская битва
                                2) Битва на реке Калке
                                3) Столетняя война"
                                grisha "а) 213
                                б) 321
                                в) 231
                                г) 132"
                                grisha "Только быстро"
                                lyonya "История, конечно, не мой конек, но я попробую.
                                Ну битва на Калке была прям очень давно, так что либо
                                а) либо в) Наверное..."
                                grisha "Давай скорее"
                                lyonya "а"
                                grisha "Ты уверен?"
                                lyonya "Да, я погуглил"
                                grisha "Ладно, спасибо"
                                menu:
                                    "а":
                                        $ gosexam += 1
                                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                                        call gosexam_5
                                    "б":
                                        call gosexam_wrong
                                    "в":
                                        call gosexam_wrong
                                    "г":
                                        call gosexam_wrong
                            "50/50":
                                $ fifty_fifty = True
                                show mill_4_ques_50 at left with dissolve
                                menu:
                                    "а":
                                        $ gosexam += 1
                                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                                        sokratova "МОЛОДЕЦ! Следующий вопрос"
                                        call gosexam_5
                                    "г":
                                        call gosexam_wrong
                    "Выбрать ответ":
                        menu:
                            "а":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "МОЛОДЕЦ! Следующий вопрос"
                                call gosexam_5
                            "б":
                                call gosexam_wrong
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
        "Уйти с зачетом":
            play music neutral_4 fadein 1 fadeout 1 volume 0.5
            scene before_aud with fade
            show lyonya_usual at left with dissolve
            if valya_score > 0:
                show valya_usual with dissolve
            show ang_usual at right with dissolve
            grisha "Фух, я сдал"
            angelina "Поздравляю"
            if call_lyonya:
                lyonya "Ну да-да, спасибо кое-кому"
                grisha "Да-да, спасибо"
            else:
                grisha "Без помощи друзей даже"
            grisha "Ладно, удачи, ребят, вы справитесь"
    return

# 5 вопрос
label gosexam_5:
    if fifty_fifty:
        hide mill_4_ques_50 with dissolve
        hide mill_4_ques with dissolve
    else:
        hide mill_4_ques with dissolve
    play sound mill_ques fadein 1 fadeout 1 volume 0.5
    show mill_5_ques at left with dissolve
    if call_lyonya and not fifty_fifty:
        menu:
            "50/50":
                $ fifty_fifty = True
                show mill_5_ques_50 at left with dissolve
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                        play music neutral_4 fadein 1 fadeout 1 volume 0.5
                        scene before_aud with fade
                        show lyonya_usual at left with dissolve
                        if valya_score > 0:
                            show valya_usual with dissolve
                        show ang_usual at right with dissolve
                        grisha "Я сдал на ПЯТЬ!!!"
                        angelina "Вау"
                        if call_lyonya:
                            lyonya "Ну да-да, спасибо кое-кому"
                            grisha "Да-да, спасибо"
                        else:
                            grisha "Без помощи друзей даже"
                        grisha "Ладно, удачи, ребят, вы справитесь"
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                        play music neutral_4 fadein 1 fadeout 1 volume 0.5
                        scene before_aud with fade
                        show lyonya_usual at left with dissolve
                        if valya_score > 0:
                            show valya_usual with dissolve
                        show ang_usual at right with dissolve
                        grisha "Я сдал на ПЯТЬ!!!"
                        angelina "Вау"
                        if call_lyonya:
                            lyonya "Ну да-да, спасибо кое-кому"
                            grisha "Да-да, спасибо"
                        else:
                            grisha "Без помощи друзей даже"
                        grisha "Ладно, удачи, ребят, вы справитесь"
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    elif not call_lyonya and fifty_fifty:
        menu:
            "Звонок Лёне":
                $ call_lyonya = True
                play sound mill_call fadein 1 fadeout 1 volume 0.5
                grisha "Лёня, мне очень нужна твоя помощь. Какие опасности
                относятся к техногенным?"
                grisha "а) наводнение
                б) производственные аварии в больших масштабах
                в) загрязнение воздуха
                г) природные катаклизмы"
                grisha "Только быстро"
                lyonya "Ну-у-у, техногенная опасность -  это состояние,
                внутренне присущее технической системе, ....дальше
                дальше.... промышленному или транспортному объекту,
                реализуемое в виде поражающих воздействий источника
                техногенной чрезвычайной ситуации....что то похожее...
                наверное это точно не в) хотя я не уверен"
                grisha "Давай скорее"
                lyonya "б"
                grisha "Ты уверен?"
                lyonya "Да, я погуглил"
                grisha "Ладно, спасибо"
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                        play music neutral_4 fadein 1 fadeout 1 volume 0.5
                        scene before_aud with fade
                        show lyonya_usual at left with dissolve
                        if valya_score > 0:
                            show valya_usual with dissolve
                        show ang_usual at right with dissolve
                        grisha "Я сдал на ПЯТЬ!!!"
                        angelina "Вау"
                        if call_lyonya:
                            lyonya "Ну да-да, спасибо кое-кому"
                            grisha "Да-да, спасибо"
                        else:
                            grisha "Без помощи друзей даже"
                        grisha "Ладно, удачи, ребят, вы справитесь"
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                        play music neutral_4 fadein 1 fadeout 1 volume 0.5
                        scene before_aud with fade
                        show lyonya_usual at left with dissolve
                        if valya_score > 0:
                            show valya_usual with dissolve
                        show ang_usual at right with dissolve
                        grisha "Я сдал на ПЯТЬ!!!"
                        angelina "Вау"
                        if call_lyonya:
                            lyonya "Ну да-да, спасибо кое-кому"
                            grisha "Да-да, спасибо"
                        else:
                            grisha "Без помощи друзей даже"
                        grisha "Ладно, удачи, ребят, вы справитесь"
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    elif call_lyonya and fifty_fifty:
        menu:
            "а":
                call gosexam_wrong
            "б":
                $ gosexam += 1
                play sound mill_right fadein 1 fadeout 1 volume 0.5
                sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                play music neutral_4 fadein 1 fadeout 1 volume 0.5
                scene before_aud with fade
                show lyonya_usual at left with dissolve
                if valya_score > 0:
                    show valya_usual with dissolve
                show ang_usual at right with dissolve
                grisha "Я сдал на ПЯТЬ!!!"
                angelina "Вау"
                if call_lyonya:
                    lyonya "Ну да-да, спасибо кое-кому"
                    grisha "Да-да, спасибо"
                else:
                    grisha "Без помощи друзей даже"
                grisha "Ладно, удачи, ребят, вы справитесь"
            "в":
                call gosexam_wrong
            "г":
                call gosexam_wrong
    elif not call_lyonya and not fifty_fifty:
        menu:
            "Взять подсказку":
                menu:
                    "Звонок Лёне":
                        $ call_lyonya = True
                        play sound mill_call fadein 1 fadeout 1 volume 0.5
                        grisha "Лёня, мне очень нужна твоя помощь. Какие опасности
                        относятся к техногенным?"
                        grisha "а) наводнение
                        б) производственные аварии в больших масштабах
                        в) загрязнение воздуха
                        г) природные катаклизмы"
                        grisha "Только быстро"
                        lyonya "Ну-у-у, техногенная опасность -  это состояние,
                        внутренне присущее технической системе, ....дальше
                        дальше.... промышленному или транспортному объекту,
                        реализуемое в виде поражающих воздействий источника
                        техногенной чрезвычайной ситуации....что то похожее...
                        наверное это точно не в) хотя я не уверен"
                        grisha "Давай скорее"
                        lyonya "б"
                        grisha "Ты уверен?"
                        lyonya "Да, я погуглил"
                        grisha "Ладно, спасибо"
                        menu:
                            "а":
                                call gosexam_wrong
                            "б":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                                play music neutral_4 fadein 1 fadeout 1 volume 0.5
                                scene before_aud with fade
                                show lyonya_usual at left with dissolve
                                if valya_score > 0:
                                    show valya_usual with dissolve
                                show ang_usual at right with dissolve
                                grisha "Я сдал на ПЯТЬ!!!"
                                angelina "Вау"
                                if call_lyonya:
                                    lyonya "Ну да-да, спасибо кое-кому"
                                    grisha "Да-да, спасибо"
                                else:
                                    grisha "Без помощи друзей даже"
                                grisha "Ладно, удачи, ребят, вы справитесь"
                            "в":
                                call gosexam_wrong
                            "г":
                                call gosexam_wrong
                    "50/50":
                        $ fifty_fifty = True
                        show mill_5_ques_50 at left with dissolve
                        menu:
                            "а":
                                call gosexam_wrong
                            "б":
                                $ gosexam += 1
                                play sound mill_right fadein 1 fadeout 1 volume 0.5
                                sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                                play music neutral_4 fadein 1 fadeout 1 volume 0.5
                                scene before_aud with fade
                                show lyonya_usual at left with dissolve
                                if valya_score > 0:
                                    show valya_usual with dissolve
                                show ang_usual at right with dissolve
                                grisha "Я сдал на ПЯТЬ!!!"
                                angelina "Вау"
                                if call_lyonya:
                                    lyonya "Ну да-да, спасибо кое-кому"
                                    grisha "Да-да, спасибо"
                                else:
                                    grisha "Без помощи друзей даже"
                                grisha "Ладно, удачи, ребят, вы справитесь"
            "Выбрать ответ":
                menu:
                    "а":
                        call gosexam_wrong
                    "б":
                        $ gosexam += 1
                        play sound mill_right fadein 1 fadeout 1 volume 0.5
                        sokratova "ПОЗДРАВЛЯЮ! Сдали на ОТЛИЧНО!"
                        play music neutral_4 fadein 1 fadeout 1 volume 0.5
                        scene before_aud with fade
                        show lyonya_usual at left with dissolve
                        if valya_score > 0:
                            show valya_usual with dissolve
                        show ang_usual at right with dissolve
                        grisha "Я сдал на ПЯТЬ!!!"
                        angelina "Вау"
                        if call_lyonya:
                            lyonya "Ну да-да, спасибо кое-кому"
                            grisha "Да-да, спасибо"
                        else:
                            grisha "Без помощи друзей даже"
                        grisha "Ладно, удачи, ребят, вы справитесь"
                    "в":
                        call gosexam_wrong
                    "г":
                        call gosexam_wrong
    return

# Гриша не сдал госэкзамен
label gosexam_wrong:
    play sound mill_wrong fadein 1 fadeout 1 volume 0.8
    sokratova "УВЫ! Вам не дано понять эту сложную науку."
    play music neutral_4 fadein 1 fadeout 1 volume 0.5
    scene before_aud with fade
    show lyonya_usual at left with dissolve
    if valya_score > 0:
        show valya_usual with dissolve
    show ang_usual at right with dissolve
    grisha "Штож..."
    lyonya "Ну ты не расстраивайся. Может не отчислят."
    if exam_score >= 3:
        grisha "Ну да, в целом, я остальные экзамены сдавал. Может пронесет"
    else:
        grisha "У меня половина экзаменов не сдано"
    grisha "Ладно, удачи, ребят, вы справитесь"
    return

# Концовки Ангелины, Лёни и Вали в кафе
label scene_54:
    scene cafe with fade
    author "Экзамены пройдены. Почти все закончилось. Ребята решили встретиться
    в кафе, чтобы отпраздновать окончание обучения и подвести итоги всех 4 лет."
    if ang_score >= 8 and dance_partner_ang:
        show lyonya_usual at left with dissolve
        if valya_score > 0:
            show valya_usual with dissolve
        show ang_usual at right with dissolve
        angelina "Мое самое хорошее воспоминание за эти 4 года это, конечно
        же конкурс \"Мисс Унитех 2022\". Эта победа многое значит для меня.
        Гриша, спасибо, что помог мне тогда"
        if love:
            $ best_end += 1
            grisha "Да не за что, любимая"
            angelina "Я тебя люблю"
            grisha "И я тебя"
            lyonya "Фу, меня сейчас стошнит"
            $ renpy.notify("Концовка Ангелины: \"Любовь-морковь\"")
            pause(1.0)
        else:
            grisha "Да не за что. Друзьям всегда помогают"
            lyonya "Ты тогда была прекрасна в платье. Хорошо, что ты танцевала
            с Гришей, а не со мной, я бы тебе все ноги отдавил"
            if valya_score > 0:
                valya " Да уж, танцевать тектоник у тебя выходит лучше, чем вальс"
            $ renpy.notify("Концовка Ангелины: \"Хорошие ДРУЗЬЯ\"")
            pause(1.0)
    elif ang_score < 8:
        if valya_score > 0:
            show lyonya_usual at left with dissolve
            show valya_usual at right with dissolve
        else:
            show lyonya_usual with dissolve
        author "Но Ангелина даже не пришла на эту встречу. Она все еще обижается
        на Гришу."
        author "Ведь она не выиграла в конкурсе из-за Гриши"
        lyonya "Зря ты так поступил тогда"
        grisha "В смысле?"
        if dance_partner_ang:
            lyonya "Ну Ангелина тебе намекала, что ты ей нравишься, а ты даже
            внимание на это не обратил. Ну хотя бы танцевал лучше, Ангелина бы
            выиграла и все было бы хорошо. А так ни себе, ни людям"
            grisha "Мне жаль, но давайте больше не будем говорить об Ангелине.
            Проехали"
        elif alina_score >= 6 and dance_partner_alina:
            lyonya "Ангелину ты знаешь много лет, она тебя просила о помощи,
            а ты повелся на дешевые подкаты незнакомки, которая тебя еще и кинула"
            grisha "Кто ж знал. Давайте больше не будем говорить об Ангелине.
            Проехали"
        elif alina_score < 6 and dance_partner_alina:
            $ worth_end += 1
            lyonya "Тебя о помощи просили две девушки, а ты ни одной из них не
            помог"
            grisha "Так получилось. Давайте больше не будем говорить о них.
            Проехали"
        $ renpy.notify("Концовка Ангелины: \"Ни себе, ни людям\"")
        pause(1.0)
    if lyonya_score >= 2 and valya_score > 0:
        $ best_end += 1
        grisha "Ну а вы, голубки, что у вас?"
        hide lyonya_usual
        show lyonya_confused at left
        lyonya "Э-э-э"
        valya "Все хорошо, завтра поедем к моим родителям знакомиться"
        lyonya "Я стесняюсь. А вдруг я им не понравлюсь..."
        valya "Ничего страшного, они тебя не съедят"
        grisha "Какие вы милые. Не зря я вас свел"
        hide lyonya_confused
        show lyonya_usual at left
        hide valya_usual with dissolve
        hide ang_usual with dissolve
        lyonya "Пс-с-с, Гриш"
        grisha "Что?"
        lyonya "Смотри"
        show ring with dissolve
        pause (2.0)
        hide ring with dissolve
        grisha "Вау, ты что собираешься делать предложение Вале?"
        lyonya "Да, завтра как раз когда к родителям поедем"
        grisha "Круто, счастья вам. Детишек там побольше"
        lyonya "Какие детишки???"
        grisha "Шучу"
        show valya_usual with dissolve
        show ang_usual at right with dissolve
        author "Ребята посидели еще некоторое время и разошлись"
        $ renpy.notify("Концовка Лёни: \"Эх, свадьба пела и плясала\"")
        pause(2.0)
    elif lyonya_score < 2 and valya_score > 0:
        grisha "Ну а вы, голубки, что у вас?"
        hide lyonya_usual
        show lyonya_sad at left
        lyonya "Э-э-э, ничего"
        valya "А что должно быть? У меня вообще-то парень есть"
        grisha "Я что зря сводил вас все эти годы???"
        hide lyonya_sad
        show lyonya_usual at left
        valya "А ты сводил?"
        grisha "Ну вы же такие милые"
        hide lyonya_usual
        show lyonya_sad at left
        lyonya "Мы просто друзья."
        grisha "Да ну вас"
        author "Ребята посидели еще некоторое время и разошлись"
        $ renpy.notify("Концовка Лёни: \"Одинокий волк\"")
        pause(2.0)
    elif valya_score < 0:
        $ worth_end += 1
        grisha "Ты что так погрустнел?"
        hide lyonya_usual
        show lyonya_sad at left
        lyonya "Вспомнил, что Вали рядом с нами нет"
        grisha "Ну она же не умерла"
        lyonya "И что??? Она была для меня всем! А мы ее не спасли.
        Ты ее не спас!"
        grisha "Почему я? Почему я должен всем помогать? Кто поможет мне,
        например???"
        hide lyonya_sad
        show lyonya_angry at left
        lyonya "Да что ты за друг после этого? Я все эти годы терпел, но больше
        не могу! Мне противно с тобой общаться..."
        hide lyonya_angry
        author "Лёня встает из-за стола и уходит из кафе."
        grisha "Ну и ну..."
        $ renpy.notify("Концовка Лёни: \"ДЕЛА ОТСТОЙ\"")
        pause(2.0)
    return

# Перед вручением дипломов
label scene_55:
    scene central_entrance with fade
    author "Последний день в Унитехе. Объявление результатов обучения. Кто же
    получит заветный диплом, а кого отчислят за неуспеваемость?"
    return

# Вручение дипломов - концовки Гриши
label scene_56:
    play music solemn fadein 1 fadeout 1 volume 0.5
    scene baz with fade
    show zhurkin at left with dissolve
    zhurkin "Рад видеть всех, кто дошел до этого момента. Сегодня мы объявим тех,
    кто благодаря своим знаниям, получит красный диплом, кто получит синий, а
    кого мы отчислим со справкой. Или даже без. Начнем торжественное вручение
    ваших дипломов. Пойдем по списку."
    author "Журкин начал перечислять всех одногруппников ребят. И наконец дошел
    до буквы Л"
    if valya_score > 0:
        zhurkin "Диплом бакалавра получает"
        zhurkin "Лаврентьева Валентина"
        show valya_usual at right with dissolve
        author "Валя выходит на сцену за своим дипломом"
        valya "Ура, наконец-то."
        hide zhurkin with dissolve
        hide valya_usual with dissolve
        show lyonya_usual at left with dissolve
        show valya_usual at right with dissolve
        lyonya "Поздравляю!"
        valya "Спасибо"
        hide lyonya_usual with dissolve
        hide valya_usual with dissolve
        show zhurkin at left with dissolve
    zhurkin "Диплом бакалавра с отличием получает"
    zhurkin "Лукьянов Леонид"
    show lyonya_happiness at right with dissolve
    author "Лёня поднимается на сцену и забирает свой заслуженный диплом"
    lyonya "О божечки! Спасибо!"
    hide lyonya_happiness with dissolve
    zhurkin "Диплом бакалавра с отличием получает"
    zhurkin "Муравьева Ангелина"
    show ang_happiness at right with dissolve
    author "Ангелина тоже забирает свой заслуженный диплом"
    hide ang_happiness with dissolve
    hide zhurkin with dissolve
    show lyonya_usual at left with dissolve
    show ang_happiness at right with dissolve
    lyonya "Поздравляю!"
    grisha "Поздравляю"
    angelina "Спасибо!"
    hide lyonya_usual with dissolve
    hide ang_happiness with dissolve
    show zhurkin at left with dissolve
    zhurkin "И последний"
    if diplom >= 4 and exam_score >= 3:
        $ best_end += 1
        zhurkin "Григорий Орехов получает диплом бакалавра с отличием"
        author "Гриша поднялся на сцену и получил красный диплом"
        grisha "Ничего себе я гений"
        zhurkin "На этой ноте наше мероприятие подходит к концу. Всем спасибо.
        Удачи в поисках работы!"
        $ renpy.notify("Концовка Гриши: \"Гений\"")
        pause(2.0)
    elif exam_score >= 3 and diplom < 4:
        zhurkin "Григорий Орехов получает диплом бакалавра"
        author "Гриша поднялся на сцену и получил свой диплом"
        grisha "Класс"
        zhurkin "На этой ноте наше мероприятие подходит к концу. Всем спасибо.
        Удачи в поисках работы!"
        $ renpy.notify("Концовка Гриши: \"Хорошая работа, Гриша\"")
        pause(2.0)
    elif exam_score < 3:
        $ worth_end += 1
        zhurkin "Григорий Орехов отчислен за неуспеваемость. Справку получите
        в деканате"
        grisha ".............."
        grisha "Не получилось, не фортануло"
        zhurkin "На этой ноте наше мероприятие подходит к концу. Всем спасибо.
        Удачи в поисках работы!"
        $ renpy.notify("Концовка Гриши: \"Не фортануло\"")
        pause(2.0)
    return

# Конец игры
label scene_57:
    play music neutral_4 fadein 1 fadeout 1 volume 0.5
    scene central_entrance with fade
    grisha "Даже не верю, что это все закончилось. Интересный, конечно, был опыт."
    scene central_entrance_blur with Dissolve(3)
    return

# Общие концовки игры
label scene_58:
    if best_end == 3:
        scene art_best_end with fade
        $ renpy.notify("Вы прошли игру. Ваша концовка: \"Мегахарош\"")
        pause(5.0)
    elif best_end < 3 and worth_end < 3:
        if valya_score > 0:
            scene art_neutral_end_valya with fade
        else:
            scene art_neutral_end with fade
        $ renpy.notify("Вы прошли игру. Ваша концовка: \"Стандарт\"")
        pause(5.0)
    elif worth_end == 3:
        scene art_bad_end with fade
        $ renpy.notify("Вы прошли игру. Ваша концовка: \"Мегаотстой\"")
        pause(5.0)
    stop music
    scene black with fade
    author "Любой Ваш выбор влияет на дальнейшую судьбу."
    author "Но можно ли изменить исход событий?.."
    scene black with dissolve
    pause (2.0)
    return

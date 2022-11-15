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
    call credits
    pause(4.0)
    scene black with fade
    pause (2.0)
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
    return

#
label scene_55:

    return

#
label scene_56:

    return

#
label scene_57:

    return

#
label scene_58:

    return

# 1 курс
label first_year:
    call scene_6
    call scene_7
    call scene_8
    call scene_9
    return

# Вводная фраза
label scene_6:
    scene bg_autumn with fade
    play music neutral_2 fadein 1
    author "1 курс и первые учебные дни, месяцы... Ребята привыкают к студенческой жизни.
    Не всегда получается сдавать вовремя контрольные работы, коллоквиумы.
    В целом учеба проходит довольно спокойно и без каких-либо сложностей."
    author "Помимо учебы Гриша со своими одногруппниками - Лёней и Валей - общаются
    и развлекаются в различных заведениях. Однако не все бывает так сладко -
    наступает черед экзаменов, которые предстоит сдать."
    return

# Гриша идет на экзы
label scene_7:
    scene central_entrance with fade
    author "Гриша идет на свои первые экзамены. Нервничает,
    потому что особо не готовился к ним, но все же расчитывает
    на успех или какую-нибудь помощь. Стараясь заглушить мысли
    о надвигающихся проблемах, решил оглянуться по сторонам на улице."
    grisha "Старшекурсники стоят... Надеюсь, что я доучусь до 4 курса
    без приключений. Хотя приключения уже были..."
    return

# День первака - клубешник
label scene_8:
    scene black with fade
    pause (2.0)
    scene club with fade
    play music disco_1 fadein 1 fadeout 1 volume 0.3
    author "Наступил долгожданный день первокурсника.
    Гриша пришел на него один и пытается найти знакомые лица -
    Лёню и Валю, которые тоже обещали прийти."
    show lyonya_usual with dissolve
    grisha "О, Лёня! Че как"
    lyonya "Да норм. Такая крутая музыка тут играет."
    grisha "Отстой какой-то, а не музыка."
    lyonya "Не правда! Ладно, как тебе начало учебы?"
    grisha "Ну как видишь, пришел отдохнуть от нее,
    скучно как-то. А тебе?"
    lyonya "Ничего нового, все уже знал в школе, я вообще-то
    в специализированном лицее учился! Есть конечно пару
    факультативов интересных, например..."
    grisha "О, смотри, Валя танцует уже во всю"
    if grisha_romantic:
        $ lyonya_score += 1
        grisha "Пошли к ней?"
        lyonya "Пойдем"
        hide lyonya_usual with dissolve
        scene dance_floor with fade
        show valya_usual at right with dissolve
        girsha "Привет, Валя. Ты давно тут?"
        valya "Ого, Лёня, ты все таки нашел время. Не, пришла минут 15 назад, а вы?"
        hide lyonya_usual
        show lyonya_confused
        lyonya "Ну-у-у, я..."
        grisha "Мы тоже недавно."
        valya "Тут такая классная музыка играет!"
        girsha "Вы че, сговорились что-ли..."
        hide lyonya_confused
        show lyonya_usual
        lyonya "Мне тоже нравится!"
        valya "Ладно, неважно, давайте пустимся сегодня
        во все тяжкие мы ведь сюда за этим пришли!"
        lyonya "Д-д-да! Давайте..."
        author "Ребята танцуют под какой-то странный тектоник.
        В 2022 году тектоник... Спустя время Гриша решает пойти к барной стойке."
        hide valya_usual
        hide lyonya_usual
    else:
        menu:
            "Пойду-ка я к ней":
                hide lyonya_usual with dissolve
                scene dance_floor with fade
                grisha "Привет, Валя"
                show valya_usual with dissolve
                valya "Привет, присоединяйся"
                "Гриша и Валя танцуют под какой-то странный тектоник.
                В 2022 году тектоник..."
                valya "А ты не видел Лёню? Кажется, ему не нравится танцевать."
                grisha "Похоже, что да."
                hide valya_usual with dissolve
                "Спустя некоторое время Гриша решил пойти к барной стойке."
            "Пошли к ней?":
                $ lyonya_score += 1
                lyonya "Пойдем"
                hide lyonya_usual with dissolve
                scene dance_floor with fade
                show lyonya_usual at left with dissolve
                show valya_usual at right with dissolve
                grisha "Привет, Валя. Ты давно тут?"
                valya "Ого, Лёня, ты все таки нашел время. Не, пришла минут 15 назад, а вы?"
                hide lyonya_usual
                show lyonya_confused at left
                lyonya "Ну-у-у, я..."
                grisha "Мы тоже недавно."
                valya "Тут такая классная музыка играет!"
                grisha "Вы че, сговорились что-ли..."
                hide lyonya_confused
                show lyonya_usual at left
                lyonya "Мне тоже нравится!"
                valya "Ладно, неважно, давайте пустимся сегодня
                во все тяжкие мы ведь сюда за этим пришли!"
                lyonya "Д-д-да! Давайте..."
                author "Ребята танцуют под какой-то странный тектоник.
                В 2022 году тектоник... Спустя время Гриша решает пойти к барной стойке."
                hide valya_usual
                hide lyonya_usual
    return

# Замес у барной стойки
label scene_9:
    scene bar_ with fade
    play music disco_2 fadein 1 volume 0.3
    show barman with dissolve
    grisha "Можно мне смузи из петрушки?"
    barman "Да, конечно"
    hide barman with dissolve
    author "Рядом с барной стойкой начинается словесная потасовка
    каких-то людей. Гриша решает подслушать о чем идет речь."
    show abuser at right with dissolve
    show defender at left with dissolve
    abuser "Валя куртизанка, все об этом знают!"
    defender "Мамка твоя куртизанка, рот свой не розевай на даму!"
    abuser "Да я ее в туалет позову и она согласится!"
    defender "Да как ты смеешь такое говорить о девушке, псина сутулая!"
    menu:
        "Защитить Валю":
            $ undergraduate = True
            $ valya_score += 1
            grisha "Да тебе за такие слова в моем селе уже бы лицо снесли"
            defender "Внатуре, а я помогу даже!"
            grisha "Да слыш, пёс"
            abuser "Ты че, блин"
            defender "Ты нарываешься явно"
            grisha "Мы тебе все косточки переломаем"
            abuser "Ну попробуй, давай!"
            author "Разговор явно переходит границы культурного общения.
            Внезапно подходит Лёня."
            show lyonya_usual with dissolve
            lyonya "Э-э-э, ребята, давайте решим мирным путем всё"
            abuser "Ты еще кто такой?..."
            grisha "Только попробуй его тронуть, он КМС по боксу"
            abuser "Ну да, по нему видно..."
            author "Обидчик Вали решил закончить сей бессмысленный разговор."
            abuser "Да пошли вы..."
            defender "Давай катись отсюда"
            hide abuser with dissolve
            hide lyonya_usual with dissolve
            show lyonya_usual at right with dissolve
            hide defender
            show sanya_usual at left
            defender "Тебя как зовут хоть?"
            grisha "Гриша"
            defender "Я - Саня. Если вдруг помощь какая понадобится, зови,
            ты вроде не мутный поц."
            grisha "Ок, буду иметь ввиду."
            hide defender
            show sanya_usual
            sanya "Давай, бывай."
            hide sanya_usual with dissolve
        "Промолчать, чтобы не получить по лицу":
            defender "Да слыш, пёс"
            abuser "Ты че, блин"
            defender "Ты нарываешься явно. Я тебе все косточки переломаю"
            abuser "Ну попробуй, давай!"
            author "Разговор явно переходит границы культурного общения."
            hide abuser with dissolve
            hide defender with dissolve
    grisha "Такого развития вечера я не ожидал.
    Бедная Валя, надеюсь она не знает об этих слухах...
    Мало ли как могло бы это на нее повлиять.
    Пожалуй, пойду домой."
    return

# 1 курс
label first_year:
    call scene_6
    call scene_7
    call scene_8
    call scene_9
    call scene_10
    call scene_11
    call scene_12
    call scene_12_a
    call scene_13
    call scene_14
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
    scene central_entrance_blur with Dissolve(1.5)
    return

# День первака - клубешник
label scene_8:
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
        grisha "Привет, Валя. Ты давно тут?"
        valya "Ого, Лёня, ты все таки нашел время. Не, пришла минут 15 назад, а вы?"
        hide lyonya_usual
        show lyonya_confused
        lyonya "Ну-у-у, я..."
        grisha "Мы тоже недавно."
        valya "Тут такая классная музыка играет!"
        grisha "Вы че, сговорились что-ли..."
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
    play music neutral_2 fadein 1 fadeout 1 volume 0.5
    scene bar_blur with Dissolve(1.5)
    return

# Разговор со старшеками
label scene_10:
    scene central_entrance with fade
    if undergraduate:
        grisha "Блин, это же Саня! Надо к нему подойти.
        Может поможет советом хоть."
        show sanya_usual with dissolve
        sanya "Дарова, братан!"
        grisha "Здарова, че как"
        sanya "Да все по-старому, ты куда таким важным шагом направляешься?"
        grisha "Экзамены..."
        sanya "Кому сдаешься-то?"
        grisha "Фичаев и Пряморуков"
        sanya "Ты че сразу не сказал, у меня уже 2 года в рюкзаке
        лежат шпоры по их предметам. Как сдал, так и не вытаскивал.
        На удачу ношу. На. Тебе щас нужнее."
        grisha "Спасибо, спас, а то я особо не учил ничего."
        sanya "С моими шпорами точно сдашь, проверено."
        hide sanya_usual
    else:
        grisha "Как хорошо старшекам, они уже все сдали. А я как лох иду туда."
    return

# Гриша перед экзаменом Пряморукова
label scene_11:
    scene before_aud with fade
    author "Гриша поднимается к аудитории, в которой будет
    проходить экзамен."
    grisha "А че вы все тут сидите?"
    show ang_usual with dissolve
    angelina "Так по одному все заходят. Присаживайся."
    author "Гриша начинает чувствовать панику, подступающую к горлу."
    grisha "Чур я последний, я вообще не готовился."
    angelina "Как хочешь."
    grisha "А как Пряморукова зовут?"
    angelina "Владимир Степанович"
    grisha "Надо быстро вспомнить все, что проходили на парах,
    может попадутся похожие задания."
    scene before_aud_blur with Dissolve(1.5)
    hide ang_usual
    return

# Контрольная у Пряморукова
label scene_12:
    scene aud with fade
    author "На одном из занятий Пряморуков дает
    контрольную работу. Гриша же как всегда,
    особо не готовился и надеется списать."
    grisha "Так ну это я точно не решу,
    второе - даже слов таких не знаю, третье - ну-у-у...
    Ладно, надо подумать у кого списать."
    author "В это время Ангелина уже встала и пошла сдавать работу."
    grisha "О, пс-с-с, Ангелин, скажи ответы, пж."
    show ang_usual with dissolve
    if ang_score == 1:
        angelina "Ладно, сейчас напишу."
        author "Ангелина передает скомканую бумажку с ответами."
        grisha "Спасибо!!! Повезло-повезло"
        show aud_blur with Dissolve(1.5)
        hide ang_usual
        return
    else:
        hide ang_usual
        show ang_angry
        angelina "Ты бы лучше манерам поучился, хамло."
        grisha "Ну эй, я же не специально тогда."
        angelina "Ну вот и пиши контрольную сам."
        grisha "Дела отстой."
        show aud_blur with Dissolve(1.5)
        hide ang_angry
        return

# Снова перед экзаменом Пряморукова
label scene_12_a:
    scene before_aud with fade
    if ang_score == 1:
        author "Гриша облегченно вздыхает, потому что
        получил пятерку за ту контрольную."
        grisha "Может мне это чем-то поможет."
    else:
        author "Гриша еще больше расстраивается,
        потому что не смог списать, и получил 2."
        grisha "Дела отстой."
    author "Совершенно незаметно вся очередь уже прошла
    и около аудитории остался только он. Из аудитории
    выходит Лёня с очень удивленным видом и достаточно
    ошарашенный."
    show lyonya_usual with dissolve
    grisha "Ну че-че там?"
    lyonya "Н-н-ничего... Иди, ты последний остался."
    grisha "Ладно, от судьбы не убежать."
    return

# Выбор перед экзаменом Пряморукова
label scene_13:
    scene auditorium with fade
    show pryamorukov_usual with dissolve
    pryamorukov "Ну что, Орехов, сдаемся?"
    grisha "Русские не сдаются"
    menu:
        "Сдавать экзамен":
            call scene_13_exam_1q
        "Попробовать выкрутиться":
            if ang_score == 0 and undergraduate == False:
                author "К сожалению, у Гриши нет друзей,
                которые ему могли бы помочь."
                call scene_13_exam_1q
            if ang_score == 0 and undergraduate == True:
                author "Гриша решил воспользоваться шпорами,
                которые дал ему Саня"
                grisha "Саня хороший чел... Дай Бог ему здоровья"
                pryamorukov "Иди, сдал."
                grisha "Фух, пронесло"
                $ exam_score += 1
            if ang_score == 1:
                grisha "Владимир Степанович, я там контрольную написал
                же на 5. Может троечку автоматом поставите?"
                pryamorukov "У, бестолочь! Ладно, не хочу с тобой возиться."
                $ exam_score += 1
    return

# Экзамен Пряморукова
label scene_13_exam_1q:
    play music fighting fadein 1 fadeout 1 volume 0.5
    scene exam_pryam_start with fade
    hide pryamorukov_usual with dissolve
    show pryamorukov_usual at right with dissolve
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'scene_13_exam_1q_wrong'
    author "Резко над головой у Пряморукова появляется шкала здоровья.
    Гриша замечает, что у него тоже она появилась."
    grisha "чего..."
    pryamorukov "Итак, первый вопрос... Как зовут Алексеева?"
    if grisha_smart:
        grisha "Ростислав Евгеньевич"
        scene exam_pryam_full_grisha_2_3_pryam with hpunch
        hide pryamorukov_usual
        show pryamorukov_wound at right
        pryamorukov "Ох-х-х"
        hide pryamorukov_wound
        show pryamorukov_usual at right
        pryamorukov "Второй вопрос: В честь кого, назвали большее количество объектов
        (теоремы, формулы и т.д.)"
        grisha "Эйлер"
    else:
        show screen countdown
        menu:
            "Елисей Ростиславович":
                hide screen countdown
                call scene_13_exam_1q_wrong
            "Ростислав Евгеньевич":
                hide screen countdown
                $ exam_pryam_1q = True
                call scene_13_exam_1q_right
            "Родион Ефимович":
                hide screen countdown
                call scene_13_exam_1q_wrong
    return

label scene_13_exam_1q_wrong:
    scene exam_pryam_2_3_grisha_full_pryam with hpunch
    hide pryamorukov_usual
    show pryamorukov_angry at right
    grisha "Ау, больно"
    pryamorukov "У, бестолочь!"
    hide pryamorukov_angry
    show pryamorukov_usual at right
    call scene_13_exam_2q
    return

label scene_13_exam_1q_right:
    scene exam_pryam_full_grisha_2_3_pryam with hpunch
    hide pryamorukov_usual
    show pryamorukov_wound at right
    pryamorukov "Ох-х-х"
    hide pryamorukov_wound
    show pryamorukov_usual at right
    call scene_13_exam_2q
    return

label scene_13_exam_2q:
    pryamorukov "Второй вопрос: В честь кого, назвали большее количество объектов
    (теоремы, формулы и т.д.)"
    $ time = 300
    $ timer_range = 300
    $timer_call = 'scene_13_exam_2q_wrong'
    show screen countdown
    menu:
        "Коши":
            hide screen countdown
            call scene_13_exam_2q_wrong
        "Гаусс":
            hide screen countdown
            call scene_13_exam_2q_wrong
        "Эйлер":
            hide screen countdown
            $ exam_pryam_2q = True
            call scene_13_exam_2q_right
    return

label scene_13_exam_2q_wrong:
    if exam_pryam_1q:
        scene exam_pryam_2_3_grisha_2_3_pryam with hpunch
    else:
        scene exam_pryam_1_3_grisha_full_pryam with hpunch
    hide pryamorukov_usual
    show pryamorukov_angry at right
    grisha "Ау, больно"
    pryamorukov "У, бестолочь!"
    hide pryamorukov_angry
    show pryamorukov_usual at right
    call scene_13_exam_3q
    return

label scene_13_exam_2q_right:
    if exam_pryam_1q:
        scene exam_pryam_full_grisha_1_3_pryam with hpunch
    else:
        scene exam_pryam_2_3_grisha_2_3_pryam with hpunch
    hide pryamorukov_usual
    show pryamorukov_wound at right
    pryamorukov "Ох-х-х"
    hide pryamorukov_wound
    show pryamorukov_usual at right
    call scene_13_exam_3q
    return

label scene_13_exam_3q:
    pryamorukov "Третий вопрос: Сколько здесь треугольников?"
    show q3_pryam at left with dissolve
    $ time = 300
    $ timer_range = 300
    $ timer_call = 'scene_13_exam_3q_wrong'
    show screen countdown
    menu:
        "9":
            $ timer_call = 'scene_13_exam_3q_wrong'
            $ time = -10
            hide screen countdown
            call scene_13_exam_3q_wrong
        "6":
            $ timer_call = 'scene_13_exam_3q_wrong'
            $ time = -10
            hide screen countdown
            call scene_13_exam_3q_wrong
        "8":
            $ exam_pryam_3q = True
            $ timer_call = 'scene_13_exam_3q_right'
            $ time = -10
            hide screen countdown
            call scene_13_exam_3q_right
    return

label scene_13_exam_3q_wrong:
    if exam_pryam_1q and exam_pryam_2q:
        scene exam_pryam_2_3_grisha_1_3_pryam with hpunch
    if (exam_pryam_1q and not exam_pryam_2q) or (not exam_pryam_1q and exam_pryam_2q):
        scene exam_pryam_1_3_grisha_2_3_pryam with hpunch
    if not exam_pryam_1q and not exam_pryam_2q:
        scene exam_pryam_0_grisha_full_pryam with hpunch
        grisha "Ой..."
        grisha "Дела отстой."
        pryamorukov "Бестолочь... И  чему только совремённая школа учит?
        Вот советская школа..."
        return
    hide pryamorukov_usual
    show pryamorukov_angry at right
    grisha "Ау, больно"
    pryamorukov "У, бестолочь!"
    hide pryamorukov_angry
    show pryamorukov_usual at right
    pryamorukov "Иди, сдал."
    grisha "Фух, пронесло."
    $ exam_score += 1
    hide pryamorukov_usual with dissolve
    return

label scene_13_exam_3q_right:
    if exam_pryam_1q and exam_pryam_2q:
        scene exam_pryam_full_grisha_0_pryam with hpunch
        hide pryamorukov_usual
        show pryamorukov_wound at right
        pryamorukov "Ой..."
        pryamorukov "Не ожидал такого уровня знаний."
        grisha "Да я тоже не ожидал, честно говоря"
        $ exam_score += 1
        $ diplom += 1
        return
    if (exam_pryam_1q and not exam_pryam_2q) or (not exam_pryam_1q and exam_pryam_2q):
        scene exam_pryam_2_3_grisha_1_3_pryam with hpunch
    if not exam_pryam_1q and not exam_pryam_2q:
        scene exam_pryam_1_3_grisha_2_3_pryam with hpunch
    hide pryamorukov_usual
    show pryamorukov_wound at right
    pryamorukov "Ох-х-х"
    hide pryamorukov_wound
    show pryamorukov_usual at right
    pryamorukov "Иди, сдал."
    grisha "Фух, пронесло."
    $ exam_score += 1
    hide pryamorukov_usual with dissolve
    return

label scene_14:
    scene before_aud with fade
    play music neutral_2 fadein 1 fadeout 1 volume 0.5
    show lyonya_usual with dissolve
    author "Проходит первый экзамен Гриши в унитехе."
    grisha "Фух, наконец-то это закончилось. Кажется, старшекурсники не врали,
    такого от унитеха я не ожидал. Леня, когда там следующий экзамен?"
    lyonya "Вроде через час, может сходим до Спара?"
    grisha "Мне больше Хадуп нравится, там булочки свежие."
    return

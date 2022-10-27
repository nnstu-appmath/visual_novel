# 2 курс
label second_year:
    call scene_19
    call scene_20
    call scene_22
    call scene_30
    scene black with fade
    pause (2.0)
    return

# Пара Потемкина
label scene_19:
    scene bg_winter with fade
    author "Второй курс начался совершенно предсказуемо -
    обычные пары у обычных перподавателей. Ну, не совсем, конечно..."
    scene aud with fade
    show potemkin_usual with dissolve
    potemkin "Утро к обеду доброе! Не стал дожидаться занятия,
    чтобы взяться за очередную порцию работ, вытряхивая письма
    из ящика. Кажется, что остаток короткой жизни проведу в вычитывании
    глупейших ошибок в работах подрастающего поколения. Пока
    удерживает на плаву от одного берега реки жизни до другого
    музыка — на данный момент блюз-рок."
    grisha "Это что за покемон?"
    hide potemkin_usual with dissolve
    show lyonya_usual at left with dissolve
    lyonya "Новый препод. Странный немного, до работ докапывается."
    show ang_usual at right with dissolve
    angelina "Так, Орехов тут, Лукьянов тоже, а где Лаврентьева?"
    lyonya "Я не видел Валю сегодня"
    grisha "Я тоже"
    angelina "В сети она была позавчера в 10 вечера."
    lyonya "Я ей позвоню сейчас."
    hide lyonya_usual with dissolve
    pause (1.5)
    show lyonya_emotional at left with dissolve
    lyonya "Телефон не доступен... Может с ней что-то случилось?
    Может съездить к ней домой? Может?!..."
    hide ang_usual with dissolve
    hide lyonya_emotional with dissolve
    show potemkin_usual with dissolve
    potemkin "Казалось бы, уважение и дисциплина прививается
    еще с отрочества. Шепот и обсуждения можно было бы прервать,
    указав на данные оплошности, но вот всё опять завертелось-
    закружилось… А я, как белка в колесе, бежал бы да бежал.
    Я и сейчас всё бегу да бегу. Сам себе сказал... Побежал дальше..."
    hide potemkin_usual with dissolve
    show lyonya_emotional at left with dissolve
    show ang_usual at right with dissolve
    grisha "Да че ты распереживался так, может уехала куда-то
    или спит человек, отдыхает."
    lyonya "Нет-нет-нет!!! Я уверен что, что-то случилось. Пожалуйста,
    давайте вместе ее поищем!"
    angelina "Ты себя накручиваешь. Что с ней может случиться?
    Гриша прав, всего один день прошел, успокойся."
    hide ang_usual with dissolve
    hide lyonya_emotional with dissolve
    show potemkin_usual with dissolve
    potemkin "Преподавая в низшем университете астрологии,
    студенты проявляли гораздо большие способности в обучении.
    Кто бы мог подумать? Неожиданно осознавать, что данное учебное
    заведение даже не располагает аудиториями с проектором.
    Прискорбно. Однако..."
    hide potemkin_usual with dissolve
    show lyonya_emotional at left with dissolve
    show ang_usual at right with dissolve
    grisha "Лёнь, да ладно тебе, ну человек просто на пару не пришел, че ты"
    lyonya "Ты не понимаешь..."
    hide ang_usual with dissolve
    hide lyonya_emotional with dissolve
    show potemkin_usual with dissolve
    potemkin "Встретимся на следующем занятии"
    hide potemkin_usual with dissolve
    return

# Начало расследования
label scene_20:
    play music detectiv fadein 1 fadeout 1 volume 0.5
    scene before_aud with fade
    show lyonya_emotional at left with dissolve
    lyonya "Ребят, вас действительно не волнует, что случилось с Валей?"
    grisha "Да, господи, ты паникер."
    show ang_usual at right with dissolve
    angelina "Ну, хотя может Леня и прав... Можно к ней съездить и проверить"
    hide lyonya_emotional
    show lyonya_happiness at left
    lyonya "Да-да-да! Спасибо за поддержку!"
    menu:
        "Ладно, поехали":
            scene entrance with fade
            $ lyonya_score += 1
            author "Оказалось, что Валя живет в каком-то опасном районе,
            а подъезд ее дома выглядит, как аудитории унитеха."
            play sound knock_knock
            scene door with fade
            play sound door
            author "Соседка немного приоткрыла дверь, не решившись выйти в подъезд."
            roommate "Привет. А вы кто?"
            show ang_usual at left with dissolve
            show lyonya_emotional at right with dissolve
            angelina "Мы одногруппники Вали. Ее сегодня не было на парах,
            не отвечает на звонки, мы начали беспокоиться. Не знаешь где она?"
            roommate "Она позавчера ушла куда-то вечером с рюкзаком с
            вещами. Сказала, что идет в бар \"Белочка\"."
            grisha "А ты ничего подозрительного не замечала в последнее время?"
            roommate "Ну она стала апатичная, менее разговорчивая. Бормочет
            себе под нос что-то. Но я не стала лезть."
            grisha "Тогда поедем туда?"
            angelina "Можно. Ладно, спасибо."
            roommate "Не за что."
            play sound close_door
            lyonya "А я ведь говорил что что-то случилось! Говорил!!!"
        "Зачем беспокоить человека, может она хочет побыть одна":
            hide ang_usual with dissolve
            hide lyonya_happiness with dissolve
            author "Леня с Ангелиной поехали на квартиру к Вале без Гриши.
            Он же остался на занятиях грызть гранит науки. Вернувшись,
            они поделились с Гришей полученной информацией."
            show lyonya_emotional at left with dissolve
            show ang_usual at right with dissolve
            angelina "В общем соседка сказала, что Валя ушла в бар \"Белочка\"
            позавчера вечером."
            grisha "Ну давайте туда скатаемся, выбора особо нет у нас."
            lyonya "А я ведь говорил что что-то случилсоь! Говорил!!!"
    return

# Бар "Белочка"
label scene_22:
    scene bar_squirrel with fade
    author "Бар \"Белочка\". Довольно странное название для бара.
    Ребят же это не смутило и они пошли туда разузнать о Вале."
    show ang_usual at right with dissolve
    angelina "Давайте бармена спросим, может он на смене был
    в тот день, вспомнит чего-нибудь"
    grisha "Норм идея"
    grisha "Доброго денечка"
    show barman at left with dissolve
    grisha "(Где-то я его уже видел)"
    grisha "Не видели ее позавчера?"
    show photo_valya with dissolve
    barman "Да, а что?"
    hide photo_valya with dissolve
    grisha "Да мы с подругой не можем связаться, вот ищем.
    Можно задать пару вопросов?"
    barman "Только один, а то у меня мало времени."
    menu:
        "С кем она была?":
            barman "Я ее заметил, потому что она сидела
            в довольно странной компании. Их было человек
            10, что-то постоянно проговаривали неслишком
            громко, не улыбались. Взяли закусок на весь стол.
            Ушли всей толпой ровно через полтора часа как
            пришли."
            angelina "А не слышали куда направлялись?"
            barman "Нет, не слышал. Разве, что видел что у
            них на одежде одинаковые значки, но я не
            рассмотрел, что именно на них"
        "Что она заказывала?":
            barman "Напитки не брала, закуски были вроде на весь стол."
        "Во сколько она ушла и куда?":
            barman "Я откуда знаю?"
    hide barman
    show lyonya_usual at left with dissolve
    angelina "Ну что думаете?"
    grisha "Да че-то нет у меня зацепок"
    lyonya "Может еще каких-то Валиных друзей спросить?"
    grisha "А ты кстати, Валин угодник, может знаешь
    каких-нибудь странных типов, с которыми она общалась?"
    lyonya "Э-э-э, я не угодник, я вообще ничего, э-э-э, ладно,
    странные типы, да, были какие-то двое. Один похож
    на дилера, всегда улыбается, я честно говоря, ни
    разу не слышал о том, что бы он работал где-то.
    Второй тихоня, вроде учился тоже когда-то в нашем
    вузе, бормотал себе чето под нос постоянно."
    grisha "Ты знаешь как связаться с ними?"
    lyonya "Ну у Вали в друзьях наверное они есть,
    можем написать им"
    grisha "Так а к кому поедем то?"
    lyonya "Мне всегда казался очень подозрительным
    первый тип. И я теперь очень сильно переживаю за Валю!"
    angelina "А я думаю, что если второй учился у нас,
    то он возможно больше общался с Валей."
    menu:
        "Ладно, поехали к дилеру":
            $ lyonya_score += 1
            call scene_23
        "Ладно, поехали к тихоне":
            $ angelina_score += 1
            call scene_25
    return

# Квартира Аслана
label scene_23:
    play music oxxxymiron fadein 1 fadeout 1 volume 0.5
    scene aslan_apartment with fade
    author "Подъезд у дилера выглядит даже хуже, чем у Вали.
    Но квартирка неплохая."
    show lyonya_usual at left with dissolve
    show ang_usual at right with dissolve
    lyonya "Привет?..."
    show aslan with dissolve
    aslan "Кто я, где я? О, заходите."
    aslan "Че хотели?"
    grisha "Во-первых, почему во дворе так много цыган?"
    aslan "Да они в соседних домах живут, воруют постоянно."
    grisha "Во-вторых, ты ведь знаешь Валю Лаврентьеву?"
    aslan "Ну знаю."
    hide lyonya_usual
    show lyonya_angry at left
    lyonya "Говори где она!!! Ты знаешь!!!"
    angelina "Да Лёня, успокойся ты"
    aslan "Да, господи, виделся я с ней последний раз очень давно.
    Пару раз зависали. С той тусовки и не виделись."
    author "Гриша решил осмотреть жилище Аслана."
    hide lyonya_angry
    hide aslan
    hide ang_usual
    menu:
        "Валяющиеся вещи на диване":
            author "Гриша обратил внимание на вещи на диване.
            Среди мужских вещей виднелась толстовка,
            которая кажется очень знакомой."
            menu:
                "Что открыто на компьютере":
                    author "Открыта вкладка как скачать матлаб на линукс"
                "Котик":
                    author "Черный милый котик. Отзывается на \"Барсик\"."
                "Стикер на доске":
                    $ detective = True
                    author "\"Малинова, 38. 19:00\""
        "Что открыто на компьютере":
            author "Открыта вкладка как скачать матлаб на линукс"
            menu:
                "Валяющиеся вещи на диване":
                    author "Гриша обратил внимание на вещи на диване.
                    Среди мужских вещей виднелась толстовка,
                    которая кажется очень знакомой."
                "Котик":
                    author "Черный милый котик. Отзывается на \"Барсик\"."
                "Стикер на доске":
                    $ detective = True
                    author "\"Малинова, 38. 19:00\""
        "Котик":
            author "Черный милый котик. Отзывается на \"Барсик\"."
            menu:
                "Валяющиеся вещи на диване":
                    author "Гриша обратил внимание на вещи на диване.
                    Среди мужских вещей виднелась толстовка,
                    которая кажется очень знакомой."
                "Что открыто на компьютере":
                    author "Открыта вкладка как скачать матлаб на линукс"
                "Стикер на доске":
                    $ detective = True
                    author "\"Малинова, 38. 19:00\""
        "Стикер на доске":
            $ detective = True
            author "\"Малинова, 38. 19:00\""
            menu:
                "Валяющиеся вещи на диване":
                    author "Гриша обратил внимание на вещи на диване.
                    Среди мужских вещей виднелась толстовка,
                    которая кажется очень знакомой."
                "Что открыто на компьютере":
                    author "Открыта вкладка как скачать матлаб на линукс"
                "Котик":
                    author "Черный милый котик. Отзывается на \"Барсик\"."
    show lyonya_usual at left with dissolve
    show ang_usual at right with dissolve
    show aslan with dissolve
    lyonya "Валя просто не выходит на связь уже второй день, мы очень беспокоимся,
    думали, может ты знаешь"
    aslan "Я не знаю."
    angelina "Ладно, спасибо."
    if detective and time_detective:
        grisha "Я заметил записку с адресом предлагаю
        туда съездить. Это Унитех"
        angelina "Ну у нас другого выбора и нет. Костю мы уже упустили."
        call scene_24
    if detective and not time_detective:
        grisha "Я заметил записку с адресом предлагаю туда съездить."
        angelina "Да вы видели вообще этого чела? Он дальше своего дивана не
        встает. Надо еще второго чела допросить"
        menu:
            "Поехать по адресу в записке":
                grisha "Странно, это адрес Унитеха..."
                call scene_24
            "Поехать ко второму челу":
                $ time_detective = True
                call scene_25
    if not detective and time_detective:
        call scene_29
    if not detective and not time_detective:
        $ time_detective = True
        angelina "Что-то ничего полезного этот челик нам не дал."
        grisha "Поехали ко второму, может он полезнее будет."
        play music detectiv fadein 1 fadeout 1 volume 0.5
    return

# Ребята в унитехе ищут Валю
label scene_24:
    play music detectiv fadein 1 fadeout 1 volume 0.5
    scene doors with fade
    author "В одном из помещений унитеха слышны какие-то необычные звуки."
    show lyonya_surprised at left with dissolve
    show ang_usual at right with dissolve
    lyonya "Там происходит что-то странное..."
    angelina "Давайте проверим"
    grisha "Ладно, но если вас съедят, я предупреждал"
    call scene_28
    return

# Встреча с Костей
label scene_25:
    scene street with fade
    author "С Костей ребята решили встретиться на нейтральной территории,
    то есть на улице"
    show lyonya_angry_winter at left with dissolve
    show ang_usual_winter at right with dissolve
    show kostya_usual with dissolve
    angelina "Привет!"
    kostya "Привет..."
    angelina "Ты когда в последний раз видел Валю Лаврентьеву?"
    lyonya "Отвечай!!!"
    grisha "Да тише ты"
    kostya "А вам какое дело? Я ей просто с домашкой помогал!"
    grisha "Ты че такой нервный, братан, мы тебя не избивать приехали"
    kostya "Д-д-д-да я не нервный... Мне вообще идти надо, вы меня
    задерживаете"
    grisha "Да подожди ты. Мы просто ее потеряли, может ты знаешь где она?"
    kostya "Ничего я не знаю, отстаньте"
    hide kostya_usual with dissolve
    author "Костя ускакал в неизвестном направлении"
    angelina "Странный чел..."
    grisha "Ну может ты и была права, конечно"
    lyonya "Что делать то будем? Этот хрен не дал нам никакой информации."
    if time_detective:
        call scene_26
    else:
        menu:
            "Проследить за Костей":
                call scene_26
            "Поехать к первому типу":
                $ time_detective = True
                call scene_23
    return

# Слежка за Костей
label scene_26:
    grisha "Давайте просто проследим за ним,
    может приведет нас в полезное место."
    author "Лёня немножко (на самом деле множко) в панике, но согласился
    на предложение Гриши. Ангелина тоже присоединилась к ним."
    scene street_2 with fade
    show kostya_phone with dissolve
    kostya "Да, я приду. С собой все взял. Кодовое слово тоже помню.
    Вы приведете ее? Понял."
    hide kostya_phone
    show lyonya_emotional_winter with dissolve
    show ang_usual_winter with dissolve
    lyonya "Вы слышали это? Она сто процентов там!"
    grisha "Ты че так орешь, вообще ведешь себя не как ниндзя.
    Надо аккуратно, чтобы не спугнуть."
    hide lyonya_emotional
    show lyonya_confused_winter
    lyonya "Ладно, я просто так переживаю за Валю, как же я без
    нее буду. То есть как мы без нее..."
    scene before_club with fade
    author "Ребята дошли до какого-то места.
    Костя заходит в помещение по кодовому слову.
    Только Лёня почему-то засмущался."
    show lyonya_confused_winter with dissolve
    lyonya "Ой, может не пойдем туда? Мне кажется нам ЯВНО не сюда."
    grisha "Ты чего так мнение резко изменил? 5 минут назад
    ты был готов туда ворваться."
    lyonya "Э-э-э, ну-у-у, просто доверьтесь мне!!!"
    menu:
        "Уйти":
            $ lyonya_score += 1
        "Пойти за Костей дальше":
            grisha " Да харе, Лёнь, ты чего, если ничего не найдем, то уйдем."
            call scene_27
            scene before_club with fade
            show lyonya_confused at left with dissolve
            show ang_usual at right with dissolve
    grisha "Ладно, может в унитех зайдем? Ну это моя последняя мысль про место,
    где мы еще что-то можем найти."
    angelina "Была не была"
    call scene_24
    return

# Клуб девственников
label scene_27:
    author "Гриша стучится и говорит кодовое слово."
    boy_club "Проходите."
    scene virgin_club with fade
    author "В помещении сидит Костя и еще 8 примерно
    также выглядивших как он парней. В центре сидит
    одна девушка, но это не Валя. По всей комнате
    висят вырезки из взрослых журналов, а напротив
    входа вывеска \"Клуб для борьбы с целомудрием\""
    show girl_club with dissolve
    girl_club "О, Лёня, ты привел друзей?"
    show lyonya_confused at left with dissolve
    lyonya "Э-э-э-э, ребята, пойдем-те, пожалуйста отсюда..........."
    show ang_funny at right with dissolve
    author "Ангелина и Гриша переглядываются и пытаются сдержать смех."
    grisha "Мы, пожалуй, пойдем, Лёня к вам еще заглянет ;)"
    return

# Клуб свидетелей Унитеха
label scene_28:

    return

# Плохая концовка Вали
label scene_29:

    return

# Конец 2 курса
label scene_30:

    return

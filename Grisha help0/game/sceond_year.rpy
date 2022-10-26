# 2 курс
label second_year:
    call scene_19
    call scene_20
    call scene_22
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

    return

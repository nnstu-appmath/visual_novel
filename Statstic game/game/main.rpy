init python:
    config.rollback_enabled = False
    config.has_autosave = False
    config.has_quicksave = False
    config.allow_skipping  = False

# Определение персонажей игры
define author = Character(None)

# Выбор игрока
define g_close = False
define g_open = False
define g_secret = False

# Ход природы
define n_close = False
define n_open = False
define n_secret = False

define random = 0

# Музыка и звуки
define audio.neutral_1 = "/music/neutral_1.mp3"
define audio.knock_knock = "/music/knock_knock.mp3"
define audio.door = "/music/door.mp3"
define audio.answer_wrong = "/music/answer_wrong.mp3"
define audio.applause = "/music/applause.mp3"

# Инициализация файлов
init:
    # Инициализация фонов
    image doors = "doors.jpg"
    image aud = "auditorium.jpg"
    image black = "black.jpg"
    
# Main
label start:
    scene doors with fade
    play music neutral_1 fadein 1
    author "Сделайте предположение: открыта или закрыта дверь, или же за ней находится секрет"
    menu:
        "Открыта":
            $g_open = True
        "Закрыта":
            $g_close = True
        "Секрет":
            $g_secret = True
    call answer from _call_answer
return

label answer:
    $random = renpy.random.randint(1, 15)
    play sound knock_knock
    if random == 1 or random == 2 or random == 3 or random == 4:
        play sound door
        $n_secret = True
        scene black with fade
        pause(0.5)
        $ renpy.movie_cutscene("screamer.mpeg")
    if random == 5 or random == 6 or random == 7 or random == 8 or random == 9:
        play sound door
        $n_open = True
        scene aud with fade
    if random == 10 or random == 11 or random == 12 or random == 13 or random == 14 or random == 15:
        author "Закрыто"
        $n_close = True
    call end from _call_end
    return

label end:
    if (g_open and n_open) or (g_close and n_close):
        play sound applause
        author "Поздравляем, вы отгадали! Вы заработали 1 балл."
    if (g_open and n_close) or (g_secret and n_open) or (g_secret and n_close):
        play sound answer_wrong
        author "Увы! Вы не угадали. 0 баллов."
    if (g_open and n_secret):
        play sound applause
        author "Вы, конечно, не угадали, но наткнулись на секрет! Удача! Вы заработали 2 балла."
    if (g_close and n_open):
        play sound applause
        author "Вы конечно не угадали, но дверь оказалась открытой! Вы заработали 1 балл."
    if (g_close and n_secret):
        play sound applause
        author "Вы наткнулись на секрет! Вы заработали 1 балл."
    if (g_secret and n_secret):
        play sound applause
        author "Ничего себе, вы отгадали секрет! Большая удача! Вы заработали 3 балла."
    scene black with fade
    pause (0.5)
    return

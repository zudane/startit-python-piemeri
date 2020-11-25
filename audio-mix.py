from pydub import AudioSegment
from pydub.playback import play

# Dokumentācija: https://github.com/jiaaro/pydub
# Skaņas datnes var atrast, piemēram, šeit - http://soundbible.com/


def miksejam_skanas(datne):
    sound = AudioSegment.from_file(datne, format="wav")
    # spēlējam orginālo skaņu
    play(sound)
    
    # Visi laiki ir milisekundēs, definējam sekundi vienkāršībai
    s = 1 * 1000
    # lietojam parastu Python list slicing sintaksi
    # lai izveidotu nelielus fragmentus no dotās skaņas
    sakums = sound[:2 * s]
    beigas = sound[-6 * s:-3 * s]

    # mainam skaļumu
    one = sakums + 6
    two = sakums + 3
    three = sakums
    four = sakums - 3
    five = sakums - 6
    # izveidojam jaunu skaņu
    mod = one + two + three + four + five
    # pārbaudām skaņas garumu
    print(mod.duration_seconds)
    # atskaņojam jauno skaņu
    play(mod)


miksejam_skanas("clock-chimes-daniel_simon.wav")

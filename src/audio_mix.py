from pydub import AudioSegment
from pydub.playback import play

# Dokumentācija: https://github.com/jiaaro/pydub
# Skaņas datnes var atrast, piemēram, šeit - http://soundbible.com/


def atskano(datne):
    skana = AudioSegment.from_file(datne, format="wav")
    # spēlējam orginālo skaņu
    # pamata atbalstītais audio formāts ir wav
    # lai atbalstītu citus, jāinstalē papildus bibliotēkas
    play(skana)


def mikse_skanas(datne):
    skana = AudioSegment.from_file(datne, format="wav")
    # Visi laiki ir milisekundēs, definējam sekundi vienkāršībai
    s = 1 * 1000
    # lietojam parastu Python list slicing sintaksi
    # lai izveidotu nelielus fragmentus no dotās skaņas
    sakums = skana[:2 * s] # no sakuma līdz 2 sekundei
    beigas = skana[-6 * s:-3 * s] # 6 sekundes no beigām līdz 3 sekundes no beigām

    # mainam skaļumu
    one = sakums + 6
    two = sakums + 3
    three = sakums
    four = sakums - 3
    five = sakums - 6
    # izveidojam jaunu skaņu
    jauna = one + two + three + four + five
    # pārbaudām skaņas garumu
    print(jauna.duration_seconds)
    # atskaņojam jauno skaņu
    play(jauna)
    # atgriežam skaņu tālākām darbībām
    return jauna


def saglaba_skanu(skana, datne, formats="wav"):
    skana.export(datne, format=formats)

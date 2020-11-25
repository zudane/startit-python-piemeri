import numpy as np
import simpleaudio as sa

# Dokumentācija: https://simpleaudio.readthedocs.io/
# Skaņas datnes var atrast, piemēram, šeit - http://soundbible.com/


def parbaudam_darbibu():
    import simpleaudio.functionchecks as fc
    fc.run_all()


def atskano_datni(datne):
    """Atskaņo dotu datni wav formātā

    Args:
        datne (string): datnes atrašanās vieta un nosaukums
    """
    wave_obj = sa.WaveObject.from_wave_file(datne)
    play_obj = wave_obj.play()
    play_obj.wait_done()


def piiksteet(frekvence=440, sekundes=3):
    """Atskaņo pīkstienu dotā frekvencē un ilgumā

    Args:
        frekvence (int): skaņas frekvence Herzos
        sekundes (int): skaņas ilgums sekundēs
    """
    afb = 44100  # audio frekvences biežums (sample rate)

    # Izveidojam masīvu ar sekundes*afb soļiem, 
    # robežās no 0 līdz dotajam ilgumam sekundēs
    t = np.linspace(0, sekundes, sekundes * afb, False)

    # Izveidojam dotas frekvences sinusoīdu
    nots = np.sin(frekvence * t * 2 * np.pi)

    # Panākam, ka lielāka vērtība ir 16 bitu robežās
    audio = nots * (2**15 - 1) / np.max(np.abs(nots))
    # Pārvēršam 16 bitu datos
    audio = audio.astype(np.int16)

    # Sākam atskaņot
    play_obj = sa.play_buffer(audio, 1, 2, afb)

    # Pirms iziet no funkcjas, sagaidam atskaņošanas beigas
    play_obj.wait_done()


# parbaudam_darbibu()


# atskano_datni("clock-chimes-daniel_simon.wav")

# 261.626	294.33	327.03	348.83	392.44	436.04	490.55	523.25
# piiksteet(261.626, 1)   # DO
# piiksteet(294.33, 1)    # RE
# piiksteet(327.03, 1)    # MI
# piiksteet(348.83, 1)    # FA
# piiksteet(392.44, 1)    # SOL
# piiksteet(436.04, 1)    # LA
# piiksteet(490.55, 1)    # SI
# piiksteet(523.25, 1)    # DO
# piiksteet()

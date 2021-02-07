# ******************************************************************************
#  Direitos Autorais (c) 2019-2021 Nurul-GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e Medicina.                                        *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

import pyaudio
import wave
import sys


def reprodutor():
    print("""
    [*] REPRODUZINDO UM ARQUIVO DE AUDIO (.wav) [*]
-------------------------------------------------------
""")
    CHUNK = 1024

    wf = wave.open("sound/Franco.wav", 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    data = wf.readframes(CHUNK)

    while data != '':
        stream.write(data)
        data = wf.readframes(CHUNK)

    stream.stop_stream()
    stream.close()

    p.terminate()


if __name__ == '__main__':
    reprodutor()
